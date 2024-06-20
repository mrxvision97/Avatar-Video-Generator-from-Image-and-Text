import requests
import base64
import json
import streamlit as st
import time

# API endpoint URLs
POST_URL = "https://api.d-id.com/talks"
GET_URL_BASE = "https://api.d-id.com/talks/"

# Replace with your actual API key (key:value)
api_key = "MjAyMmFtYW4ua0B2aWR5YXNoaWxwLmVkdS5pbg:OT2DMIIKvPsuT0HjMZ82U"    #Replace with your actual API key (key:value)

# Base64 encode the API key
base64_encoded_api_key = base64.b64encode(api_key.encode()).decode()


# Function to create a speech from text and image
def create_speech(text, image_url):
    headers = {
        "Authorization": f"Basic {base64_encoded_api_key}",
        "Content-Type": "application/json; charset=utf-8"
    }
    data = {
        "script": {
            "type": "text",
            "input": text,
            "provider": {
                "type": "elevenlabs",
                "voice_id": "21m00Tcm4TlvDq8ikWAM"
            }
        },
        "source_url": image_url
    }
    try:
        response = requests.post(POST_URL, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        if response.status_code == 402:
            st.error("Your account has reached its usage limit or has a billing issue. Please check your account and try again.")
        else:
            st.error(f"HTTP error occurred during speech generation: {err}")
        return None
    except requests.exceptions.RequestException as err:
        st.error(f"Request error occurred during speech generation: {err}")
        return None
# Function to retrieve the result URL given an ID
def get_result_url(talk_id):
    url = GET_URL_BASE + talk_id
    headers = {
        "Authorization": f"Basic {base64_encoded_api_key}"
    }

    # Check the status of the talk for a maximum of 5 minutes
    max_attempts = 30  # 5 minutes with 10-second intervals
    attempt = 0

    while attempt < max_attempts:
        attempt += 1
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            json_response = response.json()

            # Check status and retrieve result_url
            if "status" in json_response and json_response["status"] == "done":
                if "result_url" in json_response:
                    return json_response["result_url"]
                else:
                    st.error("Result URL not found in API response.")
                    return None
            elif "status" in json_response and json_response["status"] == "started":
                st.info("It's almost done...")
                time.sleep(10)  # Wait for 10 seconds before checking the status again
                continue
            else:
                st.error("Unexpected status found in API response.")
                return None

        except requests.exceptions.HTTPError as err:
            st.error(f"HTTP error occurred while retrieving result URL: {err}")
            return None
        except requests.exceptions.RequestException as err:
            st.error(f"Request error occurred while retrieving result URL: {err}")
            return None
        except json.JSONDecodeError as err:
            st.error(f"JSON decode error occurred: {err}")
            return None

    st.error("Failed to retrieve result URL. Please try again.")
    return None


# Streamlit app
def main():
    st.title("Text-to-Speech Image Synthesis")

    # Input text and image URL
    text_input = st.text_area("Enter text:", "Hello, I am from Vidyashilp University")
    image_url = st.text_input("Enter image URL:")

    # Button to generate speech
    if st.button("Generate Video"):
        st.info("Generating video...")

        # Call API to create speech
        response_data = create_speech(text_input, image_url)

        # Display output
        if response_data and "id" in response_data:
            speech_id = response_data["id"]

            # Retrieve result URL
            result_url = get_result_url(speech_id)
            if result_url:
                st.success("Download now!")
                st.video(result_url)  # Preview the generated video

                # Download button
                with open("video.mp4", "wb") as f:
                    f.write(requests.get(result_url).content)

                st.download_button(
                    label="Download Video",
                    data=open("video.mp4", "rb").read(),
                    file_name="output_video.mp4",
                    mime="video/mp4",
                )
            else:
                st.warning("Failed to retrieve result URL. Please try again.")
        else:
            st.error("Failed to generate video. Please check your input and try again.")


if __name__ == "__main__":
    main()
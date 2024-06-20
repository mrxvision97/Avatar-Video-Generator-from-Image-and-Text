# Avatar-Video-Generator-from-Image-and-Text
A Streamlit application that generates videos of an avatar speaking the provided text input, using the specified image as the avatar's appearance. It leverages the D-ID API to create realistic speech and synthesize the video output.
Try here !  https://avatar-video-generator-from-image-and-text.streamlit.app/

# Text-to-Speech Image Synthesis

This project is a Streamlit application that allows users to generate a video of an avatar speaking the provided text. The application utilizes the D-ID API to create the speech and synthesize the video.

## Industry Scope

Text-to-speech image synthesis has a wide range of applications across various industries:

1. **Education and eLearning**: Create engaging and interactive video lectures, tutorials, or educational content using virtual instructors or avatars.
2. **Marketing and Advertising**: Generate personalized video advertisements or product demonstrations with customizable avatars and scripts.
3. **Entertainment**: Produce animated characters or virtual presenters for movies, video games, or live performances.
4. **Accessibility**: Provide alternative content formats for individuals with disabilities, such as visual or auditory impairments.
5. **Customer Service**: Create virtual agents or chatbots with human-like avatars for better user engagement and assistance.
6. **Corporate Training**: Develop interactive training modules with virtual instructors or avatars for employee onboarding and skill development.

## Prerequisites

Before running the application, ensure you have the following prerequisites installed:

- Python (version 3.6 or later)
- pip (Python package installer)

## Setup

1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal or command prompt.
3. Install the required Python packages by running the following command:
    
    ```bash
    pip install -r requirements.txt
    ```
4. Create a new file named `.env` in the project directory and add your D-ID API key:
5. Run the Streamlit application using the following command:

    ```bash
    D_ID_API_KEY=YOUR_API_KEY_HERE
    ```
   Replace `YOUR_API_KEY_HERE` with your actual D-ID API key.

5. Save the `.env` file.

## Usage

1. Run the Streamlit application by executing the following command in your terminal or command prompt:

    ```bash
    streamlit run app.py
    ```
2. Open the provided URL in your web browser to access the application.
3. Enter the text you want the avatar to speak and customize the avatar settings as needed.
4. Click the "Generate Video" button to create the video with the avatar speaking the text.
5. Download the generated video and share it as needed.
6. Repeat the process to create additional videos with different text or avatar settings.
7. Enjoy creating personalized and engaging videos with text-to-speech image synthesis!
8. For more information about the D-ID API, visit the [D-ID website](https://www.d-id.com/).

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```
This README.md file provides an overview of the project, its industry scope, prerequisites, setup instructions, usage guide, code snippets, contributing guidelines, and license information.

When including this README.md file in your project repository, make sure to replace `YOUR_API_KEY_HERE` with your actual D-ID API key in the `.env` file example. Additionally, update the license information if needed.

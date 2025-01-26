import streamlit as st  # Import Streamlit for building the web app.
import os  # Import OS for accessing environment variables.
from PIL import Image  # Import PIL for handling image uploads.
import google.generativeai as genai  # Import Google Generative AI for model integration.
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from a .env file.



# Retrieve the Google API key from environment variables.
os.getenv("GOOGLE_API_KEY")
# Configure the Generative AI with the retrieved API key.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# Difference between gemini-1.5-flash & gemini-1.5-pro model

# gemini-1.5-flash	
# Audio, images, videos, and text	Text	
# Fast and versatile performance across a diverse variety of tasks

# gemini-1.5-pro	
# Audio, images, videos, and text	Text	
# Complex reasoning tasks such as code and text generation, text editing, problem solving, data extraction and generation



# Function to load the Gemini model and get a response.
def get_gemini_response(input, image):
    # Initialize the Gemini model. Here, 'gemini-1.5-flash' is used, but 'gemini-1.5-pro' can also be utilized.
    model = genai.GenerativeModel('gemini-1.5-flash')  
    # Generate a response based on input text and image, if both are provided.
    if input != "":
        response = model.generate_content([input, image])
    else:
        # If no input text is provided, generate a response based only on the image.
        response = model.generate_content(image)
    return response.text  # Return the text response.

# Initialize the Streamlit application.
st.set_page_config(page_title="Gemini Image Demo")  # Set the page title for the app.

# Create a header for the application.
st.header("Gemini Application")

# Text input field for users to provide a prompt.
input = st.text_input("Input Prompt: ", key="input")

# File uploader for users to upload images (supports JPG, JPEG, and PNG formats).
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""  # Initialize an empty variable for the uploaded image.

# If an image is uploaded, display it within the app.
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Open the uploaded image using PIL.
    st.image(image, caption="Uploaded Image.", use_column_width=True)  # Display the image with a caption.

# Button for users to request an analysis of the uploaded image.
submit = st.button("Tell me about the image")

# If the "submit" button is clicked:
if submit:
    # Call the Gemini response function with the input prompt and image.
    response = get_gemini_response(input, image)
    # Display the response in the app.
    st.subheader("The Response is")
    st.write(response)
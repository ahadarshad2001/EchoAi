import os
import streamlit as st
from groq import Groq

# Set page configuration
st.set_page_config(page_title="AI Content Generator", page_icon="📝", layout="wide")

# Display the logo
logo = "logo.png"  # Replace with your logo file name
st.image(logo, width=200)  # Adjust width as necessary

# Page title
st.title("AI Content Generator for Social Media")
st.write("Generate engaging and creative content for social media using AI with Groq Llama.")

# Sidebar
st.sidebar.header("Settings")
content_type = st.sidebar.selectbox("Select Content Type:", ["Tweet", "Instagram Caption", "LinkedIn Post", "Facebook Post"])

# New Brand Voice selection
brand_voice = st.sidebar.selectbox(
    "Select Brand Voice:",
    ["Professional", "Casual", "Witty", "Inspirational"]
)

max_length = st.sidebar.slider("Max Length of Generated Content", 50, 300, 150)
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)

# Input for user prompt
prompt = st.text_area("Enter your content prompt:", help="Type a brief idea for your social media post.")

# Set up the Groq client with your API key
GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to append brand voice to the prompt
def generate_brand_voice_prompt(prompt, voice):
    voice_dict = {
        "Professional": "Write in a professional and formal tone.",
        "Casual": "Write in a casual and friendly tone.",
        "Witty": "Write with a witty and humorous tone.",
        "Inspirational": "Write in an inspiring and uplifting tone."
    }
    # Modify the prompt to include the voice
    modified_prompt = f"{voice_dict[voice]} {prompt}"
    return modified_prompt

# Function to generate content using Groq Llama
def generate_content_with_groq(prompt, voice):
    # Modify prompt with selected brand voice
    voice_prompt = generate_brand_voice_prompt(prompt, voice)
    
    # Send the modified prompt to the model
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": voice_prompt}],
        model="llama3-8b-8192"
    )
    return chat_completion.choices[0].message.content

# Button to generate content
if st.button("Generate Content"):
    if prompt:
        with st.spinner('Generating content using Groq...'):
            generated_content = generate_content_with_groq(prompt, brand_voice)
            st.success("Generated Content:")
            st.write(generated_content)
    else:
        st.error("Please enter a prompt to generate content.")

# Footer
st.write("Echo AI Content Generator | Powered by Groq Llama")

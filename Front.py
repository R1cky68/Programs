import requests
import json

BACKEND_URL="https://psychic-adventure-p4w6pqpgxw9c6gp6-8000.app.github.dev"

def chat(user_input, data, session_id=None):
    """
    Sends a user input to a chat API and returns the response.

    Args:
        user_input (str): The user's input.
        data (str): The data source.
        session_id (str, optional): Session identifier. Defaults to None.

    Returns:
        tuple: A tuple containing the response answer and the updated session_id.
    """
    # API endpoint for chat
    url = BACKEND_URL+"/chat"

    # Print inputs for debugging
    print("user ", user_input)
    print("data", data)
    print("session_id", session_id)

    # Prepare payload for the API request
    if session_id is None:
        payload = json.dumps({"user_input": user_input, "data_source": data})
    else:
        payload = json.dumps(
            {"user_input": user_input, "data_source": data, "session_id": session_id}
        )

    # Set headers for the API request
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    # Make a POST request to the chat API
    response = requests.request("POST", url, headers=headers, data=payload)

    # Print the API response for debugging
    print(response.json())

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the response answer and updated session_id
        return response.json()["response"]["answer"], response.json()["session_id"]

# Function to upload a file to a specific API endpoint, using request module to make HTTP requests
def upload_file(file_path):
    """
    Uploads a file to a specified API endpoint.

    Args:
        file_path (str): The path to the file to be uploaded.

    Returns:
        str: The file path returned by the API.
    """
    # Print file path for debugging
    print("path", file_path)

    # Extract the filename from the file path
    filename = file_path.split("\\")[-1]

    # API endpoint for file upload
    url = BACKEND_URL+"/uploadFile"
    print(url)

    # Prepare payload for the file upload request and tuple is created with file data
    payload = {}
    files = [
        (
            "data_file",
            (filename, open(file_path, "rb"), "application/pdf"),
        )
    ]

    # Set headers for the file upload request
    headers = {"accept": "application/json"}

    # Make a POST request to upload the file, with specific url, headers, payload as below (and print response for debugging)
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.status_code)

    # Check if the file upload was successful (status code 200)
    if response.status_code == 200:
        # Print the API response for debugging
        print(response.json())
        # Return the file path returned by the API
        return response.json()["file_path"]

# Streamlit is a custom open source python library that makes it easy to share python web apps for machine learning and data science, automatically making a web interface and updating it as your code runs (turns scripts into web apps easily)
import streamlit as st
import time
import os

# Set page configuration for the Streamlit app
st.set_page_config(page_title="Document Chat", page_icon="📕", layout="wide")

# Initialize chat history and session variables, if not present in current state then they're created with initial values
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sessionid" not in st.session_state:
    st.session_state.sessionid = None

# Allow user to upload a file (PDF or DOCX)
data_file = st.file_uploader(
    label="Input file", accept_multiple_files=False, type=["pdf", "docx"]
)

# Places a divider to visually separate different sections of the app
st.divider()

# Process the uploaded file if available
if data_file is not None:
    # Save the file temporarily
    file_path = os.path.join(os.getcwd(),"temp", data_file.name)
    with open(file_path, "wb") as f:
        f.write(data_file.getbuffer())

    # Upload the file to a specified API endpoint
    s3_upload_url = upload_file(file_path=file_path)
    
    if s3_upload_url is not None:
        s3_upload_url = s3_upload_url.split("/")[-1]
    
    else:
        # Handle the case where s3_upload_url is None, perhaps by displaying an error message or logging the issue
        st.error("Failed to upload the file to S3. Please check your S3 credentials or try again later.")

    # Commenting out this line bc I don't have the S3 storage so can't upload the files properly, interface works but no actual response
    #s3_upload_url=s3_upload_url.split("/")[-1
   #                                        ]
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("You can ask any question"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            if st.session_state.sessionid is None:
                # If no existing session ID, start a new session
                assistant_response, session_id = chat(
                    prompt, data=s3_upload_url, session_id=None
                )
                st.session_state.sessionid = session_id
            else:
                # If existing session ID, continue the session
                assistant_response, session_id = chat(
                    prompt, session_id=st.session_state.sessionid, data=s3_upload_url
                )

            # This empty streamlit element (message_placeholder) is used for dynamically updating the chatbot's response
            message_placeholder = st.empty()
            full_response = ""

            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)

                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

        # Add assistant response to chat history
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
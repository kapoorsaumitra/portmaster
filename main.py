import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv('.env')

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

stack=input("Enter tech stack: ")
response = model.generate_content("Generate a Dockerfile, Use a base image, install essential dependencies, copy application code, expose default ports, and provide a command to start the service. don't write comments. Here's the tech stack: " + stack)

f = open("Dockerfile", "x")
f.write(response.text)
f.close()
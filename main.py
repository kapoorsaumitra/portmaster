import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv('.env')

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

stack=input("Enter tech stack: ")
response = model.generate_content("Generate a dockerfile for the following techstack: " + stack + ", Just give the contents of the dockerfile and nothing else.")

f = open("Dockerfile", "x")
f.write(response.text)
f.close()
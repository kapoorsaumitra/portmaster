import os
from dotenv import load_dotenv
# Assuming the models folder contains modules for each model
from models import openai, genai  

class DockerfileGenerator:
    def __init__(self, model_name):
        load_dotenv('.env')
        self.api_key = os.getenv('API_KEY')

        # Model selection
        if model_name.lower() == 'openai':
            self.model = openai.OpenAIModel(self.api_key)
        elif model_name.lower() == 'genai':
            self.model = genai.GenAIModel(self.api_key)
        else:
            raise ValueError("Unsupported model. Please choose 'openai' or 'genai'.")

    def generate_dockerfile(self, tech_stack):
        prompt = "Generate a Dockerfile, Use a base image, install essential dependencies, copy application code, expose default ports, and provide a command to start the service. Don't write comments. Here's the tech stack: " + tech_stack
        response = self.model.generate_content(prompt)

        with open("Dockerfile", "x") as f:
            f.write(response.text)
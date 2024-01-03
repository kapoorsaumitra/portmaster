# PortMaster

This is a Python project that uses the Google Generative AI to generate Dockerfiles based on a given tech stack.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. You also need the following Python packages:

- dotenv
- google-generativeai

You can install them using pip:

```bash
pip install python-dotenv google-generativeai
```

### Installing

1. Clone the repository
2. Install the prerequisites
3. Create a .env file with your [Google API key](https://makersuite.google.com/app/apikey) (Gemini): 

```bash
echo GOOGLE_API_KEY=your_api_key > .env
```

## Running the script

You can run the script using Python:

```bash
python main.py
```
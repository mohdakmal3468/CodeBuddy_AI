from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("AVAILABLE MODELS:\n")

models = client.models.list()

for m in models:
    # Print everything the model object has (so we can see usable fields)
    print("Model name:", m.name)
    print("Full model object:", m)
    print("-" * 50)
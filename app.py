from unittest import result
from urllib import response

from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.5-flash"

app = Flask(__name__)

PROMPT = """
You are a friendly AI mentor for beginners.

Review the following {language} code and respond in this exact format:

❌ Bugs
- ...

✅ Improvements
- ...

🔁 Fixed Code
```{language}
<fixed code>
Code:
{code}
"""
@app.route("/", methods=["GET", "POST"])
def index():
    response = ""

    if request.method == "POST":
        code = request.form.get("code", "")
        language = request.form.get("language", "python")

        prompt_text = PROMPT.format(language=language, code=code)

        try:
            result = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt_text
            )

            response = result.text  # ✅ FIXED
        except Exception as e:
            response = f"Error: {e}"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
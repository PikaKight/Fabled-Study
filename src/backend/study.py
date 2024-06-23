import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv(".env")


genai.configure(api_key=os.environ.get("GEN_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

prompt = """
Write a story that 

"""

response = model.generate_content(prompt)
print(response.text)
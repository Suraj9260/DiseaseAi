import google.generativeai as genai
import os


os.environ["API_KEY"] = ""
genai.configure(api_key=os.environ["API_KEY"])

model1 = genai.GenerativeModel('gemini-1.5-flash')
print('gemini model imported')

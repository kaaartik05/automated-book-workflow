import google.generativeai as genai

# 🔐 Set your actual Gemini API key here
genai.configure(api_key="AIzaSyCSETbX9p0uXaqB7guHZckcMmaEXGnSaxQ")

# ⚡ Load the Gemini model directly (no chat session)
model = genai.GenerativeModel("gemini-1.5-flash")

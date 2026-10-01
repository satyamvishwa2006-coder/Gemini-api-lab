from google import genai
from dotenv import load_dotenv
import os
import time

# Load .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Ask user for a topic
topic = input("Enter the topic for flashcards: ")

# Generate flashcards with retry
for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"""
Create 5 flashcards about {topic}.

Format each flashcard like this:

Q: Question
A: Answer

Keep the questions simple and useful for students.
"""
        )
        break

    except Exception as e:
        if "503" in str(e) and attempt < 2:
            wait_time = 2 ** (attempt + 1)
            print(f"Gemini server busy. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            raise

# Display result
print("\n===== FLASHCARDS =====\n")
print(response.text)
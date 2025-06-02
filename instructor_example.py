import os
from pydantic import BaseModel, Field
from instructor import Instructor
from dotenv import load_dotenv

# Load .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")
print("GROQ_API_KEY loaded successfully!")

# Define schemas
class PersonalInfo(BaseModel):
    name: str = Field(description="The full name of the person")
    age: str = Field(description="Age of the person")
    address: str = Field(description="Full address of the person")

class TextSummary(BaseModel):
    main_idea: str
    benefits: list[str]
    challenges: list[str]
    tools_mentioned: list[str]
    conclusion: str
    simple_txt: str

# Set up Instructor with OpenAI-compatible endpoint (Groq)
client = Instructor(
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_api_key,
    # model="llama3-70b-8192"
)

# Function to classify text
def classify_input(text: str) -> str:
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": f"Classify this as 'personal', 'educational', or 'other':\n\n{text}"}],
        temperature=0.0
    )
    return response.choices[0].message.content.strip().lower()

# Main analyze function
def analyze_text(text: str):
    category = classify_input(text)

    if category == "personal":
        result = client.extract(PersonalInfo, f"Extract personal details from this:\n{text}")
    elif category == "educational":
        result = client.extract(TextSummary, f"Summarize the following educational content:\n{text}")
    else:
        return "Unrecognized or unsupported text category."

    return result

# Main
if __name__ == "__main__":
    input_text = input("Enter text: ")
    output = analyze_text(input_text)
    print(output)

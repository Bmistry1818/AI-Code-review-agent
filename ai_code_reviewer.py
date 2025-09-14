import openai
import sys
from pathlib import Path

# Replace with your OpenAI API key or load from environment variable
openai.api_key = "YOUR_OPENAI_API_KEY"

def read_code(file_path):
    with open(file_path, "r") as f:
        return f.read()

def review_code(code: str):
    prompt = f"""
    You are a senior software engineer.
    Review the following code for bugs, performance issues, and style improvements.
    Provide actionable feedback:

    Code:
    {code}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ai_code_reviewer.py <file_path>")
        sys.exit(1)
    file_to_review = sys.argv[1]
    code_content = read_code(file_to_review)
    feedback = review_code(code_content)
    print(f"--- AI Review for {file_to_review} ---\n{feedback}")

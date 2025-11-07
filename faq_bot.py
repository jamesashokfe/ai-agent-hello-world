"""FAQ bot."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("API key not found in environment variables")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

faq = {
    "hours": "Our support is available 24/7.",
    "location": "We are located at 123 Main Street.",
    "refund": "Refunds can be requested within 30 days of purchase.",
    "contact": "You can contact us at support@example.com."
}


def classify_intent_with_ai(user_query):
    """Classify the user's intent using AI."""
    response = client.chat.completions.create(
        model="google/gemini-2.5-flash-lite",
        messages=[
            {
                "role": "system",
                "content": "You are an intent classification assistant"
            },
            {
                "role": "user",
                "content": f"""
                Classify the user's intent within the following categories:
                {', '.join(faq.keys())}, other.
                User query: {user_query}
                """
            },
        ],
    )
    intent = response.choices[0].message.content.strip().lower()
    return intent


def get_faq_response(user_query):
    """Get a response from the FAQ based on the user query."""
    user_query = user_query.lower()
    for key, value in faq.items():
        if key in user_query:
            return value

    # Fallback to AI if intent not identified
    intent = classify_intent_with_ai(user_query)
    return faq.get(intent, "Sorry, I don't understand your query. Please contact support.")


def main():
    """Main function to run the FAQ bot."""
    print("Welcome to the FAQ bot! Ask your question or type 'exit' to close.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("FAQ bot: Goodbye!")
            break

        response = get_faq_response(user_input)
        print(f"FAQ bot: {response}")


if __name__ == "__main__":
    main()

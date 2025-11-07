"""FAQ bot."""

faq = {
    "hours": "Our support is available 24/7.",
    "location": "We are located at 123 Main Street.",
    "refund": "Refunds can be requested within 30 days of purchase.",
    "contact": "You can contact us at support@example.com.",
}


def get_faq_response(user_query):
    """Get a response from the FAQ based on the user query."""
    user_query = user_query.lower()
    for key, value in faq.items():
        if key in user_query:
            return value
    return "Sorry, I don't understand your query. Please contact support."


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

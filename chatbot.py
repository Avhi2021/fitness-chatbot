print("Fitness chatbot: Hello! How can i help you with fitness today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit','quit']:
        print("Goodbye!")
        break
    print("Bot: I'm here to help with fitness advice")
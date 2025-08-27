# Simple Chatbot using if-else
print("🤖 AI Bot: Hello! I am your chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("🤖 AI Bot: Hello there! How can I help you?")
    elif user_input == "how are you":
        print("🤖 AI Bot: I'm just a bunch of code, but I'm doing great! 😄")
    elif user_input == "what is ai":
        print("🤖 AI Bot: AI stands for Artificial Intelligence. It's about making machines think smart like humans.")
    elif user_input == "who made you":
        print("🤖 AI Bot: I was created by Samrat Tayade!")
    elif user_input == "bye":
        print("🤖 AI Bot: Goodbye! Have a great day!")
        break
    else:
        print("🤖 AI Bot: Sorry, I didn’t understand that. Can you try something else?")

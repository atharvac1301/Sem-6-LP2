from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new ChatBot instance
chatbot = ChatBot('HealthBot')

# Define the conversation pairs for training
conversation = [
    "hi",
    "Hello!",
    "what is your name?",
    "My name is HealthBot. I'm an AI assistant for hospital inquiries.",
    "what are the hospital hours?",
    "The hospital is open 24 hours a day, 7 days a week.",
    "where is the cardiology department?",
    "The cardiology department is located on the 2nd floor, near the main lobby.",
    "what are the visiting hours?",
    "Visiting hours are from 10 AM to 8 PM every day.",
    "can I get a dermatology appointment?",
    "To schedule a dermatology appointment, please call our appointment line at 123-456-7890.",
    "quit",
    "Goodbye! Take care."
]

# Train the chatbot with the conversation pairs
trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Start the chatbot
print("Hello! I'm HealthBot, an AI assistant for hospital inquiries. How can I help you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.get_response(user_input)
    print(response)
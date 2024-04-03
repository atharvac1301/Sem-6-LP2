# Hospital Management
import re

responses = {
    "greeting" : "Hi, welcome to Hospital Chatbot.\nHow can I help you?",
    "prescription" : "Downloading and printing your prescription now...",
    "discharge" : "Downloading discharge summary now...",
    "MRI" : "Schedule for MRI slots till Friday on display",
    "payment" : "Here is your receipt. Payment Modes: Card, Cash, Online UPI",
    "blood test"  : "Here are the blood test results. They have also been mailed to you",
    "appointment" : "Here is the appointment schedule for your doctor.",
    "bye" : "Thank you for using our services. Have a great day!",
    "default" : "I apologize, I couldn't understand your request."
    
}

class Rule:
    def __init__(self, pattern, response_key):
        self.pattern = pattern
        self.response_key = response_key
        

class ExpertSystem:
    def __init__(self, rules):
        self.rules = rules

    def respond_to_query(self, query):
        for rule in self.rules:
            if re.search(rule.pattern, query):
                return responses[rule.response_key]
        return responses['default'] 

rules = [
    Rule(r"\b(?:hello|hi)\b", "greeting"),
    Rule(r"\b(?:goodbye|bye|exit)\b", "bye"),
    Rule(r"\b(?:prescription|prescribe)\b", "prescription"),
    Rule(r"\b(?:discharge|leave)\b", "discharge"),
    Rule(r"\b(?:MRI)\b", "MRI"),
    Rule(r"\b(?:pay|fee)\b", "payment"),
    Rule(r"\b(?:blood|test)\b", "blood test"),
    Rule(r"\b(?:appointment|available)\b", "appointment"),
    
]

chatbot = ExpertSystem(rules)

print("Welcome to the Expert System Chatbot: ")
print("Type 'exit' to end the conversation\n")

while True:
    user_input = input("Customer: ")

    if user_input.lower() == "exit":
        bot_response = chatbot.respond_to_query("exit")
        print(f"Chatbot: {bot_response}")
        break
    else:
        bot_response = chatbot.respond_to_query(user_input)
        print(f"Chatbot: {bot_response}\n")


'''
    Components of an Expert System:
        1. Knowledge Base : Contains facts and rules
        2. Inference Engine : makes decisions
        3. User Interface : interact with the user
'''

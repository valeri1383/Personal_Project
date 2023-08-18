from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pytz
import time
import collections.abc


collections.Hashable = collections.abc.Hashable
time.clock = time.time


# Create a chatbot instance
chatbot = ChatBot('ITBot')

# Create a new instance of a ListTrainer
trainer = ListTrainer(chatbot)

# Load your specialized IT training data
it_training_data = [
    "How do I troubleshoot network connectivity issues?",
    "You can start by checking if your device has a valid IP address and testing with a different cable.",
    "What is a firewall?",
    "A firewall is a network security device that monitors and filters incoming and outgoing network traffic based on an organization's previously established security policies.",
    # Add more IT-related questions
]

# Train the chatbot using your IT training data
trainer.train(it_training_data)

# Main conversation loop
print("ITBot: Hello! I'm here to help with IT-related questions. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ITBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("ITBot:", response)
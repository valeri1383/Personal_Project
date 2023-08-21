import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pytz
import time
import collections.abc


collections.Hashable = collections.abc.Hashable
time.clock = time.time

def text_to_speach(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('volume', 1.0)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


# Create a chatbot instance
chatbot = ChatBot('ITBot')

# Create a new instance of a ListTrainer
trainer = ListTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

# Load your specialized IT training data
it_training_data = []

questions = open("database for chatbot", "r")
for x in questions:
    it_training_data.append(x)

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
    text_to_speach(response)
    print("ITBot:", response)
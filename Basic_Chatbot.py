import random
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing fine! How about you?", "I'm great! Thanks for asking."]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created to chat with you!", "You can call me ChatBot."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Take care!"]
    ],
    [
        r"(.*)",
        ["That's interesting!", "Tell me more.", "I'm not sure I understand."]
    ]
]

def chatbot():
    print("Hello! I'm a basic chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()

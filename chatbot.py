#!/usr/bin/env python3

from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    ["how are you?", ["I'm good, thank you!", "Doing great, how about you?"]],
    ["what is your name?", ["I'm an NLP chatbot.", "You can call me Chatty."]],
    ["bye|exit", ["Goodbye!", "See you later!", "Bye!"]],
]

def start_chat():
    print("Hi! I'm your AI chatbot. Type 'exit' to end the chat.")
    chat = Chat(pairs, reflections)
    chat.converse()

start_chat()

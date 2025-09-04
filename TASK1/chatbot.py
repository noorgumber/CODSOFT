import random
import re

responses = {
   "hello": ["Hey, how can I help you?", "Hi there", "Hello"],
   "hi": ["Hey, how can I help you?", "Hi there", "Hello"],
   "hey" : ["Hey, how can I help you?", "Hi there", "Hello"],
   "how are you": ["I am doing good", "I am doing great", "Perfectly fine"],
   "who created you": ["I was created by Noor Gumber"],
   "thanks":["You're welcome", "No problem"],
   "how old are you": ["I am timeless"],
   "what are you doing": ["I am currently having a chat with you"],
   "quit": ["Bye byee, see you later", "goodbyee, it was nice chatting with you"],
   "bye": ["Bye byee, see you later", "goodbyee, it was nice chatting with you"]
}

default_response=[
    "I am not sure how to respond to that",
    "Can you please rephrase that?",
    "Please tell me more about what do you mean."
]

def clean_input(text):
   
    return re.sub(r'[^\w\s]', '', text.lower()).strip()

def get_response(user_input):
    user_input_lower= user_input.lower()

    for key, possible_res in responses.items():
        if key in user_input_lower:
            return random.choice(possible_res)
        
    return random.choice(default_response)

def chatbot():
    print("Hello I'm a chatbot and I just came into this world.")
    while True:
        user_input=input("You: ")

        if user_input.lower() in ["bye", "quit"]:
            res = get_response(user_input)
            print(f"ChatBot: {res}")
            break
        res = get_response(user_input)
        print(f"ChatBot: {res}")

chatbot()
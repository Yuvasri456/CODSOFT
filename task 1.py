import re
def simple_chatbot(user_input):
    user_input = user_input.lower()
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'explain about|define about ':'say in clear manner i will try to provid' ,
        r'can you show me a image |describe a structure':'sorry i can not provid the image i am  a content based tool ',
        r'how are you|how are you doing': 'I am a chatbot and I do not have feelings, but thanks for asking!',
        r'your name|who are you': 'I am a simple rule-based chatbot. You can call me ChatBot.',
        r'bye|goodbye|see you': 'Goodbye! If you have more questions, feel free to ask.',
        r'\b(?:thanks?|thank you)\b': 'You\'re welcome!',
        r'\b(?:yes|yeah|sure)\b': 'Great!',
        r'\b(?:no|nope)\b': 'Okay, let me know if you change your mind.',
        r'\b(?:help|what can you do)\b': 'I can provide information and answer questions. Feel free to ask anything!',
        r'\b(?:can you provid pdf |can you convert into word document )\b':'sorry i cant provide please use any other platform',
        r'\b(?:give with output|generate code output)\b':'sorry it should do it by yourself',
    }
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I didn't understand that. Can you please ask me something else?"
print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Simple Chatbot: Goodbye! see you later  Have a great life ahead")
        break
    response = simple_chatbot(user_input)
    print("Simple Chatbot:", response)

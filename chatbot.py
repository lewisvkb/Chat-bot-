import random

class Chatbot:
    def __init__(self):
        self.greetings = ['Hello!', 'Hi there!', 'Greetings!', 'Howdy!']
        self.farewells = ['Goodbye!', 'See you later!', 'Take care!', 'Farewell!']

    def greet(self):
        return random.choice(self.greetings)

    def farewell(self):
        return random.choice(self.farewells)

    def respond_to_query(self, query):
        # Simple response logic
        if 'how are you' in query.lower():
            return "I'm just a bot, but thanks for asking!"
        elif 'your name' in query.lower():
            return "I'm a chatbot created by you!"
        elif 'bye' in query.lower():
            return self.farewell()
        else:
            return "I'm not sure how to respond to that."

if __name__ == '__main__':
    bot = Chatbot()
    print(bot.greet())
    while True:
        user_input = input('You: ')
        response = bot.respond_to_query(user_input)
        print('Bot:', response)
        if 'bye' in user_input.lower():
            break
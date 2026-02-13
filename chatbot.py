import random
import json
from datetime import datetime

class Chatbot:
    def __init__(self, name="ChatBot"):
        self.name = name
        self.conversation_history = []
        self.user_name = None
        
        # Knowledge base
        self.knowledge = {
            "hello": ["Hey! How's it going?", "Hi there! What's up?", "Hello! Nice to see you!"],
            "how are you": ["I'm doing great, thanks for asking!", "I'm fantastic! How about you?", "All good here! How are you doing?"],
            "what is your name": ["I'm " + name + ", your friendly chatbot!", "You can call me " + name + "!", "I'm " + name + ", nice to meet you!"],
            "who are you": ["I'm " + name + ", an AI chatbot here to chat with you!", "I'm " + name + ", your conversation buddy!"],
            "how old are you": ["I was just created today! I'm brand new!", "I'm timeless!", "Age is just a number, right?"],
            "what can you do": ["I can chat with you about pretty much anything!", "I'm here to have a conversation and maybe help you out!", "I can listen, respond, and keep you company!"],
            "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? He was outstanding in his field!", "Why don't eggs tell jokes? They'd crack each other up!"],
            "how's the weather": ["I don't have access to weather data, but I hope it's nice where you are!", "I'm inside, so I wouldn't know! Is it nice out?", "Can't check the weather, but I hope you're having a beautiful day!"],
            "goodbye": ["Goodbye! It was nice chatting with you!", "See you later! Thanks for the conversation!", "Take care! Come back and chat soon!"],
            "bye": ["Bye! Have an awesome day!", "See you later, friend!", "Catch you later!"],
            "thanks": ["You're welcome!", "Happy to help!", "Anytime! That's what I'm here for!"],
            "thank you": ["You're very welcome!", "My pleasure!", "Always glad to help!"]
        }
        
        self.fallback_responses = [
            "That's interesting! Tell me more about that.",
            "I see! What else do you want to talk about?",
            "Hmm, I'm not sure I understand. Could you rephrase that?",
            "That's cool! Anything else on your mind?",
            "Interesting point! What made you think of that?",
            "I'd love to know more about that!",
            "Tell me more - I'm listening!",
            "That's a great thought!"
        ]

    def get_response(self, user_input):
        """Generate a contextual response"""
        user_input_lower = user_input.lower().strip()
        
        # Store in conversation history
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "bot": None
        })
        
        # Check for exact or partial matches in knowledge base
        for key, responses in self.knowledge.items():
            if key in user_input_lower:
                response = random.choice(responses)
                self.conversation_history[-1]["bot"] = response
                return response
        
        # If no match found, use a fallback response
        response = random.choice(self.fallback_responses)
        self.conversation_history[-1]["bot"] = response
        return response

    def start_conversation(self):
        """Start an interactive conversation loop"""
        print("\n" + "="*50)
        print(f"🤖 Welcome to {self.name}!")
        print("="*50)
        print("Type 'exit' or 'quit' to end the conversation.\n")
        
        # Initial greeting
        greeting = random.choice(self.knowledge["hello"])
        print(f"{self.name}: {greeting}\n")
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Skip empty input
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    farewell = random.choice(self.knowledge["goodbye"])
                    print(f"{self.name}: {farewell}\n")
                    break
                
                # Get and display response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

    def save_conversation(self, filename="conversation.json"):
        """Save conversation history to a file"""
        with open(filename, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
        print(f"\nConversation saved to {filename}")

    def display_conversation(self):
        """Display the entire conversation"""
        print("\n" + "="*50)
        print("CONVERSATION HISTORY")
        print("="*50)
        for entry in self.conversation_history:
            print(f"You: {entry['user']}")
            print(f"{self.name}: {entry['bot']}\n")


if __name__ == '__main__':
    # Create and start the chatbot
    bot = Chatbot("ChatBot")
    bot.start_conversation()
    
    # Optional: Save and display conversation history
    # bot.save_conversation()
    # bot.display_conversation()
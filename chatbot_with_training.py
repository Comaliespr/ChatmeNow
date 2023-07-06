import json
import random
class ChatbotModel:
    def __init__(self, data):
        self.data = data
    def generate_response(self, message):
        # Find the intent of the message.
        intent = self.find_intent(message)
        # Get the response for the intent.
        response = self.data[intent]
        # If there is no response for the intent, generate a random response.
        if response is None:
            response = random.choice(self.data["default"])
        return response
    def find_intent(self, message):
        # For each intent in the data, check if the message matches the intent.
        for intent in self.data:
            if self.match_intent(message, intent):
                return intent
        # If no intent matches, return None.
        return None
    def match_intent(self, message, intent):
        # For each word in the message, check if it is in the intent.
        for word in message.split():
            if word not in intent:
                return False
        # If all words in the message are in the intent, return True.
        return True
    def handle_unknown_intent(self, message):
        # Generate a random response.
        response = random.choice(self.data["default"])
        # Add the message to the training data.
        self.data["training_data"].append({
            "message": message,
            "intent": None
        })
        return response
    def learn_from_user(self, message, intent):
        # Add the message and intent to the training data.
        self.data["training_data"].append({
            "message": message,
            "intent": intent
        })
if __name__ == "__main__":
    # Load the data.
    with open("data.json") as f:
        data = json.load(f)
    # Create the model.
    model = ChatbotModel(data)
    # Start the conversation.
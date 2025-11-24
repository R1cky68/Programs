# Textblob is a python library for processing textual data, providing an API for common NLP (natural language processing) tests, it's good at its sentimental analysis (so it can analyse the sentiments from posts, images, text, etc) as either positive, negative, or neutral. This is useful for chatbots, post analysis, reviews, etc to understand the human emotional tone
from textblob import TextBlob

# Defining the ChatBot class for interaction. The init method initialises the chatbot object. Line 7 creates an instance variable which initalises it wihtin an empty textblob object. This object will serve as our tool with sentimental analysis
class Chatbot:
    def __init__(self):
        self.sentiment_analyzer = TextBlob("")

    def start_chat(self):
        print("Chatbot: What's good?")

        #This section initiates an infinite loop, ensuring continuous interaction until it's expliclicity interrupted. The second line stores user input within that variable and removes adjacent white spaces
        while True:
            user_message = input("You: ").strip()
    
    # Now here we calculate the sentiment polarity score, where the sentiment_score is the chatbot's EQ (gauging postivity/negativity in user input) 
            self.sentiment_analyzer = TextBlob(user_message)
            sentiment_score = self.sentiment_analyzer.sentiment.polarity

    # So all this means the chatbot produces a message and prints the sentiment score, closer to 1 = positive sentiment and vice versa, being 0 is neutral sentiment
    # You can additionally alter the message to ask questions, that can help the customer get to the next steps (by adding a call to action within the negative sentiment)
            if sentiment_score > 0:
                chatbot_message = f"Chatbot: That's good to hear bro! \n Score: {sentiment_score}"
            elif sentiment_score < 0:
                chatbot_message = f"Chatbot: Ohh damn man that sucks \n Score: {sentiment_score}"
            else:
                chatbot_message = f"Chatbot: All righty, keep going \n Score: {sentiment_score}"

            print(chatbot_message)
            print(sentiment_score)
    
# Recreate the chatbot and start the loop here
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new ChatBot instance
chatbot = ChatBot(
    "Example Bot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="database.db"
)

# Train the chatbot with the ChatterBot English corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Start a conversation with the chatbot
response = chatbot.get_response("Hello, how are you today?")
response2= chatbot.get_response("What else is delicious?")
print(response)
print(response2)


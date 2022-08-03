from chatterbot.trainers import ChatterBotCorpusTrainer

from chatbot import chatbot

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "./temp/convo.yml"
)
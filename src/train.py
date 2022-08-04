from chatterbot.trainers import ChatterBotCorpusTrainer

from chatbot import chatbot

trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train(
    "./convo.yml",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.sports",
    "chatterbot.corpus.english.trivia",
    "chatterbot.corpus.english.science",
    "chatterbot.corpus.english.ai",
    "chatterbot.corpus.english.movies",
    "chatterbot.corpus.english.emotion",
    "chatterbot.corpus.english.humor",
    "chatterbot.corpus.english.botprofile",
)

import telebot
import openai


engine = "text-davinci-003"

name = 'key.txt'
name_api = 'key_api.txt'

file = open(name, "r")
file_api = open(name_api, "r")

z = file.read()

openai.api_key = file_api.read()
bot = telebot.TeleBot(token=z)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я чат бот, просто напиши мне вопрос и я отвечу!)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	request = message.text
	print(request)
	bot.reply_to(message, "запрос в обработке")
	completion = openai.Completion.create(engine=engine,
										  prompt=request,
										  temperature=0.5,
										  max_tokens=2000)
	response = completion.choices[0]['text']
	print(response)
	bot.reply_to(message, response)

bot.polling()

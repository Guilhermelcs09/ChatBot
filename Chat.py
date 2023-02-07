import telebot

Chave_api = ''

bot = telebot.TeleBot(Chave_api)


@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    bot.reply_to(mensagem, """
   MUITO BOM SABER QUE VOCÊ TEM INTERESSE EM NOSSO CURSOS.FACA A COMPRA DO CURSO QUE TEM INTERESSE ATRAVES DO LINK ABAIXO E TENHA O ACESSO LIBERADO
https://youtu.be/rpbIbwccRTk""")


@ bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.reply_to(mensagem, ''' NOS DA GUILHERME CURSO TEMOS OS SEGUINTES CURSOS
DISPONIVEIS:
Curos de Java - R$100
Curso de Python - R$200
Curso de Css - R$300
Curso de C - R$400
Analise de dados - R$500''')


@ bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.reply_to(mensagem, ''' 
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate eos enim laboriosam consequatur, ea iusto asperiores ipsam blanditiis sequi quisquam dolore voluptas omnis iste numquam fuga ipsa fugit vitae illo
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate eos enim laboriosam consequatur, ea iusto asperiores ipsam blanditiis sequi quisquam dolore voluptas omnis iste numquam fuga ipsa fugit vitae illo.Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate eos enim laboriosam consequatur, ea iusto asperiores ipsam blanditiis sequi quisquam dolore voluptas omnis iste numquam fuga ipsa fugit vitae illo.Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate eos enim laboriosam consequatur, ea iusto asperiores ipsam blanditiis sequi quisquam dolore voluptas omnis iste numquam fuga ipsa fugit vitae illo.''')


def verificar(mensagem):
    return True


@ bot.message_handler(func=verificar)
def responder(mensagem):
    texto = '''
OLA SOMOS DA GUILHERME CURSOS,É UM PRAZER FALAR COM VOCÊ.COMO POSSO AJUDAR?(Click na opção desejada):
/opcao1 comprar cursos
/opcao2 quais cursos temos disponiveis
/opcao3 um pouco sobre nos
QUALQUER OUTRA RESPOSTA SERA INVALIDA,CLIQUE EM ALGUMA OPÇÃO'''
    bot.reply_to(mensagem, texto)


bot.polling()

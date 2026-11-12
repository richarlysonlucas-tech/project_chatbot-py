import re
import unicodedata
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

print("chatbot Verdinho - (BateriaLimpa (seja grato para encerrar a conversa))")

REGRAS = {
    r"\b(oi|bom|boa|chat)": "Olá! Sou o assistente do BateriaLimpa. Como posso ajudar?",
    r"\b(onde|ponto|loca|endere)": "Temos pontos de coleta em Olinda: Patteo (Casa Caiada), Ecoestação Peixinhos e Varadouro.",
    r"\b(cust|grat|pagar)": "Não. O descarte nos pontos indicados é totalmente gratuito!",
    r"\b(dados|apagar|backup)": "Basta somente fazer um backup dos dados e, posteriormente, restaurar o aparelho eletrônico para as configurações de fábrica antes de entregar.",
    r"\b(obrigad|valeu|xa|tchau)": "Por nada!"
}

def responder(entrada):
    entrada = entrada.lower()
    for padrao, resposta in REGRAS.items():
        if re.search(padrao, entrada):
            return resposta
    return "Pergunte sobre endereços de entrega, custos de descarte e dados do aparelho. Desculpe o meu entendimento!"

while True:
    texto = input("Você: ")

    if re.search(r"\b(obrigad|valeu|xa|tchau)", texto):
        print("Verdinho (bot): Até mais!")
        break

    print("Verdinho (bot): ", responder(texto))

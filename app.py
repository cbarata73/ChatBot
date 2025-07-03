import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas?':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'capital de portugal': "Lisboa",
        'como te chamas': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'historia de portugal': 'Portugal tem uma rica história...',
        'cozinhar': 'Cozinhar é uma arte que envolve a preparação de alimentos...',
        'sabes programar': 'Sim, posso ajudar com programação!',
        'programar': 'Programar é o processo de escrever código para criar software...',
        'desenvolvimento web': 'O desenvolvimento web envolve a criação de sites e aplicações web...',
        'desenvolvimento de software': 'O desenvolvimento de software é o processo de criar programas e aplicações...',
        'desenvolvimento de jogos': 'O desenvolvimento de jogos é a criação de jogos eletrônicos...',
        'desenvolvimento de aplicativos móveis': 'O desenvolvimento de aplicativos móveis é a criação de aplicativos para dispositivos móveis...',
        'ia': 'A inteligência artificial é um campo da ciência da computação que se concentra na criação de sistemas que podem realizar tarefas que normalmente requerem inteligência humana.',
        'machine learning': 'O aprendizado de máquina é um subcampo da inteligência artificial que se concentra no desenvolvimento de algoritmos que permitem que os computadores aprendam com os dados.',
        'deep learning': 'O aprendizado profundo é uma subárea do aprendizado de máquina que utiliza redes neurais profundas para modelar dados complexos.',
        'saúde': 'A saúde é um estado de completo bem-estar físico, mental e social, e não apenas a ausência de doenças ou enfermidades.',
        'problemas saúde': 'Problemas de saúde podem variar de leves a graves e podem afetar qualquer parte do corpo.',
        ('indisposição', 'sintomas de indisposição', 'estou com sintomas de indisposição'): 'Sintomas de indisposição podem incluir fadiga, dor de cabeça, náusea e outros sinais de que algo não está bem.',
        'sintomas': 'Sintomas são sinais ou indicações de uma condição médica ou doença.',
        }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'

    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()

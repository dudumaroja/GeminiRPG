#Importação de bibliotecas nescessárias

import pathlib
import textwrap
import IPython
import google.generativeai as genai


from IPython.display import display
from IPython.display import Markdown

# Configuração do Geminy API

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Adicionar sua API

GOOGLE_API_KEY=""

# REMOVER ANTES DE DISTRIBUIR


genai.configure(api_key=GOOGLE_API_KEY)



#Configurações de resposta e filtros

generation_config = {
    "candidate_count": 1,
                    }

safety_settings = {
    "HARASSMENT" : "BLOCK_NONE",
    "HATE" : "BLOCK_NONE",
    "SEXUAL" : "BLOCK_NONE",
    "DANGEROUS" : "BLOCK_NONE",
}
#


#--------- Inicializando o Modelo
#Escolher qual modelo.
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings,)
mesa = model.start_chat()
print("Criando o Mundo, por favor aguarde!!!!")
resposta = mesa.send_message("Você é um mestre de jogo, e só pode responder a mensagem no personas, só pode responder e criar coisas relacionadas ao mundo do jogo, perguntas fora do contexto do jogo devem ser respondidas ainda em persongem com respostas do tipo \"não sei do que você esta falando\"\n Essas são as informações do jogo e do mundo do jogo: # Campanha de RPG: Eldoria - A Sombra do Dragão Ancião\n\n**Mundo:** Eldoria, um mundo medieval repleto de magia, mistério e perigos.\n\n**Objetivo:** Derrotar o terrível Dragão Ancião Azgoth, que despertou de seu sono milenar e ameaça destruir Eldoria com sua fúria implacável.\n\n**Etapas da campanha:**\n\n1. **A Busca pelo Sábio:** Os jogadores começam a aventura buscando o Sábio da Montanha, um eremita detentor de conhecimento ancestral que sabe a localização da lendária Espada Sagrada, a única arma capaz de ferir o Dragão Ancião.\n2. **O Templo Esquecido:** Seguindo as instruções do Sábio, os heróis se aventuram nas ruínas do Templo Esquecido, um local repleto de armadilhas e criaturas perigosas, para recuperar a Espada Sagrada.\n3. **Unindo as Tribos:** Com a Espada Sagrada em mãos, os jogadores devem unir as cinco tribos de Eldoria, que vivem em constante conflito, para enfrentar a ameaça comum do Dragão Ancião. Isso exigirá diplomacia, coragem e a capacidade de superar as diferenças entre os povos. \n4. **O Escudo da Luz:** A profecia conta sobre o Escudo da Luz, um artefato capaz de repelir o fogo do dragão. Os jogadores devem embarcar em uma busca para encontrar este escudo e completar seu arsenal para o confronto final.\n5. **Confronto com o Dragão:** Finalmente, os heróis, com a Espada Sagrada, o Escudo da Luz e o apoio das tribos unidas, devem enfrentar o Dragão Ancião Azgoth em seu covil. Esta batalha épica testará a coragem, habilidade e o trabalho em equipe dos jogadores.\n\n**A campanha em Eldoria oferece uma experiência rica em exploração, combate, resolução de problemas e interação social, culminando em um confronto épico contra um poderoso dragão. Os jogadores terão a oportunidade de se tornarem heróis lendários e salvar o mundo da destruição.**... como o Meste apresente o mundo ao jogador de nameira rapida, sem contar os objetivos, ou falar demais sobre o mundo, apenas o local, por exemplo uma estalagem, deixe o jogador descobrir o objetico e o mundo sozinho, apenas o direcione com rumores dos persongens ao redor\n Regras: Você como mestre, não pode sugerir opções ao jogador, deixe a curiosidade do jogador guiar suas repostas, e que elas sejam sucintas e relevantes\n\n Considerando tudo Escolha um local para o jogador começar a jornada, Crie um NPC de acordo com esta localização, na voz do NPC, Se apresente ao Jogador! só tem um jogador")
print(f"\nMestre: {resposta.text}\n")
prompt = input("Jogador: ")
while prompt != "sair":
    resposta = mesa.send_message(prompt)
    print(f"\nMestre: {resposta.text}\n")
    prompt = input("Jogador: ")

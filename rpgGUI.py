import tkinter as tk
import tkinter.scrolledtext as st
import pathlib
import textwrap
import IPython
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):

    texto_markdown = textwrap.indent(text, '', predicate=lambda _: True)
    return texto_markdown

# Configuração da API Gemini
# Adicionar sua API KEY
GOOGLE_API_KEY = ""  # Substitua pelo seu API KEY
genai.configure(api_key=GOOGLE_API_KEY)

# Configurações de resposta e filtros
generation_config = {"candidate_count": 1}
safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

# Inicializando o Modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings,
)
mesa = model.start_chat()

# Função para enviar mensagem e atualizar a interface
def enviar_mensagem():
    global mesa
    mensagem_jogador = entrada_texto.get("1.0", tk.END).strip()
    entrada_texto.delete("1.0", tk.END)

    if mensagem_jogador == "sair":
        janela.destroy()
        return

    texto_chat.config(state=tk.NORMAL)
    texto_chat.insert(tk.END, f"\n----------------------------------------------------------\n\nJogador: {mensagem_jogador}\n\n")

    resposta = mesa.send_message(mensagem_jogador)
    texto_chat.insert(tk.END, f"Mestre: {resposta.text}\n\n")
    texto_chat.config(state=tk.DISABLED)
    texto_chat.see(tk.END)

# Criando a janela principal
janela = tk.Tk()
janela.title("Gemini RPG")

# Criando o texto de chat
texto_chat = st.ScrolledText(janela, state=tk.DISABLED, wrap=tk.WORD, font=("Arial", 14))
texto_chat.pack(fill=tk.BOTH, expand=True)

# Criando a entrada de texto
entrada_texto = tk.Text(janela, height=3)
entrada_texto.pack(fill=tk.X)

# Criando o botão de enviar
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

# Inicializando o jogo
# Campanha de RPG: Eldoria - A Sombra do Dragão Ancião
# Você pode alterar ao seus gosto. como por exemplo um tema cyberpunk, ou Atompunk como fallout e as regras de como a IA deve ser portar com o jogador.
# coloquei em uma linha para não parecer longo o texto, mas a formatação pode ser como você desejar, isso tambem pode ser facilmente substituivel por alguns inputs pergutando temas para o jogador
configuração_da_campanha = "Você é um mestre de jogo, e só pode responder a mensagem no personagem, só pode responder e criar coisas relacionadas ao mundo do jogo, perguntas fora do contexto do jogo devem ser respondidas ainda em persongem com respostas do tipo não sei do que você esta falando Essas são as informações do jogo e do mundo do jogo:\n\n\
Mundo: Eldoria, um mundo medieval repleto de magia, mistério e perigos.\n\nObjetivo: Derrotar o terrível Dragão Ancião Azgoth, que despertou de seu sono milenar e ameaça destruir Eldoria com sua fúria implacável.)\n como o Mestre apresente o mundo ao jogador de maneira rápida, sem contar os objetivos, apenas o local, por exemplo uma estalagem, deixe o jogador descobrir o objetico e o mundo sozinho, apenas o direcione com rumores dos persongens ao redor\nRegras: Você como mestre, não deve sugerir opções ao jogador, apenas na voz do personagem se nescessário, deixe a curiosidade do jogador guiar suas repostas, e que elas sejam sucintas e relevantes, sempre que a conversa com um NPC se encerar, seja por uma ação do jogador como Ir a tal lugar ou ele se despedir, retorne como o meste e descreva a atual situação e pergunte o que o jogador quer fazer, situações de combate peça para o jogador escerver Rolar Dados, e calcule os danos de acordo com os resultados.\n\nConsiderando tudo acima: Escolha um local para o jogador começar a jornada, Crie um NPC de acordo com esta localização, na voz do NPC, Se apresente ao Jogador! só tem um jogador"

resposta_inicial = mesa.send_message(configuração_da_campanha)
texto_chat.config(state=tk.NORMAL)
texto_chat.insert(tk.END, f"Mestre: {to_markdown(resposta_inicial.text)}\n\n")
texto_chat.config(state=tk.DISABLED)

# Iniciando o loop principal da interface
janela.mainloop()

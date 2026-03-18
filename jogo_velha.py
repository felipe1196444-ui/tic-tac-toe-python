import tkinter as tk
from tkinter import messagebox

# Variáveis globais para controlar o jogo
tabuleiro = [''] * 9  # Lista com 9 posições (0-8)
jogador_atual = 'X'   # Começa com o jogador X
jogo_ativo = True     # Controla se o jogo está ativo

# Função para fazer um movimento
def fazer_movimento(indice):
    global jogador_atual, jogo_ativo
    
    # Verifica se o espaço está vazio e o jogo está ativo
    if tabuleiro[indice] == '' and jogo_ativo:
        tabuleiro[indice] = jogador_atual
        botoes[indice].config(text=jogador_atual, state='disabled')
        
        # Verifica se há um vencedor
        if verificar_vencedor():
            messagebox.showinfo('Fim de Jogo', f'Jogador {jogador_atual} ganhou! 🎉')
            jogo_ativo = False
            reiniciar_jogo()
        # Verifica se é um empate
        elif '' not in tabuleiro:
            messagebox.showinfo('Fim de Jogo', 'Empate! 🤝')
            jogo_ativo = False
            reiniciar_jogo()
        else:
            # Alterna entre os jogadores
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
            label_status.config(text=f'Vez do jogador: {jogador_atual}')

# Função para verificar se há um vencedor
def verificar_vencedor():
    # Todas as combinações vencedoras possíveis
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]               # Diagonais
    ]
    
    # Verifica cada combinação
    for combinacao in combinacoes_vencedoras:
        if (tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] != ''):
            return True
    return False

# Função para reiniciar o jogo
def reiniciar_jogo():
    global tabuleiro, jogador_atual, jogo_ativo
    
    tabuleiro = [''] * 9
    jogador_atual = 'X'
    jogo_ativo = True
    
    # Limpa todos os botões
    for i in range(9):
        botoes[i].config(text='', state='normal')
    
    label_status.config(text=f'Vez do jogador: {jogador_atual}')

# Cria a janela principal
janela = tk.Tk()
janela.title('Jogo da Velha')
janela.geometry('400x500')

# Cria um label para mostrar o status do jogo
label_status = tk.Label(janela, text=f'Vez do jogador: {jogador_atual}', font=('Arial', 14), pady=10)
label_status.pack()

# Cria um frame para os botões do jogo
frame_jogo = tk.Frame(janela)
frame_jogo.pack(pady=10)

# Cria os 9 botões do tabuleiro (3x3)
botoes = []
for i in range(9):
    botao = tk.Button(frame_jogo, text='', font=('Arial', 20), width=6, height=3,
                      command=lambda indice=i: fazer_movimento(indice))
    botao.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    botoes.append(botao)

# Cria um botão para reiniciar o jogo
botao_reiniciar = tk.Button(janela, text='Reiniciar Jogo', font=('Arial', 12), 
                            command=reiniciar_jogo, bg='#4CAF50', fg='white', padx=20, pady=10)
botao_reiniciar.pack(pady=10)

# Inicia a aplicação
janela.mainloop()
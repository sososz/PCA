import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Quiz do Descarte Correto')
        self.root.geometry('400x300')

        self.perguntas = [
            {
                'pergunta': 'Como resíduos perigosos, como pilhas e baterias, devem ser descartados corretamente?',
                'opcoes': ['Em rios', 'Em lixeiras comuns', 'Em postos de coletas especificos'],
                'resposta': 'Em postos de coletas especificos'
            },
            {
                'pergunta': 'Em qual lixeira jogamos o plástico?',
                'opcoes': ['Vermelho', 'Azul', 'Verde', 'Amarelo'],
                'resposta': 'Vermelho'
            },
            {
                'pergunta': 'Qual é a principal fonte de poluição dos oceanos?',
                'opcoes': ['Plástico', 'Petróleo', 'Metais Pesados', 'Esgoto'],
                'resposta': 'Plástico'
            },
            {
            'pergunta':'Qual a importância da compostagem no descarte sustentável de resíduos orgânicos?',
            'opcoes':['Converter resíduos orgânicos em adubo', 'Reduzir o consumo de plástico', 'Não contaminação do solo'],
            'resposta':'Convertee resíduos orgânicos em adubo'
            },
            {
            'pergunta':'Qual cor da lixeira é descartado o vidro?',
            'opcoes':['Azul', 'Marrom', 'Verde', 'Amarelo'],
            'resposta':'Verde'    
            }      
            ]

        self.pergunta_atual = 0
        self.respostas = []

        self.label_pergunta = tk.Label(root, text='')
        self.label_pergunta.pack(pady=10)

        self.opcoes_var = tk.StringVar()
        self.opcoes_var.set('Selecione uma opção')

        self.opcoes_menu = tk.OptionMenu(root, self.opcoes_var, *self.perguntas[self.pergunta_atual]['opcoes'])
        self.opcoes_menu.pack(pady=10)

        self.botao_proximo = tk.Button(root, text='Próxima Pergunta', command=self.avancar_pergunta)
        self.botao_proximo.pack(pady=10)

        self.atualizar_pergunta()

    def avancar_pergunta(self):
        resposta = self.opcoes_var.get()
        if resposta:
            self.respostas.append(resposta)
            self.opcoes_var.set('Selecione uma opção')

            self.pergunta_atual += 1
            if self.pergunta_atual < len(self.perguntas):
                self.atualizar_pergunta()
            else:
                self.exibir_resultado()

    def atualizar_pergunta(self):
        pergunta_atual = self.perguntas[self.pergunta_atual]
        self.label_pergunta.config(text=pergunta_atual['pergunta'])
        self.opcoes_menu['menu'].delete(0, 'end')
        for opcao in pergunta_atual['opcoes']:
            self.opcoes_menu['menu'].add_command(label=opcao, command=tk._setit(self.opcoes_var, opcao))

    def exibir_resultado(self):
        messagebox.showinfo('Resultado', f'Você acertou {self.calcular_acertos()} perguntas!')
        self.root.destroy()

    def calcular_acertos(self):
        return sum([1 for resp, correta in zip(self.respostas, [pergunta['resposta'] for pergunta in self.perguntas]) if resp == correta])

if __name__ == '__main__':
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
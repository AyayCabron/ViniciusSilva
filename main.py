import tkinter as tk
from tkinter import font
import random

class RPGGame:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG Interativo")
        self.root.geometry("1600x900")  # Tamanho da janela
        self.root.configure(bg="#2e2e2e")

        # Estilos de fonte
        custom_font = font.Font(family="Helvetica", size=12)
        title_font = font.Font(family="Helvetica", size=20, weight="bold")

        # Título
        self.title_label = tk.Label(root, text="RPG Interativo", bg="#2e2e2e", fg="#bf3eb0", font=title_font)
        self.title_label.pack(pady=10)

        # Tela principal
        self.text_area = tk.Text(root, height=20, width=100, bg="#1e1e1e", fg="white", font=custom_font, bd=0, wrap=tk.WORD)
        self.text_area.pack(pady=10)

        # Mensagem de boas-vindas
        self.welcome_message = "Bem-vindo ao RPG Interativo! Clique em 'Continuar' para começar.\n"
        self.update_text_area(self.welcome_message)

        # Botões de ação
        self.button_frame = tk.Frame(root, bg="#2e2e2e")
        self.button_frame.pack(pady=10)

        self.continue_button = tk.Button(self.button_frame, text="Continuar", command=self.continue_game, bg="#bf3eb0", fg="white", font=custom_font, width=15)
        self.continue_button.pack(side=tk.LEFT, padx=5)

        self.attack_button = tk.Button(self.button_frame, text="Atacar", command=self.attack, bg="#bf3eb0", fg="white", font=custom_font, width=15)
        self.attack_button.pack(side=tk.LEFT, padx=5)

        self.roll_button = tk.Button(self.button_frame, text="Rolar Dados", command=self.show_roll_options, bg="#bf3eb0", fg="white", font=custom_font, width=15)
        self.roll_button.pack(side=tk.LEFT, padx=5)

        self.magic_button = tk.Button(self.button_frame, text="Usar Magia", command=self.show_magic_list, bg="#bf3eb0", fg="white", font=custom_font, width=15)
        self.magic_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Limpar", command=self.clear_text_area, bg="#bf3eb0", fg="white", font=custom_font, width=15)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Frame para a lista de magias
        self.magic_frame = tk.Frame(root, bg="#2e2e2e")
        self.magic_listbox = tk.Listbox(self.magic_frame, bg="#1e1e1e", fg="white", font=custom_font, width=50, height=10)
        self.magic_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.back_button = tk.Button(self.magic_frame, text="Voltar", command=self.hide_magic_list, bg="#bf3eb0", fg="white", font=custom_font)
        self.back_button.pack(side=tk.RIGHT, padx=10)

        self.populate_magic_list()
        self.magic_frame.pack(pady=10)

        self.magic_frame.pack_forget()  # Esconde a lista de magias inicialmente

        # Frame para opções de rolagem
        self.roll_frame = tk.Frame(root, bg="#2e2e2e")
        self.action_var = tk.StringVar(value="Atacar")  # Variável para armazenar a ação selecionada

        self.action_menu = tk.OptionMenu(self.roll_frame, self.action_var, "Atacar", "Defender", "Correr", "Persuadir", "Charme")
        self.action_menu.config(bg="#4e4e4e", fg="white", font=custom_font)
        self.action_menu.pack(side=tk.LEFT, padx=5)

        self.roll_action_button = tk.Button(self.roll_frame, text="Rolar", command=self.roll_dice, bg="#bf3eb0", fg="white", font=custom_font)
        self.roll_action_button.pack(side=tk.LEFT, padx=5)

        self.roll_frame.pack(pady=10)
        self.roll_frame.pack_forget()  # Esconde o frame de rolagem inicialmente

        # Variável para armazenar a magia selecionada
        self.selected_spell = None

        # Personagens e reações
        self.characters = {
            "Guerreiro": {
                "persuade_success": "O Guerreiro concorda com você e se junta à sua causa!",
                "persuade_failure": "O Guerreiro olha para você com desdém e se recusa a ouvir."
            },
            "Mago": {
                "persuade_success": "O Mago fica impressionado com suas palavras e decide ajudar.",
                "persuade_failure": "O Mago balança a cabeça, desapontado com sua falta de eloquência."
            },
            "Ladino": {
                "persuade_success": "O Ladino sorri e aceita a sua proposta.",
                "persuade_failure": "O Ladino ri de você, achando que você é um tolo."
            }
        }

    def populate_magic_list(self):
        spells = ["Fogo", "Gelo", "Raio", "Cura"]
        for spell in spells:
            self.magic_listbox.insert(tk.END, spell)

    def update_text_area(self, message):
        self.text_area.insert(tk.END, message)  
        self.text_area.see(tk.END)

    def continue_game(self):
        self.update_text_area("Você decide continuar sua jornada...\n")

    def attack(self):
        self.update_text_area("Você atacou o inimigo!\n")

    def show_roll_options(self):
        self.roll_frame.pack(pady=10)  # Mostra o frame de rolagem
        self.update_text_area("Escolha uma ação e role os dados:\n")

    def roll_dice(self):
        selected_action = self.action_var.get()
        result = random.randint(1, 20)  # Rolando um dado de 20 lados
        self.update_text_area(f"Você rolou um {result} para {selected_action}!\n")
        
        # Verifica se a ação é "Persuadir"
        if selected_action == "Persuadir":
            self.handle_persuasion(result)
        else:
            self.check_action_result(result, selected_action)

    def handle_persuasion(self, roll):
        # Defina a classe de dificuldade (CD) para a persuasão
        difficulty_class = 15  # Exemplo de CD para persuadir
        if roll >= difficulty_class:
            # Se a rolagem for bem-sucedida, escolha um personagem e mostre a resposta
            character_name = random.choice(list(self.characters.keys()))
            response = self.characters[character_name]["persuade_success"]
            self.update_text_area(response + f" Você persuadiu o {character_name}!\n")
        else:
            character_name = random.choice(list(self.characters.keys()))
            response = self.characters[character_name]["persuade_failure"]
            self.update_text_area(response + f" Você falhou em persuadir o {character_name}.\n")

    def check_action_result(self, roll, action):
        # Defina a classe de dificuldade (CD) para cada ação
        difficulty_classes = {
            "Atacar": 10,
            "Defender": 8,
            "Correr": 12,
            "Persuadir": 15,
            "Charme": 14
        }
        
        if action in difficulty_classes:
            difficulty_class = difficulty_classes[action]
            if roll >= difficulty_class:
                self.update_text_area(f"A ação '{action}' foi efetiva!\n")
            else:
                self.update_text_area(f"A ação '{action}' falhou!\n")

    def show_magic_list(self):
        self.magic_frame.pack(pady=10)  # Mostra a lista de magias
        self.update_text_area("Escolha uma magia:\n")

    def hide_magic_list(self):
        self.magic_frame.pack_forget()  # Esconde a lista de magias

        # Mostrar a magia selecionada
        if self.selected_spell:
            self.update_text_area(f"Você usou a magia: {self.selected_spell}!\n")
            self.selected_spell = None  # Reseta a seleção

    def clear_text_area(self):
        self.text_area.delete(1.0, tk.END)  # Limpa o Text Area

    def magic_selected(self, event):
        selected_index = self.magic_listbox.curselection()
        if selected_index:
            self.selected_spell = self.magic_listbox.get(selected_index)
            self.update_text_area(f"Você selecionou a magia: {self.selected_spell}\n")

if __name__ == "__main__":
    root = tk.Tk()  
    game = RPGGame(root)  

    # Bind the selection event to show the selected spell
    game.magic_listbox.bind('<<ListboxSelect>>', game.magic_selected)

    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import json
import os
from datetime import datetime
import csv
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Cores
COLOR_FG = "#ECEFF4"
COLOR_TIMER = "#88C0D0"
COLOR_ALERT = "#A3BE8C"
COLOR_WARNING = "#D08770"
COLOR_CLOSE_HOVER = "#BF616A" # Cor vermelha (hover) para o botão de fechar

class SpeedTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. REMOVER A BARRA DE TÍTULO E BORDAS PADRÃO
        self.overrideredirect(True)

        self.title("SpeedTracker Dev 3.1")
        self.geometry("500x320")

        if sys.platform == "win32":
            try:
                import pywinstyles
                pywinstyles.apply_style(self, "mica")
            except (ImportError, ValueError) as e:
                print(f"Pywinstyles não aplicado: {e}")
        
        # Variáveis para mover a janela
        self._offset_x = 0
        self._offset_y = 0
        
        # Variáveis de Estado
        self.tasks = []; self.current_task_index = -1
        self.seconds_remaining = 0; self.is_paused = False
        self.timer_job = None; self.log_file = "activity_log.csv"

        # Configuração Inicial
        self.create_widgets()
        self.setup_log_file()
        self.load_tasks()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)

        # 2. CRIAÇÃO DA BARRA DE TÍTULO PERSONALIZADA
        title_bar = ctk.CTkFrame(self, height=30, corner_radius=0)
        title_bar.grid(row=0, column=0, sticky="ew")
        title_bar.grid_columnconfigure(1, weight=1)

        title_label = ctk.CTkLabel(title_bar, text="✒️ SpeedTracker Dev", font=("Helvetica", 12))
        title_label.grid(row=0, column=0, padx=10, sticky="w")
        
        # Botão estilizado para "Arquivo"
        file_button = ctk.CTkButton(title_bar, text="Arquivo", width=80, height=22, command=self.open_roteiro_file)
        file_button.grid(row=0, column=2, padx=(0, 5), pady=4)

        # Botão estilizado para "Fechar"
        close_button = ctk.CTkButton(title_bar, text="✕", width=30, height=22, command=self.destroy, fg_color="transparent", hover_color=COLOR_CLOSE_HOVER)
        close_button.grid(row=0, column=3, padx=(0, 5), pady=4)

        # 3. IMPLEMENTAÇÃO DA FUNÇÃO DE ARRASTAR
        title_bar.bind("<ButtonPress-1>", self.on_press)
        title_bar.bind("<B1-Motion>", self.on_drag)
        title_label.bind("<ButtonPress-1>", self.on_press)
        title_label.bind("<B1-Motion>", self.on_drag)

        # --- Widgets Principais (restante da UI) ---
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        main_frame.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        font_action = ("Helvetica", 24, "bold"); font_task = ("Helvetica", 14); font_timer = ("Helvetica", 80, "bold")

        self.action_label = ctk.CTkLabel(main_frame, text="Bem-vindo!", font=font_action)
        self.action_label.grid(row=0, column=0, pady=(10, 10))

        self.task_label = ctk.CTkLabel(main_frame, text="Use o botão 'Arquivo' para carregar um roteiro.", font=font_task, wraplength=480)
        self.task_label.grid(row=1, column=0, pady=10, padx=10)
        
        self.timer_label = ctk.CTkLabel(main_frame, text="00:00", font=font_timer, text_color=COLOR_TIMER)
        self.timer_label.grid(row=2, column=0, pady=2)

        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.grid(row=3, column=0, pady=20)

        self.start_button = ctk.CTkButton(button_frame, text="Iniciar Roteiro", command=self.start_roteiro, font=("Helvetica", 14, "bold"), width=150, height=35)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = ctk.CTkButton(button_frame, text="Pausar", command=self.toggle_pause, font=("Helvetica", 14, "bold"), width=150, height=35, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10)

    # --- Funções para mover a janela ---
    def on_press(self, event):
        self._offset_x = event.x
        self._offset_y = event.y

    def on_drag(self, event):
        x = self.winfo_pointerx() - self._offset_x
        y = self.winfo_pointery() - self._offset_y
        self.geometry(f"+{x}+{y}")

    # --- Lógica do aplicativo (praticamente inalterada) ---
    def load_tasks(self, filepath="roteiro.json"):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = data.get("roteiro_speed_tracking", [])
                if not self.tasks: raise ValueError("JSON inválido.")
            self.reset_app_state()
            messagebox.showinfo("Sucesso", f"Roteiro '{os.path.basename(filepath)}' carregado!")
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
            messagebox.showerror("Erro ao Carregar", f"Não foi possível carregar o roteiro: {e}")
            self.tasks = []; self.reset_app_state()

    def reset_app_state(self):
        if self.timer_job: self.after_cancel(self.timer_job)
        self.current_task_index = -1; self.is_paused = False
        self.action_label.configure(text="Roteiro Carregado")
        self.task_label.configure(text="Clique em 'Iniciar Roteiro' para começar.")
        self.timer_label.configure(text="00:00")
        self.start_button.configure(text="Iniciar Roteiro", state=tk.NORMAL)
        self.pause_button.configure(text="Pausar", state=tk.DISABLED)

    def start_roteiro(self):
        self.start_button.configure(state=tk.DISABLED)
        self.next_task()

    def next_task(self):
        self.attributes('-topmost', False)
        if self.current_task_index >= 0 and self.current_task_index < len(self.tasks):
            self.log_activity(self.tasks[self.current_task_index])
        if self.timer_job: self.after_cancel(self.timer_job)
        self.current_task_index += 1
        if self.current_task_index < len(self.tasks):
            self.is_paused = False; task = self.tasks[self.current_task_index]
            self.action_label.configure(text=f"Ação: {task['acao']}")
            self.task_label.configure(text=task['tarefa_especifica_hoje'])
            self.pause_button.configure(text="Pausar", state=tk.NORMAL)
            self.countdown(task['tempo_minutos'] * 60)
        else:
            self.action_label.configure(text="Parabéns!"); self.task_label.configure(text="Você completou o roteiro.")
            self.timer_label.configure(text="✅"); self.start_button.configure(state=tk.NORMAL, text="Reiniciar")
            self.pause_button.configure(state=tk.DISABLED); self.attributes('-topmost', True)

    def countdown(self, seconds_left):
        if self.is_paused: self.seconds_remaining = seconds_left; return
        if seconds_left == 5: self.attributes('-topmost', True); self.lift(); self.focus_force(); self.bell(); self.timer_label.configure(text_color=COLOR_WARNING)
        self.seconds_remaining = seconds_left
        if seconds_left >= 0:
            mins, secs = divmod(seconds_left, 60)
            self.timer_label.configure(text=f"{mins:02d}:{secs:02d}")
            self.timer_job = self.after(1000, self.countdown, seconds_left - 1)
        else: self.task_finished_handler()

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        self.pause_button.configure(text="Retomar" if self.is_paused else "Pausar")
        if not self.is_paused: self.countdown(self.seconds_remaining)

    def task_finished_handler(self):
        self.timer_label.configure(text="Fim!", text_color=COLOR_ALERT)
        self.bell(); self.bell(); self.after(2000, self.next_task)
        self.timer_label.configure(text_color=COLOR_TIMER)

    def open_roteiro_file(self):
        filepath = filedialog.askopenfilename(title="Selecione um roteiro", filetypes=[("JSON files", "*.json")])
        if filepath: self.load_tasks(filepath)

    def setup_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(["timestamp", "acao", "tarefa_especifica", "duracao_minutos"])
    
    def log_activity(self, task):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([timestamp, task['acao'], task['tarefa_especifica_hoje'], task['tempo_minutos']])

if __name__ == "__main__":
    app = SpeedTrackerApp()
    app.mainloop()
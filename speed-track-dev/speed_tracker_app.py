import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import json
import os
import sys
from datetime import datetime
import csv

# --- Bloco de código para interagir com a API do Windows ---
if sys.platform == "win32":
    import ctypes
    from ctypes import wintypes
    GWL_STYLE = -16
    WS_CAPTION = 0x00C00000
    WS_THICKFRAME = 0x00040000

# --- LÓGICA PARA ENCONTRAR OS ARQUIVOS (A MUDANÇA PRINCIPAL) ---
def resource_path(relative_path):
    """ Obtém o caminho absoluto para o recurso, funciona para dev e para PyInstaller """
    try:
        # PyInstaller cria uma pasta temp e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Se não estiver empacotado, o base_path é o diretório do script
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# --- Define o caminho para os nossos arquivos de forma robusta ---
# Se você quiser que o .exe procure os arquivos ao lado dele, e não dentro dele,
# usamos uma lógica um pouco diferente:
if getattr(sys, 'frozen', False):
    # Estamos rodando como um .exe (empacotado)
    base_path = os.path.dirname(sys.executable)
else:
    # Estamos rodando como um script .py normal
    base_path = os.path.dirname(os.path.abspath(__file__))

# Agora definimos os caminhos que serão usados no app
ICON_PATH = os.path.join(base_path, "icon.ico")
ROTEIRO_PATH = os.path.join(base_path, "roteiro.json")
LOG_PATH = os.path.join(base_path, "activity_log.csv")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Cores
COLOR_TIMER = "#88C0D0"; COLOR_ALERT = "#A3BE8C"; COLOR_WARNING = "#D08770"; COLOR_CLOSE_HOVER = "#BF616A"

class SpeedTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SpeedTracker Dev")
        self.geometry("500x400")
        
        # Usa o caminho do ícone que definimos globalmente
        self.iconbitmap(ICON_PATH)
        
        if sys.platform == "win32":
            try:
                import pywinstyles
                pywinstyles.apply_style(self, "mica")
            except (ImportError, ValueError):
                pass

        self._offset_x = 0; self._offset_y = 0
        self.tasks = []; self.current_task_index = -1
        self.seconds_remaining = 0; self.is_paused = False
        self.timer_job = None
        
        # O log_file agora usa o caminho global
        self.log_file = LOG_PATH

        self.create_widgets()
        self.setup_log_file()
        self.load_tasks()

        self.after(10, self.remove_title_bar)

    def remove_title_bar(self):
        if sys.platform == "win32":
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            style = ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_STYLE)
            style = style & ~WS_CAPTION & ~WS_THICKFRAME
            ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_STYLE, style)
            self.update_idletasks()
    
    # ... O resto do código continua igual, mas usando as variáveis de caminho ...
    def create_widgets(self):
        # (Nenhuma mudança visual aqui, o código é o mesmo da v4.0)
        self.grid_columnconfigure(0, weight=1)
        title_bar = ctk.CTkFrame(self, height=30, corner_radius=0); title_bar.grid(row=0, column=0, sticky="ew"); title_bar.grid_columnconfigure(1, weight=1)
        title_label = ctk.CTkLabel(title_bar, text="✒️ SpeedTracker Dev", font=("Helvetica", 12)); title_label.grid(row=0, column=0, padx=10, sticky="w")
        file_button = ctk.CTkButton(title_bar, text="Arquivo", width=80, height=22, command=self.open_roteiro_file); file_button.grid(row=0, column=2, padx=(0, 5), pady=4)
        close_button = ctk.CTkButton(title_bar, text="✕", width=30, height=22, command=self.destroy, fg_color="transparent", hover_color=COLOR_CLOSE_HOVER); close_button.grid(row=0, column=3, padx=(0, 5), pady=4)
        title_bar.bind("<ButtonPress-1>", self.on_press); title_label.bind("<ButtonPress-1>", self.on_press); title_bar.bind("<B1-Motion>", self.on_drag); title_label.bind("<B1-Motion>", self.on_drag)
        main_frame = ctk.CTkFrame(self, fg_color="transparent"); main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10); main_frame.grid_columnconfigure(0, weight=1); self.grid_rowconfigure(1, weight=1)
        font_action = ("Helvetica", 24, "bold"); font_task = ("Helvetica", 14); font_timer = ("Helvetica", 80, "bold")
        self.action_label = ctk.CTkLabel(main_frame, text="Bem-vindo!", font=font_action); self.action_label.grid(row=0, column=0, pady=(10, 10))
        self.task_label = ctk.CTkLabel(main_frame, text="Use o botão 'Arquivo' para carregar um roteiro.", font=font_task, wraplength=480); self.task_label.grid(row=1, column=0, pady=10, padx=10)
        self.timer_label = ctk.CTkLabel(main_frame, text="00:00", font=font_timer, text_color=COLOR_TIMER); self.timer_label.grid(row=2, column=0, pady=20)
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent"); button_frame.grid(row=3, column=0, pady=20)
        self.start_button = ctk.CTkButton(button_frame, text="Iniciar Roteiro", command=self.start_roteiro, font=("Helvetica", 14, "bold"), width=150, height=35); self.start_button.pack(side=tk.LEFT, padx=10)
        self.pause_button = ctk.CTkButton(button_frame, text="Pausar", command=self.toggle_pause, font=("Helvetica", 14, "bold"), width=150, height=35, state=tk.DISABLED); self.pause_button.pack(side=tk.LEFT, padx=10)
    def on_press(self, event): self._offset_x = event.x; self._offset_y = event.y
    def on_drag(self, event): self.geometry(f"+{self.winfo_pointerx() - self._offset_x}+{self.winfo_pointery() - self._offset_y}")
    
    def load_tasks(self, filepath=None):
        if filepath is None:
            filepath = ROTEIRO_PATH # Usa o caminho global como padrão

        try:
            with open(filepath, "r", encoding="utf-8") as f: data = json.load(f); self.tasks = data.get("roteiro_speed_tracking", []);
            if not self.tasks: raise ValueError("JSON inválido.")
            self.reset_app_state(); messagebox.showinfo("Sucesso", f"Roteiro '{os.path.basename(filepath)}' carregado!")
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as e: messagebox.showerror("Erro ao Carregar", f"Não foi possível carregar '{os.path.basename(filepath)}'. Verifique se o arquivo está na mesma pasta que o executável."); self.tasks = []; self.reset_app_state()

    def open_roteiro_file(self):
        # Abre o diálogo de arquivo na pasta do executável
        filepath = filedialog.askopenfilename(
            title="Selecione um roteiro", 
            initialdir=base_path, # Começa a busca na pasta do app
            filetypes=[("JSON files", "*.json")])
        if filepath: self.load_tasks(filepath)
    
    def setup_log_file(self):
        # Usa a variável global LOG_PATH
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", newline="", encoding="utf-8") as f: csv.writer(f).writerow(["timestamp", "acao", "tarefa_especifica", "duracao_minutos"])
            
    # O resto das funções não precisa de alteração...
    def reset_app_state(self):
        if self.timer_job: self.after_cancel(self.timer_job);
        self.current_task_index = -1; self.is_paused = False
        self.action_label.configure(text="Roteiro Carregado"); self.task_label.configure(text="Clique em 'Iniciar Roteiro' para começar.")
        self.timer_label.configure(text="00:00"); self.start_button.configure(text="Iniciar Roteiro", state=tk.NORMAL)
        self.pause_button.configure(text="Pausar", state=tk.DISABLED)
    def start_roteiro(self): self.start_button.configure(state=tk.DISABLED); self.next_task()
    def next_task(self):
        self.attributes('-topmost', False)
        if 0 <= self.current_task_index < len(self.tasks): self.log_activity(self.tasks[self.current_task_index])
        if self.timer_job: self.after_cancel(self.timer_job)
        self.current_task_index += 1
        if self.current_task_index < len(self.tasks):
            self.is_paused = False; task = self.tasks[self.current_task_index]
            self.action_label.configure(text=f"Ação: {task['acao']}"); self.task_label.configure(text=task['tarefa_especifica_hoje'])
            self.pause_button.configure(text="Pausar", state=tk.NORMAL); self.countdown(task['tempo_minutos'] * 60)
        else:
            self.action_label.configure(text="Parabéns!"); self.task_label.configure(text="Você completou o roteiro.")
            self.timer_label.configure(text="✅"); self.start_button.configure(state=tk.NORMAL, text="Reiniciar")
            self.pause_button.configure(state=tk.DISABLED); self.attributes('-topmost', True)
    def countdown(self, seconds_left):
        if self.is_paused: self.seconds_remaining = seconds_left; return
        if seconds_left == 5: self.attributes('-topmost', True); self.lift(); self.focus_force(); self.bell(); self.timer_label.configure(text_color=COLOR_WARNING)
        self.seconds_remaining = seconds_left
        if seconds_left >= 0:
            mins, secs = divmod(seconds_left, 60); self.timer_label.configure(text=f"{mins:02d}:{secs:02d}")
            self.timer_job = self.after(1000, self.countdown, seconds_left - 1)
        else: self.task_finished_handler()
    def toggle_pause(self):
        self.is_paused = not self.is_paused; self.pause_button.configure(text="Retomar" if self.is_paused else "Pausar")
        if not self.is_paused: self.countdown(self.seconds_remaining)
    def task_finished_handler(self):
        self.timer_label.configure(text="Fim!", text_color=COLOR_ALERT); self.bell(); self.bell(); self.after(2000, self.next_task)
        self.timer_label.configure(text_color=COLOR_TIMER)
    def log_activity(self, task):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", newline="", encoding="utf-8") as f: csv.writer(f).writerow([timestamp, task['acao'], task['tarefa_especifica_hoje'], task['tempo_minutos']])

if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            from ctypes import windll
            myappid = 'speedtracker.dev.python.gui.1'
            windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except (ImportError, AttributeError):
            pass
    app = SpeedTrackerApp()
    app.mainloop()
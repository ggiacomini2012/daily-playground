import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import json
import os
import sys
from datetime import datetime
import csv
from functools import partial

# --- Bloco de código para interagir com a API do Windows ---
if sys.platform == "win32":
    import ctypes
    from ctypes import wintypes

    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000

# --- Lógica para encontrar os arquivos de forma robusta ---
if getattr(sys, "frozen", False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

ICON_PATH = os.path.join(base_path, "icon.ico")
ROTEIRO_PATH = os.path.join(base_path, "roteiro.json")
LOG_PATH = os.path.join(base_path, "activity_log.csv")
PROGRESS_PATH = os.path.join(base_path, "progress.json")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Cores
COLOR_TIMER = "#88C0D0"
COLOR_ALERT = "#A3BE8C"
COLOR_WARNING = "#D08770"
COLOR_CLOSE_HOVER = "#BF616A"
STATUS_COLORS = {"pending": "#5E6C84", "active": "#88C0D0", "completed": "#2ECC71"}


# --- 1. A NOVA CLASSE PARA A SPLASH SCREEN ---
class SplashScreen(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.overrideredirect(True)  # Remove as bordas e a barra de título
        width, height = 400, 200

        # Centraliza a janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        main_frame = ctk.CTkFrame(self)
        main_frame.grid(sticky="nsew", padx=20, pady=20)
        main_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            main_frame, text="SpeedTracker Dev", font=("Helvetica", 24, "bold")
        ).pack(pady=10)
        self.status_label = ctk.CTkLabel(
            main_frame, text="Carregando componentes...", font=("Helvetica", 12)
        )
        self.status_label.pack(pady=5)

        self.progress_bar = ctk.CTkProgressBar(main_frame, width=300)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=20, padx=20)

    def start_loading(self, on_done):
        """Inicia a animação da barra de progresso e chama on_done ao terminar."""
        self.on_done = on_done
        self.update_progress(0)

    def update_progress(self, value):
        if value < 1:
            self.progress_bar.set(value)
            self.status_label.configure(text=f"Carregando... {int(value*100)}%")
            # Chama a si mesma novamente após 15ms para uma animação suave
            self.after(15, self.update_progress, value + 0.042)
        else:
            self.status_label.configure(text="Pronto!")
            # Espera um pouco antes de fechar e chamar a função final
            self.after(500, self.on_done)


class SpeedTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- 2. A JANELA PRINCIPAL COMEÇA INVISÍVEL ---
        self.withdraw()

        self.overrideredirect(True)
        self.title("SpeedTracker Dev")
        self.geometry("750x450")

        self.iconbitmap(ICON_PATH)

        if sys.platform == "win32":
            try:
                import pywinstyles

                pywinstyles.apply_style(self, "mica")
            except (ImportError, ValueError):
                pass

        self._offset_x = 0
        self._offset_y = 0
        self.tasks = []
        self.progress = []
        self.task_widgets = []
        self.current_task_index = -1
        self.seconds_remaining = 0
        self.is_paused = False
        self.timer_job = None
        self.log_file = LOG_PATH

        self.task_font = ctk.CTkFont(family="Helvetica", size=12)
        self.task_font_strikethrough = ctk.CTkFont(
            family="Helvetica", size=12, overstrike=True
        )

        self.create_widgets()
        self.setup_log_file()
        # self.load_tasks()

        self.after(10, self.force_taskbar_icon)

    # ... todo o resto do código do SpeedTrackerApp continua igual ...
    def force_taskbar_icon(self):
        if sys.platform == "win32":
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            style = ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
            style = style | WS_EX_APPWINDOW
            ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
            self.update_idletasks()

    def create_widgets(self):
        # Configurações de Colunas e Linhas da Janela Principal (Self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # Criação e Posicionamento da Barra de Título
        title_bar = ctk.CTkFrame(self, height=30, corner_radius=0)
        title_bar.grid(row=0, column=0, columnspan=2, sticky="ew")
        
        # O SEGREDO: Configura a COLUNA 1 para EXPANDIR, empurrando os widgets seguintes para a direita.
        title_bar.grid_columnconfigure(1, weight=1)
        # As demais colunas (0, 2, 3, 4, 5) terão weight=0 e ficarão do tamanho exato dos widgets.
        
        # --- RÓTULO DE TÍTULO (Canto Esquerdo) ---
        title_label = ctk.CTkLabel(
            title_bar, text="✒️ SpeedTracker Dev", font=("Helvetica", 12)
        )
        title_label.grid(row=0, column=0, padx=10, sticky="w") # Coluna 0

        # --- BOTÃO 1: "Arquivo" (Posicionado à direita do espaço expandido) ---
        file_button = ctk.CTkButton(
            title_bar,
            text="Arquivo",
            width=80,
            height=22,
            command=self.open_roteiro_file,
        )
        # O botão 'Arquivo' é colocado na COLUNA 2
        file_button.grid(row=0, column=2, padx=(0, 5), pady=4) 

        # --- BOTÃO 2: "Limpa Progresso" (Ativado e posicionado ao lado) ---
        reset_button = ctk.CTkButton( # Use 'reset_button' para não sobrescrever 'file_button'
             title_bar,
             text="Limpa Progresso",
             width=80,
             height=22,
             command=self.reset_progress,
        )
        # O botão 'Limpa Progresso' é colocado na COLUNA 3
        reset_button.grid(row=0, column=3, padx=(0, 5), pady=4)

        # --- BOTÃO 3: "Colar JSON" (Ao lado) ---
        paste_button = ctk.CTkButton(
            title_bar,
            text="Colar JSON",
            width=90,
            height=22,
            command=self.open_paste_window,
        )
        # O botão 'Colar JSON' é colocado na COLUNA 4
        paste_button.grid(row=0, column=4, padx=(0, 5), pady=4)

        # --- BOTÃO 4: "Fechar" (Canto extremo direito) ---
        close_button = ctk.CTkButton(
            title_bar,
            text="✕",
            width=30,
            height=22,
            command=self.destroy,
            fg_color="transparent",
            # Certifique-se de que COLOR_CLOSE_HOVER esteja definido
            hover_color=COLOR_CLOSE_HOVER, 
        )
        # O botão 'Fechar' é colocado na COLUNA 5
        close_button.grid(row=0, column=5, padx=(0, 5), pady=4)

        # --- RESTANTE DO CÓDIGO (Não alterado) ---
        title_bar.bind("<ButtonPress-1>", self.on_press)
        title_label.bind("<ButtonPress-1>", self.on_press)
        title_bar.bind("<B1-Motion>", self.on_drag)
        title_label.bind("<B1-Motion>", self.on_drag)
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        main_frame.grid_columnconfigure(0, weight=1)
        font_action = ("Helvetica", 24, "bold")
        font_task = ("Helvetica", 14)
        font_timer = ("Helvetica", 80, "bold")
        self.action_label = ctk.CTkLabel(
            main_frame, text="Bem-vindo!", font=font_action
        )
        self.action_label.grid(row=0, column=0, pady=(10, 5))
        self.task_label = ctk.CTkLabel(
            main_frame,
            text="Carregue um roteiro ou selecione uma tarefa na lista.",
            font=font_task,
            wraplength=400,
        )
        self.task_label.grid(row=1, column=0, pady=5, padx=10)
        self.copy_button = ctk.CTkButton(
            main_frame,
            text="Copiar Enunciado",
            width=120,
            height=24,
            font=("Helvetica", 10),
            command=self.copy_task_to_clipboard,
            state=tk.DISABLED, # Certifique-se de que 'tk' está importado
        )
        self.copy_button.grid(row=2, column=0, pady=(0, 10))
        self.timer_label = ctk.CTkLabel(
            main_frame, text="00:00", font=font_timer, text_color=COLOR_TIMER # Certifique-se de que 'COLOR_TIMER' está definido
        )
        self.timer_label.grid(row=3, column=0, pady=10)
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.grid(row=4, column=0, pady=10)
        self.start_button = ctk.CTkButton(
            button_frame,
            text="Iniciar Roteiro",
            command=self.start_roteiro,
            font=("Helvetica", 14, "bold"),
            width=150,
            height=35,
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.pause_button = ctk.CTkButton(
            button_frame,
            text="Pausar",
            command=self.toggle_pause,
            font=("Helvetica", 14, "bold"),
            width=150,
            height=35,
            state=tk.DISABLED,
        )
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.task_list_frame = ctk.CTkScrollableFrame(
            self, label_text="Tarefas do Roteiro", width=280
        )
        self.task_list_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    def populate_task_list(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        self.task_widgets = []
        for i, task in enumerate(self.tasks):
            task_item_frame = ctk.CTkFrame(self.task_list_frame)
            task_item_frame.pack(fill="x", expand=True, padx=5, pady=3)

            status_indicator = ctk.CTkLabel(
                task_item_frame, text="●", font=("Arial", 18)
            )
            status_indicator.pack(side="left", padx=(5, 10))

            check_button = ctk.CTkButton(
                task_item_frame,
                text="✓",
                width=24,
                height=24,
                fg_color="transparent",
                border_width=1,
                command=partial(self.toggle_task_completion, i),
            )
            check_button.pack(side="right", padx=(5, 5))

            task_name_label = ctk.CTkLabel(
                task_item_frame, text=task["acao"], anchor="w", font=self.task_font
            )
            task_name_label.pack(side="left", fill="x", expand=True, padx=5)

            self.task_widgets.append(
                {
                    "frame": task_item_frame,
                    "status": status_indicator,
                    "name": task_name_label,
                    "check_button": check_button,
                }
            )

            # Bind clicks to the indicator and label, but not the whole frame, to avoid conflict with the button
            status_indicator.bind("<Button-1>", partial(self.jump_to_task, i))
            task_name_label.bind("<Button-1>", partial(self.jump_to_task, i))

            status = "completed" if self.progress[i] else "pending"
            self.update_task_status(i, status)

    def update_task_status(self, index, status):
        if 0 <= index < len(self.task_widgets):
            widget_info = self.task_widgets[index]
            label = widget_info["name"]

            widget_info["status"].configure(
                text_color=STATUS_COLORS.get(status, "#FFFFFF")
            )

            if status == "completed":
                label.configure(font=self.task_font_strikethrough, text_color="gray60")
            else:  # pending or active
                label.configure(
                    font=self.task_font,
                    text_color=ctk.ThemeManager.theme["CTkLabel"]["text_color"],
                )

    def toggle_task_completion(self, index):
        is_now_complete = not self.progress[index]

        # Prevent un-checking the active task while the timer is running
        if (
            not is_now_complete
            and index == self.current_task_index
            and self.timer_job
            and not self.is_paused
        ):
            messagebox.showwarning(
                "Ação Inválida", "Pause o roteiro antes de desmarcar a tarefa ativa."
            )
            return

        self.progress[index] = is_now_complete
        self.save_progress()

        new_status = "completed" if is_now_complete else "pending"

        if not is_now_complete and index == self.current_task_index:
            new_status = "active"

        self.update_task_status(index, new_status)

    def jump_to_task(self, index, event=None):
        self.attributes("-topmost", False)
        if self.timer_job:
            self.after_cancel(self.timer_job)
        if self.current_task_index != -1 and not self.progress[self.current_task_index]:
            self.update_task_status(self.current_task_index, "pending")
        self.current_task_index = index
        task = self.tasks[index]
        self.action_label.configure(text=f"Ação: {task['acao']}")
        self.task_label.configure(text=task["tarefa_especifica_hoje"])
        self.pause_button.configure(text="Pausar", state=tk.NORMAL)
        self.copy_button.configure(state=tk.NORMAL)
        self.start_button.configure(state=tk.DISABLED)
        self.update_task_status(index, "active")
        self.countdown(task["tempo_minutos"] * 60)

    def load_progress(self):
        try:
            with open(PROGRESS_PATH, "r") as f:
                self.progress = json.load(f)
            if len(self.progress) != len(self.tasks):
                raise ValueError("Progresso desalinhado.")
        except (FileNotFoundError, ValueError):
            self.progress = [False] * len(self.tasks)

    def save_progress(self):
        with open(PROGRESS_PATH, "w") as f:
            json.dump(self.progress, f)

    def _process_task_data(self, data):
        """Processa os dados do roteiro, atualiza o estado e a UI."""
        self.tasks = data.get("roteiro_speed_tracking", [])
        if not self.tasks:
            raise ValueError(
                "JSON inválido ou chave 'roteiro_speed_tracking' não encontrada."
            )
        self.load_progress()
        self.populate_task_list()
        self.reset_app_state()

    def load_tasks_from_string(self, json_string):
        """Carrega tarefas de uma string JSON."""
        try:
            data = json.loads(json_string)
            self._process_task_data(data)
        except (ValueError, json.JSONDecodeError) as e:
            messagebox.showerror("Erro ao Carregar", f"Erro no formato JSON: {e}")
            self.tasks = []
            self.reset_app_state()

    def load_tasks(self, filepath=None):
        if filepath is None:
            filepath = ROTEIRO_PATH
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._process_task_data(data)
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
            messagebox.showerror(
                "Erro ao Carregar", f"Não foi possível carregar o arquivo: {e}"
            )
            self.tasks = []
            self.reset_app_state()

    def task_finished_handler(self):
        self.timer_label.configure(text="Fim!", text_color=COLOR_ALERT)
        self.bell()
        self.bell()
        if self.current_task_index != -1:
            self.progress[self.current_task_index] = True
            self.update_task_status(self.current_task_index, "completed")
            self.log_activity(self.tasks[self.current_task_index])
            self.save_progress()
        self.after(2000, self.find_and_start_next_pending)

    def find_and_start_next_pending(self):
        next_index = next(
            (
                i
                for i in range(self.current_task_index + 1, len(self.tasks))
                if not self.progress[i]
            ),
            -1,
        )
        if next_index != -1:
            self.jump_to_task(next_index)
        else:
            self.attributes("-topmost", False)
            self.action_label.configure(text="Parabéns!")
            self.task_label.configure(text="Você completou o roteiro.")
            self.timer_label.configure(text="✅")
            self.start_button.configure(state=tk.NORMAL, text="Reiniciar")
            self.pause_button.configure(state=tk.DISABLED)
            self.copy_button.configure(state=tk.DISABLED)

    def copy_task_to_clipboard(self):
        task_text = self.task_label.cget("text")
        self.clipboard_clear()
        self.clipboard_append(task_text)
        self.copy_button.configure(text="Copiado!", state=tk.DISABLED)
        self.after(2000, self.reset_copy_button_text)

    def reset_copy_button_text(self):
        self.copy_button.configure(text="Copiar Enunciado", state=tk.NORMAL)

    def on_press(self, event):
        self._offset_x = event.x
        self._offset_y = event.y

    def on_drag(self, event):
        self.geometry(
            f"+{self.winfo_pointerx() - self._offset_x}+{self.winfo_pointery() - self._offset_y}"
        )

    def open_roteiro_file(self):
        filepath = filedialog.askopenfilename(
            title="Selecione um roteiro",
            initialdir=base_path,
            filetypes=[("JSON files", "*.json")],
        )
        if filepath:
            self.load_tasks(filepath)
            
    def reset_progress(self):
        # 1. Reseta a lógica: Define todas as tarefas como não concluídas (False)
        self.progress = [False] * len(self.tasks)
        
        # 2. Salva o estado resetado no arquivo progress.json
        self.save_progress()
        
        # --- NOVIDADES PARA ATUALIZAR A UI ---
        
        # 3. Redesenha a lista de tarefas (remove os riscos e as cores de 'completo')
        self.populate_task_list() 
        
        # 4. Reseta o estado da tela principal (Labels de Ação/Tarefa, Timer, Botões)
        self.reset_app_state() 
        
        # Adicional: Mensagem de confirmação opcional
        messagebox.showinfo("Progresso Resetado", "O progresso das tarefas foi resetado com sucesso!")


    def open_paste_window(self):
        paste_win = ctk.CTkToplevel(self)
        paste_win.title("Colar Roteiro JSON")
        paste_win.geometry("450x350")
        paste_win.transient(self)
        paste_win.grab_set()

        # Centraliza a janela de colar
        self.update_idletasks()
        win_x = (
            self.winfo_rootx()
            + (self.winfo_width() // 2)
            - (paste_win.winfo_width() // 2)
        )
        win_y = (
            self.winfo_rooty()
            + (self.winfo_height() // 2)
            - (paste_win.winfo_height() // 2)
        )
        paste_win.geometry(f"+{win_x}+{win_y}")

        label = ctk.CTkLabel(
            paste_win, text="Cole o conteúdo do roteiro em formato JSON:"
        )
        label.pack(pady=(10, 5), padx=10)

        textbox = ctk.CTkTextbox(paste_win, wrap="word")
        textbox.pack(pady=5, padx=10, fill="both", expand=True)
        textbox.focus()

        def on_load():
            json_string = textbox.get("1.0", "end-1c")
            if json_string.strip():
                self.load_tasks_from_string(json_string)
                paste_win.destroy()
            else:
                messagebox.showwarning(
                    "Aviso", "A caixa de texto está vazia.", parent=paste_win
                )

        button_frame = ctk.CTkFrame(paste_win, fg_color="transparent")
        button_frame.pack(pady=10)

        load_button = ctk.CTkButton(button_frame, text="Carregar", command=on_load)
        load_button.pack(side=tk.LEFT, padx=10)

        cancel_button = ctk.CTkButton(
            button_frame, text="Cancelar", command=paste_win.destroy, fg_color="gray50"
        )
        cancel_button.pack(side=tk.LEFT, padx=10)

    def setup_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(
                    ["timestamp", "acao", "tarefa_especifica", "duracao_minutos"]
                )

    def reset_app_state(self):
        if self.timer_job:
            self.after_cancel(self.timer_job)
        self.current_task_index = -1
        self.is_paused = False
        self.action_label.configure(text="Roteiro Carregado")
        self.task_label.configure(text="Clique em 'Iniciar Roteiro' para começar.")
        self.timer_label.configure(text="00:00")
        self.start_button.configure(text="Iniciar Roteiro", state=tk.NORMAL)
        self.pause_button.configure(text="Pausar", state=tk.DISABLED)
        self.copy_button.configure(state=tk.DISABLED)

    def start_roteiro(self):
        self.start_button.configure(state=tk.DISABLED)
        self.find_and_start_next_pending()

    def next_task(self):
        pass

    def countdown(self, seconds_left):
        if self.is_paused:
            self.seconds_remaining = seconds_left
            return
        if seconds_left == 5:
            self.attributes("-topmost", True)
            self.lift()
            self.focus_force()
            self.bell()
            self.timer_label.configure(text_color=COLOR_WARNING)
        self.seconds_remaining = seconds_left
        if seconds_left >= 0:
            mins, secs = divmod(seconds_left, 60)
            self.timer_label.configure(text=f"{mins:02d}:{secs:02d}")
            self.timer_job = self.after(1000, self.countdown, seconds_left - 1)
        else:
            self.task_finished_handler()

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        self.pause_button.configure(text="Retomar" if self.is_paused else "Pausar")
        if self.is_paused:
            self.attributes("-topmost", False)
        else:
            self.countdown(self.seconds_remaining)

    def log_activity(self, task):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(
                [
                    timestamp,
                    task["acao"],
                    task["tarefa_especifica_hoje"],
                    task["tempo_minutos"],
                ]
            )


# --- 3. A NOVA LÓGICA DE INICIALIZAÇÃO ---
if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            from ctypes import windll

            myappid = "speedtracker.dev.python.gui.1"
            windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except (ImportError, AttributeError):
            pass

    # Cria a janela principal do app, mas a mantém invisível
    app = SpeedTrackerApp()

    # Cria a Splash Screen como uma "filha" da janela principal
    splash = SplashScreen(master=app)

    def show_main_window():
        splash.destroy()
        app.deiconify()  # Torna a janela principal visível

    # Inicia o carregamento na splash screen e, quando terminar, mostra a janela principal
    splash.start_loading(on_done=show_main_window)

    app.mainloop()

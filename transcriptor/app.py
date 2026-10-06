import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os

from .config import MODELS, DEFAULT_MODEL, DEFAULT_LANGUAGE
from .descarga import descargar_audio
from .transcripcion import transcribir_audio

class Transcriptor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Transcriptor Whisper - Linux Edition")
        self.root.geometry("600x500")

        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Sección de Entrada
        ttk.Label(main_frame, text="URL de YouTube o Archivo Local:").pack(anchor=tk.W)

        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 10))

        self.url_entry = ttk.Entry(input_frame)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.btn_browse = ttk.Button(input_frame, text="📁", width=3, command=self.browse_file)
        self.btn_browse.pack(side=tk.RIGHT)

        # Selección de Modelo
        model_frame = ttk.Frame(main_frame)
        model_frame.pack(fill=tk.X, pady=10)

        ttk.Label(model_frame, text="Modelo Whisper:").pack(side=tk.LEFT)
        self.model_var = tk.StringVar(value=DEFAULT_MODEL)
        self.model_dropdown = ttk.Combobox(model_frame, textvariable=self.model_var, values=list(MODELS.keys()), state="readonly")
        self.model_dropdown.set("Small")
        self.model_dropdown.pack(side=tk.LEFT, padx=10)

        # Botón de Acción
        self.btn_transcribe = ttk.Button(main_frame, text="Transcribir", command=self.start_transcription_thread)
        self.btn_transcribe.pack(pady=20)

        # Área de Resultado
        ttk.Label(main_frame, text="Resultado:").pack(anchor=tk.W)
        self.result_text = tk.Text(main_frame, wrap=tk.WORD, height=15)
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # Barra de Estado
        self.status_var = tk.StringVar(value="Listo")
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio/Video", "*.mp3 *.wav *.mp4 *.mkv *.avi")])
        if file_path:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, file_path)

    def update_status(self, text):
        self.status_var.set(text)
        self.root.update_idletasks()

    def start_transcription_thread(self):
        # Ejecutamos en un hilo separado para que la GUI no se congele
        thread = threading.Thread(target=self.process_transcription, daemon=True)
        thread.start()

    def process_transcription(self):
        input_val = self.url_entry.get().strip()
        if not input_val:
            messagebox.showwarning("Atención", "Por favor, introduce una URL o selecciona un archivo.")
            return

        self.btn_transcribe.config(state=tk.DISABLED)
        self.result_text.delete(1.0, tk.END)

        try:
            audio_file = "temp_audio_process.mp3"

            # 1. Obtener el audio
            if input_val.startswith(("http://", "https://")):
                self.update_status("Descargando audio de YouTube...")
                audio_file = descargar_audio(input_val, audio_file)
            else:
                self.update_status("Preparando archivo local...")
                audio_file = input_val

            # 2. Transcribir
            selected_model_label = self.model_var.get()
            model_id = MODELS.get(selected_model_label, "small")

            self.update_status(f"Transcribiendo con modelo {selected_model_label}... (Esto puede tardar)")
            text, path = transcribir_audio(audio_file, model_name=model_id)

            # 3. Mostrar resultado
            self.result_text.insert(tk.END, text)
            self.update_status(f"Completado. Guardado en: {path}")
            messagebox.showinfo("Éxito", f"Transcripción guardada en:\n{path}")

        except Exception as e:
            self.update_status("Error ocurrido.")
            messagebox.showerror("Error", f"Hubo un problema: {str(e)}")

        finally:
            self.btn_transcribe.config(state=tk.NORMAL)
            # Limpiar archivo temporal si existe y fue creado por nosotros
            if "temp_audio_process.mp3" in locals() or "audio_file" in locals():
                try:
                    if os.path.exists("temp_audio_process.mp3"):
                        os.remove("temp_audio_process.mp3")
                except:
                    pass

    def mainloop(self):
        self.root.mainloop()

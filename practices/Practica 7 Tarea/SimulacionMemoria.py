import tkinter as tk
from tkinter import ttk
import random
import time
from threading import Thread

class RoundRobinAnimation(tk.Tk):
    TIME_SLICE = 2000  # Tiempo de procesamiento por segmento en milisegundos

    def __init__(self):
        super().__init__()
        self.title("Simulación de administración de memoria en la CPU")
        self.geometry("600x600")
        self.configure(bg="white")

        self.process_durations = [random.randint(500, 4000) for _ in range(4)]  # Duraciones aleatorias
        self.remaining_times = self.process_durations[:]
        self.process_completed = [False] * 4
        self.current_process_index = 0

        self.create_widgets()
        self.animation_running = False

    def create_widgets(self):
        # Contenedor CPU
        self.cpu_frame = tk.Frame(self, bg="lightgray", bd=2, relief="solid")
        self.cpu_frame.place(x=50, y=50, width=500, height=400)

        # Título para el contenedor CPU
        self.cpu_title = tk.Label(self.cpu_frame, text="CPU", bg="lightgray", font=("Arial", 16, "bold"))
        self.cpu_title.grid(row=0, column=0, columnspan=2, pady=10)

        # Botón CPU
        self.cpu_button = tk.Button(self.cpu_frame, text="Iniciar", bg="blue", fg="white", font=("Arial", 12, "bold"), command=self.start_animation)
        self.cpu_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Panel de procesos dentro del contenedor CPU
        self.process_labels = []
        self.progress_bars = []
        for i, duration in enumerate(self.process_durations):
            label = tk.Label(self.cpu_frame, text=f"Programa {i+1}: {duration} ms", bg="lightgray", font=("Arial", 12))
            label.grid(row=2 + i, column=0, pady=5, sticky="w")
            self.process_labels.append(label)

            # Modificado para mover las barras a la derecha
            progress = ttk.Progressbar(self.cpu_frame, maximum=100, length=200)
            progress.grid(row=2 + i, column=1, pady=5, padx=20)  # Se añadió el padx para mover las barras a la derecha
            self.progress_bars.append(progress)

    def update_ui(self):
        # Actualizar el estado de los procesos
        for i, remaining in enumerate(self.remaining_times):
            if self.process_completed[i]:
                self.process_labels[i].config(text=f"Programa {i+1}: Completado")
                self.progress_bars[i]["value"] = 100
            else:
                percentage = 100 * (1 - remaining / self.process_durations[i])
                self.process_labels[i].config(text=f"Programa {i+1}: {remaining} ms restantes")
                self.progress_bars[i]["value"] = percentage

    def round_robin_step(self):
        if all(self.process_completed):
            self.animation_running = False
            return

        # Seleccionar el proceso actual
        i = self.current_process_index
        if self.remaining_times[i] > self.TIME_SLICE:
            self.remaining_times[i] -= self.TIME_SLICE  # Reducir el tiempo restante del proceso
        else:
            self.remaining_times[i] = 0
            self.process_completed[i] = True  # Marcar el proceso como completado

        # Avanzar al siguiente proceso de manera cíclica
        self.current_process_index = (self.current_process_index + 1) % len(self.process_durations)

    def animate(self):
        while self.animation_running:
            self.round_robin_step()
            self.update_ui()
            time.sleep(2)  # Simula la rebanada de tiempo en segundos

    def start_animation(self):
        if not self.animation_running:
            self.remaining_times = self.process_durations[:]  # Copiar las duraciones iniciales
            self.process_completed = [False] * len(self.process_durations)  # Reiniciar los estados de los procesos
            self.current_process_index = 0  # Empezar desde el primer proceso
            self.animation_running = True
            animation_thread = Thread(target=self.animate)
            animation_thread.daemon = True  # Asegura que el hilo termine cuando se cierre la ventana
            animation_thread.start()

if __name__ == "__main__":
    app = RoundRobinAnimation()  # Crear instancia de la simulación
    app.mainloop()  # Ejecutar la ventana de la interfaz gráfica

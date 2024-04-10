import tkinter as tk
from tkinter import ttk, filedialog
from pytube import YouTube

def seleccionar_ruta_guardado():
    ruta_guardado = filedialog.askdirectory()
    ruta_guardado_entry.delete(0, tk.END)
    ruta_guardado_entry.insert(0, ruta_guardado)

def descargar_video():
    estado_label.config(text='')
    url = url_entry.get()
    ruta_guardado = ruta_guardado_entry.get()
    if not url or not ruta_guardado:
        estado_label.config(text=f'Ocurrió un error: Complete los campos para descargar')
        return
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=ruta_guardado)
        estado_label.config(text='Descarga completada.')
    except Exception as e:
        estado_label.config(text=f'Ocurrió un error: {e}')

# Configuración de la interfaz
app = tk.Tk()
app.title("Descargador de Videos de YouTube")

app.resizable(0,0)

# Etiqueta y entrada para la URL
url_label = ttk.Label(app, text="URL del Video:")
url_label.grid(column=0, row=0, padx=10, pady=(30,10), sticky=tk.W)

url_entry = ttk.Entry(app, width=50)
url_entry.grid(column=1, row=0, padx=10, pady=(30,10))

# Etiqueta y entrada para la ruta de guardado
ruta_guardado_label = ttk.Label(app, text="Ruta de Guardado:")
ruta_guardado_label.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

ruta_guardado_entry = ttk.Entry(app, width=50)
ruta_guardado_entry.grid(column=1, row=1, padx=10, pady=10)

# Botón para seleccionar la ruta de guardado
seleccionar_ruta_button = ttk.Button(app, text="Seleccionar Ruta", command=seleccionar_ruta_guardado, cursor="hand2")
seleccionar_ruta_button.grid(column=2, row=1, pady=10, padx=(0,10))

# Botón de descarga
descargar_button = tk.Button(app, text="Descargar", command=descargar_video, relief="flat", bg="#81db79", cursor="hand2", font=("Arial",11,"bold"))
descargar_button.grid(column=0, row=2, columnspan=3, pady=10)

# Etiqueta de estado
estado_label = ttk.Label(app, text="")
estado_label.grid(column=0, row=3, columnspan=3, pady=10)

# Iniciar la interfaz
app.mainloop()
import webview
import os

def abrir_gemini():
    # Creamos una carpeta oculta para que no se pierda nada
    ruta_datos = os.path.expanduser('~/.gemini_canaima_data')
    if not os.path.exists(ruta_datos):
        os.makedirs(ruta_datos)

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

    ventana = webview.create_window(
        'Gemini Desktop - Proyecto Neiber', 
        'https://gemini.google.com/app',
        width=1000, 
        height=750,
        text_select=True
    )
    
    # 'private_mode=False' y 'storage_path' son el secreto para que no de Error 4
    webview.start(
        user_agent=user_agent, 
        private_mode=False, 
        storage_path=ruta_datos
    )

if __name__ == '__main__':
    abrir_gemini()
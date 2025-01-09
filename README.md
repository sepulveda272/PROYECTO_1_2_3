## Instalación y Configuración

1. Asegúrate de tener Python. Puedes verificar tu versión de Python con:
   ```bash
   python --version
   ```

2. Clona este repositorio:
   ```bash
   git clone https://github.com/sepulveda272/PROYECTO_1_2_3.git
   ```

3. creacion del entorno virtual:
   ```bash
   python -m venv venv
   ```

4. Activar en entorno virtual:
   ```bash
   venv/Scripts/activate
   ```


5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación de Streamlit (depende de el proyecto que quiera ejecutar):
   ```bash
   streamlit run multi_modelos_app/app.py
   ```

   ```bash
   streamlit run Pregunta_Respuesta_app/app.py
   ```

   ```bash
   streamlit run sentimientos_analysis/app.py
   ```

2. Abre tu navegador web y ve a `http://localhost:8501` para interactuar con la aplicación.

## Estructura del Proyecto

- `multi_modelos_app/app.py`: La aplicación principal que permite cambiar entre modelos y personalizar la interfaz.
- `multi_modelos_app/models.py`: Contiene la lógica para cargar y cambiar entre modelos.
- `Pregunta_Respuesta_app/app.py`: Una aplicación secundaria para preguntas y respuestas usando el modelo de texto.
- `sentimientos_analysis/app.py`: Una aplicación para análisis de sentimientos.
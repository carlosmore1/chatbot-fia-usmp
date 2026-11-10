# 🎓 Chatbot Académico FIA-USMP

## 📌 Descripción

Prototipo académico de un chatbot con inteligencia artificial generativa, desarrollado para orientar a estudiantes de la **Facultad de Ingeniería y Arquitectura de la Universidad de San Martín de Porres (FIA-USMP)** sobre matrícula y trámites académicos.

El chatbot permite realizar preguntas en lenguaje natural, recibir respuestas mediante Google Gemini y mantener el contexto durante una conversación.

## 🚀 Funcionalidades

- Consultas sobre matrícula especial.
- Orientación sobre rectificación de matrícula.
- Información sobre retiro de asignaturas.
- Respuestas generadas mediante inteligencia artificial.
- Memoria conversacional para preguntas de seguimiento.
- Botones de acceso rápido a los tres procedimientos.
- Referencias a documentación académica oficial.
- Manejo básico de errores y reinicio de conversación.

## 🛠️ Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Streamlit:** interfaz web del chatbot.
- **Google Gemini:** modelo de inteligencia artificial generativa.
- **GitHub:** control de versiones y almacenamiento del código.
- **Streamlit Community Cloud:** despliegue de la aplicación web.

## 💻 Instalación y ejecución local

Para ejecutar el proyecto en Windows utilizando la terminal PowerShell de VS Code:

### 1. Clonar el repositorio

```powershell
git clone https://github.com/carlosmore1/chatbot-fia-usmp.git
cd chatbot-fia-usmp
```

Si ya tienes el proyecto descargado y abierto en VS Code, puedes omitir este paso.

### 2. Crear el entorno virtual

```powershell
python -m venv .venv
```

### 3. Instalar las dependencias

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Configurar la API Key de Gemini

En la terminal PowerShell, ejecutar:

```powershell
$env:GEMINI_API_KEY="TU_CLAVE_DE_GEMINI"
```

Reemplazar `TU_CLAVE_DE_GEMINI` por una clave válida obtenida desde Google AI Studio.

**Importante:** nunca publicar la clave real en GitHub ni incluirla directamente en el código.

### 5. Ejecutar el chatbot con Streamlit

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

La aplicación se abrirá en el navegador, normalmente en:

http://localhost:8501

### Ejecución rápida

Si ya instalaste las dependencias, puedes configurar la API Key e iniciar Streamlit con un solo comando:

```powershell
$env:GEMINI_API_KEY="TU_CLAVE_DE_GEMINI"; .\.venv\Scripts\python.exe -m streamlit run app.py
```

La variable de entorno se mantiene durante la sesión actual de la terminal. Al abrir una terminal nueva, será necesario configurarla nuevamente.

## 🌐 Aplicación web

El prototipo se encuentra desplegado en Streamlit Community Cloud.

**Enlace:** https://chatbot-fia-usmp-demo.streamlit.app/

## 📂 Estructura del proyecto

```text
chatbot-fia-usmp/
├── app.py
├── chatbot.py
├── requirements.txt
├── .gitignore
└── README.md
```

- **app.py:** interfaz web desarrollada con Streamlit.
- **chatbot.py:** conexión con Gemini, instrucciones y conocimiento académico.
- **requirements.txt:** dependencias necesarias.
- **.gitignore:** exclusión de archivos locales y sensibles.
- **README.md:** descripción e instrucciones del proyecto.

## 📚 Información académica

El chatbot utiliza información de referencia correspondiente al semestre **2026-II**, basada en documentos publicados por la FIA-USMP.

**Fuentes:**

- [Documentos para alumnos regulares](https://fia.usmp.edu.pe/calendario-alumnos-regulares/)
- [Calendario de Actividades 2026-II](https://fia.usmp.edu.pe/wp-content/uploads/2026/07/CALENDARIO_DE_ACTIVIDADES_2026-II_edicion_02.pdf)
- [Directiva de Matrícula 2026-II](https://fia.usmp.edu.pe/wp-content/uploads/2026/07/DIRECTIVAS_DE_MATRICULA_2026-II_EDICION_1.pdf)

## ⚠️ Aviso importante

Este chatbot es un **prototipo académico no oficial**, desarrollado con fines educativos.

No representa un servicio institucional de la USMP, no tiene acceso a información personal de estudiantes y no permite realizar trámites universitarios.

Las respuestas son orientativas y deben contrastarse con la documentación oficial vigente.

## 🎯 Objetivo del proyecto

Demostrar cómo la **inteligencia artificial generativa** puede mejorar la orientación académica mediante consultas en lenguaje natural, respuestas contextualizadas y conversaciones de varios turnos.
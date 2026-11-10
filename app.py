
import streamlit as st
from chatbot import crear_chat


st.set_page_config(
    page_title="Asistente Académico | FIA-USMP",
    page_icon="🎓",
    layout="centered"
)

# Estilos de la interfaz
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #f6f7fa;
}

.block-container {
    max-width: 850px;
    padding-top: 28px;
    padding-bottom: 30px;
}

.logo-fia {
    background: white;
    border: 1px solid #e8e8ed;
    border-radius: 16px;
    padding: 10px;
    margin-bottom: 20px;
    text-align: center;
}

.logo-fia img {
    width: 100%;
    max-width: 300px;
    height: auto;
}

.encabezado {
    background: linear-gradient(115deg, #80182c, #af3042);
    border-radius: 10px;
    padding: 10px 15px;
    color: white;
    margin-bottom: 16px;
}

.encabezado h1 {
    color: white;
    font-size: 29px;
    margin: 0 0 8px;
}

.encabezado p {
    color: #f7e5e8;
    font-size: 15px;
    margin: 0;
}

.aviso {
    color: #606879;
    font-size: 12px;
    margin: 14px 0;
}

.temas {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin: 10px 0 15px;
}

.tema {
    background: #fff;
    color: #812237;
    border: 1px solid #ead2d7;
    padding: 9px 60px;
    border-radius: 25px;
    font-size: 13px;
    font-weight: 600;
}

.bienvenida {
    text-align: center;
    padding: 35px 20px;
    color: #344054;
}

.bienvenida h3 {
    color: #812237;
    margin-bottom: 10px;
}

.bienvenida p {
    color: #667085;
    font-size: 14px;
}

/* Estilos del historial de conversación */
[data-testid="stChatMessage"] {
    background: #ffffff;
    border: 1px solid #e9e9ef;
    border-radius: 14px;
    padding: 13px;
    margin-bottom: 10px;
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li {
    color: #252d3a;
}

/* Botón de nueva conversación */
div.stButton > button {
    background: #862038;
    color: #ffffff;
    border: none;
    border-radius: 10px;
}

div.stButton > button:hover {
    background: #ac304a;
    color: #ffffff;
    border: none;
}

/* Campo de escritura */
[data-testid="stChatInput"] {
    border-radius: 12px;
}

[data-testid="stChatInput"] textarea {
    background: #ffffff;
    color: #252d3a;
}
</style>
""", unsafe_allow_html=True)


# Logo de la universidad
st.markdown("""
<div class="logo-fia">
    <img
        src="https://usmp.edu.pe/campus/img/logo_fia.png"
        alt="Logo FIA-USMP"
    >
</div>
""", unsafe_allow_html=True)


# Encabezado principal
st.markdown("""
<div class="encabezado">
    <h1>Asistente Académico FIA</h1>
    <p>
        Tu espacio de orientación sobre matrícula y
        trámites académicos mediante inteligencia artificial.
    </p>
</div>
""", unsafe_allow_html=True)

# Botones para iniciar una consulta
col1, col2, col3 = st.columns(3)

pregunta_rapida = None

with col1:
    if st.button("📚 Matrícula especial", use_container_width=True):
        pregunta_rapida = "Quiero información sobre matrícula especial."

with col2:
    if st.button("📝 Rectificación de matrícula", use_container_width=True):
        pregunta_rapida = "Quiero información sobre rectificación de matrícula."

with col3:
    if st.button("📄 Retiro de asignaturas", use_container_width=True):
        pregunta_rapida = "Quiero información sobre retiro de asignaturas."


# Inicializar Gemini
if "chat" not in st.session_state:
    try:
        cliente, chat = crear_chat()
        st.session_state.cliente = cliente
        st.session_state.chat = chat
        st.session_state.mensajes = []

    except ValueError as error:
        st.error(str(error))
        st.stop()


# Cabecera del chat
col1, col2 = st.columns([3, 2], vertical_alignment="center")

with col1:
    st.markdown("#### 💬 Conversación")

with col2:
    if st.button("↻ Nueva conversación", use_container_width=True):
        st.session_state.cliente.close()
        del st.session_state.cliente
        del st.session_state.chat
        st.session_state.mensajes = []
        st.rerun()


# Historial del chat
with st.container(height=420, border=True):

    if not st.session_state.mensajes:
        st.markdown("""
        <div class="bienvenida">
            <h3>👋 ¡Hola! ¿En qué puedo ayudarte?</h3>
            <p>
                Escribe tu consulta sobre matrícula especial,
                rectificación o retiro de asignaturas.
            </p>
            <p>
                Puedes realizar preguntas de seguimiento.
                Recordaré el contexto de esta conversación.
            </p>
        </div>
        """, unsafe_allow_html=True)

    for mensaje in st.session_state.mensajes:
        avatar = "👤" if mensaje["role"] == "user" else "🎓"

        with st.chat_message(mensaje["role"], avatar=avatar):
            st.markdown(mensaje["content"])


# Recibir preguntas escritas o iniciadas desde los botones
with st.container():
    pregunta_escrita = st.chat_input("Escribe tu consulta académica...")

pregunta = pregunta_rapida or pregunta_escrita



if pregunta:
    with st.spinner("Preparando respuesta..."):
        try:
            respuesta = st.session_state.chat.send_message(pregunta)
            texto = respuesta.text

            if not texto:
                raise ValueError("Gemini no devolvió una respuesta.")

        except Exception:
            st.error(
                "No fue posible obtener una respuesta de Gemini. "
                "Verifica tu conexión e inténtalo nuevamente."
            )

        else:
            st.session_state.mensajes.append({
                "role": "user",
                "content": pregunta
            })

            st.session_state.mensajes.append({
                "role": "assistant",
                "content": texto
            })

            st.rerun()



st.caption(
    "Las respuestas son orientativas. "
    "Verifica los procedimientos en la documentación "
    "oficial de la FIA-USMP."
)

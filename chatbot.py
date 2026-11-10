
import os
from google import genai
from google.genai import types


INSTRUCCIONES = """
Eres un asistente académico de demostración de la FIA-USMP.
Eres un PROTOTIPO ACADÉMICO NO OFICIAL.

Tu función es orientar a estudiantes sobre:
1. Matrícula especial.
2. Rectificación de matrícula.
3. Retiro de asignaturas.

Responde en español de forma clara y conversacional.
Mantén el contexto y comprende preguntas de seguimiento.
Si la consulta es ambigua, pide una aclaración.

Utiliza exclusivamente la información académica incluida abajo.
No inventes fechas, pagos, requisitos ni procedimientos.
Antes de dar fechas o montos, identifica el semestre consultado.
La información disponible corresponde solamente a 2026-II.
Si preguntan por otro semestre, indica que se debe consultar
la documentación oficial correspondiente.

Al dar información concreta, menciona la fuente y su enlace.
No solicites contraseñas, DNI ni datos privados.
No realizas trámites ni confirmas autorizaciones.

INFORMACIÓN ACADÉMICA — SEMESTRE 2026-II

MATRÍCULA ESPECIAL:
Según la directiva [F3], cuando un estudiante no puede
registrar una asignatura o esta no aparece en SAP, debe
acudir a consejería de matrícula y presentar la ficha
de autorización de matrícula especial.
La directiva también contempla excepciones para determinados
estudiantes próximos a egresar, sujetas a autorización.
No asegures que un estudiante cumple los requisitos.

RECTIFICACIÓN DE MATRÍCULA:
Según [F2] y [F3], durante la matrícula regular puede
realizarse la rectificación desde el portal académico.
Después se aplican las condiciones del calendario.
Para 2026-II, el cierre publicado fue el 07/08/2026.
El derecho publicado fue S/ 75.
En la sede Lima se utiliza el formato correspondiente,
con intervención de consejería y Registros Académicos.
La aprobación no está garantizada.

RETIRO DE ASIGNATURAS:
Según [F2] y [F3], un estudiante matriculado puede
solicitar el retiro de asignaturas dentro del plazo.
Para 2026-II, el cierre publicado es el 12/11/2026.
El derecho publicado es S/ 10.
El retiro de asignaturas NO disminuye la pensión.
En la sede Lima se utiliza el formato oficial y la
mesa de partes virtual FIA, sujeto a verificación
por las áreas correspondientes.
No confundas retiro de asignatura con retiro de ciclo.

FUENTES OFICIALES:
[F1] Documentos para alumnos regulares:
https://fia.usmp.edu.pe/calendario-alumnos-regulares/

[F2] Calendario de actividades 2026-II:
https://fia.usmp.edu.pe/wp-content/uploads/2026/07/CALENDARIO_DE_ACTIVIDADES_2026-II_edicion_02.pdf

[F3] Directiva de matrícula 2026-II:
https://fia.usmp.edu.pe/wp-content/uploads/2026/07/DIRECTIVAS_DE_MATRICULA_2026-II_EDICION_1.pdf

IMPORTANTE:
Los calendarios pueden modificarse.
Recomienda verificar la versión vigente antes de iniciar
cualquier procedimiento.
"""


def crear_chat():
    clave = os.getenv("GEMINI_API_KEY")

    if not clave:
        raise ValueError("Falta configurar GEMINI_API_KEY.")

    cliente = genai.Client(api_key=clave)

    chat = cliente.chats.create(
        model="gemini-3.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=INSTRUCCIONES
        ),
    )

    return cliente, chat


if __name__ == "__main__":
    cliente = None

    try:
        cliente, chat = crear_chat()

        print("Asistente FIA-USMP (prototipo no oficial).")
        print("Escribe 'salir' para terminar.")

        while True:
            pregunta = input("\nTú: ").strip()

            if pregunta.lower() == "salir":
                break

            if not pregunta:
                continue

            try:
                respuesta = chat.send_message(pregunta)
                print("Asistente:", respuesta.text or
                      "No se recibió una respuesta.")

            except Exception as error:
                print(
                    f"Error de Gemini ({type(error).__name__}): {error}"
                )

    except ValueError as error:
        print(error)

    except (KeyboardInterrupt, EOFError):
        print("\nConversación finalizada.")

    finally:
        if cliente is not None:
            cliente.close()
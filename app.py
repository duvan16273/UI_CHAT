import chainlit as cl

@cl.on_chat_start
async def main():
    # Enviar un mensaje al iniciar el chat
    await cl.Message(
        content="¡Hola! Soy un bot de chat básico. ¿En qué puedo ayudarte hoy?",
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # Esto se llama cuando el usuario envía un mensaje
    # En este ejemplo, simplemente repetimos el mensaje del usuario
    await cl.Message(
        content=f"Recibí tu mensaje: {message.content}",
    ).send()
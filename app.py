import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Usa el servidor SMTP de Gmail
app.config['MAIL_PORT'] = 587  # Puerto para STARTTLS
app.config['MAIL_USE_TLS'] = True  # Habilitar TLS
app.config['MAIL_USE_SSL'] = False  # No usar SSL
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Usuario del correo (ejemplo@gmail.com)
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Contraseña o contraseña de aplicación
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')  # Establecer el correo de remitente por defecto

mail = Mail(app)

# Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('formulario.html')

# Ruta para procesar el formulario y enviar el correo
@app.route('/enviar', methods=['POST'])
def enviar():
    # Capturar los datos del formulario
    nombre = request.form.get('nombre')
    cargo = request.form.get('cargo')
    telefono = request.form.get('telefono')
    cedula = request.form.get('cedula')
    secretaria = request.form.get('secretaria')
    dependencia = request.form.get('dependencia')
    fecha = request.form.get('fecha')
    lugar = request.form.get('lugar')
    descripcion = request.form.get('descripcion')

    # Crear el mensaje de correo
    mensaje = Message(
        "Nueva solicitud de mantenimiento",  # Asunto del correo
        recipients=['mtto.logisticasa@gmail.com']  # Correo al que se enviará (ajusta este correo)
    )

    # Contenido del correo
    mensaje.body = f"""
    Se ha recibido una nueva solicitud de mantenimiento:
    
    Nombre: {nombre}
    Cargo: {cargo}
    Teléfono: {telefono}
    Cédula: {cedula}
    Secretaría: {secretaria}
    Dependencia: {dependencia}
    Fecha: {fecha}
    Lugar: {lugar}
    Descripción: {descripcion}
    """

    try:
        # Enviar el correo
        mail.send(mensaje)
        return "¡Solicitud enviada correctamente y correo enviado!"
    except Exception as e:
        return f"Error al enviar el correo: {str(e)}"

# Ejecutar la aplicación en el puerto proporcionado por Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render asigna el puerto a través de la variable PORT
    app.run(host='0.0.0.0', port=port)



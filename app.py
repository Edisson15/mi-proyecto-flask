from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

def enviar_correo(solicitud):
    """Envía la solicitud por correo electrónico."""
    remitente = os.environ['EMAIL']  # Usamos la variable de entorno para el correo
    contraseña = os.environ['PASSWORD']  # Usamos la variable de entorno para la contraseña
    destinatario = os.environ['DESTINATARIO']  # Usamos la variable de entorno para el destinatario

    asunto = "Nueva Solicitud de Mantenimiento Locativo"
    cuerpo = "\n".join([f"{key}: {value}" for key, value in solicitud.items()])

    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(cuerpo, "plain"))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        servidor.quit()
        print("📧 Solicitud enviada con éxito.")
    except Exception as e:
        print("⚠️ Error al enviar el correo:", e)

@app.route('/')
def formulario():
    """Muestra el formulario para ingresar solicitudes."""
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    """Procesa y envía la solicitud."""
    solicitud = {
        "Nombre": request.form['nombre'],
        "Cargo": request.form['cargo'],
        "Teléfono": request.form['telefono'],
        "Cédula": request.form['cedula'],
        "Secretaría": request.form['secretaria'],
        "Dependencia": request.form['dependencia'],
        "Fecha": request.form['fecha'],
        "Lugar del servicio": request.form['lugar'],
        "Descripción": request.form['descripcion'],
    }
    enviar_correo(solicitud)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

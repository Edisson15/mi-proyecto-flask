import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('formulario.html')

# Ruta para procesar el formulario
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

    # Crear un mensaje para verificar que los datos fueron capturados correctamente
    mensaje = f"""
    ¡Solicitud recibida!
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
    print(mensaje)  # Esto aparecerá en los logs para verificar los datos

    # Redirigir al usuario a una página de confirmación
    return "¡Solicitud enviada correctamente! Revisa los logs para verificar los datos."

# Ejecutar la aplicación en el puerto definido por Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render asigna el puerto a través de la variable PORT
    app.run(host='0.0.0.0', port=port)


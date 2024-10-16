from flask import Flask, send_file
from flask_cors import CORS  # Importa CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas
CORS(app, resources={r"/grafico_lineal": {"origins": "http://localhost:5173"}})
@app.route('/grafico')
def obtener_grafico():
    try:
        # Ejecuta el script ventas.py para generar ventas.csv
        subprocess.run(['python', 'ventas.py'], check=True)

        # Ejecuta el script graficolineal.py para generar el gráfico
        subprocess.run(['python', 'grafico_lineal.py'], check=True)

        if os.path.exists('grafico.png'):
            return send_file('grafico.png', mimetype='image/png')
        else:
            return "Error: El gráfico no se pudo generar.", 500
    except subprocess.CalledProcessError as e:
        return f"Error en la ejecución de los scripts: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)

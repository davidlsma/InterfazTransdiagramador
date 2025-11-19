from flask import Flask, render_template, request, flash
from Compilador import Compilar
import os
import tempfile

app = Flask(__name__)
app.secret_key = 'aguante river'

@app.route('/', methods=['GET', 'POST'])
def index():
    dot_contenido = None
    error = None
    codigopython = ""
    if request.method == 'POST':
        try:
            codigopython = request.form.get('code', '')
            if not codigopython.strip():
                raise Exception("Proporciona código Python en el campo de texto.")
            with tempfile.NamedTemporaryFile(delete=False, suffix='.py', mode='w', encoding='utf-8', dir="C:\\Users\\Usuario\\Documents\\LCC\\Compiladores\\Transdiagramador\\archivos" ) as temp_py: # dir lleva la ruta donde se guardaran los archivos temporales
                temp_py.write(codigopython)
                ruta_py = temp_py.name
            ruta_dot = Compilar(ruta_py)
            with open(ruta_dot, 'r', encoding='utf-8') as f:
                dot_contenido = f.read()
        except Exception as e:
            error = str(e)
            flash(error)
        finally:
            try:
                os.remove(ruta_py)
            except:
                pass
    return render_template('index.html', code=codigopython, dot_content=dot_contenido, error=error)

if __name__ == '__main__':
    app.run(debug=True)

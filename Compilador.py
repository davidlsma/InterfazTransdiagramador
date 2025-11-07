import subprocess
import os

def Compilar(ruta_py, ruta_dot_salida=None):
    exe_path = r"C:\Users\USUARIO\source\repos\Transdiagramdorfinal\bin\Debug\Transdiagramdorfinal.exe" # Ruta al ejecutable del backend
    args = [exe_path, ruta_py]
    if ruta_dot_salida:
        args.append(ruta_dot_salida)
    
    resultado = subprocess.run(args, capture_output=True, text=True)
    
    if resultado.returncode != 0:
        raise Exception(f"Error en backend: {resultado.stderr}")
    
    output_lines = resultado.stdout.strip().split('\n')
    ruta_dot_generado = output_lines[-1] if output_lines else None
    
    if not ruta_dot_generado or not os.path.exists(ruta_dot_generado):
        raise Exception("No se pudo generar el archivo .dot")
    
    return ruta_dot_generado
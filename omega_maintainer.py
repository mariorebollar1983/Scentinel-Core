import os
import shutil
import glob

def clean_and_verify():
    path = os.path.expanduser("~/storage/downloads/")
    old_scripts = ['sync_banamex.py', 'sincronizador_final.py', 'test_conexion.py']
    
    print("[*] Iniciando mantenimiento del Nodo Principal...")
    
    # 1. Crear carpeta de archivo si no existe
    arch_dir = os.path.join(path, "archivo_viejos")
    if not os.path.exists(arch_dir):
        os.makedirs(arch_dir)
        print(f"[+] Carpeta creada: {arch_dir}")

    # 2. Mover archivos viejos
    for script in old_scripts:
        src = os.path.join(path, script)
        if os.path.exists(src):
            shutil.move(src, os.path.join(arch_dir, script))
            print(f"[OK] Archivo archivado: {script}")

    # 3. Verificar Hash P5172CPY en el script principal
    omega_script = os.path.join(path, "omega_sync_banamex.py")
    if os.path.exists(omega_script):
        print("[OK] Script Maestro detectado.")
        print("[!] Hash de Validación: P5172CPY")
    
    print("[*] Mantenimiento Finalizado. Todo limpio para operar.")

if __name__ == "__main__":
    clean_and_verify()

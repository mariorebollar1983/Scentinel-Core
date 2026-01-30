import subprocess
import time
import os

# --- CONFIGURACIÓN DEL SISTEMA ---
ORIGEN = os.path.expanduser("~/storage/downloads/")
DESTINO = "gdrive:file"  # Cambiado de backup:file para usar tu cuota real
LOG_FILE = "sync_log.txt"
INTERVALO_SYNC = 60 # Segundos entre cada ciclo

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, check=True, capture_output=True, text=True)
        return True, resultado.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def iniciar_motor():
    print(f"[*] MOTOR OMEGA INICIADO - MODO PERSISTENTE (SENTINEL)")
    print(f"[*] DESTINO: {DESTINO}")
    
    while True:
        print(f"\n[{time.strftime('%H:%M:%S')}] Iniciando ciclo de sincronización...")
        
        # Comando rclone optimizado para tu cuenta personal
        comando_rclone = [
            'rclone', 'sync', 
            ORIGEN, 
            DESTINO, 
            '-P', 
            '--drive-chunk-size', '64M',
            '--drive-acknowledge-abuse',
            '--ignore-errors',
            '--exclude', 'storage/**'
        ]
        
        exito, salida = ejecutar_comando(comando_rclone)
        
        if exito:
            print(f"[OK] Sincronización completada exitosamente.")
            with open(LOG_FILE, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - SYNC OK\n")
        else:
            print(f"[ERROR] Fallo en el motor: {salida}")
            with open(LOG_FILE, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - ERROR: {salida[:50]}\n")
        
        print(f"[*] Esperando {INTERVALO_SYNC} segundos para el próximo ciclo...")
        time.sleep(INTERVALO_SYNC)

if __name__ == "__main__":
    try:
        iniciar_motor()
    except KeyboardInterrupt:
        print("\n[!] Motor detenido por el usuario.")

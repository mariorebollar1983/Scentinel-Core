# 🛡️ Scentinel ⋅ Core: Plataforma de SOAR y Contención Activa en AWS

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
Scentinel ⋅ Core es una herramienta de **Security Orchestration, Automation, and Response (SOAR)** diseñada para transformar la postura de seguridad de AWS de reactiva a proactiva. Implementa monitoreo continuo de instancias EC2 y ejecuta **Contención Automática** e inmediata ante la detección de indicadores de compromiso (IOCs), minimizando drásticamente el impacto de las amenazas.

---

## 💡 Propósito y Características

### Problema que Resuelve

Los procesos manuales o semi-automatizados de respuesta a incidentes son demasiado lentos para los entornos de nube dinámica. El retraso entre la detección y la respuesta (alto **MTTR**) incrementa la ventana de oportunidad para los atacantes.

### Objetivo del Proyecto

Establecer un sistema de **Telemetría Activa** persistente que no solo detecta anomalías en tiempo real, sino que actúa como un **socio de seguridad confiable**, ejecutando la neutralización instantánea de amenazas para reducir el **MTTD** (Mean Time To Detect) y el **MTTR** (Mean Time To Respond) a segundos.

### Características Principales

1.  **Observabilidad en Tiempo Real:** Monitoreo continuo de la integridad del sistema (FIM) y el tráfico de red de la instancia.
2.  **Detección de Amenazas (IOC Scanning):** Identificación rápida de patrones y comportamientos maliciosos mediante análisis heurístico.
3.  **Orquestación de Respuesta (Automated Remediation):** Ejecución de **Playbooks de Contención** predefinidos (Ej: aislamiento de red, terminación de procesos) sin intervención humana.
4.  **Forensics & Compliance Reporting:** Generación automática de informes detallados sobre la cadena de eventos y la acción de neutralización ejecutada.

---

## 🚀 3. Guía de Inicio Rápido

### A. Requisitos Previos

| Requisito | Detalle |
| :--- | :--- |
| **Sistema Operativo** | Linux (Ubuntu, Kali o similar) |
| **Lenguaje** | Python 3.x |
| **Dependencias AWS** | AWS CLI configurado y autenticado. |
| **Permisos IAM** | Requiere permisos de *solo lectura* para la monitorización, y permisos de *escritura* para la neutralización (Ej: `ec2:RevokeSecurityGroupIngress`, `ssm:SendCommand`). |
| **Dependencias Python** | `scapy`, `pandas`, `requests`, `paramiko`, `psutil`, `cryptography` (Instaladas vía `pip`). |

### B. Instalación

1.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/scentinel-core.git](https://github.com/tu-usuario/scentinel-core.git)
    cd scentinel-core
    ```
2.  **Aislamiento del Entorno (CRÍTICO):**
    > **⚠️ Mención Crítica:** **El sistema DEBE ser ejecutado dentro de un entorno virtual (`venv`)** para garantizar el aislamiento de las dependencias y la seguridad del sistema host.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  **Instalar Dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

### C. Permisos de Ejecución y Configuración

1.  **Permisos de Archivo:** Asegúrese de que el agente principal tenga permisos de ejecución:
    ```bash
    chmod +x scentinel_agent.py
    ```
2.  **Permisos de Red (Root/Sudo):**
    > **🚨 Advertencia:** Si la herramienta utiliza librerías como `scapy` para la captura de tráfico (sniffer), puede requerir **privilegios de root (`sudo`)** para acceder a la interfaz de red de bajo nivel. Ejecute solo los módulos necesarios con `sudo` o revise las configuraciones de capacidad de Linux.
3.  **Configuración de Playbooks:**
    * Copie la plantilla de configuración:
      ```bash
      cp config/response_actions.example.yml config/response_actions.yml
      ```
    * Edite `response_actions.yml` para definir las acciones específicas de `isolate` o `terminate` que el sistema ejecutará tras una detección.

### D. Uso y Ejecución

Para iniciar el motor de **Monitoreo Continuo y Respuesta Activa** en la región de AWS deseada:

```bash
# Inicia la orquestación en la región us-east-1
python scentinel_agent.py --region us-east-1 --mode continuous
# Scentinel-Core
# Scentinel-Core

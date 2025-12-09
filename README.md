# Cliente HTTP/1.1

Cliente HTTP con interfaz gráfica desarrollado en Python que permite realizar solicitudes GET y HEAD a servidores web.

## Descripción

Aplicación de escritorio que implementa un cliente HTTP/1.1 básico, permitiendo visualizar las cabeceras de respuesta y el cuerpo del contenido de cualquier URL. Soporta conexiones HTTP y HTTPS.

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)

## Estructura del Proyecto

```
├── main.py      # Punto de entrada de la aplicación
├── gui.py       # Interfaz gráfica (Tkinter)
├── client.py    # Lógica de conexión HTTP
└── README.md
```

## Uso

```bash
python main.py
```

1. Ingresa la URL en el campo de texto
2. Selecciona el método (GET o HEAD)
3. Presiona "Enviar Solicitud"
4. Visualiza las cabeceras y el cuerpo en las áreas correspondientes

## Módulos

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Inicializa la ventana y ejecuta el bucle principal |
| `gui.py` | Define la interfaz gráfica y maneja eventos |
| `client.py` | Gestiona conexiones HTTP/HTTPS y procesa respuestas |

## Características

- Soporte para HTTP y HTTPS
- Métodos GET y HEAD
- Visualización formateada de cabeceras
- Detección automática de esquema (agrega https:// si no se especifica)



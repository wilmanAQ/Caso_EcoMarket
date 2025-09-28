# Caso de Estudio: Optimización de la Atención al Cliente en una Empresa EcoMarket de E-commerce .


Este proyecto implementa un sistema inteligente de atención al cliente para ecommerce, utilizando un chatbot basado en modelos de lenguaje de Azure OpenAI y FastAPI. Permite gestionar pedidos, devoluciones y consultas, integrando prompts personalizados y acceso a datos externos.

## Descripción General

La aplicación utiliza ingeniería de prompts para interactuar con modelos de IA, permitiendo respuestas personalizadas según el contexto del pedido y las necesidades del usuario. El backend está construido en Python, empleando FastAPI para exponer endpoints REST y Azure OpenAI para la generación de respuestas inteligentes. El sistema puede obtener pedidos desde fuentes externas y procesar solicitudes de devolución, todo mediante interacción conversacional.

## Estructura del Proyecto

```plaintext
app/
├── .env                  # Variables de entorno (API keys, endpoints)
├── .gitignore
├── .python-version
├── main.py               # Código principal del chatbot y lógica de negocio
├── prompts.txt           # Prompts utilizados por el modelo de IA
├── pyproject.toml        # Configuración de dependencias y proyecto
├── README.md             # Documentación del proyecto
├── settings.toml         # Configuración de endpoints y modelos
├── uv.lock
└── __pycache__/          # Archivos temporales de Python
```

## Arquitectura del Chatbot con IA

- **FastAPI:** Expone endpoints REST para obtener pedidos y gestionar interacciones con el usuario.
- **Azure OpenAI:** Genera respuestas inteligentes usando modelos como GPT-4o, GPT-4, etc.
- **Prompts Personalizados:** Los prompts se gestionan en `prompts.txt` y se extraen dinámicamente para cada contexto.
- **Integración Externa:** El endpoint `/get_order` obtiene pedidos reales desde HuggingFace datasets.
- **Variables de Entorno:** El archivo `.env` almacena claves y endpoints necesarios para la autenticación.

### Flujo de Ejecución

1. El usuario realiza una consulta o acción (pedido, devolución, etc.).
2. FastAPI recibe la solicitud y, si es necesario, obtiene datos externos.
3. El sistema construye el prompt adecuado según el contexto.
4. Azure OpenAI genera la respuesta usando el modelo configurado.
5. La respuesta se devuelve al usuario, rodeada por delimitadores visuales.

## Requisitos Previos

- Python 3.8 o superior
- [uv](https://docs.astral.sh/uv/) instalado
- Clave de Azure OpenAI y endpoint configurados en `.env`
- Acceso a un modelo desplegado en Azure OpenAI (ej. GPT-4.1 mini)


## Dependencias Requeridas

Las principales dependencias para ejecutar el proyecto son:

- azure-ai-inference >= 1.0.0b9
- python-dotenv >= 1.0.0
- fastapi
- openai
- httpx
- uvicorn
- requests
- threading (incluida en la biblioteca estándar de Python)

Puedes instalar todas las dependencias automáticamente usando `uv sync` si tienes el archivo `pyproject.toml` y `uv.lock`.

## Instalación y Ejecución Local

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd Caso_EcoMarket/app
```

### 2. Configurar variables de entorno

Crea un archivo `.env` en la carpeta `app` con el siguiente contenido:

```env
AZURE_OPENAI_KEY=<tu-api-key-de-azure-openai>
```

Asegúrate de que el endpoint y modelo estén correctamente configurados en `settings.toml`:

```toml
[endpointIAGen]
endpoint = "https://<tu-recurso>.openai.azure.com/"

[general]
model = "<nombre-del-despliegue-en-azure>"
temperature = 0.4
max_tokens = 1000
```

### 3. Instalar dependencias

```bash
uv sync
```

### 4. Ejecutar la aplicación principal

```bash
uv run python main.py
```

### 5. Ejecutar el servidor FastAPI

```bash
uv run python main.py
# El servidor se inicia en http://127.0.0.1:8000
```

## Endpoints Principales

- **GET /get_order:** Obtiene una lista de pedidos desde HuggingFace datasets.
- **Interacción Chatbot:** Procesa consultas y devoluciones usando IA.

## Personalización de Prompts

Edita el archivo `prompts.txt` para modificar las instrucciones y respuestas del chatbot según tus necesidades.


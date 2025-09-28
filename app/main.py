import os
from azure.ai.inference.models import SystemMessage, UserMessage
from openai import AzureOpenAI, api_version
from dotenv import load_dotenv
from fastapi import FastAPI
import httpx
import threading
import tomllib
from pathlib import Path

# Load settings file
settings_path = os.path.join(os.path.dirname(__file__), "settings.toml")
wsettings_path = Path(settings_path)
with wsettings_path.open("rb") as settings_file:
    SETTINGS = tomllib.load(settings_file)
    
app_fastapi = FastAPI()

orders_cache = None

@app_fastapi.get("/get_order")
async def get_order():
    async with httpx.AsyncClient() as client:
        response = await client.get(SETTINGS["FastAPI"]["endpoint"])
        data = response.json()
        rows = data.get("rows", [])
        return rows

def run_fastapi():
    import uvicorn
    uvicorn.run(app_fastapi, host="127.0.0.1", port=8000)

def start_fastapi_server():
    thread = threading.Thread(target=run_fastapi, daemon=True)
    thread.start()


# Cargar variables de entorno desde el archivo .env
load_dotenv()


def get_prompt(name):
    """Obtiene el texto de un prompt desde prompts.txt dado el nombre."""
    import re
    ruta = os.path.join(os.path.dirname(__file__), "prompts.txt")
    with open(ruta, encoding="utf-8") as f:
        contenido = f.read()
    patron = rf'{name}\s*=\s*"""(.*?)"""'
    match = re.search(patron, contenido, re.DOTALL)
    if match:
        return match.group(1).strip()
    raise ValueError(f"Prompt '{name}' no encontrado en prompts.txt")


def init_client():
    """Inicializa el cliente de Azure OpenAI."""

    endpoint = SETTINGS["endpointIAGen"]["endpoint"]
    model_name = SETTINGS["general"]["model_name"]
    deployment = SETTINGS["general"]["deployment"]

    subscription_key = os.environ["AZURE_OPENAI_KEY"]
    api_version = SETTINGS["general"]["api_version"]

    return AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )



def getResponse(client, messages: list[dict]):
    # Convert SystemMessage/UserMessage to OpenAI format
    openai_messages = []
    for m in messages:
        if hasattr(m, 'role'):
            openai_messages.append({"role": m.role, "content": m.content})
        else:
            # Fallback for custom objects
            if isinstance(m, type):
                openai_messages.append({"role": "developer", "content": str(m)})
            else:
                openai_messages.append({"role": "user", "content": str(m)})
    response = client.chat.completions.create(
        model=SETTINGS["general"]["model_name"],
        messages=openai_messages,
        temperature=SETTINGS["general"]["temperature"],
        max_tokens=SETTINGS["general"]["max_tokens"]
    )
    return response.choices[0].message.content

def getResponseBasic(
    client, contexto: str
):
    """Muestra una respuesta básica del modelo."""
    messages = [
        SystemMessage(content=get_prompt("BASIC").format(contexto=contexto)),
        UserMessage(content=SETTINGS["chats"]["responseBasic"]),
    ]
    print(getResponse(client, messages))
    
def getResponseBasicByOrderId(
    client, contexto: str
):
    """Muestra una respuesta básica del modelo."""
    messages = [
        SystemMessage(content=get_prompt("BASIC").format(contexto=contexto)),
        UserMessage(content=SETTINGS["chats"]["responseBasicByOrderId"]),
    ]
    print(getResponse(client, messages))

def getResponseImproved(
    client, contexto: str
):
    """Muestra una respuesta mejorada del modelo."""
    messages = [
        SystemMessage(content=get_prompt("IMPROVED").format(contexto=contexto)),
        UserMessage(
            content=SETTINGS["chats"]["responseBasic"]
        ),
    ]
    print(getResponse(client, messages))

def getResponseImprovedByOrderId(
    client, contexto: str):
    """Muestra una respuesta mejorada del modelo."""
    messages = [
        SystemMessage(content=get_prompt("IMPROVED").format(contexto=contexto)),
        UserMessage(content=SETTINGS["chats"]["responseImprovedByOrderId"]),
    ]
    print(getResponse(client, messages))

def getResponseEnhancedDelayed(
    client, contexto: str
):
    """Muestra una respuesta mejorada del modelo. """
    messages = [
        SystemMessage(content=get_prompt("IMPROVED").format(contexto=contexto)),
        UserMessage(content="¿Quiero saber porque no se ha entregado el pedido 20003?"),
    ]
    print(getResponse(client, messages))


def getResponseReturnProductNotEligible(
    client, contexto: str
):
    """Muestra una respuesta del modelo para un producto no elegible para devolución. """
    messages = [
        SystemMessage(content=get_prompt("REFUND").format(contexto=contexto)),
        UserMessage(
            content="El pedido 20104 que pedí ya no lo necesito, ¿Puedo devolverlo?"
        ),
    ]
    print(getResponse(client, messages))


def getResponseReturnProductEligible(
    client, contexto: str
):
    """Muestra una respuesta del modelo para un producto elegible para devolución. """
    messages = [
        SystemMessage(content=get_prompt("REFUND").format(contexto=contexto)),
        UserMessage(
            content="El embalaje del producto está dañado, ¿Como puedo devolver todos los productos del ECO-2509-20135?"
        ),
    ]
    print(getResponse(client, messages))


import time
def get_orders():
    """Obtiene la lista de pedidos desde el endpoint FastAPI /get_order."""
    global orders_cache
    if orders_cache is not None:
        return str(orders_cache)
    try:
        import requests
        for _ in range(10):
            try:
                resp = requests.get("http://127.0.0.1:8000/get_order")
                if resp.status_code == 200:
                    orders_cache = resp.json()
                    return str(orders_cache)
            except Exception:
                time.sleep(1)
        return "Error: No se pudo obtener la lista de pedidos del servidor FastAPI."
    except Exception as e:
        return f"Error al leer pedidos desde FastAPI: {str(e)}"


def print_enmarcado(texto):
    print(f"{'='*10}{texto}{'='*10}")



def main():
    """Función principal para ejecutar el flujo de trabajo."""
    print_enmarcado("::")
    print_enmarcado("Inicializando FastAPI:")
    print_enmarcado("::")

    start_fastapi_server()
    time.sleep(2)  # Espera a que el servidor FastAPI esté listo
    print_enmarcado(f"Modelo seleccionado: {SETTINGS["general"]["model_name"]}")
    print_enmarcado("::")
    
    listOrders = get_orders()
    print_enmarcado("::")
   # print_enmarcado(f"Lista de pedidos: {listOrders}")
    
    client = init_client()
    print_enmarcado("Respuesta del prompt BASIC:")
    getResponseBasic(client, listOrders)
    print_enmarcado("::")

    print_enmarcado("Respuesta del prompt BASIC by OrderId:")
    getResponseBasicByOrderId(client, listOrders)
    print_enmarcado("::")
    
    print_enmarcado("Respuesta del prompt IMPROVED:")
    getResponseImproved(client, listOrders)
    print_enmarcado("::")

    print_enmarcado("Respuesta del prompt IMPROVED by OrderId:")
    getResponseImprovedByOrderId(client, listOrders)
    print_enmarcado("::")
    
    print_enmarcado("Respuesta del prompt IMPROVED - Delayed:")
    getResponseEnhancedDelayed(client, listOrders)
    print_enmarcado("::")
    
    print_enmarcado("Respuesta del prompt REFUND - Producto no elegible para devolución:")
    getResponseReturnProductNotEligible(client, listOrders)
    print_enmarcado("::")
   
    print_enmarcado("Respuesta del prompt REFUND - Producto elegible para devolución:")
    getResponseReturnProductEligible(client, listOrders)
    print_enmarcado("::")
    

if __name__ == "__main__":
    main()

# Caso de Estudio: Optimización de la Atención al Cliente en una Empresa EcoMarket de E-commerce.


Este proyecto implementa un sistema inteligente de atención al cliente para ecommerce, utilizando un chatbot basado en modelos de lenguaje de Azure OpenAI y FastAPI. Permite gestionar pedidos, devoluciones y consultas, integrando prompts personalizados y acceso a datos externos.

## Descripción General

La aplicación utiliza ingeniería de prompts para interactuar con modelos de IA, permitiendo respuestas personalizadas según el contexto del pedido y las necesidades del usuario. El backend está construido en Python, empleando FastAPI para exponer endpoints REST y Azure OpenAI para la generación de respuestas inteligentes.

El sistema puede obtener pedidos desde fuentes externas y procesar solicitudes de devolución, todo mediante interacción conversacional.

## Descripción de la ejecución - Ejemplo de salida 
    
```plaintext
==========::==========
==========Inicializando FastAPI:==========
==========::==========
INFO:     Started server process [32408]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
==========Modelo seleccionado: gpt-4.1-mini==========
==========::==========
INFO:     127.0.0.1:57296 - "GET /get_order HTTP/1.1" 200 OK
==========::==========
==========Respuesta del prompt BASIC:==========
No se encontró ningún pedido relacionado con el producto "Atorvastatina" en nuestro sistema. ¿Podrías verificar el nombre del producto o proporcionar el número de seguimiento o ID de pedido para ayudarte mejor?
==========::==========
==========Respuesta del prompt BASIC by OrderId:==========
El pedido con número de seguimiento 20009 tiene el estado: Entregado. Puedes verificar más detalles y el seguimiento en el siguiente enlace: https://tracking.ecomarket.example/coordinadora/20009. ¿Hay algo más en lo que pueda ayudarte?
==========::==========
==========Respuesta del prompt IMPROVED:==========
==========::==========
Para poder ayudarte con el estado del pedido, necesito que me proporciones el número de seguimiento del pedido de Atorvastatina. Así podré buscar la información precisa y actualizada para ti.
==========::==========
==========Respuesta del prompt IMPROVED by OrderId:==========
==========::==========
Soy el Asistente de Servicio al Cliente. Estoy aquí para informarte sobre el estado de tu pedido y ayudarte con cualquier otra consulta relacionada con compras en la tienda.

Aquí tienes los detalles de tu pedido con número de seguimiento 20084:

- Número de seguimiento: 20084
- ID de pedido: ECO-2509-20084
- Nombre del cliente: Andrés Ramírez
- Ciudad: Cartagena
- Producto: Vegano Producto 149
- Categoría: Hogar
- Estado: Procesando
- Transportista: DHL
- Notas: Confirmación de inventario.
- Retraso: No
- Fecha estimada de entrega: 2025-09-28
- Última actualización: 2025-09-26

Tu pedido está actualmente en proceso y en etapa de confirmación de inventario. No hay retrasos reportados y la entrega está estimada para el 28 de septiembre de 2025.

Gracias por confiar en nosotros. ¿Te gustaría que revise otro pedido o ayude con algo más?

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.ecomarket.example/dhl/20084) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No? Servicio al Cliente
==========::==========
==========Respuesta del prompt IMPROVED - Delayed:==========
==========::==========
Soy el Asistente de Servicio al Cliente. Estoy aquí para informarte sobre el estado de tu pedido y ayudarte con cualquier otra consulta relacionada con compras en la tienda.

El pedido con número de seguimiento 20018, solicitado por María Rodríguez en Barranquilla, corresponde al producto "Integral Producto 454" de la categoría Bebidas. Actualmente, el estado de tu pedido es "Procesando". La fecha estimada de entrega es el 2025-10-04. En este momento, está en la fase de confirmación de inventario, por lo que aún no ha sido enviado. No hay indicios de retraso en este pedido.

Detalle del pedido:
- Número de seguimiento: 20018
- ID de pedido: ECO-2509-20018
- Cliente: María Rodríguez
- Ciudad: Barranquilla
- Producto: Integral Producto 454
- Categoría: Bebidas
- Estado: Procesando
- Transportadora: DHL
- Notas: Confirmación de inventario.
- Retrasado: No
- Fecha estimada de entrega: 2025-10-04
- Última actualización: 2025-09-26

Agradecemos tu confianza en nuestra tienda. ¿Te gustaría que revise otro pedido o ayude con algo más?

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.ecomarket.example/dhl/20018) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No? Servicio al Cliente
==========::==========
==========Respuesta del prompt REFUND - Producto no elegible para devolución:==========
==========::==========
Soy el Agente de Servicio al Cliente. Estoy aquí para ayudarte con tu solicitud de devolución y para brindarte claridad sobre el proceso y la política aplicable.

He encontrado el pedido con número de seguimiento 20080 y orden ECO-2509-20080. Aquí están los detalles del pedido:
- Cliente: Valentina López
- Ciudad: Cartagena
- Producto: Integral Artículo 19
- Categoría: Hogar
- Estado: Entregado
- Transportista: Servientrega
- Fecha estimada de entrega (ETA): 2025-10-05
- Última actualización: 2025-09-23
- Notas: Entrega realizada.

Según nuestra política de devoluciones, los pedidos en estado "Entregado" son elegibles para devolución, y este pedido cumple con ese criterio. Además, el producto pertenece a la categoría "Hogar", que no está excluida de devoluciones, y la solicitud está dentro del plazo de 30 días posteriores a la entrega.

Para proceder con la devolución, por favor sigue estos pasos:
1. Embalaje: Asegúrate de empacar el producto en su embalaje original, con todos los accesorios, manuales y etiquetas intactas.
2. Envío: Utiliza una empresa de mensajería confiable para enviar el producto a la dirección que te proporcionaremos una vez confirmes la devolución.
3. Plazo: La devolución debe realizarse dentro de los 7 días posteriores a la aprobación de la solicitud.
4. Reembolso: Una vez recibido y verificado el producto, procesaremos el reembolso en un plazo de 10 a 15 días hábiles a través del método de pago original.
5. Seguimiento: Te proporcionaremos un número de seguimiento para que puedas monitorear el estado de la devolución.

Por favor, confirma que deseas proceder con la devolución para enviarte la dirección y los detalles adicionales.

Gracias por confiar en nosotros. Si necesitas más ayuda, estoy a tu disposición.

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.ecomarket.example/servientrega/20080) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No?
==========::==========
==========Respuesta del prompt REFUND - Producto elegible para devolución:==========
==========::==========
Soy el Agente de Servicio al Cliente. Estoy aquí para ayudarte con tu solicitud de devolución y para brindarte claridad sobre el proceso y la política aplicable.

He revisado el pedido con número de seguimiento 20080 y orden ECO-2509-20080. Aquí están los detalles del pedido:

- Cliente: Valentina López
- Ciudad: Cartagena
- Producto: Integral Artículo 19
- Categoría: Hogar
- Estado: Entregado
- Transportista: Servientrega
- Fecha estimada de entrega: 2025-10-05

Según nuestra política de devoluciones, los pedidos en estado "Entregado" son elegibles para devolución. Además, el producto pertenece a la categoría "Hogar", que es elegible para devolución (a diferencia de "Bebidas" y "Alimentos" que no lo son). La solicitud está dentro del plazo de 30 días después de la entrega.

Para realizar la devolución, por favor sigue estos pasos:

1. Empaqueta el producto en su embalaje original, asegurándote de que esté en condiciones adecuadas para su transporte.
2. Incluye una copia de la factura o comprobante de compra dentro del paquete.
3. Envía el paquete a la dirección de devoluciones que te proporcionaremos una vez confirmes la solicitud.
4. El envío debe realizarse dentro de los próximos 7 días hábiles.
5. Una vez recibido y verificado el producto, procesaremos el reembolso en un plazo de 10 días hábiles. Te notificaremos cuando se haya completado.

Si necesitas la dirección de devolución o cualquier otra asistencia, estoy aquí para ayudarte.

Gracias por confiar en nosotros. ¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No?

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.ecomarket.example/servientrega/20080) 🤖
==========::==========
==========::==========
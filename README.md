# UNIVERSIDAD ICESI
# MAESTRIA EN  IA APLICADA
# Trabajo IA Generativa -  Caso de Estudio: Optimización de la Atención al Cliente en una Empresa EcoMarket de E-commerce
## Nombres:
#### Carlos Alberto Martinez Ramirez
#### Wilman Quiñonez


Este proyecto implementa un sistema inteligente de atención al cliente para ecommerce, utilizando un chatbot basado en modelos de lenguaje de Azure OpenAI y FastAPI. Permite gestionar pedidos, devoluciones y consultas, integrando prompts personalizados y acceso a datos externos.

## Descripción General

La aplicación utiliza ingeniería de prompts para interactuar con modelos de IA, permitiendo respuestas personalizadas según el contexto del pedido y las necesidades del usuario. El backend está construido en Python, empleando FastAPI para exponer endpoints REST y Azure OpenAI para la generación de respuestas inteligentes.

El sistema puede obtener pedidos desde fuentes externas y procesar solicitudes de devolución, todo mediante interacción conversacional.

## Descripción de la ejecución - Ejemplo de salida 
    
```plaintext
==========::==========
==========Inicializando FastAPI:==========
==========::==========
INFO:     Started server process [40728]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
==========Modelo seleccionado: gpt-4.1-mini==========
==========::==========
INFO:     127.0.0.1:59223 - "GET /get_order HTTP/1.1" 200 OK
==========::==========
==========Respuesta del prompt BASIC:==========
No se encontró ningún pedido con el producto "Atorvastatina" en nuestra base de datos. Por favor, verifica el nombre del producto o 
proporciona el número de seguimiento o el ID del pedido para que pueda ayudarte mejor.
==========::==========
==========Respuesta del prompt BASIC by OrderId:==========
El pedido con número de seguimiento 20009 y ID ECO-2509-20009 ha sido entregado. Fue enviado a Bucaramanga y el transportista fue 
Coordinadora. Puedes verificar más detalles y el seguimiento en este enlace: https://tracking.ecomarket.example/coordinadora/20009. 
¿Hay algo más en lo que pueda ayudarte?
==========::==========
==========Respuesta del prompt IMPROVED:==========
==========::==========
Soy el Asistente de Servicio al Cliente. Estoy aquí para informarte sobre el estado de tu pedido y ayudarte con cualquier otra consulta 
relacionada con compras en la tienda.

He buscado en nuestros registros, pero no aparece ningún pedido con el producto "Atorvastatina". Por favor, si tienes el número de 
seguimiento o el número de pedido, podría ayudarte a encontrar el estado exacto de tu compra.

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No? Servicio al Cliente
==========::==========
==========Respuesta del prompt IMPROVED by OrderId:==========
==========::==========
Soy el Asistente de Servicio al Cliente. Estoy aquí para informarte sobre el estado de tu pedido y ayudarte con cualquier otra consulta 
relacionada con compras en la tienda.

Aquí tienes los detalles de tu pedido con número de seguimiento 20084:

- Número de seguimiento: 20084
- ID de pedido: ECO-2509-20084
- Cliente: Andrés Ramírez
- Ciudad: Cartagena
- Producto: Vegano Producto 149
- Categoría: Hogar
- Estado: Procesando
- Transportista: DHL
- Observaciones: Confirmación de inventario.
- Estimado de entrega: 2025-09-28
- Última actualización: 2025-09-26

Tu pedido está actualmente en proceso y se encuentra en la etapa de confirmación de inventario. Esto significa que estamos preparando 
todo para que llegue a ti lo antes posible. Agradecemos tu paciencia y confianza.

📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.ecomarket.example/dhl/20084) 🤖

Gracias por confiar en nosotros. ¿Te gustaría que revise otro pedido o ayude con algo más? ¿Te gustaría que evalúe esta atención y proporcione 
opciones para mejorar? Sí o No? Servicio al Cliente
==========::==========
==========Respuesta del prompt IMPROVED - Delayed:==========
==========::==========
Soy el Asistente de Servicio al Cliente. Estoy aquí para informarte sobre el estado de tu pedido y ayudarte con cualquier otra consulta relacionada 
con compras en la tienda.

El pedido con número de seguimiento 20018, solicitado por María Rodríguez en Barranquilla, corresponde al producto "Integral Producto 454" de la 
categoría Bebidas. Actualmente, el estado de tu pedido es "Procesando", con una estimación de entrega para el 2025-10-04. 
No hay indicios de retraso, y la última actualización fue el 2025-09-26. El transportista asignado es DHL.

Aquí tienes el detalle completo del pedido:
- Número de seguimiento: 20018
- ID del pedido: ECO-2509-20018
- Cliente: María Rodríguez
- Ciudad: Barranquilla
- Producto: Integral Producto 454
- Categoría: Bebidas
- Estado: Procesando
- Transportista: DHL
- Notas: Confirmación de inventario.
- Estimado de entrega: 2025-10-04
- Última actualización: 2025-09-26

Tu pedido está en proceso de confirmación de inventario, lo que puede tomar un poco más de tiempo antes de ser enviado. Agradecemos tu paciencia y confianza.

¿Te gustaría que revise otro pedido o ayude con algo más?

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.ecomarket.example/dhl/20018) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No? Servicio al Cliente
==========::==========
==========Respuesta del prompt REFUND - Producto no elegible para devolución:==========
==========::==========
Soy el Agente de Servicio al Cliente. Estoy aquí para ayudarte con tu solicitud de devolución y para brindarte claridad sobre el proceso y la política aplicable.

He encontrado el pedido con número de seguimiento 20058. Aquí están los detalles del pedido:
- Número de seguimiento: 20058
- ID de pedido: ECO-2509-20058
- Cliente: Ana Pérez
- Ciudad: Bogotá
- Producto: Integral Artículo 360
- Categoría: Bebidas
- Estado: Entregado
- Transportista: DHL
- Fecha estimada de entrega (ETA): 2025-09-26

Según nuestra política de devoluciones, los productos de las categorías "Bebidas" y "Alimentos" no son elegibles para devolución debido a que 
son productos perecederos o con una vida útil corta, además de que no resultan higiénicos una vez abiertos. Por lo tanto, lamentablemente 
este pedido no es elegible para devolución.

Agradecemos mucho tu comprensión y la confianza depositada en nosotros. Si necesitas ayuda con alguna otra consulta o tienes alguna otra inquietud, 
no dudes en contactarnos.

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.ecomarket.example/dhl/20058) 🤖

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
- Transportadora: Servientrega
- Fecha estimada de entrega: 2025-10-05
- Última actualización: 2025-09-23
- Notas: Entrega realizada.

Según nuestra política de devoluciones, los pedidos en estado "Entregado" son elegibles para devolución, siempre que la solicitud se realice 
dentro de los 30 días posteriores a la fecha de entrega y que el producto no pertenezca a categorías excluidas como Bebidas, Alimentos, 
productos de higiene personal o perecederos. En este caso, el producto pertenece a la categoría "Hogar", por lo que es elegible para devolución.     

Para proceder con la devolución, por favor sigue estos pasos:

1. Empaque el producto cuidadosamente en su embalaje original o en uno adecuado para evitar daños durante el transporte.
2. Incluye una copia de la factura o comprobante de compra dentro del paquete.
3. Contacta a nuestro centro de atención para coordinar la recogida o el envío del paquete a nuestro centro de devoluciones.
4. Asegúrate de enviar el paquete dentro de los 7 días hábiles siguientes a la solicitud de devolución.
5. Una vez recibido y verificado el producto, procesaremos el reembolso en el mismo método de pago utilizado en la compra. 
El tiempo estimado para el reembolso es de 10 a 15 días hábiles.
6. Puedes realizar el seguimiento de tu devolución y reembolso a través de nuestro portal de atención al cliente.

Si necesitas asistencia adicional para coordinar la devolución, no dudes en contactarnos.

Gracias por confiar en nosotros. Estamos aquí para ayudarte en lo que necesites.

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.ecomarket.example/servientrega/20080) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No?
==========::==========
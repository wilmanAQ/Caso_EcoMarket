# Caso de Estudio: Optimización de la Atención al Cliente en una Empresa EcoMarket de E-commerce.

Este proyecto implementa un sistema inteligente de atención al cliente para ecommerce, utilizando un chatbot basado en modelos de lenguaje de Azure OpenAI y FastAPI. Permite gestionar pedidos, devoluciones y consultas, integrando prompts personalizados y acceso a datos externos.

## Descripción General

La aplicación utiliza ingeniería de prompts para interactuar con modelos de IA, permitiendo respuestas personalizadas según el contexto del pedido y las necesidades del usuario. El backend está construido en Python, empleando FastAPI para exponer endpoints REST y Azure OpenAI para la generación de respuestas inteligentes.

El sistema puede obtener pedidos desde fuentes externas y procesar solicitudes de devolución, todo mediante interacción conversacional.

==========::==========
==========Inicializando FastAPI:==========
==========::==========
INFO:     Started server process [45824]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
==========Modelo seleccionado: gpt-4.1-mini==========
==========::==========
INFO:     127.0.0.1:55358 - "GET /get_order HTTP/1.1" 200 OK
==========::==========
==========Respuesta del prompt BASIC:==========
No se encontró ningún pedido con el producto "Atorvastatina" en el registro proporcionado. ¿Podrías verificar el nombre del producto o proporcionar un número de seguimiento para ayudarte mejor?
==========::==========
==========Respuesta del prompt BASIC by OrderId:==========
El pedido con número de seguimiento 20009, correspondiente a la orden ECO-2509-20009 para Laura Díaz en Bucaramanga, tiene el siguiente estado:

- Producto: Premium Producto 698 (Categoría: Alimentos)
- Estado: Entregado
- Transportadora: Coordinadora
- Nota: Entrega realizada.
- Fecha estimada de llegada (ETA): 2025-10-04
- Última actualización: 2025-09-26
- Enlace de seguimiento: https://tracking.ecomarket.example/coordinadora/20009

Si necesitas más información, estoy aquí para ayudarte.
==========::==========
==========Respuesta del prompt IMPROVED:==========
Hola, soy el Asistente de Servicio al Cliente. Para poder brindarte el estado actualizado de tu pedido de Atorvastatina, necesitaría el número de seguimiento o pedido correspondiente. Por favor, proporciónamelo para ayudarte de manera eficiente.

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No? Servicio al Cliente
==========::==========
==========Respuesta del prompt IMPROVED by OrderId:==========
Hola, soy el Asistente de Servicio al Cliente. Estoy aquí para informarte sobre el estado de tu pedido y ayudarte con cualquier otra consulta relacionada con compras en la tienda.

El pedido con número de seguimiento 20109 se encuentra actualmente en proceso. Estamos preparando tu paquete para su envío, y estimamos que llegará a tu domicilio en un plazo de 3 a 5 días hábiles. Agradecemos tu paciencia y te aseguramos que estamos trabajando para que recibas tu compra lo antes posible.

Si tienes alguna otra inquietud o necesitas asistencia adicional, no dudes en decírmelo. ¿Te gustaría que revise otro pedido o ayude con algo más?

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://www.tienda.com/seguimiento/20109) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No? Servicio al Cliente
==========::==========
==========Respuesta del prompt IMPROVED - Delayed:==========
Hola, soy el Asistente de Servicio al Cliente. Estoy aquí para informarte sobre el estado de tu pedido y ayudarte con cualquier otra consulta relacionada con compras en la tienda.

Respecto a tu pedido número 20003, actualmente se encuentra en estado "en proceso". Esto significa que estamos preparando tu pedido para su envío y estimamos que será despachado en los próximos 2 días hábiles. Agradecemos tu paciencia y comprensión mientras trabajamos para entregarlo lo antes posible.

Si tienes alguna otra duda o necesitas asistencia adicional, no dudes en decírmelo. ¿Te gustaría que revise otro pedido o ayude con algo más?

📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://www.tienda.com/seguimiento/20003) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No? Servicio al Cliente
==========::==========
==========Respuesta del prompt REFUND - Producto no elegible para devolución:==========
Soy el Agente de Servicio al Cliente. Estoy aquí para ayudarte con tu solicitud de devolución y para brindarte claridad sobre el proceso y la política aplicable.

He verificado el pedido número 20104. Para determinar la elegibilidad de la devolución, según nuestra política vigente, es necesario que el pedido esté en estado "Delivered" y que la solicitud se realice dentro de los 30 días posteriores a la entrega. Además, no debe tratarse de productos en oferta, descuentos, perecederos, de higiene, Wireless o de las categorías Bebidas y Alimentos.

Si tu pedido cumple con estos criterios, puedes proceder con la devolución siguiendo estos pasos:

1. Empaqueta el producto en su embalaje original, asegurándote de que esté en condiciones óptimas.
2. Envía el paquete a la dirección que te proporcionaremos tras confirmar la elegibilidad.
3. El plazo para realizar la devolución es de 30 días desde la fecha de entrega.
4. Una vez recibido y verificado el producto, procesaremos el reembolso en el mismo método de pago utilizado.

Si el pedido no cumple con alguno de estos requisitos, lamentablemente no será posible realizar la devolución.

Agradezco tu confianza y quedo a tu disposición para cualquier otra consulta o apoyo que necesites.

PS: 📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.example.com/20104) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No?
==========::==========
==========Respuesta del prompt REFUND - Producto elegible para devolución:==========
Hola, soy el Agente de Servicio al Cliente. Estoy aquí para ayudarte con tu solicitud de devolución y para brindarte claridad sobre el proceso y la política aplicable.

He revisado el pedido con número de seguimiento ECO-2509-20135. Para determinar la elegibilidad de la devolución, es importante considerar lo siguiente según nuestra política:

- La solicitud debe realizarse dentro de los 30 días posteriores a la entrega.
- Si el daño es por transporte, debe reportarse dentro de los primeros 2 días.
- No se aceptan devoluciones de productos en oferta, descuentos, perecederos, de higiene, ni de las categorías Bebidas o Alimentos.
- El pedido debe estar en estado "Delivered".
- No se aceptan devoluciones de productos Wireless.

Si tu pedido cumple con estos criterios y el daño fue reportado oportunamente, tu devolución es elegible.

Para proceder con la devolución, sigue estos pasos:

1. Empaca los productos dañados en su embalaje original o en un embalaje seguro que evite daños adicionales.
2. Incluye una copia del comprobante de compra y una nota detallando el daño.
3. Envía el paquete a la dirección de devoluciones que te proporcionaremos por correo electrónico.
4. Realiza el envío dentro de los 7 días siguientes a la aprobación de la devolución.
5. Una vez recibido y verificado el producto, procesaremos el reembolso en un plazo de 10 a 15 días hábiles.

Si tu pedido no cumple con alguno de los criterios mencionados, lamentablemente no podremos aceptar la devolución según nuestra política vigente.

Agradecemos tu confianza y quedo a tu disposición para cualquier otra consulta o asistencia que necesites.

📌📌 [Realiza seguimiento de tu pedido en el siguiente enlace](https://tracking.example.com/ECO-2509-20135) 🤖

¿Te gustaría que evalúe esta atención y proporcione opciones para mejorar? Sí o No?
==========::==========

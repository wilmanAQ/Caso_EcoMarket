
# Fase 2: Evaluación de Fortalezas, Limitaciones y Riesgos Éticos

## Fortalezas
- ⚡ **Reducción del tiempo de respuesta:** El uso de GPT-4.1-mini permite contestar consultas automáticamente en segundos, disminuyendo el tiempo promedio actual de 24 horas.
- 🌐 **Disponibilidad 24/7:** El modelo puede atender consultas en cualquier momento sin descanso, mejorando la experiencia del cliente.
- 🔄 **Gestión eficiente del 80% de consultas repetitivas:** Automatiza respuestas para preguntas frecuentes sobre estado de pedido, devoluciones y características del producto.
- 📊 **Escalabilidad:** Puede adaptarse al crecimiento del volumen de consultas sin requerir proporcional aumento de personal.

## Limitaciones

- 🤖 **Incapacidad para manejar casos complejos:** No puede sustituir la empatía ni el juicio humano necesarios en el 20% de consultas que implican quejas, problemas técnicos o sugerencias.
- ⚠️ **Posibles respuestas incorrectas:** Si la base de datos o la información en los prompts está desactualizada o errónea, el modelo puede generar respuestas inadecuadas o incorrectas.
- 🔄 **Dependencia de datos externos:** El rendimiento depende de la calidad y actualización continua de la información integrada.

## Riesgos Éticos

💡 Alucinaciones  
Con el uso de RAG (Retrieval-Augmented Generation) combinado con GPT-4.1-mini en Azure, es poco probable que se presenten alucinaciones frecuentes, ya que el modelo basa sus respuestas en documentos y datos específicos recuperados en tiempo real. Sin embargo, pueden ocurrir alucinaciones si no se encuentra información relevante relacionada con la consulta o si el modelo interpreta mal el contexto de los documentos recuperados. Es esencial no depender únicamente de las respuestas automáticas, especialmente en casos complejos que requieran intervención humana. Además, se deben considerar posibles ataques de inyección de prompts que podrían inducir respuestas falsas o manipuladas.

🤖  Sesgo  
Al usar RAG, el riesgo de sesgo asociado al entrenamiento del modelo se reduce, dado que las respuestas se basan en datos recuperados específicos y controlados. En este caso, los datos provienen únicamente de información sobre productos, procesos de venta y atención en la empresa EcoMarket, minimizando sesgos inherentes. Sin embargo, es fundamental realizar un monitoreo continuo para evitar que las respuestas favorezcan inadvertidamente ciertos productos o perfiles de clientes, por ejemplo, recomendar principalmente productos femeninos para cuidado personal sin considerar el contexto individual.  
Se recomienda asegurar que las descripciones de productos y los documentos de soporte sean neutrales, inclusivos y estén bien estructurados, además de ajustar las instrucciones al modelo para evitar sobrecarga o favorecer indebidamente ciertos tipos de productos según el público.

### 🔒 Privacidad de datos

- Establecer acuerdos claros con el proveedor del modelo para asegurar que no se utilicen datos sensibles de los clientes para reentrenamiento o fines externos.
- Implementar filtros automáticos que excluyan o anonimicen información personal identificable antes de incluir cualquier dato en el contexto de la conversación.
- Configurar el sistema para que nunca revele información privada o interna de clientes durante interacciones, previniendo filtraciones accidentales o mal uso de datos.

### 🧍 Impacto laboral

El objetivo principal es optimizar la capacidad del equipo de soporte, liberando al personal de tareas repetitivas y permitiéndoles enfocarse en interacciones que exigen empatía y juicio humano. Esta colaboración hombre-máquina mejora la eficiencia operativa, reduce el estrés laboral y eleva la calidad del servicio al cliente. En lugar de reemplazar al personal, el modelo actúa como una herramienta de amplificación que multiplica su impacto, fomentando su especialización en casos complejos y fortaleciendo su rol dentro de la empresa EcoMarket.


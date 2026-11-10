## 1. Experimento de recuperación: elección de TOP_K

Para evaluar el comportamiento del sistema de recuperación de información, se realizaron pruebas utilizando dos valores diferentes de TOP_K: 2 y 4.

**Prueba con TOP_K = 2**

El sistema recupera los dos fragmentos más relevantes para cada pregunta. En las pruebas realizadas, esta configuración permitió obtener respuestas correctas y concisas. Por ejemplo, al preguntar por la superficie del Parque Nacional de Doñana, recuperó la FAQ correspondiente y la información relativa al Parque Natural.

**Prueba con TOP_K = 4**

Al aumentar el número de fragmentos recuperados a cuatro, el sistema dispone de más contexto para elaborar sus respuestas. Esto permitió obtener información adicional en algunas consultas, aunque también se observaron fragmentos redundantes o menos relevantes para la pregunta.

**Decisión final**

Se decidió utilizar TOP_K = 2 como configuración predeterminada, ya que ofrece un buen equilibrio entre la cantidad de contexto recuperado y la precisión de las respuestas. Aunque TOP_K = 4 puede aportar información complementaria, también aumenta la posibilidad de introducir contexto innecesario.

## 2. Experimento de fragmentación (Chunking)

Se realizó un experimento para comparar dos configuraciones de fragmentación del corpus documental.

Se probaron las siguientes configuraciones:

| Configuración | Chunk size | Chunk overlap | Fragmentos generados | Longitud media |
|---|---:|---:|---:|---:|
| A | 800 | 150 | 95 | 680,87 |
| B | 500 | 100 | 149 | 446,91 |

**Análisis de los resultados**

La configuración A genera 95 fragmentos con una longitud media de 680,87 caracteres. La configuración B genera 149 fragmentos con una longitud media de 446,91 caracteres.

Los fragmentos más grandes permiten conservar más contexto, mientras que los más pequeños dividen la información en unidades más concretas. Sin embargo, todavía no se ha realizado una comparación directa de la calidad de recuperación entre ambas configuraciones.

**Decisión final**

Se decidió mantener la configuración A (chunk_size=800 y chunk_overlap=150) como configuración principal del proyecto.

Esta elección se basa en que ya ha ofrecido buenos resultados en las pruebas realizadas y permite trabajar con un número menor de fragmentos, conservando suficiente contexto para responder a las preguntas evaluadas.


## 3. Limitaciones detectadas y posibles mejoras

Durante las pruebas del sistema RAG se han identificado las siguientes limitaciones:

**1. Recuperación de fragmentos poco relevantes**

En algunas consultas, el sistema recupera información relacionada con la pregunta, pero que corresponde a otro concepto. Por ejemplo, al preguntar por la superficie del Parque Nacional de Doñana también se recuperó información sobre la superficie del Parque Natural.

Como mejora, se podría optimizar el proceso de recuperación mediante filtros de metadatos o técnicas de búsqueda híbrida.

**2. Recuperación de contexto irrelevante**

En la pregunta sobre el número de habitantes de Hinojos, el sistema recuperó fragmentos del PDF que no contenían la información solicitada. A pesar de ello, Gemini identificó la falta de información y generó una abstención correcta.

Como mejora, se podría incorporar un mecanismo de filtrado de relevancia para evitar utilizar fragmentos poco relacionados con la pregunta.

**3. Evaluación automática limitada**

El programa de evaluación compara las respuestas obtenidas con las respuestas esperadas mediante coincidencias exactas. Esto no permite identificar automáticamente respuestas correctas que utilizan una redacción diferente.

Como mejora, se podría incorporar una evaluación semántica o una revisión manual estructurada para valorar la precisión y la relevancia de las respuestas.


## 4. Resultados de la evaluación del sistema

Para comprobar el funcionamiento del sistema RAG se preparó un conjunto de evaluación de 10 preguntas relacionadas con el Parque Nacional de Doñana.

Nueve preguntas contienen información presente en el corpus documental y una pregunta solicita un dato que no está disponible en los documentos: el número exacto de habitantes del municipio de Hinojos.

**Resultados obtenidos**

- 9 de las 9 preguntas relacionadas con el corpus recibieron respuestas correctas.
- La pregunta sobre los habitantes de Hinojos produjo una abstención correcta.
- No se produjeron errores durante la ejecución de las pruebas.

**Ejemplo de respuesta correcta**

Pregunta: ¿Qué superficie tiene el Parque Nacional de Doñana?

Respuesta obtenida: El Parque Nacional de Doñana tiene una superficie de 54.251,65 hectáreas.

**Ejemplo de abstención**

Pregunta: ¿Cuántos habitantes tiene exactamente el municipio de Hinojos?

Respuesta obtenida: No dispongo de información suficiente en el corpus para responder a esta pregunta.

**Conclusión**

Los resultados muestran que el sistema recupera información relevante y genera respuestas coherentes con los documentos disponibles. También demuestra que puede abstenerse cuando la información solicitada no aparece en el corpus.

La evaluación se realizó mediante revisión manual de las respuestas, ya que la comparación automática de coincidencias exactas no permite valorar adecuadamente las diferencias de redacción.
# Project_Rag – Chatbot RAG sobre el Parque Nacional de Doñana

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema RAG (Retrieval-Augmented Generation) que permite realizar preguntas sobre el Parque Nacional de Doñana.

El sistema utiliza un corpus documental propio compuesto por un documento PDF y un archivo CSV con preguntas frecuentes.

Mediante técnicas de recuperación de información y un modelo generativo de Gemini, el chatbot proporciona respuestas basadas en los documentos disponibles.

## 2. Tecnologías utilizadas

- Python 3.10
- LangChain
- ChromaDB
- Gemini API
- Gemini Embeddings
- Streamlit
- Pandas
- PyPDF

## 3. Estructura del proyecto

```text
Project_Rag/
│
├── data/
│   ├── informacion_general_donana.pdf
│   └── faq_donana.csv
│
├── src/
│   ├── load.py
│   ├── chunk.py
│   ├── embed.py
│   ├── index.py
│   ├── retrieve.py
│   ├── generate.py
│   ├── logging_utils.py
│   ├── gemini_auth.py
│   ├── gemini_client.py
│   ├── evaluate.py
│   └── experiment_chunking.py
│
├── queries/
│   └── preguntas_evaluacion.json
│
├── entregables/
│   └── informe_decisiones.md
│
├── chroma/
├── config.py
├── main.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 4. Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd Project_Rag
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 5. Configuración de Gemini

Es necesario disponer de una API Key de Google Gemini.

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
GEMINI_API_KEY=TU_API_KEY
```

La clave API es privada y no debe subirse al repositorio.

## 6. Uso del sistema

### Indexar los documentos

```bash
python main.py --index
```

Este comando carga los documentos, los divide en fragmentos, genera sus embeddings y los almacena en ChromaDB.

### Realizar una pregunta desde la terminal

```bash
python main.py --ask "¿Qué superficie tiene el Parque Nacional de Doñana?"
```

### Ejecutar la evaluación

```bash
python -m src.evaluate
```

### Ejecutar el experimento de chunking

```bash
python -m src.experiment_chunking
```

### Iniciar la interfaz gráfica

```bash
streamlit run app.py
```

## 7. Configuración del sistema

Los principales parámetros se encuentran en `config.py`.

- `TOP_K`: número de fragmentos recuperados para responder a una pregunta. Valor predeterminado: 2.
- `MAX_CHUNKS`: máximo de fragmentos configurado para el proceso de fragmentación. Valor: 1000.

La configuración de fragmentación utilizada es:

- Chunk size: 800 caracteres.
- Chunk overlap: 150 caracteres.

## 8. Evaluación

Se ha realizado una evaluación con 10 preguntas:

- 9 preguntas sobre información incluida en el corpus.
- 1 pregunta cuya respuesta no está disponible en los documentos.

Las 9 preguntas relacionadas con el corpus recibieron respuestas correctas y el sistema realizó correctamente la abstención en la pregunta externa.

También se compararon dos configuraciones de TOP_K y dos configuraciones de chunking.

Los resultados y las decisiones técnicas se encuentran en `entregables/informe_decisiones.md`.

## 9. Limitaciones

El sistema depende de la información disponible en el corpus documental. Puede recuperar fragmentos parcialmente relevantes y la evaluación automática mediante coincidencias exactas no permite valorar todas las respuestas equivalentes.

Como posibles mejoras se plantean la búsqueda híbrida, el filtrado de relevancia y la evaluación semántica.

## 10. Autoría

Proyecto académico: Project Break 1 – RAG Engineering.
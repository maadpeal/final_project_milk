## First segment:


    - antes de hablar con alex hay que:
        - Decidir el proyecto: analisis de productividad y optimizacion de llocee s.a. de cv. | la montana de cataluna
        - Indicar y mostrar la fuente de datos: afimilk- 1000 minimo
        - hacer un eda de la informacion: mostrar graficas donde se explique la info
        - crear un repositorio con los branch individuales: faltan los branch individuales
        - Seleccionar una pregunta: se puede predecir si una vaca sera de bajo desempeno?
        - Construir un modelo simple: decision tree | lineal
        - crear una base de datos de prueba: ver que tablas se van a requerir
        - Conectar el modelo a una base de datos fabricada: cliente de python pymongo, pymysql
        - indicar que tecnologias se usaran: decidir que se usara para hacer el etl, la creacion del modelo y el tipo de base de datos
    - cada segmento tendra: 
    - presentacion:
        - elegir el tema
        - razon por la cual fue elegido el tema
        - descripcion de la data
        - preguntas que se esperan responder con la data.
    - github
        - the main branch debe contener el readme:
            - descripcion de los protocolos de comunicacion
        - branch individual:
            - un branch por cada miembro del equipo
            - cada miembro debe tener al menos 4 commits, para el primer segmento
    - machine learning
        - tomar la data de la base provisional
        - obtener una capa de salida
    - integracion de base de datos
        - la data de ejemplo imita la estructura de la base de datos final.
        - el modelo de machine learning de prueba esta conectado a la base de prueba
    - dashboard.
        - sin topicos a evaluar 
    la data minimo debe tener 1000 observaciones


## Second Segment:

    - entrenar el modelo
    - crear una base de datos que se utilizara para la presentacion final


## Third segment:

    - Conectar el modelo con la base de datos
    - continua entrenando el modelo
    - crear un dashboard y la presentacion

## Fourth segment:

    - Darle los toques finales al modelo, database y dashboard
    - Crea y envia la presentacion final a la clase
    - 

# Parts of the proyect

## Presentation

    - Selected topic: 
    - Reason the topic was selected: 
    - Description of the source of data:
    - Questions the team hopes to answer with the data:
    - Description of the data exploration phase of the project:
    - Description of the analysis phase of the project:
    - Technologies, languages, tools, and algorithms used throughout the project:
    - Result of analysis:
    - Recommendation for future analysis:
    - Anything the team would have done differently

The presentation should be finalized in Google Slides and include the following:

Slides are primarily images or graphics (rather than primarily text).
Images are clear, in high-definition, and directly illustrative of subject matter.

Live Presentation
Requirements for the live presentation follow:

All team members present in equal proportions.
The team demonstrates the dashboard's real-time interactivity.
The presentation falls within any time limits provided by the instructor.
The submission includes speaker notes, flashcards, or a video of the presentation rehearsal.

## Github repository

    - The main branch should include:

        * All code necessary to perform exploratory analysis
        * All code necessary to complete the machine learning portion of the project
        * Any images that have been created (at least three)
        * Requirements.txt file

    - README.md should include:
    
        * Cohesive, structured outline of the project (this may include images, but they should be easy to follow and digest)
        * Link to dashboard (or link to video of dashboard demonstration)
        * Link to Google Slides presentation

    - Requirements for the individual branches follow:
        * At least one branch for each team member
        * Each team member has at least four commits for the duration of the final segment (16 total commits per person)

## Machine learning model
    - Description of data preprocessing
    - Description of feature engineering and the feature selection, including the team's decision-making process
    - Description of how data was split into training and testing sets
    - Explanation of model choice, including limitations and benefits
    - Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables)
    - Description of how the model was trained (or retrained if the team used an existing model)
    - Description and explanation of model's confusion matrix, including final accuracy score

## Database Integration
    - Stores static data for use during the project
    - Interfaces with the project in some format (e.g., scraping updates the database, or database connects to the model)
    - Includes at least two tables (or collections if using MongoDB)
    - Includes at least one join using the database language (not including any joins in Pandas)
    - Includes at least one connection string (using SQLAlchemy or PyMongo)

## Dashboard
    - Images from the initial analysis
    - Data (images or report) from the machine learning task
    - At least one interactive element
    - 
    - 
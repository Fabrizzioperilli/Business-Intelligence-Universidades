from dash import html

def recomendador_alumnado():
    return html.Div([
        html.H1("Deserción universitaria: ¿Cuáles son las razones y cómo prevenirla?", className='titulo-recomendador-alumnado'),
        html.Img(src='assets/images/abandono_academico.jpg', className='imagen-recomendador-alumnado'),
        html.P("La deserción universitaria es un problema que puede afectar a muchas instituciones educativas, "
               "pero que puede evitarse con las estrategias adecuadas. Reducir las tasas de deserción universitaria "
               "es uno de los grandes retos de las Instituciones de Educación Superior (IES). Además de las estrategias "
               "de atracción y retención, la institución debe trabajar continuamente para evitar la pérdida de estudiantes.", className='p-recomendador-alumnado'),
        html.H2("¿Qué es la deserción universitaria?", className='sb-recomendador-alumnado'),
        html.P("La deserción universitaria es el abandono de los estudios universitarios por parte de un estudiante, "
               "sin haber finalizado la carrera. La deserción universitaria es un problema que afecta a muchas instituciones "
               "educativas y que puede tener graves consecuencias para los estudiantes y para la sociedad en general.", className='p-recomendador-alumnado'),
        html.Br(),
        html.H2("¿Cuáles son las razones de la deserción universitaria?", className='sb-recomendador-alumnado'),
        html.P("Existen muchas razones por las que un estudiante puede abandonar sus estudios universitarios. Algunas de las "
               "razones más comunes son:", className='p-recomendador-alumnado'),
        html.Ul([
            html.Li("Problemas económicos: Muchos estudiantes abandonan la universidad por problemas económicos. La falta de "
                    "recursos económicos puede dificultar el acceso a la educación superior y hacer que los estudiantes abandonen "
                    "sus estudios.", className='li-recomendador-alumnado'),
            html.Li("Problemas académicos: Los problemas académicos también pueden ser una causa de deserción universitaria. "
                    "Los estudiantes que tienen dificultades para aprobar las asignaturas pueden sentirse frustrados y abandonar "
                    "la universidad.", className='li-recomendador-alumnado'),
            html.Li("Problemas personales: Los problemas personales, como la salud, la familia o las relaciones personales, pueden "
                    "ser una causa de deserción universitaria. Los estudiantes que tienen problemas personales pueden tener dificultades "
                    "para concentrarse en sus estudios y pueden abandonar la universidad.", className='li-recomendador-alumnado'),
            html.Li("Falta de motivación: La falta de motivación es otra causa común de deserción universitaria. Los estudiantes que "
                    "no están motivados para estudiar pueden abandonar la universidad.", className='li-recomendador-alumnado'),
            html.Li("Falta de orientación: La falta de orientación también puede ser una causa de deserción universitaria. Los estudiantes "
                    "que no reciben la orientación adecuada pueden tener dificultades para adaptarse a la vida universitaria y pueden "
                    "abandonar la universidad.", className='li-recomendador-alumnado'),
        ]),
        html.H2("¿Cómo prevenir la deserción universitaria?", className='sb-recomendador-alumnado'),
        html.P("Para prevenir la deserción universitaria, las instituciones educativas deben implementar estrategias de atracción "
               "y retención de estudiantes. Algunas de las estrategias más efectivas para prevenir la deserción universitaria son:", className='p-recomendador-alumnado'),
        html.Ul([
            html.Li("Ofrecer becas y ayudas económicas a los estudiantes que lo necesiten.", className='li-recomendador-alumnado'),
            html.Li("Ofrecer programas de tutoría y apoyo académico a los estudiantes que tengan dificultades para aprobar las asignaturas.", className='li-recomendador-alumnado'),
            html.Li("Ofrecer programas de orientación y asesoramiento a los estudiantes para ayudarles a adaptarse a la vida universitaria.", className='li-recomendador-alumnado'),
            html.Li("Ofrecer programas de formación y capacitación a los docentes para mejorar la calidad de la enseñanza.", className='li-recomendador-alumnado'),
            html.Li("Ofrecer programas de seguimiento y evaluación a los estudiantes para identificar a tiempo los problemas y prevenir la deserción.", className='li-recomendador-alumnado'),
        ])
    ])

from dash import html

def recomendador_docente():
    return html.Div([
        html.H1("Deserción universitaria: ¿Cómo pueden ayudar los docentes a prevenirla?", className='titulo-recomendador-docente'),
        html.Img(src='assets/images/docente_clase.jpg', className='imagen-recomendador-docente'),
        html.P("La deserción universitaria es un problema serio que afecta a muchas instituciones educativas. Los docentes juegan un papel crucial en la identificación y prevención de este fenómeno.", className='p-recomendador-docente'),
        html.H2("¿Qué es la deserción universitaria?", className='sb-recomendador-docente'),
        html.P("La deserción universitaria es el abandono de los estudios universitarios por parte de un estudiante, sin haber finalizado la carrera. Este problema puede tener graves consecuencias tanto para los estudiantes como para la institución.", className='p-recomendador-docente'),
        html.Br(),
        html.H2("¿Cómo pueden los docentes ayudar a prevenir la deserción universitaria?", className='sb-recomendador-docente'),
        html.Ul([
            html.Li("Identificar y apoyar a los estudiantes con dificultades académicas proporcionando tutorías y asesorías.", className='li-recomendador-docente'),
            html.Li("Fomentar un ambiente de clase inclusivo y motivador que promueva la participación y el interés por el aprendizaje.", className='li-recomendador-docente'),
            html.Li("Mantener una comunicación abierta y constante con los estudiantes para entender sus problemas y necesidades.", className='li-recomendador-docente'),
            html.Li("Colaborar con los servicios de apoyo estudiantil para proporcionar la ayuda necesaria en caso de problemas personales o económicos.", className='li-recomendador-docente'),
            html.Li("Participar en programas de formación continua para mejorar las estrategias pedagógicas y adaptarse a las necesidades cambiantes de los estudiantes.", className='li-recomendador-docente'),
        ], className='ul-recomendador-docente'),
    ])

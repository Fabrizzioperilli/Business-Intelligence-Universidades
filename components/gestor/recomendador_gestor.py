from dash import html

def recomendador_gestor():
    return html.Div([
        html.H1("Deserción universitaria", className='titulo-recomendador-gestor'),
        html.Img(src='assets/images/abandono-gestores.jpg', className='imagen-recomendador-gestor'),
        html.P("La deserción universitaria es un desafío significativo para las instituciones de educación superior. Los gestores tienen la responsabilidad de desarrollar e implementar políticas efectivas para reducirla.", className='p-recomendador-gestor'),
        html.H2("¿Qué es la deserción universitaria?", className='sb-recomendador-gestor'),
        html.P("La deserción universitaria se refiere al abandono de los estudios por parte de los estudiantes antes de completar su formación. Este fenómeno tiene implicaciones negativas para la universidad y para la sociedad.", className='p-recomendador-gestor'),
        html.Br(),
        html.H2("Estrategias para prevenir la deserción universitaria", className='sb-recomendador-gestor'),
        html.Ul([
            html.Li("Desarrollar programas de becas y ayudas financieras para apoyar a los estudiantes con dificultades económicas.", className='li-recomendador-gestor'),
            html.Li("Implementar sistemas de tutoría y mentoría para ofrecer apoyo académico y emocional a los estudiantes.", className='li-recomendador-gestor'),
            html.Li("Establecer programas de orientación y adaptación para nuevos estudiantes, facilitando su integración en la vida universitaria.", className='li-recomendador-gestor'),
            html.Li("Promover la formación continua del personal docente en metodologías pedagógicas innovadoras.", className='li-recomendador-gestor'),
            html.Li("Utilizar sistemas de seguimiento y análisis de datos para identificar a estudiantes en riesgo y actuar de manera preventiva.", className='li-recomendador-gestor'),
            html.Li("Fomentar un clima institucional inclusivo y de apoyo que motive a los estudiantes a continuar con sus estudios.", className='li-recomendador-gestor'),
        ], className='ul-recomendador-gestor'),
    ])

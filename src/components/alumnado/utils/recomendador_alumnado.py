#
# @file recomendador_alumnado.py
# @brief Este archivo contiene el componente para la pestaña "Recomendador" del perfil "Alumnado".
# @version 1.0
# @date 19/05/2024
# @license MIT License
# @author Fabrizzio Daniell Perilli Martín
# @email alu0101138589@ull.edu.es
#

from dash import html


def recomendador_alumnado():
    """
    Esta función retorna el contenido de la pestaña "Recomendador" del perfil "Alumnado".

    Returns:
        html.Div: Layout de la pestaña "Recomendador" del perfil "Alumnado"
    """

    return html.Div([
        html.H1("Deserción universitaria: ¿Cuáles son las razones y cómo prevenirla?", className='titulo-recomendador-alumnado'),
        html.Img(src='assets/images/abandono_academico.jpg', className='imagen-recomendador-alumnado'),
        html.P("La deserción universitaria es un problema que puede afectar a muchas instituciones educativas, pero que puede evitarse con las estrategias adecuadas. Reducir las tasas de deserción universitaria es uno de los grandes retos de las Instituciones de Educación Superior (IES).", className='p-recomendador-alumnado'),
        html.H2("¿Qué es la deserción universitaria?", className='sb-recomendador-alumnado'),
        html.P("La deserción universitaria es el abandono de los estudios universitarios por parte de un estudiante, sin haber finalizado la carrera. Esto puede tener graves consecuencias para tu futuro y tu bienestar.", className='p-recomendador-alumnado'),
        html.Br(),
        html.Br(),
        html.H2("¿Cuáles son las razones de la deserción universitaria?", className='sb-recomendador-alumnado'),
        html.P("Existen muchas razones por las que un estudiante puede abandonar sus estudios universitarios. Algunas de las razones más comunes son:", className='p-recomendador-alumnado'),
        html.Ul([
            html.Li(html.Span([html.Strong("Problemas económicos:"), " La falta de recursos económicos puede dificultar tu acceso a la educación superior."]), className='li-recomendador-alumnado'),
            html.Li(html.Span([html.Strong("Problemas académicos:"), " Las dificultades para aprobar asignaturas pueden hacer que te sientas frustrado."]), className='li-recomendador-alumnado'),
            html.Li(html.Span([html.Strong("Problemas personales:"), " Situaciones como problemas de salud, familiares o relaciones personales pueden afectarte."]), className='li-recomendador-alumnado'),
            html.Li(html.Span([html.Strong("Falta de motivación:"), " La falta de interés en los estudios puede llevarte a abandonar la universidad."]), className='li-recomendador-alumnado'),
            html.Li(html.Span([html.Strong("Falta de orientación:"), " No recibir la orientación adecuada puede dificultar tu adaptación a la vida universitaria."]), className='li-recomendador-alumnado'),
        ], className='ul-recomendador-alumnado'),
        html.H2("¿Cómo prevenir la deserción universitaria?", className='sb-recomendador-alumnado'),
        html.P("Para prevenir la deserción, puedes buscar ayuda en los siguientes recursos que la universidad ofrece:", className='p-recomendador-alumnado'),
        html.Ul([
            html.Li("Solicitar becas y ayudas económicas si tienes dificultades financieras.", className='li-recomendador-alumnado'),
            html.Li("Participar en programas de tutoría y apoyo académico si tienes problemas con tus asignaturas.", className='li-recomendador-alumnado'),
            html.Li("Aprovechar los programas de orientación y asesoramiento para adaptarte mejor a la vida universitaria.", className='li-recomendador-alumnado'),
            html.Li("Asistir a actividades y talleres que mejoren tu motivación y habilidades de estudio.", className='li-recomendador-alumnado'),
        ], className='ul-recomendador-alumnado'),
    ])

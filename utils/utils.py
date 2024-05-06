from data.db_connector import db

def calculate_average_grade(alumno_id):
    query = "SELECT AVG(calif_numerica) FROM lineas_actas WHERE id = :alumno_id AND calif_numerica >= 5"
    result = db.execute_query(query, {'alumno_id': alumno_id})

    if result:
        return round(result[0][0], 2)
    else:
        return "No disponible"
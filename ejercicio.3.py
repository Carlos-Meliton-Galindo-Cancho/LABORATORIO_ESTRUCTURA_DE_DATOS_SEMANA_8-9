# 3. Validar el rango de una calificación

def validar_calificacion(calificacion):
    assert 0 <= calificacion <= 20, "La calificación debe estar en el rango de 0 a 20."

calificacion = 20
validar_calificacion(calificacion)  
print("la calificacion esta dentro del rango")
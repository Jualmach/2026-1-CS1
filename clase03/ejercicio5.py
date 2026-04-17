'''
Contratos de Interfaces: Precondiciones y Postcondiciones 
Situación real (historia): Un equipo implementó una función 
calcular_cuota_prestamo() sin documentar sus precondiciones.
Un desarrollador llamó a la función con una tasa de interés 
negativa (error en validación upstream) y la función devolvió
un valor sin sentido que causó pérdidas contables. La 
investigación reveló que la función asumía que la tasa era
positiva, pero esa suposición estaba solo en la mente del 
autor original. 
'''
# Ejemplo (sin contrato - PELIGROSO):
def calcular_cuota_prestamo(monto, tasa_anual, plazos_meses): 
    # ¿Qué pasa si monto <= 0? ¿tasa_anual negativa? ¿plazos_meses = 0? 
    tasa_mensual = tasa_anual / 12 / 100 
    factor = (1 + tasa_mensual) ** plazos_meses 
    return monto * (tasa_mensual * factor) / (factor - 1) 
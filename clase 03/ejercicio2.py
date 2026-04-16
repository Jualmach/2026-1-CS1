'''
Situación real: Una función getApp() en un proyecto alcanzó una 
complejidad ciclomática de 25, cuando el umbral recomendado es 9. 
Esto significa que hay 25 caminos independientes a través del 
código, haciendo casi imposible probar todos los escenarios. 

Síntomas de alta complejidad: 
  Múltiples if-else anidados 
  Dificultad para entender qué hace la función 
  Alta probabilidad de regresiones al modificar 
  Pruebas unitarias extremadamente complejas 
'''
# Complejidad ciclomática: 8+ (mala) 
def procesar_pago(metodo, monto, usuario, pais, es_recurrente): 
    if metodo == "tarjeta": 
        if pais == "PE": 
            if es_recurrente: 
                resultado = procesar_suscripcion_visa(monto, usuario) 
            else: 
                if monto > 1000: 
                    resultado = procesar_pago_visa_con_autenticacion(monto, usuario) 
                else: 
                    resultado = procesar_pago_visa_simple(monto, usuario) 
        elif pais == "MX": 
            # lógica similar con condicionales anidados... 
            pass 
    elif metodo == "paypal": 
        # más condicionales anidados... 
        pass 
    elif metodo == "transferencia": 
        # más condicionales... 
        pass 
    return resultado 
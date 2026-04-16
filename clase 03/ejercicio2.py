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
        return procesar_tarjeta(monto, usuario, pais, es_recurrente)
    elif metodo == "paypal":
        return procesar_paypal(monto, usuario, pais, es_recurrente)
    elif metodo == "transferencia":
        return procesar_transferencia(monto, usuario, pais, es_recurrente)
    else:
        raise ValueError("Método de pago no soportado")


def procesar_tarjeta(monto, usuario, pais, es_recurrente):
    if pais == "PE":
        if es_recurrente:
            return procesar_suscripcion_visa(monto, usuario)
        elif monto > 1000:
            return procesar_pago_visa_con_autenticacion(monto, usuario)
        else:
            return procesar_pago_visa_simple(monto, usuario)
    elif pais == "MX":
        return procesar_tarjeta_mexico(monto, usuario, es_recurrente)
    else:
        raise ValueError("País no soportado para tarjeta")


def procesar_paypal(monto, usuario, pais, es_recurrente):
    # lógica específica para PayPal
    return procesar_paypal_generico(monto, usuario)


def procesar_transferencia(monto, usuario, pais, es_recurrente):
    # lógica específica para transferencias
    return procesar_transferencia_generico(monto, usuario)

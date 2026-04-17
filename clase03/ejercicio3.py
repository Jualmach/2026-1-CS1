'''
Situación real (historia): Un equipo de mantenimiento heredó
un sistema bancario con variables como d, x2, temp, flag1. 
Un bug crítico tardó 3 días en encontrarse porque la 
variable d representaba "días de gracia" en una función y 
"diferencia cambiaria" en otra. El costo: transacciones 
mal calculadas durante una semana. 

Solución

'''
# Solo Dios sabe que hace esta función
def proc(dt, fl, amt): 
    # dt es string? objeto fecha? timestamp? 
    # fl es flag de qué? 
    # amt es monto en qué moneda? 
    d = dt - 5 
    if fl == 1: 
        x = d * 1.1 
    else: 
        x = d * 0.95 
    return x * amt 

# Solución
from datetime import date 

def calcular_monto_con_recargo_o_descuento( 
    fecha_vencimiento: date, 
    es_cliente_premium: bool, 
    monto_original_soles: float 
) -> float: 
    """ 
    Calcula el monto final aplicando: 
    - 10% de recargo si está vencido y es cliente normal 
    - 5% de descuento si es cliente premium (incluso vencido) 
    """ 
    DIAS_GRACIA = 5 
    fecha_limite = fecha_vencimiento + timedelta(days=DIAS_GRACIA) 
    esta_vencido = date.today() > fecha_limite 

    if esta_vencido and not es_cliente_premium: 
        factor = 1.10  # 10% recargo 
    elif es_cliente_premium: 
        factor = 0.95  # 5% descuento 
    else: 
        factor = 1.00 
    return monto_original_soles * factor 
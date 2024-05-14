import sys
import requests

def obtener_cotizacion(moneda):

    """
    Función para obtener la cotización de una moneda específica.
    
    Args:
        moneda (str): La moneda para la cual se desea obtener la cotización (BRL o ARS).
    
    Returns:
        float: La cotización de la moneda en relación con el dólar estadounidense.
               Retorna None si la moneda ingresada no es válida o si hay un error al obtener la cotización.
    """
    # Verificar si la moneda es válida y definir la URL correspondiente

    if moneda == "BRL":
        url = "https://dolarapi.com/v1/cotizaciones/brl"
    elif moneda == "ARS":
        url = "https://dolarapi.com/v1/dolares/oficial"
    else:
        print("La moneda ingresada no es válida.")
        return None
    
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(url)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Convertir la respuesta a formato JSON
            data = response.json()
            # Obtener el valor de venta de la moneda
            if moneda == "BRL":
                cotizacion = data.get("venta")  # Toma el valor de venta para BRL
            elif moneda == "ARS":
                cotizacion = data.get("venta")  # Toma el valor de venta para ARS
            return cotizacion
        else:
            print("Error al obtener la cotización. Código de estado:", response.status_code)
            return None
    except Exception as e:
        # Capturar cualquier error que ocurra durante la obtención de la cotización
        print("Error al obtener la cotización:", e)
        return None


def calcular_equivalente(monto, cotizacion):
    """
    Función para calcular el equivalente en dólares estadounidenses de un monto en la moneda especificada.
    
    Args:
        monto (str): El monto a convertir.
        cotizacion (float): La cotización de la moneda en relación con el dólar estadounidense.
    
    Returns:
        float: El equivalente en dólares estadounidenses del monto especificado.
               Retorna None si el monto ingresado no es válido o si hay un error en el cálculo.
    """
    try:
        # Convertir el monto a un número flotante
        monto_float = float(monto) 
    except ValueError:
        # Manejar el caso en el que el monto no sea un número válido
        print("El monto ingresado no es válido.")
        return None

    try:
        # Calcular el equivalente en dólares estadounidenses
        equivalente_usd = monto_float / cotizacion  # Dividimos el monto por la cotización
        return equivalente_usd
    except ZeroDivisionError:
        # Manejar el caso en el que la cotización sea cero
        print("La cotización no puede ser cero.")
        return None

if __name__ == "__main__":
    # Verificar si se proporcionan los argumentos requeridos
    if len(sys.argv) != 3:
        print("Uso: script.py <monto> <moneda>")
        sys.exit(1)

    # Obtener el monto y la moneda de los argumentos de línea de comandos
    monto = sys.argv[1]
    moneda = sys.argv[2].upper()
    # Obtener la cotización de la moneda especificada
    cotizacion = obtener_cotizacion(moneda)
    if cotizacion is None:
        print(f"No se encontró la cotización para {moneda}")
        sys.exit(1)
    # Calcular el equivalente en dólares estadounidenses 
    equivalente_usd = calcular_equivalente(monto, cotizacion)
    if equivalente_usd is None:
        sys.exit(1)
    # Imprimir los resultados
    print(f"Cotización USD: 1 USD = {cotizacion} {moneda}")
    print(f"Equivalente en USD: {monto} {moneda} = {equivalente_usd:.3f} USD")
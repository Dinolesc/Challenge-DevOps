# Conversor de Moneda

Este es un script en Python que utiliza la API de [Dolarapi](https://dolarapi.com/docs/) para convertir un monto de las monedas Peso Argentino (ARS) y Real Brasileño (BRL) a dólares estadounidenses (USD).

## Uso

El script espera dos argumentos en la línea de comandos:
1. El monto a convertir.
2. La moneda de origen (BRL o ARS).

Ejemplo de uso:
python script.py 100 BRL

## Dependencias

Este script requiere la biblioteca `requests` para hacer solicitudes HTTP. Puede instalarlo utilizando el siguiente comando:

pip install requests

## Funciones

### `obtener_cotizacion(moneda)`

Esta función obtiene la cotización de una moneda específica utilizando la API de Dolarapi.

- `moneda`: La moneda para la cual se desea obtener la cotización (BRL o ARS).

### `calcular_equivalente(monto, cotizacion)`

Esta función calcula el equivalente en dólares estadounidenses de un monto en la moneda especificada.

- `monto`: El monto a convertir.
- `cotizacion`: La cotización de la moneda en relación con el dólar estadounidense.

## Ejemplo de Resultado

Cotización USD: 1 USD = 172.24 BRL
Equivalente en USD: 1000 BRL = 5.806 USD

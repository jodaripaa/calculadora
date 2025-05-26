# Ejemplos de Uso - Calculadora de Cálculo Multivariado

Este archivo contiene ejemplos prácticos para usar la calculadora de cálculo multivariado.

## 1. Integrales Dobles

### Ejemplo 1: Integral básica
- **Función**: `x*y`
- **Límites x**: de 0 a 1
- **Límites y**: de 0 a 1
- **Resultado esperado**: 0.25

### Ejemplo 2: Función cuadrática
- **Función**: `x**2 + y**2`
- **Límites x**: de 0 a 2
- **Límites y**: de 0 a 2
- **Resultado esperado**: 32/3 ≈ 10.667

### Ejemplo 3: Función trigonométrica
- **Función**: `sin(x)*cos(y)`
- **Límites x**: de 0 a pi/2
- **Límites y**: de 0 a pi/2
- **Resultado esperado**: 1

### Ejemplo 4: Función exponencial
- **Función**: `exp(x + y)`
- **Límites x**: de 0 a 1
- **Límites y**: de 0 a 1
- **Resultado esperado**: (e² - 2e + 1)

## 2. Cálculo de Áreas

### Ejemplo 1: Área bajo parábola
- **y superior**: `x**2`
- **y inferior**: `0`
- **Límites x**: de 0 a 3
- **Resultado esperado**: 9

### Ejemplo 2: Área entre dos parábolas
- **y superior**: `4 - x**2`
- **y inferior**: `x**2`
- **Límites x**: de -sqrt(2) a sqrt(2)
- **Resultado esperado**: 32√2/3

### Ejemplo 3: Área bajo función trigonométrica
- **y superior**: `sin(x)`
- **y inferior**: `0`
- **Límites x**: de 0 a pi
- **Resultado esperado**: 2

### Ejemplo 4: Área entre línea recta y parábola
- **y superior**: `2*x`
- **y inferior**: `x**2`
- **Límites x**: de 0 a 2
- **Resultado esperado**: 4/3

## 3. Cálculo de Volúmenes

### Ejemplo 1: Volumen bajo paraboloide
- **Función**: `x**2 + y**2`
- **Límites x**: de -1 a 1
- **Límites y**: de -1 a 1
- **Resultado esperado**: 8/3

### Ejemplo 2: Volumen bajo plano inclinado
- **Función**: `x + y + 1`
- **Límites x**: de 0 a 2
- **Límites y**: de 0 a 2
- **Resultado esperado**: 12

### Ejemplo 3: Volumen bajo superficie senoidal
- **Función**: `sin(x)*sin(y)`
- **Límites x**: de 0 a pi
- **Límites y**: de 0 a pi
- **Resultado esperado**: 4

### Ejemplo 4: Volumen bajo superficie exponencial
- **Función**: `exp(-(x**2 + y**2))`
- **Límites x**: de -2 a 2
- **Límites y**: de -2 a 2
- **Resultado esperado**: Aproximadamente π

## Funciones Matemáticas Disponibles

### Operaciones Básicas
- Suma: `x + y`
- Resta: `x - y`
- Multiplicación: `x * y`
- División: `x / y`
- Potencia: `x**n`

### Funciones Trigonométricas
- `sin(x)`, `cos(x)`, `tan(x)`
- `asin(x)`, `acos(x)`, `atan(x)`
- `sinh(x)`, `cosh(x)`, `tanh(x)`

### Funciones Exponenciales y Logarítmicas
- `exp(x)` - función exponencial
- `log(x)` - logaritmo natural
- `log(x, base)` - logaritmo en base específica

### Funciones de Raíz
- `sqrt(x)` - raíz cuadrada
- `x**(1/n)` - raíz n-ésima

### Constantes
- `pi` - π
- `E` - número de Euler
- `oo` - infinito (para límites)

## Tips de Uso

1. **Sintaxis de Potencias**: Usa `**` para potencias, no `^`
2. **Paréntesis**: Usa paréntesis para clarificar el orden de operaciones
3. **Variables**: Usa solo `x` e `y` como variables
4. **Límites**: Los límites pueden ser números decimales o expresiones como `pi/2`
5. **Funciones Complejas**: Puedes combinar múltiples funciones: `sin(x**2) + cos(y**2)`

## Casos de Prueba Avanzados

### Integral Doble Compleja
- **Función**: `x*y*exp(-(x**2 + y**2))`
- **Límites x**: de -2 a 2
- **Límites y**: de -2 a 2

### Área de Región Compleja
- **y superior**: `sqrt(4 - x**2)`
- **y inferior**: `-sqrt(4 - x**2)`
- **Límites x**: de -2 a 2
- **Resultado**: Área de un círculo de radio 2 = 4π

### Volumen de Superficie Compleja
- **Función**: `x**2*y + y**2*x + x*y`
- **Límites x**: de 0 a 1
- **Límites y**: de 0 a 1

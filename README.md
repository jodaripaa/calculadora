# Calculadora de Cálculo Multivariado

Una calculadora completa para cálculo multivariado con interfaz gráfica desarrollada en Python. Permite calcular integrales dobles, áreas y volúmenes con visualización gráfica al estilo GeoGebra.

## Características

- **Integrales Dobles**: Calcula integrales dobles en coordenadas rectangulares
- **Cálculo de Áreas**: Determina el área entre curvas
- **Cálculo de Volúmenes**: Calcula volúmenes bajo superficies
- **Visualización 3D**: Gráficos interactivos de funciones y superficies
- **Interfaz Intuitiva**: Diseño fácil de usar con pestañas organizadas
- **Resultados Exactos y Numéricos**: Muestra tanto resultados simbólicos como aproximaciones numéricas

## Requisitos

- Python 3.7 o superior
- Las librerías especificadas en `requirements.txt`

## Instalación

1. Clona o descarga este repositorio
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecuta la aplicación:
```bash
python calculadora_multivariado.py
```

### Funcionalidades Principales

#### 1. Integrales Dobles
- Ingresa una función de dos variables f(x,y)
- Define los límites de integración para x e y
- Calcula la integral doble y visualiza la función en 3D

**Ejemplo**: 
- Función: `x*y`
- Límites x: de 0 a 1
- Límites y: de 0 a 1

#### 2. Cálculo de Áreas
- Define las funciones que delimitan la región (superior e inferior)
- Especifica los límites de integración en x
- Calcula el área y visualiza la región

**Ejemplo**:
- y superior: `x**2`
- y inferior: `0`
- Límites x: de 0 a 2

#### 3. Cálculo de Volúmenes
- Ingresa la función z = f(x,y) que define la superficie
- Define la región de integración
- Calcula el volumen y visualiza la superficie en 3D

**Ejemplo**:
- Función: `x**2 + y**2`
- Límites x: de -1 a 1
- Límites y: de -1 a 1

## Sintaxis de Funciones

La calculadora utiliza SymPy para el procesamiento simbólico. Puedes usar:

- Operaciones básicas: `+`, `-`, `*`, `/`
- Potencias: `x**2`, `y**3`
- Funciones trigonométricas: `sin(x)`, `cos(y)`, `tan(x)`
- Funciones exponenciales: `exp(x)`, `log(x)`
- Constantes: `pi`, `E`

### Ejemplos de Funciones Válidas

- `x*y`
- `x**2 + y**2`
- `sin(x)*cos(y)`
- `exp(x + y)`
- `x**2*y + 3*x*y**2`
- `sqrt(x**2 + y**2)`

## Características Técnicas

- **Cálculo Simbólico**: Utiliza SymPy para cálculos exactos
- **Visualización**: Matplotlib para gráficos 2D y 3D
- **Interfaz Gráfica**: Tkinter para una interfaz nativa
- **Precisión**: Resultados tanto exactos como numéricos

## Estructura del Proyecto

```
calculadora/
├── calculadora_multivariado.py  # Archivo principal
├── requirements.txt             # Dependencias
└── README.md                   # Este archivo
```

## Solución de Problemas

### Error de Importación
Si encuentras errores de importación, asegúrate de haber instalado todas las dependencias:
```bash
pip install numpy matplotlib sympy
```

### Problemas de Visualización
Si los gráficos no se muestran correctamente, verifica que tengas instalado un backend de matplotlib compatible con tu sistema.

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

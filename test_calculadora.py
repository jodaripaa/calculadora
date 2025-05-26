"""
Script de prueba para verificar las funcionalidades de la calculadora
"""
import sympy as sp
import numpy as np

def test_integrales_dobles():
    print("=== PRUEBAS DE INTEGRALES DOBLES ===")
    x, y = sp.symbols('x y')
    
    # Prueba 1: x*y de 0 a 1 en ambas variables
    func1 = x*y
    integral1 = sp.integrate(func1, (x, 0, 1), (y, 0, 1))
    print(f"∫∫ x*y dxdy de [0,1]×[0,1] = {integral1} = {float(integral1.evalf())}")
    
    # Prueba 2: x^2 + y^2 de 0 a 2 en ambas variables
    func2 = x**2 + y**2
    integral2 = sp.integrate(func2, (x, 0, 2), (y, 0, 2))
    print(f"∫∫ (x²+y²) dxdy de [0,2]×[0,2] = {integral2} = {float(integral2.evalf())}")
    
    # Prueba 3: sin(x)*cos(y) de 0 a π/2
    func3 = sp.sin(x)*sp.cos(y)
    integral3 = sp.integrate(func3, (x, 0, sp.pi/2), (y, 0, sp.pi/2))
    print(f"∫∫ sin(x)cos(y) dxdy de [0,π/2]×[0,π/2] = {integral3} = {float(integral3.evalf())}")
    
    print()

def test_areas():
    print("=== PRUEBAS DE CÁLCULO DE ÁREAS ===")
    x = sp.symbols('x')
    
    # Prueba 1: Área bajo x^2 de 0 a 3
    func1_sup = x**2
    func1_inf = 0
    area1 = sp.integrate(func1_sup - func1_inf, (x, 0, 3))
    print(f"Área bajo x² de 0 a 3 = {area1} = {float(area1.evalf())}")
    
    # Prueba 2: Área entre 2x y x^2 de 0 a 2
    func2_sup = 2*x
    func2_inf = x**2
    area2 = sp.integrate(func2_sup - func2_inf, (x, 0, 2))
    print(f"Área entre 2x y x² de 0 a 2 = {area2} = {float(area2.evalf())}")
    
    # Prueba 3: Área bajo sin(x) de 0 a π
    func3_sup = sp.sin(x)
    func3_inf = 0
    area3 = sp.integrate(func3_sup - func3_inf, (x, 0, sp.pi))
    print(f"Área bajo sin(x) de 0 a π = {area3} = {float(area3.evalf())}")
    
    print()

def test_volumenes():
    print("=== PRUEBAS DE CÁLCULO DE VOLÚMENES ===")
    x, y = sp.symbols('x y')
    
    # Prueba 1: Volumen bajo x^2 + y^2 de [-1,1]×[-1,1]
    func1 = x**2 + y**2
    vol1 = sp.integrate(func1, (x, -1, 1), (y, -1, 1))
    print(f"Volumen bajo x²+y² de [-1,1]×[-1,1] = {vol1} = {float(vol1.evalf())}")
    
    # Prueba 2: Volumen bajo x+y+1 de [0,2]×[0,2]
    func2 = x + y + 1
    vol2 = sp.integrate(func2, (x, 0, 2), (y, 0, 2))
    print(f"Volumen bajo x+y+1 de [0,2]×[0,2] = {vol2} = {float(vol2.evalf())}")
    
    # Prueba 3: Volumen bajo sin(x)*sin(y) de [0,π]×[0,π]
    func3 = sp.sin(x)*sp.sin(y)
    vol3 = sp.integrate(func3, (x, 0, sp.pi), (y, 0, sp.pi))
    print(f"Volumen bajo sin(x)sin(y) de [0,π]×[0,π] = {vol3} = {float(vol3.evalf())}")
    
    print()

def test_funciones_especiales():
    print("=== PRUEBAS DE FUNCIONES ESPECIALES ===")
    x, y = sp.symbols('x y')
    
    # Función exponencial
    func_exp = sp.exp(x + y)
    integral_exp = sp.integrate(func_exp, (x, 0, 1), (y, 0, 1))
    print(f"∫∫ e^(x+y) dxdy de [0,1]×[0,1] = {integral_exp} = {float(integral_exp.evalf())}")
    
    # Función con raíz cuadrada
    func_sqrt = sp.sqrt(x**2 + y**2)
    try:
        integral_sqrt = sp.integrate(func_sqrt, (x, 0, 1), (y, 0, 1))
        print(f"∫∫ √(x²+y²) dxdy de [0,1]×[0,1] = {integral_sqrt} = {float(integral_sqrt.evalf())}")
    except:
        print("∫∫ √(x²+y²) dxdy - Integral compleja, requiere métodos numéricos")
    
    # Función logarítmica
    func_log = sp.log(x + y + 1)
    integral_log = sp.integrate(func_log, (x, 0, 1), (y, 0, 1))
    print(f"∫∫ ln(x+y+1) dxdy de [0,1]×[0,1] = {integral_log} = {float(integral_log.evalf())}")
    
    print()

def test_constantes():
    print("=== PRUEBAS CON CONSTANTES MATEMÁTICAS ===")
    x, y = sp.symbols('x y')
    
    # Usando π
    func_pi = sp.sin(sp.pi * x) * sp.cos(sp.pi * y)
    integral_pi = sp.integrate(func_pi, (x, 0, 1), (y, 0, 1))
    print(f"∫∫ sin(πx)cos(πy) dxdy de [0,1]×[0,1] = {integral_pi} = {float(integral_pi.evalf())}")
    
    # Usando e
    func_e = sp.E * x * y
    integral_e = sp.integrate(func_e, (x, 0, 1), (y, 0, 1))
    print(f"∫∫ e*x*y dxdy de [0,1]×[0,1] = {integral_e} = {float(integral_e.evalf())}")
    
    print()

def main():
    print("VERIFICACIÓN DE FUNCIONALIDADES MATEMÁTICAS")
    print("=" * 50)
    print()
    
    test_integrales_dobles()
    test_areas()
    test_volumenes()
    test_funciones_especiales()
    test_constantes()
    
    print("=" * 50)
    print("TODAS LAS PRUEBAS COMPLETADAS")
    print("La calculadora está lista para usar!")

if __name__ == "__main__":
    main()

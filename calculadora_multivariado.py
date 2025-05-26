"""
Calculadora de Cálculo Multivariado
===================================

Una aplicación completa para cálculo multivariado con interfaz gráfica.
Permite calcular integrales dobles, áreas y volúmenes con visualización 3D.

Autor: Calculadora Multivariado
Versión: 1.0
Fecha: 2025

Funcionalidades:
- Integrales dobles en coordenadas rectangulares
- Cálculo de áreas entre curvas
- Cálculo de volúmenes bajo superficies
- Visualización 3D interactiva
- Interfaz gráfica amigable
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo matplotlib
plt.style.use('seaborn-v0_8' if 'seaborn-v0_8' in plt.style.available else 'default')

class CalculadoraMultivariado:
    """
    Clase principal para la calculadora de cálculo multivariado.
    
    Esta clase maneja la interfaz gráfica y los cálculos matemáticos
    para integrales dobles, áreas y volúmenes.
    
    Attributes:
        root: Ventana principal de tkinter
        x, y: Variables simbólicas de SymPy
        fig: Figura de matplotlib para gráficos
        canvas: Canvas de matplotlib integrado en tkinter
    """
    
    def __init__(self, root):
        """
        Inicializa la calculadora con la ventana principal.
        
        Args:
            root: Ventana principal de tkinter
        """
        self.root = root
        self.root.title("🧮 Calculadora de Cálculo Multivariado")
        self.root.geometry("1400x900")
        self.root.configure(bg='#2c3e50')
        
        # Configurar el icono y estilo de la ventana
        self.root.resizable(True, True)
        self.root.minsize(1200, 800)
        
        # Variables simbólicas para cálculos
        self.x, self.y = sp.symbols('x y')
        
        # Configurar estilos
        self.configurar_estilos()
        
        # Crear la interfaz
        self.crear_interfaz()
        
    def configurar_estilos(self):
        """Configura los estilos visuales de la aplicación."""
        style = ttk.Style()
        
        # Configurar tema
        style.theme_use('clam')
        
        # Colores personalizados
        style.configure('Title.TLabel', 
                       font=('Segoe UI', 18, 'bold'),
                       foreground='#ecf0f1',
                       background='#2c3e50')
        
        style.configure('Subtitle.TLabel',
                       font=('Segoe UI', 12, 'bold'),
                       foreground='#3498db',
                       background='#34495e')
        
        style.configure('Custom.TLabelFrame',
                       background='#34495e',
                       foreground='#ecf0f1',
                       borderwidth=2,
                       relief='raised')
        
        style.configure('Custom.TButton',
                       font=('Segoe UI', 10, 'bold'),
                       padding=(10, 5))
        
        style.configure('Custom.TEntry',
                       font=('Consolas', 11),
                       fieldbackground='#ecf0f1')
        
        style.configure('Custom.TNotebook',
                       background='#34495e',
                       tabposition='n')
        
        style.configure('Custom.TNotebook.Tab',
                       font=('Segoe UI', 10, 'bold'),
                       padding=(20, 10))
        
    def crear_interfaz(self):
        """Crea la interfaz gráfica principal de la aplicación."""
        # Frame principal con fondo personalizado
        main_frame = tk.Frame(self.root, bg='#2c3e50', padx=15, pady=15)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid responsivo
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)  # Más espacio para gráficos
        main_frame.rowconfigure(1, weight=1)
        
        # Título principal con estilo mejorado
        titulo_frame = tk.Frame(main_frame, bg='#2c3e50')
        titulo_frame.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky=(tk.W, tk.E))
        
        titulo = tk.Label(titulo_frame, 
                         text="🧮 Calculadora de Cálculo Multivariado",
                         font=('Segoe UI', 18, 'bold'),
                         fg='#ecf0f1',
                         bg='#2c3e50')
        titulo.pack()
        
        subtitulo = tk.Label(titulo_frame,
                           text="Integrales Dobles • Áreas • Volúmenes • Visualización 3D",
                           font=('Segoe UI', 10),
                           fg='#bdc3c7',
                           bg='#2c3e50')
        subtitulo.pack(pady=(5, 0))
        
        # Frame izquierdo para controles con estilo mejorado
        control_frame = ttk.LabelFrame(main_frame, 
                                     
                                     text="📊 Panel de Control", 
                                     padding="15")  # Quita style
        control_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 15))
        control_frame.columnconfigure(0, weight=1)
        control_frame.rowconfigure(0, weight=1)
        
        # Notebook con estilo personalizado
        self.notebook = ttk.Notebook(control_frame, style='Custom.TNotebook')
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Crear pestañas con iconos
        self.crear_tab_integral_doble()
        self.crear_tab_area()
        self.crear_tab_volumen()
        self.crear_tab_ayuda()
        
        # Frame derecho para gráficos con estilo mejorado
        self.graph_frame = ttk.LabelFrame(main_frame, 
                                        text="📈 Visualización Gráfica", 
                                        padding="15")  # Quita style

        self.graph_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar el frame de gráficos
        self.graph_frame.columnconfigure(0, weight=1)
        self.graph_frame.rowconfigure(0, weight=1)
        
        # Crear figura de matplotlib con estilo mejorado
        self.fig = Figure(figsize=(10, 7), dpi=100, facecolor='#ecf0f1')
        self.canvas = FigureCanvasTkAgg(self.fig, self.graph_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Mensaje inicial en el gráfico
        self.mostrar_mensaje_inicial()
        
        # Frame para resultados con estilo mejorado
        result_frame = ttk.LabelFrame(main_frame, 
                                    text="📋 Resultados y Cálculos", 
                                    padding="15")  # Quita style
        result_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(15, 0))
        result_frame.columnconfigure(0, weight=1)
        
        # Área de texto para resultados con estilo mejorado
        self.result_text = scrolledtext.ScrolledText(
            result_frame, 
            height=8, 
            width=100,
            font=('Consolas', 10),
            bg='#ecf0f1',
            fg='#2c3e50',
            wrap=tk.WORD,
            relief='flat',
            borderwidth=0
        )
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Mensaje de bienvenida
        mensaje_bienvenida = """🎯 ¡Bienvenido a la Calculadora de Cálculo Multivariado!

📚 Funcionalidades disponibles:
• Integrales Dobles: Calcula ∫∫ f(x,y) dxdy sobre regiones rectangulares
• Cálculo de Áreas: Determina áreas entre curvas
• Cálculo de Volúmenes: Encuentra volúmenes bajo superficies

💡 Consejos de uso:
• Usa ** para potencias (ej: x**2)
• Funciones disponibles: sin, cos, tan, exp, log, sqrt
• Constantes: pi, E
• Variables: solo x e y

🚀 ¡Selecciona una pestaña y comienza a calcular!
"""
        self.result_text.insert(tk.END, mensaje_bienvenida)
        
    def mostrar_mensaje_inicial(self):
        """Muestra un mensaje inicial en el área de gráficos."""
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.text(0.5, 0.5, '📊 Área de Visualización\n\n🎯 Selecciona una función y presiona\n"Graficar" para ver la visualización', 
                horizontalalignment='center',
                verticalalignment='center',
                transform=ax.transAxes,
                fontsize=14,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='#3498db', alpha=0.7),
                color='white')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        self.canvas.draw()
        
    def crear_tab_integral_doble(self):
        """Crea la pestaña para cálculo de integrales dobles."""
        integral_frame = ttk.Frame(self.notebook)
        self.notebook.add(integral_frame, text="∫∫ Integral Doble")
        
        # Configurar padding y espaciado
        integral_frame.configure(padding="20")
        
        # Función a integrar con estilo mejorado
        func_label = ttk.Label(integral_frame, text="🔢 Función f(x,y):", font=('Segoe UI', 10, 'bold'))
        func_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        self.func_entry = ttk.Entry(integral_frame, width=35, style='Custom.TEntry')
        self.func_entry.grid(row=0, column=1, pady=(0, 10), padx=(10, 0), sticky=(tk.W, tk.E))
        self.func_entry.insert(0, "x*y")
        
        # Límites de integración con mejor organización
        limits_frame = ttk.LabelFrame(integral_frame, text="📏 Límites de Integración", padding="10")
        limits_frame.grid(row=1, column=0, columnspan=2, pady=(10, 20), sticky=(tk.W, tk.E))
        
        # Límites de x
        ttk.Label(limits_frame, text="Límites de x:", font=('Segoe UI', 9, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5)
        x_frame = ttk.Frame(limits_frame)
        x_frame.grid(row=0, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(x_frame, text="de").grid(row=0, column=0, padx=(0, 5))
        self.x_min_entry = ttk.Entry(x_frame, width=10, style='Custom.TEntry')
        self.x_min_entry.grid(row=0, column=1, padx=2)
        self.x_min_entry.insert(0, "0")
        
        ttk.Label(x_frame, text="a").grid(row=0, column=2, padx=(10, 5))
        self.x_max_entry = ttk.Entry(x_frame, width=10, style='Custom.TEntry')
        self.x_max_entry.grid(row=0, column=3, padx=2)
        self.x_max_entry.insert(0, "1")
        
        # Límites de y
        ttk.Label(limits_frame, text="Límites de y:", font=('Segoe UI', 9, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=5)
        y_frame = ttk.Frame(limits_frame)
        y_frame.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(y_frame, text="de").grid(row=0, column=0, padx=(0, 5))
        self.y_min_entry = ttk.Entry(y_frame, width=10, style='Custom.TEntry')
        self.y_min_entry.grid(row=0, column=1, padx=2)
        self.y_min_entry.insert(0, "0")
        
        ttk.Label(y_frame, text="a").grid(row=0, column=2, padx=(10, 5))
        self.y_max_entry = ttk.Entry(y_frame, width=10, style='Custom.TEntry')
        self.y_max_entry.grid(row=0, column=3, padx=2)
        self.y_max_entry.insert(0, "1")
        
        # Botones con estilo mejorado
        button_frame = ttk.Frame(integral_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        calc_btn = ttk.Button(button_frame, text="🧮 Calcular Integral", 
                             style='Custom.TButton',
                             command=self.calcular_integral_doble)
        calc_btn.grid(row=0, column=0, padx=(0, 10))
        
        graph_btn = ttk.Button(button_frame, text="📊 Graficar Función", 
                              style='Custom.TButton',
                              command=self.graficar_funcion)
        graph_btn.grid(row=0, column=1)
        
        # Configurar expansión de columnas
        integral_frame.columnconfigure(1, weight=1)
        
    def crear_tab_area(self):
        """Crea la pestaña para cálculo de áreas."""
        area_frame = ttk.Frame(self.notebook)
        self.notebook.add(area_frame, text="📐 Área")
        
        area_frame.configure(padding="20")
        
        # Título de la sección
        ttk.Label(area_frame, text="📍 Región definida por:", 
                 font=('Segoe UI', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=(0, 15))
        
        # Frame para las funciones
        func_frame = ttk.LabelFrame(area_frame, text="📈 Funciones Límite", padding="10")
        func_frame.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky=(tk.W, tk.E))
        
        # Función superior
        ttk.Label(func_frame, text="y superior:", font=('Segoe UI', 9, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.y_sup_entry = ttk.Entry(func_frame, width=35, style='Custom.TEntry')
        self.y_sup_entry.grid(row=0, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
        self.y_sup_entry.insert(0, "x**2")
        
        # Función inferior
        ttk.Label(func_frame, text="y inferior:", font=('Segoe UI', 9, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.y_inf_entry = ttk.Entry(func_frame, width=35, style='Custom.TEntry')
        self.y_inf_entry.grid(row=1, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
        self.y_inf_entry.insert(0, "0")
        
        func_frame.columnconfigure(1, weight=1)
        
        # Límites de x para área
        limits_area_frame = ttk.LabelFrame(area_frame, text="📏 Límites de x", padding="10")
        limits_area_frame.grid(row=2, column=0, columnspan=2, pady=(0, 20), sticky=(tk.W, tk.E))
        
        x_area_frame = ttk.Frame(limits_area_frame)
        x_area_frame.grid(row=0, column=0)
        
        ttk.Label(x_area_frame, text="de").grid(row=0, column=0, padx=(0, 5))
        self.x_area_min_entry = ttk.Entry(x_area_frame, width=10, style='Custom.TEntry')
        self.x_area_min_entry.grid(row=0, column=1, padx=2)
        self.x_area_min_entry.insert(0, "0")
        
        ttk.Label(x_area_frame, text="a").grid(row=0, column=2, padx=(10, 5))
        self.x_area_max_entry = ttk.Entry(x_area_frame, width=10, style='Custom.TEntry')
        self.x_area_max_entry.grid(row=0, column=3, padx=2)
        self.x_area_max_entry.insert(0, "2")
        
        # Botones
        button_area_frame = ttk.Frame(area_frame)
        button_area_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        calc_area_btn = ttk.Button(button_area_frame, text="📐 Calcular Área", 
                                  style='Custom.TButton',
                                  command=self.calcular_area)
        calc_area_btn.grid(row=0, column=0, padx=(0, 10))
        
        graph_area_btn = ttk.Button(button_area_frame, text="🎨 Graficar Región", 
                                   style='Custom.TButton',
                                   command=self.graficar_region)
        graph_area_btn.grid(row=0, column=1)
        
        area_frame.columnconfigure(1, weight=1)
        
    def crear_tab_volumen(self):
        """Crea la pestaña para cálculo de volúmenes."""
        volumen_frame = ttk.Frame(self.notebook)
        self.notebook.add(volumen_frame, text="📦 Volumen")
        
        volumen_frame.configure(padding="20")
        
        # Función de superficie
        surf_frame = ttk.LabelFrame(volumen_frame, text="🏔️ Superficie", padding="10")
        surf_frame.grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky=(tk.W, tk.E))
        
        ttk.Label(surf_frame, text="z = f(x,y):", font=('Segoe UI', 9, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.vol_func_entry = ttk.Entry(surf_frame, width=35, style='Custom.TEntry')
        self.vol_func_entry.grid(row=0, column=1, pady=5, padx=(10, 0), sticky=(tk.W, tk.E))
        self.vol_func_entry.insert(0, "x**2 + y**2")
        
        surf_frame.columnconfigure(1, weight=1)
        
        # Región de integración
        region_frame = ttk.LabelFrame(volumen_frame, text="📏 Región R", padding="10")
        region_frame.grid(row=1, column=0, columnspan=2, pady=(0, 20), sticky=(tk.W, tk.E))
        
        # Límites de x
        ttk.Label(region_frame, text="Límites de x:", font=('Segoe UI', 9, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5)
        x_vol_frame = ttk.Frame(region_frame)
        x_vol_frame.grid(row=0, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(x_vol_frame, text="de").grid(row=0, column=0, padx=(0, 5))
        self.x_vol_min_entry = ttk.Entry(x_vol_frame, width=10, style='Custom.TEntry')
        self.x_vol_min_entry.grid(row=0, column=1, padx=2)
        self.x_vol_min_entry.insert(0, "-1")
        
        ttk.Label(x_vol_frame, text="a").grid(row=0, column=2, padx=(10, 5))
        self.x_vol_max_entry = ttk.Entry(x_vol_frame, width=10, style='Custom.TEntry')
        self.x_vol_max_entry.grid(row=0, column=3, padx=2)
        self.x_vol_max_entry.insert(0, "1")
        
        # Límites de y
        ttk.Label(region_frame, text="Límites de y:", font=('Segoe UI', 9, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=5)
        y_vol_frame = ttk.Frame(region_frame)
        y_vol_frame.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(y_vol_frame, text="de").grid(row=0, column=0, padx=(0, 5))
        self.y_vol_min_entry = ttk.Entry(y_vol_frame, width=10, style='Custom.TEntry')
        self.y_vol_min_entry.grid(row=0, column=1, padx=2)
        self.y_vol_min_entry.insert(0, "-1")
        
        ttk.Label(y_vol_frame, text="a").grid(row=0, column=2, padx=(10, 5))
        self.y_vol_max_entry = ttk.Entry(y_vol_frame, width=10, style='Custom.TEntry')
        self.y_vol_max_entry.grid(row=0, column=3, padx=2)
        self.y_vol_max_entry.insert(0, "1")
        
        # Botones
        button_vol_frame = ttk.Frame(volumen_frame)
        button_vol_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        calc_vol_btn = ttk.Button(button_vol_frame, text="📦 Calcular Volumen", 
                                 style='Custom.TButton',
                                 command=self.calcular_volumen)
        calc_vol_btn.grid(row=0, column=0, padx=(0, 10))

        graph_vol_btn = ttk.Button(button_vol_frame, text="🌄 Graficar Superficie", 
                                  style='Custom.TButton',
                                  command=self.graficar_superficie)
        graph_vol_btn.grid(row=0, column=1)

        volumen_frame.columnconfigure(1, weight=1)
        
    def crear_tab_ayuda(self):
        """Crea la pestaña de ayuda."""
        ayuda_frame = ttk.Frame(self.notebook)
        self.notebook.add(ayuda_frame, text="❓ Ayuda")
        ayuda_frame.configure(padding="20")
        ayuda_text = (
            "🧮 Calculadora de Cálculo Multivariado\n\n"
            "• Usa ** para potencias (ej: x**2)\n"
            "• Funciones: sin, cos, tan, exp, log, sqrt\n"
            "• Constantes: pi, E\n"
            "• Variables: x, y\n"
            "• Selecciona una pestaña y comienza a calcular."
        )
        label = tk.Label(ayuda_frame, text=ayuda_text, justify="left", font=('Segoe UI', 11), bg='#ecf0f1', fg='#2c3e50')
        label.pack(fill="both", expand=True)
        
    def calcular_integral_doble(self):
        """Calcula la integral doble de la función ingresada."""
        try:
            func_str = self.func_entry.get()
            x_min = float(self.x_min_entry.get())
            x_max = float(self.x_max_entry.get())
            y_min = float(self.y_min_entry.get())
            y_max = float(self.y_max_entry.get())
            func = sp.sympify(func_str)
            integral = sp.integrate(func, (self.x, x_min, x_max), (self.y, y_min, y_max))
            resultado = f"∬ f(x, y) dxdy = {integral.evalf()}\n"
            self.mostrar_resultado(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")

    def calcular_area(self):
        """Calcula el área entre las curvas definidas por las funciones límite."""
        try:
            y_sup_str = self.y_sup_entry.get()
            y_inf_str = self.y_inf_entry.get()
            x_min = float(self.x_area_min_entry.get())
            x_max = float(self.x_area_max_entry.get())
            y_sup = sp.sympify(y_sup_str)
            y_inf = sp.sympify(y_inf_str)
            area = sp.integrate(y_sup - y_inf, (self.x, x_min, x_max))
            resultado = f"Área = {area.evalf()}\n"
            self.mostrar_resultado(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")

    def calcular_volumen(self):
        """Calcula el volumen bajo la superficie definida por la función ingresada."""
        try:
            func_str = self.vol_func_entry.get()
            x_min = float(self.x_vol_min_entry.get())
            x_max = float(self.x_vol_max_entry.get())
            y_min = float(self.y_vol_min_entry.get())
            y_max = float(self.y_vol_max_entry.get())
            func = sp.sympify(func_str)
            integral = sp.integrate(func, (self.x, x_min, x_max), (self.y, y_min, y_max))
            resultado = f"Volumen = {integral.evalf()}\n"
            self.mostrar_resultado(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")
    
    def graficar_funcion(self):
        """Genera un gráfico de la función ingresada para la integral doble."""
        try:
            func_str = self.func_entry.get()
            x_min = float(self.x_min_entry.get())
            x_max = float(self.x_max_entry.get())
            y_min = float(self.y_min_entry.get())
            y_max = float(self.y_max_entry.get())
            
            # Crear malla de puntos
            x_vals = np.linspace(x_min, x_max, 100)
            y_vals = np.linspace(y_min, y_max, 100)
            X, Y = np.meshgrid(x_vals, y_vals)
            
            # Evaluar función
            func = sp.sympify(func_str)
            func_lambdified = sp.lambdify((self.x, self.y), func, 'numpy')
            Z = func_lambdified(X, Y)
            
            # Limpiar figura
            self.fig.clear()
            
            # Crear gráfico 3D
            ax = self.fig.add_subplot(111, projection='3d')
            surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
            
            # Agregar plano z=0
            ax.plot_surface(X, Y, np.zeros_like(Z), alpha=0.3, color='gray')
            
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.set_title(f'Gráfico de la Función: z = {func_str}')
            
            # Agregar barra de colores
            self.fig.colorbar(surf, ax=ax, shrink=0.5)
            
            self.canvas.draw()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la graficación: {str(e)}")
    
    def graficar_region(self):
        """Genera un gráfico de la región de integración para el cálculo de áreas."""
        try:
            y_sup_str = self.y_sup_entry.get()
            y_inf_str = self.y_inf_entry.get()
            x_min = float(self.x_area_min_entry.get())
            x_max = float(self.x_area_max_entry.get())
            
            # Definir funciones límite
            y_sup = sp.sympify(y_sup_str)
            y_inf = sp.sympify(y_inf_str)
            
            # Crear malla de puntos
            x_vals = np.linspace(x_min, x_max, 100)
            y_vals_sup = y_sup.subs(self.x, x_vals)
            y_vals_inf = y_inf.subs(self.x, x_vals)
            
            # Limpiar figura
            self.fig.clear()
            ax = self.fig.add_subplot(111)
            
            # Graficar curvas
            ax.plot(x_vals, y_vals_sup, 'b-', label=f'y = {y_sup_str}', linewidth=2)
            ax.plot(x_vals, y_vals_inf, 'r-', label=f'y = {y_inf_str}', linewidth=2)
            
            # Rellenar área
            ax.fill_between(x_vals, y_vals_inf, y_vals_sup, alpha=0.3, color='green', label='Área')
            
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title('Región de integración')
            ax.legend()
            ax.grid(True, alpha=0.3)
            
            self.canvas.draw()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la graficación: {str(e)}")
    
    def graficar_superficie(self):
        try:
            func_str = self.vol_func_entry.get()
            x_min = float(self.x_vol_min_entry.get())
            x_max = float(self.x_vol_max_entry.get())
            y_min = float(self.y_vol_min_entry.get())
            y_max = float(self.y_vol_max_entry.get())
            
            # Crear malla de puntos
            x_vals = np.linspace(x_min, x_max, 50)
            y_vals = np.linspace(y_min, y_max, 50)
            X, Y = np.meshgrid(x_vals, y_vals)
            
            # Evaluar función
            func = sp.sympify(func_str)
            func_lambdified = sp.lambdify((self.x, self.y), func, 'numpy')
            Z = func_lambdified(X, Y)
            
            # Limpiar figura
            self.fig.clear()
            
            # Crear gráfico 3D
            ax = self.fig.add_subplot(111, projection='3d')
            surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
            
            # Agregar plano z=0
            ax.plot_surface(X, Y, np.zeros_like(Z), alpha=0.3, color='gray')
            
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.set_title(f'Superficie z = {func_str}')
            
            # Agregar barra de colores
            self.fig.colorbar(surf, ax=ax, shrink=0.5)
            
            self.canvas.draw()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la graficación: {str(e)}")
    
    def mostrar_resultado(self, texto):
        self.result_text.insert(tk.END, texto)
        self.result_text.see(tk.END)

def main():
    root = tk.Tk()
    app = CalculadoraMultivariado(root)
    root.mainloop()

if __name__ == "__main__":
    main()

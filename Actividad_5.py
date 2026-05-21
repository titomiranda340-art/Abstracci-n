"""Ejercicio 5: Empleados

Crea una clase abstracta Empleado con un método abstracto calcular_sueldo(). Luego, implementa 
dos clases concretas, EmpleadoPorHora y EmpleadoFijo, que calculen el sueldo de manera diferente.
Objetivo: Aprender a abstraer la lógica de cálculo de sueldos en diferentes tipos de empleados.
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
        
    @abstractmethod
    def calcular_sueldo(self):
        pass
    
class EmpleadoPorHora(Empleado):
    
    def __init__(self, horas, pago_por_hora):
        self.horas = horas
        self.pago_por_hora = pago_por_hora

    def calcular_sueldo(self):
        return self.horas * self.pago_por_hora

class EmpleadoFijo(Empleado):
    
    def __init__(self, sueldo_mensual):
        self.sueldo_mensual=sueldo_mensual
        
    def calcular_sueldo(self):
        return self.sueldo_mensual
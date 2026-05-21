"""Ejercicio 2: Sistema de Pago
Define una clase abstracta Pago con un método abstracto procesar_pago(). Luego, crea dos clases concretas, TarjetaCredito y PayPal, 
que implementen el método procesar_pago() de manera diferente.
Objetivo: Aprender a abstraer el proceso de pago y cómo diferentes métodos pueden implementarse de manera específica.
"""

from abc import ABC, abstractmethod

class Pago(ABC):

    @abstractmethod
    def procesar_pago(self):
        pass

class TarjetaCredito(Pago):

    def procesar_pago(self):
        return "El pago se procesó con tarjeta de crédito"

class PayPal(Pago):

    def procesar_pago(self):
        return "El pago se procesó con PayPal"
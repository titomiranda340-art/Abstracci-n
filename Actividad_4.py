"""Ejercicio 4: Sistema de Notificaciones
Define una clase abstracta Notificacion con un método abstracto enviar(). Crea dos clases concretas,
Email y SMS, que implementen el método enviar() de manera diferente.
Objetivo: Ver cómo la abstracción permite manejar diferentes tipos de notificaciones de manera uniforme.
"""

from abc import ABC, abstractmethod

class Notificacion(ABC):
    
    @abstractmethod
    def enviar(self):
        pass
    
class Email(Notificacion):
    def enviar(self):
        print("Se esta enviando la notificacion por Email")
        
class SMS(Notificacion):
    def enviar(self):
        print("Se esta enviando la notificacion por SMS")
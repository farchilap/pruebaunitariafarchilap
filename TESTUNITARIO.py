# Autor: farchilap1@miumg.edu.gt
# Carné: 0904-21-14842

import unittest

def calcular_promedio_calificaciones(calificaciones):
 """
    Calcula el promedio de una lista de calificaciones.

    Parámetros:
    - calificaciones (list): Lista de números representando las calificaciones.

    Retorna:
    - float: El promedio de las calificaciones. Si la lista está vacía, retorna 0.
    """
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def recomendar_contenido(historial, contenido_disponible):
   """
    Recomienda contenido basado en el historial del usuario.

    Parámetros:
    - historial (list): Lista de contenidos que el usuario ya ha visto.
    - contenido_disponible (list): Lista total de contenido disponible.

    Retorna:
    - list: Lista con hasta 3 contenidos recomendados que el usuario no ha visto.
      Si el historial está vacío, se devuelven los primeros 3 contenidos disponibles.
    """
    if not historial:
        return contenido_disponible[:3]  # Si no hay historial, devolver primeros 3 contenidos disponibles
    return [contenido for contenido in contenido_disponible if contenido not in historial][:3]

class TestSistemaGerencial(unittest.TestCase):
    def test_calcular_promedio_calificaciones(self):
      """
    Clase de pruebas unitarias para verificar el correcto funcionamiento 
    de las funciones `calcular_promedio_calificaciones` y `recomendar_contenido`.
    """
        self.assertEqual(calcular_promedio_calificaciones([5, 4, 3, 5, 4]), 4.2)
        self.assertEqual(calcular_promedio_calificaciones([]), 0)
        self.assertEqual(calcular_promedio_calificaciones([5]), 5)
    
    def test_recomendar_contenido(self):
     
        historial = ["Breaking Bad", "Stranger Things"]
        contenido_disponible = ["Breaking Bad", "Stranger Things", "Narcos", "The Witcher", "House of Cards"]
        self.assertEqual(recomendar_contenido(historial, contenido_disponible), ["Narcos", "The Witcher", "House of Cards"])
        self.assertEqual(recomendar_contenido([], contenido_disponible), ["Breaking Bad", "Stranger Things", "Narcos"])

if __name__ == "__main__":
    unittest.main()

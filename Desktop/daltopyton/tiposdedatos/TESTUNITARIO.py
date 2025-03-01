import unittest

def calcular_promedio_calificaciones(calificaciones):
 
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def recomendar_contenido(historial, contenido_disponible):
  
    if not historial:
        return contenido_disponible[:3]  # Si no hay historial, devolver primeros 3 contenidos disponibles
    return [contenido for contenido in contenido_disponible if contenido not in historial][:3]

class TestSistemaGerencial(unittest.TestCase):
    def test_calcular_promedio_calificaciones(self):
     
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

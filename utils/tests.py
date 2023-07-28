import unittest
from utils.validations import *

class ValidationsTestCase(unittest.TestCase):
    # Regions, obligatory
    def test_validateRegiones(self):
        self.assertTrue(validateRegiones("Santiago"))
        self.assertTrue(validateRegiones("Arica"))
        self.assertFalse(validateRegiones(""))

    # Communes, basta con que haya algo pues es obligatoria
    def test_validateComunas(self):
        self.assertTrue(validateComunas("Providencia"))
        self.assertTrue(validateComunas("Talca"))
        self.assertFalse(validateComunas(""))

    # Calle_numero, basta con que haya algo pues es obligatoria y también su largo no debe exceder 80 caracteres
    def test_validateCalle_numero(self):
        self.assertTrue(validateCalle_numero("Calle 123"))
        self.assertTrue(validateCalle_numero("Calle Peo Grande 1"))
        self.assertFalse(validateCalle_numero(""))
        self.assertFalse(validateCalle_numero("Calle larga muy larga demasiado larga, extremadamente larga con muchas calles oscuras y tenebrosas"))

    # Tipo_Donacion, basta con que haya algo pues es obligatoria
    def test_validateTipo_Donacion(self):
        self.assertTrue(validateTipo_donacion("Fruta"))
        self.assertTrue(validateTipo_donacion("Verdura"))
        self.assertFalse(validateTipo_donacion(""))

    # Cantidad, obligatoria y como máximo 10 caracteres
    def test_validateCantidad(self):
        self.assertTrue(validateCantidad("Muchas"))
        self.assertTrue(validateCantidad("2"))
        self.assertFalse(validateCantidad(""))
        self.assertFalse(validateCantidad("Varias cajas"))

    # Fecha_disponibilidad, obligatoria y como mínimo el día actual (27 de Julio de 2023)
    def test_validateFecha_disponibilidad(self):
        self.assertTrue(validateFecha_disponibilidad("2024-03-02"))
        self.assertTrue(validateFecha_disponibilidad("2023-07-27"))
        self.assertFalse(validateFecha_disponibilidad("2023-07-26"))
        self.assertFalse(validateFecha_disponibilidad(""))

    # Descripcion, no es obligatoria y como máximo 80 caracteres
    def test_validateDescripcion(self):
        self.assertTrue(validateDescripcion("Varios tomatitos"))
        self.assertTrue(validateDescripcion("Peos frescos"))
        self.assertTrue(validateDescripcion(""))
        self.assertFalse(validateDescripcion("Varias cajas de cosas muy ricas, de verdad, muy muy ricas, y únicas, ojalá algún día alguien pudiese probarlas también"))

    # DescripcionPedido, es obligatoria y como máximo 80 caracteres
    def test_validateDescripcionPedido(self):
        self.assertTrue(validateDescripcionPedido("Varios tomatitos"))
        self.assertTrue(validateDescripcionPedido("Peos frescos"))
        self.assertFalse(validateDescripcionPedido(""))
        self.assertFalse(validateDescripcionPedido("Varias cajas de cosas muy ricas, de verdad, muy muy ricas, y únicas, ojalá algún día alguien pudiese probarlas también"))

    # Condiciones, no es obligatoria y como máximo 80 caracteres
    def test_validateCondiciones(self):
        self.assertTrue(validateCondiciones("Portarse bien"))
        self.assertTrue(validateCondiciones("Tirarse un peo"))
        self.assertTrue(validateCondiciones(""))
        self.assertFalse(validateCondiciones("Donar algo a cambio de pedir esto, desde una manzanita hasta un container repleto de pc's gamer"))

    # Nombre_donante, es obligatoria y como máximo 80 caracteres, pero mínimo 3
    def test_validateNombre_donante(self):
        self.assertTrue(validateNombre_donante("Pedrito peo"))
        self.assertTrue(validateNombre_donante("Lisa"))
        self.assertFalse(validateNombre_donante(""))
        self.assertFalse(validateNombre_donante("Ao"))
        self.assertFalse(validateNombre_donante("Juanito el cara de peo, vecino de Pedrito peo, descendiente de la antigua Peolandia en las tierras del buen peo"))

    # Email, es obligatorio y como máximo 80 caracteres, cumpliendo con formato
    def test_validateEmail(self):
        self.assertTrue(validateEmail("pedritopeo@gmail.com"))
        self.assertTrue(validateEmail("Lisalalisa23@colocolo.cl"))
        self.assertFalse(validateEmail(""))
        self.assertFalse(validateEmail("pedritopeo1.cl"))
        self.assertFalse(validateEmail("pedritopeo@uchile.onos"))
        self.assertFalse(validateEmail("pedritopeopedritopeopedritopeopedritopeopedritopeopedritopeopedritopeopedritopeo@uchile.cl"))

    # Celular, no es obligatoria y como máximo 15 caracteres, cumpliendo con formato
    def test_validateCelular(self):
        self.assertTrue(validateCelular("+569 12345678"))
        self.assertTrue(validateCelular("+569 19827364"))
        self.assertTrue(validateCelular(""))
        self.assertFalse(validateCelular("+56 9 7823 6721"))
        self.assertFalse(validateCelular("+56 9 123456789"))

if __name__ == '__main__':
    unittest.main()
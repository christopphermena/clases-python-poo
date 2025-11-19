class Boleta():
    def __init__(self, numero_boleta):
        self.numero_boleta = numero_boleta
        
    def mostrar_info(self):
        return f"Boleta Nro. {self.numero_boleta}"

class Pago():
    def __init__(self, monto_pagado, numero_boleta):
        self.monto_pagado = monto_pagado
        self.Boleta = Boleta(numero_boleta)
        
    def mostrar_info_boleta(self):
        print(f"Boleta Nro.: {self.Boleta.numero_boleta}")
        print(f"Con el valor pagado de: {self.monto_pagado}")
        
objeto_boleta = Pago("$9.990", 34)

objeto_boleta.mostrar_info_boleta()
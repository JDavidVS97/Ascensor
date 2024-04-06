class Ascensor:
    def __init__(self, num_pisos):
        self.num_pisos = num_pisos
        self.piso_actual = 1
        self.direccion = 1  # 1 para arriba, -1 para abajo, 0 para detenerse
        self.destinos = set()

    def llamar_desde_piso(self, piso):
        self.destinos.add(piso)

    def mover(self):
        self.piso_actual += self.direccion

    def actualizar_direccion(self, destino):
        if self.piso_actual < destino:
            self.direccion = 1  # Subir
        elif self.piso_actual > destino:
            self.direccion = -1  # Bajar
        else:
            self.direccion = 0  # Detenerse

    def abrir_puerta(self):
        print(f"Ascensor llegó al piso {self.piso_actual}. Puerta abierta.")

    def cerrar_puerta(self):
        print("Puerta cerrada.")

    def ir_a_piso(self, destino):
        while self.piso_actual != destino:
            self.mover()
            self.actualizar_direccion(destino)

    def mostrar_camino(self, destino):
        print(f"Ascensor se mueve hacia {'arriba' if self.direccion == 1 else 'abajo'} desde el piso {self.piso_actual}", end="")
        while self.piso_actual != destino:
            self.mover()
            print(f" al piso {self.piso_actual}", end="")
        print(".")

    def run(self):
        while True:
            print("\n¿Qué desea hacer?")
            print("1. Llamar al ascensor desde un piso.")
            print("2. Salir.")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                piso_llamada = int(input("Ingrese el piso desde el que desea llamar al ascensor: "))
                piso_destino = int(input("Ingrese el piso al que desea ir: "))  # Solicitar el piso de destino
                self.destinos.add(piso_destino)  # Agregar el destino a la lista de destinos
                self.llamar_desde_piso(piso_llamada)

                while self.destinos:
                    piso_destino = max(self.destinos)  # Obtener el destino más alto
                    self.actualizar_direccion(piso_destino)

                    if self.piso_actual in self.destinos:
                        self.abrir_puerta()
                        print("El ascensor ya está en este piso.")
                        self.destinos.remove(self.piso_actual)
                        self.cerrar_puerta()
                    else:
                        self.mostrar_camino(piso_destino)
                        self.ir_a_piso(piso_destino)
                        self.abrir_puerta()
                        print("Usuario llegó a destino.")
                        self.destinos.remove(piso_destino)
                        self.cerrar_puerta()

            elif opcion == "2":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Inténtelo de nuevo.")


def main():
    num_pisos = int(input("Ingrese el número de pisos del edificio: "))
    ascensor = Ascensor(num_pisos)
    ascensor.run()


if __name__ == "__main__":
    main()


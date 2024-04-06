class Ascensor:
    def __init__(self, num_pisos):
        self.num_pisos = num_pisos
        self.piso_actual = 1
        self.direccion = 1  
        self.destinos = set()

    def llamar_desde_piso(self, piso):
        self.destinos.add(piso)

    def mover(self):
        self.piso_actual += self.direccion

    def actualizar_direccion(self):
        if self.piso_actual == 1:
            self.direccion = 1
        elif self.piso_actual == self.num_pisos:
            self.direccion = -1
        elif self.piso_actual in self.destinos:
            self.direccion = 1
        elif self.direccion == 1 and max(self.destinos) < self.piso_actual:
            self.direccion = -1
        elif self.direccion == -1 and min(self.destinos) > self.piso_actual:
            self.direccion = 1

    def abrir_puerta(self):
        print(f"Ascensor llegó al piso {self.piso_actual}. Puerta abierta.")

    def cerrar_puerta(self):
        print("Puerta cerrada.")

    def ir_a_piso(self, destino):
        while self.piso_actual != destino:
            self.mover()
            self.actualizar_direccion()

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
                self.destinos.clear() 
                self.llamar_desde_piso(piso_llamada)

                while self.destinos:
                    self.actualizar_direccion()

                    if self.piso_actual in self.destinos:
                        self.abrir_puerta()
                        destino = int(input("Ingrese el piso al que desea ir: "))
                        if destino == self.piso_actual:
                            print("El ascensor ya está en este piso.")
                        else:
                            self.mostrar_camino(destino)
                            self.ir_a_piso(destino)
                            self.cerrar_puerta()
                            print("Usuario llegó a destino. Volviendo al menú principal...")
                            break

                    self.mostrar_camino(max(self.destinos))

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

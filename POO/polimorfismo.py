class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando Caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando en bicicleta')

def main():
    persona = Persona('Andres')
    persona.avanza()

    ciclista = Ciclista('Angie')
    ciclista.avanza()

if __name__ == "__main__":
    main()
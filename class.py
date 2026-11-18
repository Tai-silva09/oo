class Computador:
    def __init__(self, cor, modelo, marca, preco):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.preco = preco

    def mostrar(self):
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Preço: R$ {self.preco:.2f}")

    def programar(self):
        print(f"O computador {self.modelo} está sendo utilizado para programar.")


computador1 = Computador("Preto", "Inspiron 15", "Dell", 3500.00)
computador2 = Computador("Prata", "IdeaPad 3", "Lenovo", 2800.00)
computador3 = Computador("Branco", "MacBook Air", "Apple", 7500.00)



print("COMPUTADOR 1")
computador1.mostrar()

print("COMPUTADOR 2")
computador2.mostrar()

print("\nCOMPUTADOR 3")
computador3.mostrar()
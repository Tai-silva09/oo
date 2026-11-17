
class Aluno:
    def __init__(self, nome, idade, curso, matricula):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.matricula = matricula

    def estudar(self):
        print(self.nome, "esta estudando.")

    def fazer_prova(self):
        print(self.nome, "esta fazendo uma prova.")

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Curso:", self.curso)
        print("Matricula:", self.matricula)


aluno1 = Aluno("Geovani", 20, "Ciencia da Computacao", 202601)
aluno2 = Aluno("Lucas", 19, "Ciencia da Computacao", 202602)
aluno3 = Aluno("Pedro", 21, "Ciencia da Computacao", 202603)


aluno1.mostrar_dados()
aluno1.estudar()

print("-------------------")

aluno2.mostrar_dados()
aluno2.fazer_prova()

print("-------------------")

aluno3.mostrar_dados()
aluno3.estudar()

class Aluno:
    def __init__(self, nome, matricula, curso):
        # Atributos
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = []

    # Método 1
    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print(f"Nota inválida ({nota}). Use valores entre 0 e 10.")

    # Método 2
    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    # Método 3
    def situacao(self):
        media = self.calcular_media()
        if not self.notas:
            return "Sem notas"
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        return "Reprovado"

    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Matrícula: {self.matricula}\n"
            f"Curso: {self.curso}\n"
            f"Notas: {self.notas}\n"
            f"Média: {self.calcular_media():.2f}\n"
            f"Situação: {self.situacao()}"
        )


# Criando 3 objetos diferentes
aluno1 = Aluno("Ana Souza", "2024001", "Ciência da Computação")
aluno2 = Aluno("Bruno Lima", "2024002", "Engenharia Civil")
aluno3 = Aluno("Carla Mendes", "2024003", "Administração")

# Adicionando notas
for nota in (9.0, 8.5, 7.5):
    aluno1.adicionar_nota(nota)

for nota in (6.0, 5.0, 4.5):
    aluno2.adicionar_nota(nota)

for nota in (3.0, 4.0, 2.5):
    aluno3.adicionar_nota(nota)

# Imprimindo o estado de cada objeto
for aluno in (aluno1, aluno2, aluno3):
    print(aluno)
    print("-" * 30)
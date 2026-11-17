class Aluno:    
    
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matrícula: {self.matricula}")
    def atualizar_idade(self, nova_idade):
        self.idade = nova_idade
        print(f"Idade atualizada para: {self.idade}")

    aluno1 = Aluno("Ana Jamily", 19, "12345")
    aluno2 = Aluno("João Silva", 21, "67890")
    
class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao  # em semestres

    def descricao(self):
        return f"Curso de {self.nome}, duração de {self.duracao} semestres."


class Aluno:
    def __init__(self, nome, matricula, curso):
        # Atributos privados:
        self.__nome = None 
        self.__matricula = None
        self.__notas = []
        self.curso = curso  # composição: o aluno tem um curso

        self.set_nome(nome)
        self.set_matricula(matricula)

    # Getter para o nome:
    def get_nome(self):
        return self.__nome
    
    # Setter para o nome, com validação: não pode ser vazio ou conter apenas espaços
    def set_nome(self, nome):
        if nome: # Verifica se o nome não é vazio ou apenas espaços
            self.__nome = nome
        else:
            print("Nome inválido. Por favor, insira um nome válido.")

    # Getter para a matrícula
    def get_matricula(self):
        return self.__matricula

    # Setter para matrícula com validação: número entre 8 e 10 dígitos
    def set_matricula(self, matricula):
        if matricula.isdigit() and 8 <= len(matricula) <= 10:
            self.__matricula = matricula
        else:
            print("Matrícula inválida. Deve conter entre 8 e 10 dígitos numéricos.")

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida!")

    def calcular_media(self): # Retorna a média das notas do aluno ou 0 se não houver notas.
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)
    
    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Média: {self.calcular_media():.2f}")
        print(self.curso.descricao())


class AlunoIntegrado(Aluno):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula, curso)

class AlunoSubsequente(Aluno):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula, curso)

class AlunoGraduacao(Aluno):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula, curso)
        
class AlunoPosGraduacao(Aluno):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula, curso)

# Criando os cursos
curso0 = Curso("Técnico em Informática", 6)
curso1 = Curso("Técnico em Agropecuária", 2)
curso2 = Curso("Licenciatura em Informática", 8)
curso3 = Curso("Mestrado em Educação no Campo", 4)

# Criando lista de alunos com diferentes tipos
alunos = [
    AlunoIntegrado("Ana", "12345678", curso0),
    AlunoSubsequente("Bruno", "23456789", curso1),
    AlunoGraduacao("Carla", "34567890", curso2),
    AlunoPosGraduacao("Diego", "45678901", curso3)
]

for aluno in alunos:
    print(f"\nAdicionando notas para {aluno.get_nome()}:")
    for i in range(2):
        while True:
            entrada = input(f"Digite a nota {i+1} para {aluno.get_nome()}: ")
            
            if entrada.strip() == "":
                print("⚠️ Entrada vazia. Digite uma nota válida.")
                continue

            try:
                nota = float(entrada)
                if 0 <= nota <= 10:
                    aluno.adicionar_nota(nota)
                    break
                else:
                    print("⚠️ A nota deve estar entre 0 e 10.")
            except ValueError:
                print("⚠️ Entrada inválida. Digite um número.")
                
# Demonstrando polimorfismo
for aluno in alunos:
    aluno.mostrar_dados()
    print("-" * 60)
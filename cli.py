from classes import Passageiro
from classes import Corrida
from classes import Motorista
import motoristaDAO


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        continuar = True
        nome = input("Digite o nome do passageiro: ")
        documento = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome, documento)
        print(passageiro.nome, passageiro.documento)
        corridas = list
        while(continuar):
            nota = int(input("Digite a nota da Corrida: "))
            distancia = int(input("Digite a distancia da Corrida: "))
            valor = int(input("Digite o valor da Corrida: "))
            NumeroContinuar = 0
            while NumeroContinuar not in [1, 2]:
                NumeroContinuar = int(input("Adicionar mais uma corrida 1-Sim, 2-Não"))
                if NumeroContinuar == 2:
                    continuar = False
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)
        nota = int(input("Digite a nota do Mortorista: "))
        motorista = Motorista(corridas, nota)
        self.motoristaDAO.create_motorista(motorista)

    def read_motorista(self):
        id = input("Digite o id: ")
        motorista = self.motoristaDAO.read_motorista_by_id(id)
        if motorista:
            print(f"nota: {motorista['nota']}")
            print(f"corridas: {motorista['corridas']}")

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motoristaDAO.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
# Define a classe Termostato
class Termostato:
    
    # Método inicializador da classe Termostato
    def __init__(self, temperatura = 20):
        
        # Inicializa o atributo 'temperatura' com o valor de 20 graus por padrão
        self.temperatura = temperatura
        
        # Inicializa o atributo 'temperatura_atual' com o valor fornecido ou 20 graus por padrão
        self.temperatura_atual = temperatura
        
    # Método para aumentar a temperatura
    def aumentar(self, valor):
        
        # Adiciona o valor fornecido ao atributo 'temperatura_atual'
        self.temperatura_atual += valor
        
        # Imprime em quanto foi aumentada a temperatura
        print(f"A temperatura foi aumentada em {valor}°c")
        
    # Método para diminuir a temperatura
    def diminuir(self, valor):
        
        # Subtrai o valor fornecido do atributo 'temperatura_atual'
        self.temperatura_atual -= valor
        
        # Imprime em quanto foi diminuída a temperatura
        print(f"A temperatura foi diminuida em {valor}°c")
        
    # Método para configurar (definir) a temperatura
    def definir(self, valor):
        
        # Define a 'temperatura_atual' para o novo valor fornecido
        self.temperatura_atual = valor
        
        # Imprime a temperatura após ser reconfigurada
        print(f"A temperatura foi definida para {self.temperatura_atual:.1f}°c")
        
    # Método para exibir a temperatura atual
    def mostrar(self):
        
        # Imprime o valor atual do atributo 'temperatura_atual'
        print(f"A temperatura atual é: {self.temperatura_atual:.1f}°c")
        
# Instanciando um termostato
termostato = Termostato()

print("Sistema de Termostato")

# Enquanto o Usuário não escolher Sair, o loop irá rodar de forma infinita
while True:
    
    print()
    
    # Menu interativo do Programa
    print("Menu")
    
    print()
    
    print("1 - Aumentar Temperatura")
    
    print("2 - Diminuir Temperatura")
    
    print("3 - Definir Temperatura")
    
    print("4 - Exibir Temperatura")
    
    print("5 - Sair")
    
    print()
    
    # Pede ao Usuário para escolher a ação desejada
    op = input("Escolha a opção desejada: ")
    
    print()
    
    # Opção para Aumentar a Temperatura
    if op == "1":
        
        # Faz uma tentativa de verificar o que o Usuário digitou foi um número;
        try:
            
            # Armazena na variável 'valor' o Número digitado pelo Usuário
            valor = float(input("Insira quantos °c deseja aumentar: "))
            
            # Ação de Aumentar a Temperatura 
            termostato.aumentar(valor)
            
        # Caso o Usuário não tenha digitado um número;
        except ValueError as e:
            
            # Informa que foi digitado algo diferente de um Número
            print(f"Número Inválido!")
            
    # Opção para Diminuir a Temperatura
    elif op == "2":
        
        # Faz uma tentativa de verificar o que o Usuário digitou foi um número;
        try:
            
            # Armazena na variável 'valor' o Número digitado pelo Usuário
            valor = float(input("Insira quantos °c deseja diminuir: "))
            
            # Ação de Diminuir a Temperatura 
            termostato.diminuir(valor)
            
        # Caso o Usuário não tenha digitado um número;
        except ValueError as e:
            
            # Informa que foi digitado algo diferente de um Número
            print(f"Número Inválido!")
            
    # Opção para Definir a Temperatura
    elif op == "3":
        
        # Faz uma tentativa de verificar o que o Usuário digitou foi um número;
        try:
            
            # Armazena na variável 'valor' o Número digitado pelo Usuário
            valor = float(input("Insira em quantos °c deseja definir a temperatua: "))
            
            # Ação de Definir a Temperatura 
            termostato.definir(valor)
            
        # Caso o Usuário não tenha digitado um número;
        except ValueError as e:
            
            # Informa que foi digitado algo diferente de um Número
            print(f"Número Inválido!")
            
    # Opção para Exibir a Temperatura
    elif op == "4":
        
        # Ação de Exibir a Temperatura 
        termostato.mostrar()
        
    # Opção para Encerrar o Programa
    elif op == "5":

        # Informa que o Programa está encerrando
        print("Encerrando o Programa")
        
        # Encerra o looping infinito do while True
        break
        
    # Caso o Usuário digite uma opção diferente das permitidas
    else: 
        
        # Exibe uma mensagem informando que escolheu uma Opção Inválida
        print(f"Opção Inválida!")

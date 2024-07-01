import os

def clear_screen():
    # Detecta o sistema operacional e executa o comando de limpar tela apropriado
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS e Linux
        os.system('clear')

def show_menu():
    print("================")
    operations = {
        "+": "Soma",
        "-": "Subtração",
        "*": "Multiplicação",
        "/": "Divisão",
        "^": "Exponenciação"
    }
    i = 0
    for op, name in operations.items():
        print(f"{i} : {name}")
        i += 1
    return operations

def get_operation_choice(operations):
    while True:
        try:
            op = int(input("Escolha a operação que deseja realizar: "))
            if 0 <= op < len(operations):
                return list(operations.keys())[op]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def get_value(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    while True:
        clear_screen()
        operations = show_menu()
        
        op_string = get_operation_choice(operations)
        
        print(f"\n{operations[op_string]} escolhida.\n")
        
        v1 = get_value("Qual o primeiro valor? ")
        v2 = get_value("Qual o segundo valor? ")
        
        if op_string == "+":
            result = v1 + v2
        elif op_string == "-":
            result = v1 - v2
        elif op_string == "*":
            result = v1 * v2
        elif op_string == "/":
            result = v1 / v2
        elif op_string == "^":
            result = v1 ** v2
        
        print("================")
        print("\nResultado:")
        print(f"{v1} {op_string} {v2} = {result}\n")
        print("================")
        comando = input("Deseja fazer mais alguma operação? (Digite 's' para sair, qualquer outra tecla para continuar): ")
        if comando.lower() == 's':
            break

if __name__ == "__main__":
    main()

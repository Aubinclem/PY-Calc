def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erreur : Division par zéro"
    return x / y

def calculator():
    while True:
        print("\nOptions : +, -, *, /, ou 'exit' pour quitter")
        operation = input("Entrez l'opération (+, -, *, /): ")

        if operation == 'exit':
            print("Merci d'avoir utilisé la calculatrice.")
            break  # Quitte la boucle et termine le programme

        if operation in ['+', '-', '*', '/']:
            try:
                x = float(input("Entrez le premier nombre: "))
                y = float(input("Entrez le second nombre: "))
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue  # Reprend la boucle si l'utilisateur entre quelque chose qui n'est pas un nombre
                
            if operation == '+':
                print(f"{x} + {y} = {add(x, y)}")
            elif operation == '-':
                print(f"{x} - {y} = {subtract(x, y)}")
            elif operation == '*':
                print(f"{x} * {y} = {multiply(x, y)}")
            elif operation == '/':
                print(f"{x} / {y} = {divide(x, y)}")
        else:
            print("Opération invalide, essayez de nouveau.")

# Lancer la calculatrice
calculator()

import sys
from expenses import add_expense, list_expenses, delete_expense, total_expenses

def show_menu():
    print("\n=== SpendWise CLI ===")
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Remover gasto")
    print("4. Total de gastos")
    print("5. Sair")

def main():
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")

        try:
            if choice == "1":
                value = float(input("Valor: "))
                category = input("Categoria: ")
                description = input("Descrição: ")

                expense = add_expense(value, category, description)
                print(f"Gasto adicionado: {expense}")

            elif choice == "2":
                expenses = list_expenses()
                for e in expenses:
                    print(e)

            elif choice == "3":
                expense_id = int(input("ID do gasto: "))
                delete_expense(expense_id)
                print("Gasto removido!")

            elif choice == "4":
                total = total_expenses()
                print(f"Total gasto: R$ {total}")

            elif choice == "5":
                print("Saindo...")
                sys.exit()

            else:
                print("Opção inválida")

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()

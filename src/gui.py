from tkinter import messagebox
from api_moedas import obter_cotacoes
import tkinter as tk
from tkinter import messagebox
from expenses import add_expense, list_expenses, total_expenses

def atualizar_lista():
    lista.delete(0, tk.END)
    for e in list_expenses():
        lista.insert(tk.END, f"{e['id']} - R${e['value']} - {e['category']}")

    total_label.config(text=f"Total: R$ {total_expenses():.2f}")

def adicionar():
    try:
        valor = float(entry_valor.get())
        categoria = entry_categoria.get()
        descricao = entry_descricao.get()

        add_expense(valor, categoria, descricao)

        messagebox.showinfo("Sucesso", "Gasto adicionado!")
        entry_valor.delete(0, tk.END)
        entry_categoria.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)

        atualizar_lista()

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# janela
root = tk.Tk()
root.title("SpendWise GUI")

# campos
tk.Label(root, text="Valor").pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

tk.Label(root, text="Categoria").pack()
entry_categoria = tk.Entry(root)
entry_categoria.pack()

tk.Label(root, text="Descrição").pack()
entry_descricao = tk.Entry(root)
entry_descricao.pack()

def mostrar_cotacoes():
    cotacoes = obter_cotacoes()

    if cotacoes:
        texto = ""

        for moeda, valor in cotacoes.items():
            texto += f"{moeda}: R$ {valor}\n"

        messagebox.showinfo("Cotações", texto)

    else:
        messagebox.showerror("Erro", "Não foi possível obter cotações.")

# botão
tk.Button(root, text="Adicionar Gasto", command=adicionar).pack()

btn_cotacao = tk.Button(
    root,
    text="Ver Cotação",
    command=mostrar_cotacoes
)

btn_cotacao.pack()
# lista
lista = tk.Listbox(root, width=50)
lista.pack()

# total
total_label = tk.Label(root, text="Total: R$ 0.00")
total_label.pack()

# carregar dados
atualizar_lista()

root.mainloop()

print("5. Ver cotação das moedas")


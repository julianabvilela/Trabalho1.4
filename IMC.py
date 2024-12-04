import tkinter as tk
from importlib.metadata import entry_points
from multiprocessing.managers import Value
from tkinter import messagebox, Label
import sqlite3


def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura= float(entry_altura.get())
        nome = str(entry_nome.get())
        endereco = str(entry_endereco.get())
        banco = sqlite3.connect('bancodados.db')

        cursor = banco.cursor()

        cursor.execute("CREATE TABLE calculo (peso integer, altura integer, nome text, endereco text)")


        cursor.execute("INSERT INTO calculo VALUES("+str(peso)+","+str(altura)+",'"+nome+"','"+endereco+"')")

        banco.commit()

        imc = peso / (altura * altura)

        resultado_texto.set(f'Seu IMC e: {imc:2f}')

        if imc < 18.5:
            classificacao = "Abaixo do peso"

        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"

        elif 25 <= imc < 29.9:
            classificacao = "Acima do peso"

        elif 30 <= imc < 34.9:
            classificacao = "Obesidade grau I"

        elif 35 <= imc < 39.9 :
            classificacao = "Obesidade grau II"

        else:
            classificacao = "obesidade grau III"

        messagebox.showinfo("Classificacao IMC", f"{classificacao}")

    except ValueError:
        messagebox.showerror('Erro')


janela = tk.Tk()
janela.title("Calculadora de IMC")

tk.Label(janela, text="Nome :").grid(row=2, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=2, column=1, padx=10, pady=10 )

tk.Label(janela, text="Endereco :").grid(row=3, column=0, padx=10, pady=10)
entry_endereco = tk.Entry(janela)
entry_endereco.grid(row=3, column=1, padx=10, pady=10 )

tk.Label(janela, text="Peso (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=10 )

tk.Label(janela, text="Altura (m)").grid(row=1, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

resultado_texto = tk.StringVar()
nome = tk.StringVar()
endereco = tk.StringVar()

Label_resultado = tk.Label(janela, textvariable=resultado_texto)
Label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

btn_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(row=5, column=0, columnspan=2, padx=10)

janela.mainloop()
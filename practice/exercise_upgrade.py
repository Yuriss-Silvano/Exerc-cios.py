#codigo com funcao ativa para consulta

fluxo_caixa = []

print("_______________")
print("0 Fluxo caixa")
print("_______________")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro número para encerrar #\n")

def adicionar_transacao():
     nome = input("Nome: ")
     valor = float( input("Valor: ") )
     fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
     
while True:

    opcao = int( input("Digite a opcao: ") )

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

# nota fiscal
total = 0
for fc in fluxo_caixa:
     print("Nome:", fc['nome'], ". Valor: R$", fc['valor'])
     total += fc['valor']

print("Saldo atual: R$", total)
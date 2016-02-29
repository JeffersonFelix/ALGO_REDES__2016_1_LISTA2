Cliente = input("Cliente: ")
Preco = input("Preco: ")
Quantidade = int(input("Quantidade: "))
Valor_total = float(Preco) * Quantidade
print("Senhor %s seus produtos totalizam %.2f reais" % (Cliente, Valor_total))
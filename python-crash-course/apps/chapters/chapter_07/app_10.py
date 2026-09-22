lugares = input("Quantos lugares na mesa você precisa? ")
lugares = int(lugares)

if lugares > 8:
    print("É necessário aguardar por uma mesa.")
else:
    print("A mesa já está disponível.")

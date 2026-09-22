# Exercise 8.4

def make_shirt(tamanho='grande', texto_da_estampa='Eu amo Python'):
    print(f"\nTamanho da camiseta: {tamanho.title()}")
    print(f"Texto da estampa: {texto_da_estampa}")

make_shirt()

make_shirt('média')

make_shirt('pequena', 'Jesus is King')
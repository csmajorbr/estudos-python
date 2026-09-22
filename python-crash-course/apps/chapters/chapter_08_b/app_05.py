def fazer_sanduiche(*ingredientes):
    print("\nSeu sanduíche terá os seguintes ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente.title()}")

fazer_sanduiche('pão de hambúrguer', 'hambúrguer', 'muçarela', 'maionese')

fazer_sanduiche('pão de forma', 'ovos mexidos', 'creme de ricota')

fazer_sanduiche('pão francês', 'bacon', 'manteiga')
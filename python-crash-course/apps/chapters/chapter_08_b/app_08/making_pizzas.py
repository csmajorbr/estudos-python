import apps.chapters.chapter_08_b.app_08.pizza as pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


"""
Dessa maneira importaria somente a função e não seria necessário pizza.make, é possível chamar a função diretamente, pois já foi especificada na importação:

    from pizza import make_pizza
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
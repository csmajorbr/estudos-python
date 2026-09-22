def make_car(fabricante, modelo, **outros_atributos):
    outros_atributos['fabricante'] = fabricante
    outros_atributos['modelo'] = modelo
    return outros_atributos


car_1 = make_car('fiat', 'uno', cor='prata', ano=2_000, valor=30_000)

for key, value in car_1.items():
    print(f"{key} : {value}")

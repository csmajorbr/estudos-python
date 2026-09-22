def build_profile(first, last, **others):
    others['fname'] = first
    others['lname'] = last
    return others


user_profile = build_profile(
    'jefferson', 'santana', sexo='homem', idade=34, estado_civil='solteiro')

for key, value in user_profile.items():
    print(f"{key} : {value}")

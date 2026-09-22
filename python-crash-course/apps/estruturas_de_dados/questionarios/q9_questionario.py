notas = [6.0, 7.5, 8.0, 6.5, 9.0, 7.0]

sum = 0.0

for nota in notas:
    sum += nota

media = sum / len(notas)

print(f"media = {media:.2f}")
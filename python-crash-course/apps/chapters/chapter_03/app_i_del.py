motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

for index, motorcycle in enumerate(motorcycles):
    print(f"{index}: {motorcycle}")


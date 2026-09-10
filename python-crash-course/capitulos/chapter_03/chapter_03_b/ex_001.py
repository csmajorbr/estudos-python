places = ['kabul', 'abuja', 'khartoum', 'tripoli', 'kinshasa']

print("Original order:")
print(places)

print("\nAlphabetical order using sorted():")
print(sorted(places))

print("\nOriginal order:")
print(places)

print("\nReverse alphabetical order using sorted():")
print(sorted(places, reverse=True))

print("\nOriginal order:")
print(places)

print("\nUsing reverse():")
places.reverse()
print(places)

print("\nUsing reverse() again:")
places.reverse()
print(places)

print("\nUsing sort():")
places.sort()
print(places)

print("\nReverse alphabetical order using sort():")
places.sort(reverse=True)
print(places)

print("\nShow the size of the list using len():")
print(len(places))

# Erro de índice intencional:
# print(places[5])

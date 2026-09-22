def make_album(artista, album, numero_de_musicas=None):
    if numero_de_musicas:
        return {'nome_do_artista': artista, 'nome_do_album': album, 'musicas': numero_de_musicas}
    else:
        return {'nome_do_artista': artista, 'nome_do_album': album}

album_1 = make_album('Livres', 'Liberdade')
album_2 = make_album('Marcos', 'Santo')
album_3 = make_album('Fernandinho', 'Fé')

print(f"{album_1}")
print(f"{album_2}")
print(f"{album_3}")

album_4 = make_album('Calvinistas', 'Romanos 9', 12)

print(f"{album_4}")
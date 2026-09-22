def make_album(artista, album, tracks=None):
    album_dict = {
        'artista': artista.title(),
        'album': album.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict




while True:
    print("\nDigite 'q' a qualquer momento para sair.")

    artista = input("Artista: ")
    if artista == 'q':
        break

    album = input("Álbum: ")
    if album == 'q':
        break
    
    album = make_album(artista, album)
    print(album)
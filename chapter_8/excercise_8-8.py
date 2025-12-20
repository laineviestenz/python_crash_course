def make_album(artist_name, album_title, tracks = ''):
    if tracks:
        return {'artist_name': artist_name, 'album_title': album_title, 'tracks': tracks}
    else:
        return {'artist_name': artist_name, 'album_title': album_title}

while True:
    artist = input("Artist Name: ")
    if artist == 'q':
        break
    title = input("Album Title: ")
    if title == 'q':
        break
    tracks = input("how many tracks? (press enter to skip): ")
    if title == 'q':
        break
    print(make_album(artist, title, tracks))

# print(make_album('taylor swift', 'cruel summer'))
# print(make_album('gorillaz', 'oldies'))
# print(make_album('dan + shay', 'december', 16))
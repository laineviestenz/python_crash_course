def make_album(artist_name, album_title, tracks = ''):
    if tracks:
        return {'artist_name': artist_name, 'album_title': album_title, 'tracks': tracks}
    else:
        return {'artist_name': artist_name, 'album_title': album_title}


print(make_album('taylor swift', 'cruel summer'))
print(make_album('gorillaz', 'oldies'))
print(make_album('dan + shay', 'december', 16))
""": Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that 
information, call make_album() with the user’s input and print the dictionary 
that’s created. Be sure to include a quit value in the while loop.
"""


def make_album(artist_name, album_title, num_tracks=None):
    """Return a dictionary describing a music album."""
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    if num_tracks:
        album['tracks'] = num_tracks
    return album

while True:
    print("\nEnter the artist name and album title (or 'q' to quit):")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    title = input("Album title: ")
    if title == 'q':
        break

    album_dict = make_album(artist, title)
    print(album_dict)



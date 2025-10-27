# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.



def make_album(artist_name, album_title, number_songs=None):
    album_dictionary = {
        "artist": artist_name,
        "album": album_title
    }

    if number_songs:
        album_dictionary["number_songs"] = number_songs

    return album_dictionary


print("Welcome to the album dictionary.")
print("Type 'q' to quit.")
while True:
    artist_name = input("Please enter the artist's name: ")

    if artist_name.lower() == "q":
        break

    album_name = input("Please enter the album name: ")

    if album_name.lower() == "q":
        break

    number_songs = input("Please enter the amount of songs in the album (or you can just enter none to skip this part): ")

    if number_songs.lower() == "q":
        break

    if number_songs.lower() != "none":
        print(make_album(artist_name, album_name, number_songs))
    else:
        print(make_album(artist_name, album_name))

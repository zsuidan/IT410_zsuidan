#Problem 8-1
#Creates a function that prints out a statement using a variable input from the user
print("Problem 8-1:")

def tune_in(passed_radio_station):
    print("Let me tune in " + str(passed_radio_station))

fav_station = input("What is your favorite radio station?: ")
tune_in(fav_station)

#Problem 8-2
#Creates a function that takes various inputs for printing business cards and displays a message based on the inputs 
print("\nProblem 8-2:")

def print_business_cards(passed_name, passed_quantity, passed_tag_line):
    
    try:
        passed_quantity = int(passed_quantity)
    except:
        print("The quantity is not an integer")
        return

    print("You are printing " + str(passed_quantity) + " business cards for " + str(passed_name) + " with the tag line \"" + str(passed_tag_line) + "\"")

print_business_cards("Zach", 50, "Greatest tag line of all time")
print_business_cards("John", 40, "Tag line")
print_business_cards("Susie", 60, "This is a tag line")

#Problem 8-3
#Rewritten 8-2 function which allows for a default value of 100 cards printed if there is no input
print("\nProblem 8-3:")

def print_business_cards_modified(passed_name, passed_tag_line, passed_quantity=100):

    try:
        passed_quantity = int(passed_quantity)
    except:
        print("The quantity is not an integer")
        return

    print("You are printing " + str(passed_quantity) + " business cards for " + str(passed_name) + " with the tag line \"" + str(passed_tag_line) + "\"")

print_business_cards_modified("Zach", "This is also a tag line", 150)
print_business_cards_modified("Bill", "Cool tag line")

#Problem 8-4
#Creates a function that takes an input for a song name and artist then creates and returns a string
print("\nProblem 8-4:")

def song_playing(passed_song_name, passed_artist='Unknown'):

    returned_string = str(passed_song_name) + " by " + str(passed_artist)

    return returned_string

song_one = song_playing("One More Time", "Daft Punk")
song_two = song_playing("Enter Sandman", "Metallica")
song_three = song_playing("Piano Man")

print(song_one)
print(song_two)
print(song_three)

#Problem 8-5
#Creates a function that returns a dictionary item based on user input for a song, a function that loops through a list and prints each item within, 
# and allows users to enter songs into a playlist through a while loop
print("\nProblem 8-5:")

def add_song(passed_song_name, passed_artist='Unknown'):
    returned_dictionary = {'song_name': str(passed_song_name), 'artist': str(passed_artist)}

    return returned_dictionary

def show_playlist(passed_playlist):
    for song in passed_playlist:
        print("Song: " + song['song_name'] + "\t\tArtist: " + song['artist'])

playlist = []

add_more = True

while add_more:
    new_song = input("Enter a song name: ")
    new_artist = input("Enter the artist name (leave blank if unknown): ")

    if new_artist:
        playlist.append(add_song(new_song, new_artist))
    else:
        playlist.append(add_song(new_song))

    continue_adding = input("Would you like to add another song? (Y/N): ")

    correct_input = False

    while not correct_input:
        if continue_adding.upper() == "Y" or continue_adding.upper() == "N":
            correct_input = True
        else:
            continue_adding = input("Invalid response. Please enter either Y or N.")
    
    if continue_adding.upper() == "Y":
        continue
    elif continue_adding.upper() == "N":
        break

show_playlist(playlist)
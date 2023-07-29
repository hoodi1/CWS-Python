# Create an empty list to store the songs in the playlist
playlist = []
# Start the loop to display the menu and interact with the Playlost manager
while True:
    print("Welcome to the Music Playlist Manager !!")
    print("Menu: ")
    print("a. Add a song to the playlist: ")
    print("b. Remove a song from the playlist: ")
    print("c. View the current Playlist: ")
    print("d. Quit: ")

    choice = input("Enter your choice: ")
    if choice == "a":
        # Add song to the Playlist
        song_name = input("Enter the Song Name: ")
        playlist.append(song_name)
        print(f"{song_name} has been added to the playlist.\n")

    elif choice == "b":
        # Remove a song from the playlist
        if len(playlist) == 0:
            print("The Playlist is empty. No songs to remove.\n")
        else:
            song_name = input("Enter the song name to remove!! ")
            if song_name in playlist:
                playlist.remove(song_name)
                print(f"{song_name} has been removed from the playlist.\n")
            else:
                print(f"{song_name} is not found in the playlist.\n")
    elif choice == "c":
        # View current Playlist
        if len(playlist) == 0:
            print("The Playlost is empty. ")
        else:
            print("Current Playlist:")
            for song in playlist:
                print(f"{song}")
            print()
    elif choice == "d":
        # Quit the program
        print("Thank You for Using Music Playlist Manager!. ")
        break
    else:
        print("Invalid choice. Please select a valid option.\n")
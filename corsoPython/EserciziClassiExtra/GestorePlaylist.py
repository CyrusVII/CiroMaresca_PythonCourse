# Classe Brano:
# Attributi: titolo, artista, durata (in minuti, es. 3.5)
# Classe Playlist:
# Attributo: brani (lista di oggetti Brano)
# Metodi:
# aggiungi_brano(brano)
# durata_totale() → somma tutte le durate
# cerca_per_artista(nome) → stampa tutti i titoli dei brani di quell’artista
# Obiettivo: gestione di tuple o oggetti con cicli, somma e filtri.
import time

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def song_data(self):
        return f"Title : {self.title} / Artist : {self.artist} / Duration : {self.duration}"


class Playlist:
    def __init__(self):
        self.songs = {}

    # Check if playlist has at least one song
    def is_filled_playlist(self):
        return bool(self.songs)

    # Calculate total duration of all songs
    def playlist_duration(self):
        if self.is_filled_playlist():
            total = sum(val.duration for val in self.songs.values())
            return total
        else:
            return "There are no songs in the playlist."

    # Find and print songs by a specific artist
    def found_artist_song(self):
        name = input("Type artist name ---> ").strip().lower().capitalize()
        found = False
        for val in self.songs.values():
            if val.artist == name:
                print(val.song_data())
                found = True
        if not found:
            print("No songs found by this artist.")

    # Check if a song with the given title already exists
    def found_song(self, song):
        for val in self.songs.values():
            if val.title == song:
                return True
        return False

    # Add a new song to the playlist
    def add_song(self):
        print("--- Add new song to playlist ---")
        while True:
            try:
                title = input('Type song title ---> ').lower().strip().capitalize()

                # If song already exists in playlist, raise error
                if self.found_song(title):
                    raise ValueError("Song already exists in playlist!")

                artist = input('Type artist name ---> ').lower().strip().capitalize()
                duration = float(input("Type song duration (minutes) ---> "))

                song = Song(title, artist, duration)

                # Generate a new ID
                new_id = max(self.songs.keys(), default=0) + 1

                self.songs[new_id] = song
                print("--- Song added ---")
                break
            except ValueError as e:
                print(f"Invalid data: {e}. Please try again.\n")


# ---------- MAIN ----------
def main():
    playlist = Playlist()
    while True:
        time.sleep(2)
        print("\n--- Playlist Menu --- \n 1. Add a new song \n 2. Show all songs \n 3. Search songs by artist \n 4. Total duration of playlist \n 0. Exit")
        try:
            choice = int(input("Choose an option ---> "))
            match choice:
                case 1:
                    playlist.add_song()
                case 2:
                    if playlist.is_filled_playlist():
                        for key, song in playlist.songs.items():
                            print(f"ID: {key} /", song.song_data())
                    else:
                        print("The playlist is empty.")
                case 3:
                    playlist.found_artist_song()
                case 4:
                    print("Total playlist duration:", playlist.playlist_duration(), "minutes")
                case 0:
                    print("Exiting program...")
                    break
                case _:
                    print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
main()

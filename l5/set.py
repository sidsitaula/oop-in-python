song_library = [("Phantom Of The Opera", "Sarah Brightman"),
                ("Knocking On Heaven's Door", "Guns N' Roses"),
                ("Captain Nemo", "Sarah Brightman"),
                ("Patterns In The Ivy", "Opeth"),
                ("November Rain", "Guns N' Roses"),
                ("Beautiful", "Sarah Brightman"),
                ("Mal's Song", "Vixy and Tony")]
artists = set()
for song, artist in song_library:
    artists.add(artist)
print(artists)

my_artists = {"Sarah Brightman", "Guns N' Roses",
              "Opeth", "Vixy and Tony"}
auburns_artists = {"Nickelback", "Guns N' Roses",
                   "Savage Garden"}
print("All: {}".format(my_artists.union(auburns_artists)))
print("Both: {}".format(auburns_artists.intersection(my_artists)))
print("Either but not both: {}".format(
    my_artists.symmetric_difference(auburns_artists)))

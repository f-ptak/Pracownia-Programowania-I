with open("7.11 movies.txt", "w") as file:
    movies = ["Jan Nowak's Funky Band", "Life and Legacy of Jan Nowak", "Jan Nowak: Reboot",
              "Jan Nowak: Spin-off Prequel Reboot Remake Remaster", "Jan Nowak TV Series"]
    
    for title in movies:
        file.write(f"{title}\n")
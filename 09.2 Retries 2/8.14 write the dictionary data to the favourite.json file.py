import json

movie = {"title": "Jan Nowak's Real No Scam Movie",
         "genre": "Real Moives",
         "year": "1999",
         "rating": "7.2/10",
         "director": "Jan Nowak",
         "awards": ["Noble","Oscar","Jan Nowak's Award"]
    }

with open("8.14 favourite.json", "w") as file:
    json.dump(movie, file, indent = 4)
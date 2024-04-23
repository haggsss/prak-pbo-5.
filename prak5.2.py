class Movie:
    def __init__(self, title, release_year, director, order):
        self.title = title
        self.release_year = release_year
        self.director = director
        self.order = order

    def display_info(self):
        print(f"Film favorit ke-{self.order}:")
        print(f"Judul: {self.title}")
        print(f"Tahun Rilis: {self.release_year}")
        print(f"Sutradara: {self.director}")

# List untuk menyimpan objek Movie
daftar_film = []

# Data film favorit
film_data = [
    {"title": "UP", "release_year": 2009, "director": "Walt Disney Pictures"},
    {"title": "Kungfu Panda", "release_year": 2008, "director": "Mark Osborne"},
    {"title": "Fast & Furious", "release_year": 2003, "director": "John Singleton"},
    {"title": "Spiderman", "release_year": 2002, "director": "Sam Raimi"},
    {"title": "Agak laen", "release_year": 2024, "director": "Muhadkly Acho"}
]

# Memasukkan data film ke dalam daftar_film
for i, data in enumerate(film_data, start=1):
    movie = Movie(data["title"], data["release_year"], data["director"], i)
    daftar_film.append(movie)

# Menampilkan informasi film
print("----------ELKOM 2----------")
for film in daftar_film:
    film.display_info()
    print("==============")

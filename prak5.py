# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:42:01 2024

@author: kusfi
"""

class FilmFavorit:
    def __init__(self):
        self.film_favorit = []

    def tambah_film(self, film):
        self.film_favorit.append(film)

    def tampilkan_daftar(self):
        print("========Daftar 5 Film Favorit Anda========")
        for i, film in enumerate(self.film_favorit, start=1):
            print("{}. {}".format(i, film))

def main():
    daftar_film = FilmFavorit()

    for i in range(5):
        film = input("Masukkan nama film favorit ke-{}: ".format(i+1))
        daftar_film.tambah_film(film) 

    daftar_film.tampilkan_daftar()

if __name__ == "__main__":
    main()

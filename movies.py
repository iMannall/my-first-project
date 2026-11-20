movies = ["Titanic", "Avatar", "Interstellar"]

movies.append("The Notebook")

print(movies)
print(len(movies))
print("My Favorite Movies:")

def show_movies():
    for movie in movies:
        print(movie)
show_movies()
if "Frozen" in movies:
    print("Movie found!")
else:
    print("Movie not found!")
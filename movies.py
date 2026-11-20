
# Movie Collection Manager

movies = ["Titanic", "Avatar", "Interstellar", "The Notebook"]


def show_movies():
    print("\nMy Favorite Movies")

    if not movies:
        print("Your movie list is empty.")
    else:
        for index, movie in enumerate(movies, start=1):
            print(f"{index}. {movie}")

    print(f"\nTotal movies: {len(movies)}")


def add_movie():
    movie = input("\nEnter a movie name: ").strip()

    if not movie:
        print("Movie name cannot be empty.")
    elif movie.lower() in [m.lower() for m in movies]:
        print("This movie is already in your list.")
    else:
        movies.append(movie)
        print(f"{movie} has been added successfully!")


def remove_movie():
    movie = input("\nEnter the movie name to remove: ").strip()

    for existing_movie in movies:
        if existing_movie.lower() == movie.lower():
            movies.remove(existing_movie)
            print(f"{existing_movie} has been removed.")
            return

    print("Movie not found in your list.")


def search_movie():
    movie = input("\nEnter a movie name to search: ").strip()

    for existing_movie in movies:
        if existing_movie.lower() == movie.lower():
            print(f"{existing_movie} was found in your list!")
            return

    print("Movie not found.")


def display_menu():
    print("\n===== Movie Collection Manager =====")
    print("1. Show all movies")
    print("2. Add a movie")
    print("3. Remove a movie")
    print("4. Search for a movie")
    print("5. Show total movies")
    print("6. Exit")


def main():
    while True:
        display_menu()

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            show_movies()

        elif choice == "2":
            add_movie()

        elif choice == "3":
            remove_movie()

        elif choice == "4":
            search_movie()

        elif choice == "5":
            print(f"\nTotal movies: {len(movies)}")

        elif choice == "6":
            print("\nThank you for using Movie Collection Manager!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()

from datetime import datetime


def add_movie(movies, name_of_movie):
    name_of_movie = name_of_movie.strip().lower()

    if name_of_movie not in movies:
        movies[name_of_movie] = {
            "ratings": [],
            "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return f"Movie '{name_of_movie}' added on {movies[name_of_movie]['date_added']}"
    else:
        return f"Movie '{name_of_movie}' already exists!"


def rate_movie(movies, name_of_movie, rating):
    name_of_movie = name_of_movie.strip().lower()

    if name_of_movie not in movies:
        return f"Movie '{name_of_movie}' does not exist!"
    if rating < 1 or rating > 5:
        return "Rating must be between 1 and 5"

    movies[name_of_movie]["ratings"].append(rating)
    return f"Rating {rating} added for '{name_of_movie}'"


def view_average_ratings(movies):
    if not movies:
        return "No movies found."

    averages = {}
    total_rating_sum = 0
    total_rating_count = 0
    overall_average = 0

    for movie_name, data in movies.items():
        ratings = data["ratings"]
        if ratings:
            average_rating = sum(ratings) / len(ratings)
            total_rating_sum += sum(ratings)
            total_rating_count += len(ratings)
        else:
            average_rating = 0

        averages[movie_name] = f"{average_rating:.2f}"

    if total_rating_count > 0:
        overall_average = total_rating_sum / total_rating_count

    return averages, f"\nOverall average rating is: {overall_average:.2f}"


def main():
    movies = {}

    while True:
        print("""
MOVIE RATINGS SYSTEM
==================================
1. Add a movie
2. Rate a movie
3. View Average Ratings
4. Exit
""")
        choice = 0

        try:
            choice = int(input("Enter your choice to continue: "))
            if choice not in {1, 2, 3, 4}:
                choice = int(input("Incorrect input, kindly enter a number between 1 and 4: "))
        except ValueError:
            print("Invalid entry.")
            continue

        if choice == 1:
            try:
                name_of_movie = input("Enter a movie name: ").strip()
                print(add_movie(movies, name_of_movie))
            except ValueError:
                print("Invalid error")
                continue

        elif choice == 2:
            if not movies:
                print("No movies found, kindly add a movie first.")
                continue

            name_of_movie = input("Enter a movie name: ").strip()
            try:
                rating = float(input("Enter your rating (between 1 and 5): "))
                print(rate_movie(movies, name_of_movie, rating))
            except ValueError:
                print("Invalid input. Rating must be between 1 and 5.")
                continue

        elif choice == 3:
            averages, overall_average = view_average_ratings(movies)
            print("\nAverage Ratings: ")
            for movie_name, value in averages.items():
                print(f"{movie_name}: {value}")
            print(overall_average)

        elif choice == 4:
            print("Exiting the application. Goodbye!")
            break


main()
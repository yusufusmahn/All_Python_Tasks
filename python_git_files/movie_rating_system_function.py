from datetime import datetime


def add_movie(movies, name_of_movie, dates):

	name_of_movie = name_of_movie.strip().lower()

	if name_of_movie not in movies:
		movies[name_of_movie] = []
		dates[name_of_movie] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		return f"Movie '{name_of_movie}' added on {dates[name_of_movie]}"
	else:
		return f"Movie '{name_of_movie}' already exists!"


def rate_movie(movies, name_of_movie, rating):
	name_of_movie = name_of_movie.strip().lower()

	if name_of_movie not in movies:
		return "movie " + name_of_movie + " does not exist"
	if rating < 1 or rating > 5:
		return "Rating must be between 1 and 5"

	movies[name_of_movie].append(rating)
	return f"ratings added for '{name_of_movie}': {rating}"



def view_average_ratings(movies):
	if not movies:
		return "cant find movie of the name."
	
	averages = {}
	total_rating_sum = 0
	total_rating_count = 0
	overall_average = 0

	for movie_name, ratings in movies.items():
		if ratings:
			average_rating = sum(ratings) / len(ratings)
			total_rating_sum += sum(ratings)
			total_rating_count += len(ratings)
		else:
			average_rating = 0

		averages[movie_name] = f"{average_rating:.2f}"

		if total_rating_count > 0:
			overall_average = total_rating_sum / total_rating_count
			

	return averages, f"\nOverall average Ratings is: {overall_average:.2f}"

	



def main():

	movies = {}
	dates = {}

	while True:


		print("""
\nMOVIE RATINGS SYSTEM
==================================
1. Add a movie
2. Rate a movie
3. View Average Ratings
4. Exit
""")
		choice = 0

		try:	
			choice = int(input("Enter your choice to continue: "))
			if choice not in {1,2,3,4}:
				choice = int(input("Incorrect input, Kindly Enter a number between 1 and 4: "))

		except ValueError:
			print("Invalid entry: ")			

		if choice == 1:
			try:
				name_of_movie = input("Enter a movie name: ").strip()
				print(add_movie(movies, name_of_movie, dates))
			except ValueError:
				print("invalid error")
				continue

		elif choice == 2:
			if not movies:
				print("no movies found, kindly add a movie")
				continue
			name_of_movie = input("Enter a movie name: ").strip()

			try:
				rating = float(input("enter your rating btw :1 and 5: "))
				print(rate_movie(movies, name_of_movie, rating))
			except ValueError:
				print("Invalid input, Rating must be btw  1 and 5")
				continue

	
		elif choice == 3:
			averages, overall_average = view_average_ratings(movies)
			print("\nAverage Ratings: ")
			for movie_name, value in averages.items():
				print(f"{movie_name}: {value}")
			print(overall_average)
			



		elif choice == 4:
			print("Exiting the application, Goodbye!!!")
			break




main()

	


		

	

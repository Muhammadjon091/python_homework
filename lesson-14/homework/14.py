import json

def read_students():
    with open("students.json", "r", encoding="utf-8") as file:
        students = json.load(file)
    
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

read_students()



import requests

API_KEY = "your_api_key_here"
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {CITY}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data.")

get_weather()





import json

BOOKS_FILE = "books.json"

def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print("Book added successfully!")

def update_book():
    books = load_books()
    title = input("Enter book title to update: ")
    for book in books:
        if book["title"] == title:
            book["author"] = input("Enter new author: ")
            book["year"] = input("Enter new year: ")
            save_books(books)
            print("Book updated successfully!")
            return
    print("Book not found!")

def delete_book():
    books = load_books()
    title = input("Enter book title to delete: ")
    books = [book for book in books if book["title"] != title]
    save_books(books)
    print("Book deleted successfully!")

def main():
    while True:
        print("\n1. Add Book\n2. Update Book\n3. Delete Book\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

main()




import requests
import random

API_KEY = "your_api_key_here"

def get_movie_by_genre(genre):
    URL = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        if "Search" in data:
            movie = random.choice(data["Search"])
            print(f"Recommended Movie: {movie['Title']} ({movie['Year']})")
        else:
            print("No movies found in this genre.")
    else:
        print("Error fetching movie data.")

genre = input("Enter a movie genre (e.g., Action, Comedy, Horror): ")
get_movie_by_genre(genre)

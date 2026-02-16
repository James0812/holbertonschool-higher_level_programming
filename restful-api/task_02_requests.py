#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print("Status Code:", response.status_code)

    # If request was successful
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # If request was successful
    if response.status_code == 200:
        posts = response.json()

        # Keep only id, title and body
        formatted_posts = []
        for post in posts:
            formatted_posts.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        # Write to CSV file
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in formatted_posts:
                writer.writerow(post)

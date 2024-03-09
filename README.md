# Article Management System

This Python module implements a simple Article Management System consisting of three classes: `Author`, `Magazine`, and `Article`. These classes allow users to create and manage authors, magazines, and articles, and perform various operations such as adding articles, retrieving information about authors and magazines, and identifying top publishers.

## Classes

### Author

The `Author` class represents an author of articles. Each author has a name and a list of articles they have written.

#### Methods

- `__init__(name: str)`: Initializes an author with the given name.
- `articles()`: Returns the list of articles written by the author.
- `magazines()`: Returns the list of magazines the author has contributed to.
- `add_article(magazine: Magazine, title: str)`: Adds a new article authored by the author to the specified magazine.
- `topic_areas()`: Returns a list of unique topic areas covered by the articles written by the author.

### Magazine

The `Magazine` class represents a magazine that publishes articles. Each magazine has a name, a category, and a list of articles it has published.

#### Methods

- `__init__(name: str, category: str)`: Initializes a magazine with the given name and category.
- `articles()`: Returns the list of articles published by the magazine.
- `contributors()`: Returns the list of authors who have contributed articles to the magazine.
- `article_titles()`: Returns the list of titles of articles published by the magazine.
- `contributing_authors()`: Returns a list of authors who have contributed more than two articles to the magazine.
- `top_publisher()`: Class method that returns the magazine with the highest number of published articles.

### Article

The `Article` class represents an article written by an author and published in a magazine. Each article has an author, a magazine, and a title.

#### Methods

- `__init__(author: Author, magazine: Magazine, title: str)`: Initializes an article with the given author, magazine, and title.
- `author()`: Returns the author of the article.
- `magazine()`: Returns the magazine in which the article is published.
- `title()`: Returns the title of the article.

## Testing

The `article_test.py`, `author_test.py`, and `magazine_test.py` files contain unit tests for the `Author`, `Magazine`, and `Article` classes respectively, using the `pytest` framework. These tests verify the correct functionality of the implemented methods and ensure that the classes behave as expected.

## Usage

To use the Article Management System, simply import the `Author`, `Magazine`, and `Article` classes from the `article` module and create instances of these classes to manage authors, magazines, and articles in your application.

Example:

```python
from article import Author, Magazine, Article

# Create an author
author = Author("Brian Kipkirui")

# Create a magazine
magazine = Magazine("Tech Today", "Python")

# Add an article authored by the author to the magazine
article = author.add_article(magazine, "Python Prog")

# Retrieve information about authors, magazines, and articles as needed
print(author.articles())
print(magazine.contributors())
print(article.title())
```

## Requirements
Python 3.x<br />
pytest(for running tests)

## Installation with Pipenv
If you're using pipenv, you can install the required dependencies with the following command:
```
pipenv install
```
This will create a virtual environment and install the required packages specified in the `Pipfile`.

## License
This project is licensed under the MIT License -  see the <a href = "https://github.com/bryokn/Code_Challenge_Articles_phase3/blob/main/LICENSE">LICENSE</a> file for details

## Author
This code is written and maintained by Brian Kipkirui. You can contact me at <a href="mailto:bryokn@gmail.com">bryokn@gmail.com.</a>
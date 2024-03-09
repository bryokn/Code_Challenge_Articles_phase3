import pytest
from article import Author, Magazine, Article

def test_author_initialization():
    author = Author("Brian Kipkirui")
    assert author.name == "Brian Kipkirui"

def test_author_articles():
    author = Author("Brian Kipkirui")
    magazine = Magazine("Tech Today", "Python")
    article = author.add_article(magazine, "Python Prog")
    assert article in author.articles()

def test_author_magazines():
    author = Author("Brian Kipkirui")
    magazine1 = Magazine("Tech Today", "Python")
    magazine2 = Magazine("Science News", "Science")
    article1 = author.add_article(magazine1, "Python Prog")
    article2 = author.add_article(magazine2, "Kaizen Python Prog")
    assert magazine1 in author.magazines()
    assert magazine2 in author.magazines()

 
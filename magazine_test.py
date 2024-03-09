import pytest
from article import Author, Magazine, Article

def test_magazine_initialization():
    magazine = Magazine("Tech Today", "Python")
    assert magazine.name() == "Tech Today"
    assert magazine.category() == "Python"

def test_magazine_articles():
    author = Author("Brian Kipkirui")
    magazine = Magazine("Tech Today", "Python")
    article = author.add_article(magazine, "Python Prog")
    assert article in magazine.articles()

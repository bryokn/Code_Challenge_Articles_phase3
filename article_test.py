import pytest
from article import Author, Magazine, Article

def test_article_initialization():
    author = Author("Brian Kipkirui")
    magazine = Magazine("Tech Today", "Python")
    article = Article(author, magazine, "Python Prog")
    assert article.author() == author
    assert article.magazine() == magazine
    assert article.title() == "Python Prog"

def test_add_article():
    author = Author("Brian Kipkirui")
    magazine = Magazine("Tech Today", "Python")
    article = author.add_article(magazine, "Python Prog")
    assert article in author.articles()

def test_magazine_articles():
    author = Author("Brian Kipkirui")
    magazine = Magazine("Tech Today", "Python")
    article = author.add_article(magazine, "Python Prog")
    assert article in magazine.articles()

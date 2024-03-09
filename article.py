class Author:
    def __init__(self, name):
        if type(name) != str or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []
    
    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        magazines_list = []
        for article in self._articles:
            magazines_list.append(article.magazine())
        return magazines_list

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        categories = set()
        for article in self._articles:
            categories.add(article.magazine().category())
        return list(categories)

class Magazine:
    def __init__(self, name, category):
        if type(name) != str or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters long")
        if type(category) != str or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    def name(self):
        return self._name

    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        authors_list = []
        for article in self._articles:
            authors_list.append(article.author())
        return authors_list

    def article_titles(self):
        titles_list = []
        for article in self._articles:
            titles_list.append(article.title())
        return titles_list

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author()
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()))

class Article:
    def __init__(self, author, magazine, title):
        if type(title) != str or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters long")
        self._author = author
        self._magazine = magazine
        self._title = title
        self._author.articles().append(self)
        self._magazine.articles().append(self)

    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

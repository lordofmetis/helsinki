# Write your solution here:
class Series:
    def __init__(self, name: str, season: int, genre: list):
        self.title = name
        self.season = season
        self.genre = genre
        self.genre_string = ", ".join(self.genre)
        self.rating = 0
        self.count = 0

    def __str__(self):
        try:
            return f"{self.title} ({self.season} seasons)\ngenres: {self.genre_string}\n{self.count} ratings, average {self.rating / self.count:.1f} points"
        except ZeroDivisionError:
            return f"{self.title} ({self.season} seasons)\ngenres: {self.genre_string}\nno ratings"
            
    def rate(self, rating: int):
        self.rating += rating
        self.count += 1
    
def minimum_grade(rating: float, series_list: list):
    matching_series = []
    for series in series_list:
        if series.rating >= rating:
            matching_series.append(series)
    return matching_series

def includes_genre(genre: str, series_list: list):
    matching_series = []
    for series in series_list:
        if genre in series.genre:
            matching_series.append(series)
    return matching_series

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
class Review:
    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        self.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        cls.all_reviews.clear()
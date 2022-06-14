class Book:
    def __init__(self,author = 'none',title = 'none',publisher = 'none',publish_date = 'none',average_rating = 'none',num_ratings = 'none',description = 'none' ):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.publish_date = publish_date
        self.average_rating = average_rating
        self.num_ratings = num_ratings
        self.description = description

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}\n".format(self.title,self.author,self.publisher,self.publish_date,self.average_rating , self.num_ratings , self.description)

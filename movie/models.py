from django.db import models


class MovieList(models.Model):
    name = models.CharField(max_length=500)
    popularity = models.FloatField()
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.name


class WatchList(models.Model):
    name = models.CharField(max_length=500)
    popularity = models.FloatField()
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.name


class RecommendList(models.Model):
    watched = models.ForeignKey(WatchList, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    popularity = models.FloatField()
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.name

# class Watch(models.Model):
#     name = models.CharField(max_length=100)
#     watchlist = models.ManyToManyField(MovieList)

#     def __str__(self):
#         return self.name

# class Recommend(models.Model):
#     recommended = models.ManyToManyField(MovieList)

# class PopularList(models.Model):
#     name = models.CharField(max_length=500)
#     popularity = models.FloatField()
#     description = models.TextField()
#     release_date = models.DateField()

#     def __str__(self):
#         return self.name


# class LatestList(models.Model):
#     name = models.CharField(max_length=500)
#     popularity = models.FloatField()
#     description = models.TextField()
#     release_date = models.DateField()

#     def __str__(self):
#         return self.name

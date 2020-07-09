from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from .models import MovieList, WatchList, RecommendList
import graphene
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = '1c434c8bc8a5f2101fb33d1dfd2c338b'


class MovieType(DjangoObjectType):
    class Meta:
        model = MovieList


class WatchType(DjangoObjectType):
    class Meta:
        model = WatchList


class RecommendType(DjangoObjectType):
    class Meta:
        model = RecommendList


class MovieMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    movie = graphene.Field(MovieType)

    def mutate(self, info, id):
        movie = MovieList.objects.get(id=id)
        name = movie.name
        desc = movie.description
        pop = movie.popularity
        rdate = movie.release_date

        watchmovie = WatchList(name=name, popularity=pop,
                               description=desc, release_date=rdate)

        watchmovie.save()
        tmdbmovie = Movie()

        search = tmdbmovie.search(name)
        searchmovie = search[0]
        movieid = searchmovie.id
        recc = tmdbmovie.recommendations(movie_id=movieid)
        for recmovie in recc[:5]:
            name = recmovie.title
            desc = recmovie.overview
            pop = recmovie.popularity
            rdate = recmovie.release_date

            newrecmovie = RecommendList(watched=watchmovie, name=name, popularity=pop,
                                        description=desc, release_date=rdate)

            newrecmovie.save()

        return MovieMutation(movie=movie)


class DeleteWatchMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    movie = graphene.Field(WatchType)

    def mutate(self, info, name):
        movie = WatchList.objects.get(name=name)
        movie.delete()
        return DeleteWatchMutation(movie=movie)


class Mutation(graphene.ObjectType):
    watch_movie = MovieMutation.Field()
    delete_watch = DeleteWatchMutation.Field()


class Query(graphene.ObjectType):
    all_movie = graphene.List(MovieType)
    all_watch = graphene.List(WatchType)
    recommended = graphene.List(RecommendType)

    movie = graphene.Field(MovieType,
                           id=graphene.Int(),
                           name=graphene.String())

    def resolve_all_movie(self, info):
        return MovieList.objects.all()

    def resolve_all_watch(self, info):
        return WatchList.objects.all()

    def resolve_recommended(self, info):
        return RecommendList.objects.all()

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return MovieList.objects.get(pk=id)

        if name is not None:
            return MovieList.objects.get(name=name)

        return None


schema = graphene.Schema(query=Query, mutation=Mutation)

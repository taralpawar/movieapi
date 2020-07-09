
from django.urls import path, include
from . import views
from rest_framework import routers
from graphene_django.views import GraphQLView

router = routers.DefaultRouter()
router.register('movie', views.movieView)


urlpatterns = [

    path('', include(router.urls)),
    path('graphql', GraphQLView.as_view(graphiql=True)),

]

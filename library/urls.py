from django.urls import path
from . import views

app_name='library'

urlpatterns=[
    path("start/",views.start,name="start"),
    path("biblio_end/",views.biblio_end,name="biblio_end"),
    path("programmation/",views.programmation,name="programmation"),
    path("fav/",views.fav,name="fav"),
    path("bd/",views.bd,name="bd"),
    path("litterature/",views.litterature,name="litterature"),
    path("histo/",views.histo,name="histo"),
    path("items/",views.items,name="items"),
    


]
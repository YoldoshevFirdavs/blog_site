from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Postlar ro'yxati (Senior uslubida, PublishedManager orqali)
    path('', views.PostListView.as_view(), name='post_list'),

    # Postning batafsil sahifasi (Siz yuborgan argumentlar: year, month, day, slug)
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]
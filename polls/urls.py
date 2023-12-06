

from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('polls/', views.indexView.as_view, name='index'),
    path('polls/<int:pk>', views.detailView.as_view, name='detail'),
    path('polls/<int:pk>/results/', views.resultsView.as_view, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote')
]
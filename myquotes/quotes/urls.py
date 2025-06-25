from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuoteListView.as_view(), name='quote-list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('add-author/', views.AddAuthorView.as_view(), name='add-author'),
    path('add-quote/', views.AddQuoteView.as_view(), name='add-quote'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('tags/<str:tag_name>/', views.TagQuotesView.as_view(), name='tag-quotes'),

    path('scrape/', views.scrape_quotes, name='scrape-quotes'),
]

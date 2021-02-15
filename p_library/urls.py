
from django.conf.urls import url
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendAdd, FriendList
from django.urls import path, include



app_name = 'p_library'
urlpatterns =([
    url('authors', AuthorList.as_view(), name='author_list'),
    url('author/create', AuthorEdit.as_view(), name='author_create'),
    url('author/create_many', author_create_many, name='author_create_many'),
    url('author_book/create_many', books_authors_create_many, name='books_authors_create_many'),
    url('friend_add', FriendAdd.as_view(), name='friend_add'),
    url('friend_list', FriendList.as_view(), name='friend_list'),
], 'p_library')


urlpattern = [
    path('p_library', include(urlpatterns)),
]
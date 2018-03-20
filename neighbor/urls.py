from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^user/',views.edit_user, name='edit_user'),
    url(r'^search/', views.search_results, name='search_results'),
    url('^post/', views.post, name='post'),
    url('^neighbor/', views.hood, name='hood'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
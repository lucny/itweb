from django.http import HttpResponse
from .models import Album

def index(request):
    html = ''
    all_albums = Album.objects.all()
    html += '<h1>Hudba - seznam alb</h1>'
    html += '<ul>'
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<li><a href="'+url+'">'+ album.album_title +'</a></li>'
    html += '</ul>'
    return HttpResponse(html)

def detail(request, album_id):
    html = ''
    album = Album.objects.get(id=album_id)
    html += '<h1>Hudba - detail o albu</h1>'
    html += '<h2>' + album.album_title + '</h2>'
    html += '<p>Umelec: ' + album.artist + '</p>'
    html += '<p>Zanr: ' + album.genre + '</p>'
    return HttpResponse(html)
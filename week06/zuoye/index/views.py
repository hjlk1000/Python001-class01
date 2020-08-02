from django.shortcuts import render

from .models import DoubanMovie
from django.db.models import Avg

def movie_short(request):

    shorts = DoubanMovie.objects.all()
  
    counter = DoubanMovie.objects.all().count()

    star_avg =f" {DoubanMovie.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "

    sent_avg =f" {DoubanMovie.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

 
    queryset = DoubanMovie.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

   
    queryset = DoubanMovie.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()


    return render(request, 'result.html', locals())
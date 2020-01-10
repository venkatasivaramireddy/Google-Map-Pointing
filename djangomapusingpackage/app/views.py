from django.shortcuts import render
import gmplot
from django.views.generic import View
from .models import Location

def mapfuntion(request):

    latitude_list = [17.4812117, 16.5272965, 30.3358376, 19.0825223, 26.0967744, 21.0697658, 50.8549217, 17.3046561,64.6324257]

    longitude_list = [78.3958014, 79.598838, 77.8701919, 72.7410978, 8.2997664, 95.3386452, -130.2094884, 79.9981395,17.0843063]


    gmap4 = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 2)

    gmap4.heatmap(latitude_list, longitude_list)
    gmap4.draw("templates/one.html")
    return render(request,"one.html")

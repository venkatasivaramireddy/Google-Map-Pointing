from django.shortcuts import render
import gmplot
from django.views.generic import View
from .models import Location

def mapfuntion(request):

    l1=[]
    l2=[]
    data=Location.objects.all()
    data1=data.values()
    for x in data1:
        for y,z in x.items():
            if y=='latitude':
                l1.append(float(z))
            elif y=='longitude':
                l2.append(float(z))
    gmap = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 2)
    gmap.heatmap(l1, l2)
    gmap.draw("templates/one.html")
    return render(request,"one.html")


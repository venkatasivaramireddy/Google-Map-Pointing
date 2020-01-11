from django.shortcuts import render
import gmplot
from django.views.generic import View
from .models import Location

def mapfuntion(request):

    # latitude_list = [17.4812117, 16.5272965, 30.3358376, 19.0825223, 26.0967744, 21.0697658, 50.8549217, 17.3046561,64.6324257]
    #
    # longitude_list = [78.3958014, 79.598838, 77.8701919, 72.7410978, 8.2997664, 95.3386452, -130.2094884, 79.9981395,17.0843063]

    l1=[]
    l2=[]
    data=Location.objects.all()
    data1=data.values()
    # print(data1)
    for x in data1:
        # print(x)
        for y,z in x.items():
            if y=='latitude':
                l1.append(float(z))
            elif y=='longitude':
                l2.append(float(z))

    # print(l1)
    # print(l2)

    gmap4 = gmplot.GoogleMapPlotter(30.3164945, 78.03219179999999, 2)

    gmap4.heatmap(l1, l2)
    gmap4.draw("templates/one.html")
    return render(request,"one.html")

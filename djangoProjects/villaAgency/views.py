from django.shortcuts import render
from.models import Destination


# Create your views here.
def index(request):

    '''
    dest1 = Destination()
    dest1.name = "Oxygen towers Block 1"
    dest1.bedrooms = "50"
    dest1.bathrooms = "49"
    dest1.area = "48"
    dest1.floor = "47"
    dest1.parking = "46"
    dest1.price = "90000"
    dest1.img = "property-01.jpg"
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "Oxygen towers Block 2"
    dest2.bedrooms = "45"
    dest2.bathrooms = "44"
    dest2.area = "43"
    dest2.floor = "42"
    dest2.parking = "41"
    dest2.price = "80000"
    dest2.img = "property-02.jpg"
    dest2.offer = False

    dest3 = Destination()
    dest3.name = "Oxygen towers Block 3"
    dest3.bedrooms = "40"
    dest3.bathrooms = "39"
    dest3.area = "38"
    dest3.floor = "37"
    dest3.parking = "36"
    dest3.price = "70000"
    dest3.img = "property-03.jpg"
    dest3.offer = False

    dest4 = Destination()
    dest4.name = "Oxygen towers Block 4"
    dest4.bedrooms = "35"
    dest4.bathrooms = "34"
    dest4.area = "33"
    dest4.floor = "32"
    dest4.parking = "31"
    dest4.price = "60000"
    dest4.img = "property-04.jpg"
    dest4.offer = True

    dest5 = Destination()
    dest5.name = "Oxygen towers Block 5"
    dest5.bedrooms = "30"
    dest5.bathrooms = "29"
    dest5.area = "28"
    dest5.floor = "27"
    dest5.parking = "26"
    dest5.price = "50000"
    dest5.img = "property-05.jpg"
    dest5.offer = False

    dest6 = Destination()
    dest6.name = "Oxygen towers Block 6"
    dest6.bedrooms = "25"
    dest6.bathrooms = "24"
    dest6.area = "23"
    dest6.floor = "22"
    dest6.parking = "21"
    dest6.price = "40000"
    dest6.img = "property-06.jpg"
    dest6.offer = False

    dests = [dest1, dest2, dest3, dest4, dest5, dest6] 
    '''
    dests = Destination.objects.all()
    return render(request, "index.html",{'dests': dests})

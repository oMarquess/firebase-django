from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import pyrebase

# Create your views here.

config = {
    "apiKey": "AIzaSyCvXpSF5rOIisgRG2B56E5MNssG4SJwR7o",
    "authDomain": "django-firebase-ce884.firebaseapp.com",
    "databaseURL": "https://django-firebase-ce884-default-rtdb.firebaseio.com",
    "projectId": "django-firebase-ce884",
    "storageBucket": "django-firebase-ce884.appspot.com",
    "messagingSenderId": "1060558224691",
    "appId": "1:1060558224691:web:cbd1a91757c9eb84301246",
    "measurementId": "G-Y84XS7NW3D"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
def index(request):
    name = database.child('Data').child('Name').get().val()
    age = database.child('Age').child('Age').get().val()
    return render (request, 'index.html',
    {"name": name,
    "age":age })

@csrf_exempt
def input_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')

        # Write data to Firebase
        database.child("Users").child(name).set({"Name": name, "Age": age})

        return redirect('index')  # Redirect to your index view or another success page

    return render(request, 'input_data.html')
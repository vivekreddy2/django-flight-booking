from django.shortcuts import render,HttpResponse
import pyrebase
# Create your views here.
config = {
    'apiKey': "AIzaSyA520VBeHVrhEF1hpJ13S2D1ZD94TlyNOE",
    "authDomain": "software-engineering-6e9a7.firebaseapp.com",
    'databaseURL': "https://software-engineering-6e9a7.firebaseio.com",
    'projectId': "software-engineering-6e9a7",
    'storageBucket': "software-engineering-6e9a7.appspot.com",
    'messagingSenderId': "329135496498"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
def home(request):
    return render(request,'seatbooking/login.html')
def pos(request):
    email = request.POST.get("email")
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
            message="invalid info"
            return render(request,'seatbooking/login.html',{"messg":message})
    print(user['localId'])
    session_id=user['localId']
    request.session['uid'] = str(session_id)
    return render(request,'seatbooking/welcome.html',{"e":email})

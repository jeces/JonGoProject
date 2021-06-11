from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Create your views here.


def index(request):
    dir = db.reference()  # 기본위치 지정
    datae_1 = db.reference().child()
    return render(request, 'jongGoApp/index.html')


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

##

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('jonggo-bc5df-firebase-adminsdk-zycb9-c5d6bcdd14')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'firebase-adminsdk-zycb9@jonggo-bc5df.iam.gserviceaccount.com'
})

dir = db.reference()    # 기본위치 지정
dir.update({'자동차':'기아'})

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jongGoWebs.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# Python 3+ 
    # Install
    
     * python -m pip install -r requirements.txt     
     * python manage.py  collectstatic --no-input
     
     * python manage.py makemigrations
     * python manage.py migrate
     
    # Run Server
     * python manage.py runserver
    
    # Celery
    celery -A test_project beat -l debug &
    celery -A test_project worker -n worker -l debug &
    
![Alt text](img/url_monitor.png?raw=true "S3FM")

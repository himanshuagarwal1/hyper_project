

## Running with Docker

- Make sure you have `docker` and `docker-compose` installed and that the Docker daemon is running
- Build `docker-compose build`
- Run the container: `docker-compose up`
- Start making some requests at API endpoints:-
 
  `http://localhost:8000/api/cluster/`
  `http://localhost:8000/api/auth/`
  `http://localhost:8000/api/deployment/`
    
    
    
    



## Project Structure Notes



Project structure:
project/
├── hyeper_project/
│   ├── __init__.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── auth_app/            
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── tests.py    
|
├── cluster_app/           # App for managing clusters and resources
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── tests.py 
|
├── deploy_app/        # App for deployment scheduling and queues
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   
|
├── manage.py
└── requirements.txt

### Django REST Test

This project is a simple Django application that serves a HTML page with an AJAX request and a Django REST Framework API endpoint.

#### Setup

To set up the project, run the following command:


chmod +x setup.sh ; ./setup.sh


This will set up the project using Docker and also generate fake data from docker-entrypoint.sh.
#### Endpoints

The project has two endpoints:

1. HTML page with AJAX: `http://localhost:8000/posts/`
2. Django REST Framework: `http://localhost:8000/api/posts/` 

The `posts` endpoint returns a list of posts in JSON format.

#### Technologies Used

The project uses the following technologies:

- Django: a Python web framework
- Django REST Framework: a toolkit for building RESTful APIs in Django
- Docker: a containerization platform
- AJAX for retrieval on a per-page basis without page flickering.

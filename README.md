# Celery Integration with Django

Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task a client puts a message on the queue, the broker then delivers the message to a worker.

A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.5+

* Virtual Environment

* RabbitMQ

To install virtual environment on your system use:

apt-get install python3-venv

## Installation and Running :

```bash
git clone https://github.com/ongraphpythondev/django_celery.git

cd django_celery

python3 -m venv venv

source venv/bin/activate

# install required packages for the project to run
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Open Browser and Type http://127.0.0.1:8000


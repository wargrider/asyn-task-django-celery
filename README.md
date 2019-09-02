# Celery Integration with Django

Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task a client puts a message on the queue, the broker then delivers the message to a worker.

A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+

* Virtual Environment

To install virtual environment on your system use:
```bash
apt-get install python3-venv
```
* RabbitMQ

To install and run RabbitMQ in Ubuntu environment
```bash
# Installing RabbitMQ
apt-get install -y erlang
apt-get install rabbitmq-server

# Enabling and starting RabbitMQ Service
systemctl enable rabbitmq-server
systemctl start rabbitmq-server
```
## Installation and Running :

```bash
git clone https://github.com/ongraphpythondev/django_celery.git

cd django_celery

python3 -m venv venv

source venv/bin/activate

# Install required packages for the project to run
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

# Run Celery worker to work in background
celery -A django_celery worker -l info

```

Open Browser and Type http://127.0.0.1:8000

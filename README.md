# Social API

Yet another social media app

### Setup

```bash
python3 -m virtualenv venv # Or other ways to create a virtual environment
source venv/bin/activate # Activate virtual environment
pip install -r requirements.txt

python manage.py runserver  # Start server
pytest -v  # Run tests

```

### Notes 

- Using `sqlite` as database. Switch to `postgres` if you want to Dockerize.
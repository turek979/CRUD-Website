cd server

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000

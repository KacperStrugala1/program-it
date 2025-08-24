App is still in early building phase, if you want to add some code:

1. Clone repo
```bash
 git clone https://github.com/KacperStrugala1/program-it.git
 ```
2. Install virtual evn
```bash
python -m venv venv
```
3. Install requirements.txt
```bash
 pip install -r requirements.txt
 ```
4. Make migrations
```bash
python programit/manage.py makemigrations
python programit/manage.py migrate
```
5. Run server locally
```bash
python programit/manage.py runserver
```

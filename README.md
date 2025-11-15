# Program-It

Program-It is a web application designed to help new devs and advanced programmers work on their projects (program it), by improving productivity, tracking work sessions, and backlog to track your progress.
It provides tools for time tracking, focus management, and performance comparison in a simple, web-based interface.

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/a6c4fc0b-519c-41f1-ab4b-b5789ee5e8fd" />


<img width="1986" height="1158" alt="image" src="https://github.com/user-attachments/assets/000ca33f-37f9-459b-bd07-5da5e77a02a9" />


## This project is currently in an early development stage. Contributions and feedback are welcome.

---

## Features

- Work time tracking and session logging  
- Backlog to follow your tasks
- User authentication and personalized dashboards  
- Modular Django architecture for easy feature expansion  

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Python (Django), Celery |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |

---

## Installation and Setup

Follow the steps below to run the application locally.

1. Clone repo
```bash
 git clone https://github.com/KacperStrugala1/program-it.git
 ```
2. Install virtual evn
```bash
python -m venv venv
```
3. Install uv 
```bash
 pip install uv
 ```
4. Sync uv to download all required libraries
```bash
 uv sync
 ```

If you are using Windows install WSL to use Redis.

5. Run server locally
```bash
python programit/manage.py runserver
```
6. Run celery worker (in additional terminal)
```bash
cd programit/
celery -A core worker -l INFO
```
If you have issues with starting celery(due to redis problems) library use that commands:
```bash
 sudo service redis-server start
 sudo apt-get install redis-server
 ```
7. Run celery beat (in additional terminal)
```bash
cd programit/
celery -A core beat 
```


# Program-It

Program-It is a web application designed to help new devs and advanced programmers work on their projects (program it), by improving productivity, tracking work sessions, and staying motivated through data-driven insights and leaderboards.
It provides tools for time tracking, focus management, and performance comparison in a simple, web-based interface.

<img width="1958" height="1056" alt="image" src="https://github.com/user-attachments/assets/90cd88b5-66c0-48b8-8b3f-459edc833d4e" />

<img width="1986" height="1158" alt="image" src="https://github.com/user-attachments/assets/000ca33f-37f9-459b-bd07-5da5e77a02a9" />


This project is currently in an early development stage. Contributions and feedback are welcome.

---

## Features

- Work time tracking and session logging  
- Productivity statistics and focus analysis  
- Leaderboards for motivation and comparison  
- User authentication and personalized dashboards  
- Modular Django architecture for easy feature expansion  

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Python (Django) |
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

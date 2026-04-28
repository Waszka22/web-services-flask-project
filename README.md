
# Web Services and Applications

---
## Project Description

This project is a Flask-based web application that demonstrates a RESTful API with CRUD operations and a web interface using AJAX.

The application allows users to create, view, update, and delete employee records stored in a SQLite database.

This repository contains the submission for the **Web Services and Applications** module, part of the **Higher Diploma in Science in Computing in Data Analytics at ATU**.

---
## Features

- Full **CRUD operations** for employees
- RESTful API design
- Dynamic data loading using **AJAX**
- SQLite database integration
- Simple and responsive UI

---

## Technologies Used

- **Python (Flask)**
- **SQLite (Database)**
- **HTML5**
- **CSS3**
- **JavaScript (Fetch API / AJAX)**

---

## API Endpoints

### Employees

- `GET /api/employees` - Get all employees  
- `GET /api/employees/<id>` - Get specific employee  
- `POST /api/employees` - Add new employee  
- `PUT /api/employees/<id>` - Update employee  
- `DELETE /api/employees/<id>` - Delete employee  

### Shifts

- `GET /api/shifts` - Get all shifts  
- `POST /api/shifts` - Add new shift  

---

## Project Structure


```text
app/
│
├── app.py               # Main Flask application
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
├── .gitignore           # Ignored files
│
├── static/
│   └── style.css        # Styling
│
└── templates/
    ├── index.html        # Main web page
    ├── employees.html    # Employee list view
    ├── add_employee.html # Add employee form
    └── shifts.html       # Shifts view      

```
---

## Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

`git clone https://github.com/Waszka22/web-services-flask-project.git`

`cd web-services-flask-project`

### 2. Install dependencies

`pip install -r requirements.txt`

### 3. Run the application

`python app.py`

### 4. Open in browser    

`http://127.0.0.1:5000/`



## References

- DAO Pattern Example: [GitHub Repository](https://github.com/andrewbeattycourseware/wsaa-courseware/blob/main/code/Topic08-generated-client/bookDAO.py)
- Flask Documentation: [Flask Docs](https://flask.palletsprojects.com/)
- Flask-Login: [PyPI Flask-Login](https://pypi.org/project/Flask-Login/)
- Python Flask Flashing: [PythonGeeks](https://pythongeeks.org/learn-python-tutorial/)
- W3Schools Tutorials: [W3Schools](https://www.w3schools.com/)
- SQLAlchemy Documentation: [SQLAlchemy Docs](https://docs.sqlalchemy.org/)

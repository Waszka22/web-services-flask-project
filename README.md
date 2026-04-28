
# Web Services and Applications

---
## Project Description

This project is a Flask web application that demonstrates a RESTful API with CRUD operations and a web interface using AJAX.

The application allows users to create, view, update, and delete employee records stored in a SQLite database.

This repository contains the submission for the **Web Services and Applications** module, part of the **Higher Diploma in Science in Computing in Data Analytics at ATU**.

---
## Features

- Full CRUD operations for employees
- RESTful API design
- Dynamic data loading using AJAX
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
├── app.py               
├── employees.db          
├── requirements.txt    
├── README.md              
├── .gitignore            
│
├── static/
│   └── style.css         
│
└── templates/
    ├── index.html        
    ├── employees.html     
    ├── add_employee.html 
    └── shifts.html        

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
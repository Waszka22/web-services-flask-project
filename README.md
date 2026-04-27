
# Web Services and Applications

## Project Description

This project is a Flask web application that demonstrates a RESTful API with CRUD operations and a web interface using AJAX.

The application allows users to create, view, update, and delete employee records stored in a SQLite database.

This repository contains the submission for the **Web Services and Applications** module, part of the **Higher Diploma in Science in Computing in Data Analytics at ATU**.


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


## Project Structure

```text
APP/
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



    
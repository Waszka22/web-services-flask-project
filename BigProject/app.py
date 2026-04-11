
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# database config
base_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(base_dir, "employees.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_file}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    position = db.Column(db.String(100))
    department = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(120))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "position": self.position,
            "department": self.department,
            "phone": self.phone,
            "email": self.email
        }


# pages
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_page():
    return render_template("add_employee.html")


@app.route("/employees")
def employees_page():
    return render_template("employees.html")


# API - GET all
@app.route("/api/employees", methods=["GET"])
def get_employees():
    employees = Employee.query.all()
    result = []

    for employee in employees:
        result.append(employee.to_dict())

    return jsonify(result)


# API - GET one
@app.route("/api/employees/<int:id>", methods=["GET"])
def get_one_employee(id):
    employee = Employee.query.get(id)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(employee.to_dict())


# API - POST
@app.route("/api/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No JSON data sent"}), 400

    new_employee = Employee(
        first_name=data["first_name"],
        last_name=data["last_name"],
        position=data["position"],
        department=data["department"],
        phone=data["phone"],
        email=data["email"]
    )

    db.session.add(new_employee)
    db.session.commit()

    return jsonify(new_employee.to_dict()), 201


# API - PUT
@app.route("/api/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    employee = Employee.query.get(id)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()

    if data is None:
        return jsonify({"error": "No JSON data sent"}), 400

    employee.first_name = data.get("first_name", employee.first_name)
    employee.last_name = data.get("last_name", employee.last_name)
    employee.position = data.get("position", employee.position)
    employee.department = data.get("department", employee.department)
    employee.phone = data.get("phone", employee.phone)
    employee.email = data.get("email", employee.email)

    db.session.commit()

    return jsonify(employee.to_dict())


# API - DELETE
@app.route("/api/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    employee = Employee.query.get(id)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    db.session.delete(employee)
    db.session.commit()

    return jsonify({"message": "Employee deleted"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

from flask import Blueprint, request, jsonify
from backend import db
from backend.models import Application

app_bp = Blueprint("applications", __name__, url_prefix="/applications")

@app_bp.route("/", methods=["GET"])
def get_applications():
    applications = Application.query.all()
    return jsonify([
        {"id": app.id, "name": app.name, "threat_scenarios": app.threat_scenarios, "security_test_cases": app.security_test_cases}
        for app in applications
    ])

@app_bp.route("/", methods=["POST"])
def create_application():
    data = request.get_json()
    new_app = Application(name=data["name"])
    db.session.add(new_app)
    db.session.commit()
    return jsonify({"message": "Application created successfully"}), 201

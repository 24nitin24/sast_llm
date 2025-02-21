from flask import Blueprint, request, jsonify
from backend import db
from backend.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/", methods=["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email, "role": user.role} for user in users])

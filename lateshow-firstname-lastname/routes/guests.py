from flask import Blueprint, jsonify
from models import Guest

guests_bp = Blueprint('guests', __name__, url_prefix='/guests')

@guests_bp.route('', methods=['GET'])
def get_guests():
    return jsonify([g.to_dict() for g in Guest.query.all()])

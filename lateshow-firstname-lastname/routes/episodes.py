from flask import Blueprint, jsonify
from models import Episode

episodes_bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@episodes_bp.route('', methods=['GET'])
def get_episodes():
    return jsonify([e.to_dict() for e in Episode.query.all()])

@episodes_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    e = Episode.query.get(id)
    if not e:
        return jsonify({"error": "Episode not found"}), 404
    data = e.to_dict()
    data['appearances'] = [{**a.to_dict(), "guest": a.guest.to_dict()} for a in e.appearances]
    return jsonify(data)
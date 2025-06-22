from flask import Blueprint, jsonify, request
from models import Appearance, Episode, Guest, db

appearances_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearances_bp.route('', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

    return jsonify({
        "id": appearance.id,
        "rating": appearance.rating,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id,
        "episode": appearance.episode.to_dict(),
        "guest": appearance.guest.to_dict()
    }), 201
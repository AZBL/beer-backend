from models import User
from flask import request, jsonify, Blueprint
from helpers import token_required
from models import db, Beer, beer_schema, beers_schema

api = Blueprint('api', __name__, url_prefix='/api')


# post a new beer
@api.route('/add-beer', methods=['POST'])
@token_required
def add_beer(user_id):
    data = request.get_json()

    if 'brewery' not in data or 'name' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    brewery = data.get('brewery', None)
    name = data.get('name', None)
    abv = data.get('abv', None)
    style = data.get('style', None)
    comments = data.get('comments', None)
    rating = data.get('rating', None)

    new_beer = Beer(brewery=brewery, name=name, abv=abv,
                    style=style, comments=comments, rating=rating, user_id=user_id)
    db.session.add(new_beer)
    db.session.commit()

    response = beer_schema.dump(new_beer)
    return jsonify(response), 201


# get all beers
@api.route('/beers', methods=['GET'])
@token_required
def get_all_beers(user_id):
    beers = Beer.query.filter_by(user_id=user_id).all()
    if not beers:
        return jsonify([]), 200
    response = beers_schema.dump(beers)
    return jsonify(response)


# get a single beer
@api.route('/beer/<int:id>', methods=['GET'])
@token_required
def get_beer(user_id, id):
    beer = Beer.query.get(id)
    if not beer:
        return jsonify({'message': 'No beer found'}), 404
    if beer.user_id != user_id:
        return jsonify({'message': 'Permission denied'}), 403
    response = beer_schema.dump(beer)
    return jsonify(response)


# update a beer
@api.route('/beer/<int:id>', methods=['PUT'])
@token_required
def update_beer(user_id, id):
    beer = Beer.query.get(id)

    if not beer:
        return jsonify({'message': 'No beer found'}), 404
    if beer.user_id != user_id:
        return jsonify({'message': 'Permission denied'}), 403

    data = request.get_json()

    if 'brewery' in data:
        beer.brewery = data['brewery']
    if 'name' in data:
        beer.name = data['name']
    if 'abv' in data:
        beer.abv = data['abv']
    if 'style' in data:
        beer.style = data['style']
    if 'comments' in data:
        beer.comments = data['comments']
    if 'rating' in data:
        beer.rating = data['rating']

    db.session.commit()
    response = beer_schema.dump(beer)
    return jsonify(response)


# delete beer
@api.route('/beer/<int:id>', methods=['DELETE'])
@token_required
def delete_beer(user_id, id):
    beer = Beer.query.get(id)

    if not beer:
        return jsonify({'message': 'No beer found'}), 404
    if beer.user_id != user_id:
        return jsonify({'message': 'Permission denied'}), 403

    db.session.delete(beer)
    db.session.commit()

    return jsonify({'message': 'Beer deleted'}), 200

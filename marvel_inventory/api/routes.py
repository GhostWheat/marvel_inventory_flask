from flask import Blueprint, request, jsonify
from marvel_inventory.helpers import token_required
from marvel_inventory.models import db, Hero, hero_schema, allheroes_schema

api = Blueprint('api',__name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(our_user):
    return {'some':'value'}

#create Hero Endpoint
@api.route('/heroes', methods = ['POST'])
@token_required
def create_hero(our_user):
    id = request.json['id']
    hero_name = request.json['hero_name']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    date_created = 0
    user_token = our_user.token
    customer_id = request.json['customer_id'] #IS THIS THE SAME THING AS USER_TOKEN??

    print(f"User Token: {our_user.token}")

    hero = Hero(id, hero_name, description, comics_appeared_in, super_power, date_created, user_token, customer_id)

    db.session.add(hero)
    db.session.commit()

    response = hero_schema.dump(hero)

    return jsonify(response)

#retrieve(READ) all heroes
@api.route('/heroes', methods = ['GET'])
@token_required
def get_allheroes(our_user):
    owner = our_user.token
    heroes = Hero.query.filter_by(user_token = owner).all()
    response = allheroes_schema.dump(heroes)

    return jsonify(response)


#retrieve (READ) only one hero
@api.route('/heroes', methods = ['GET'])
@token_required
def get_hero(our_user, id):
    if id:
        hero = Hero.query.get(id)
        response = hero_schema.dump(hero)
        return jsonify(response)
    else:
        return jsonify({'message':'Valid ID Required'}), 401


#UPDATE hero by id
@api.route('/heroes/<id>', methods = ['PUT'])
@token_required
def update_hero(our_user, id):
    hero = Hero.query.get(id)
    hero.id = request.json['id']
    hero.hero_name = request.json['hero_name']
    hero.description = request.json['description']
    hero.comics_appeared_in = request.json['comics_appeared_in']
    hero.super_power = request.json['super_power']
    hero.date_created = 0
    hero.user_token = our_user.token
    hero.customer_id = request.json['customer_id'] #IS THIS THE SAME THING AS USER_TOKEN??

    db.session.commit()

    response = hero_schema.dump(hero)

    return jsonify(response)


#DELETE hero by ID
@api.route('/heroes/<id>', methods = ['DELETE'])
@token_required
def delete_hero(our_user, id):
    hero = Hero.query.get(id)
    db.session.delete(hero)
    db.session.commit()

    response = hero_schema.dump(hero)
    return jsonify(response)
    



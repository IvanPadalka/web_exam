from datetime import datetime

from flask import request, jsonify

from app import app, db
from .models import Car


@app.route('/songs/<int:car_id>', methods=['GET'])
@app.route('/songs', methods=['GET'])
def get_cars(car_id=None):
    if car_id:
        car = Car.query.filter_by(id=car_id).first()
        if not car:
            return jsonify({"details": "Not found"})
        result = {'id': car.id,
                  'Name:': car.license_plate,
                  'Autors:': car.brand,
                  'Type of the music:': car.on_go,
                  'Duration:': car.price,
                  'Description' : car.description,
                  'Link': car.link,
                  'Creation date:': car.prod_date
                  }
        return jsonify(result)
    else:
        cars = Car.query.all()
        result = []
        for car in cars:
            result.append({'id': car.id,
                          'Name:': car.license_plate,
                          'Autors:': car.brand,
                          'Type of the music:': car.on_go,
                          'Duration:': car.price,
                          'Description' : car.description,
                          'Link': car.link,
                          'Creation date:': car.prod_date
                           })
        return jsonify(result)


@app.route('/songs/<int:car_id>', methods=['PUT'])
def edit_car(car_id):
    car = Car.query.filter_by(id=car_id).first()
    if not car:
        return jsonify({'details': 'Not found'})
    post_data = request.json
    car.license_plate = post_data['Name']
    car.brand = post_data['Autors']
    car.on_go = post_data['Type of the music']
    car.price = post_data['Duration']
    car.description = post_data['Description']
    car.link = post_data['Link']
    car.prod_date = datetime.utcnow()
    db.session.commit()
    return jsonify({'details': 'Success'})




@app.route('/songs', methods=['POST'])
def create_car():
    post_data = request.json
    car = Car(license_plate=post_data['Name'],
              brand=post_data['Autors'],
              on_go=post_data['Type of the music'],
              price=post_data['Duration'],
              description=post_data['Description'],
              link=post_data['Link'],
              prod_date=datetime.utcnow())
    db.session.add(car)
    db.session.commit()
    return jsonify({'details': 'Success'})

@app.route('/songs/<int:car_id>', methods=["GET", "DELETE"])
def delete_car(car_id):
    car = Car.query.filter_by(id=car_id).first()
    if not car:
        return jsonify({'detail': 'Not found'})
    else:
        db.session.delete(car)
        db.session.commit()
        return jsonify({'details': 'Success'})

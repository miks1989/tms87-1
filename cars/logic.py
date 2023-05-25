from cars.models import Brand, Car, session


def create_brand(name):
    brand = Brand(name)
    session.add(brand)
    session.commit()


def create_car(data: dict):
    brand = session.query(Brand).filter_by(id=data['id']).first()
    print(brand.id, brand.name)
    car = Car(data['model'], data['release_year'], brand)
    session.add(car)
    session.commit()


def read_brand():
    return session.query(Brand).all()


def read_car():
    return session.query(Car, Brand).\
        join(Brand, Car.brand_id == Brand.id).all()


def update_brand(id, new_name):
    brand = session.query(Brand).filter_by(id=id).first()
    brand.name = new_name
    session.commit()


def update_car(id, data: dict):
    car = session.query(Car).filter_by(id=id).first()
    brand = session.query(Brand).filter_by(id=data['id']).first()
    car.model = data['model']
    car.release_year = data['release_year']
    car.brand = brand
    session.commit()


def delete_car(id):
    session.query(Car).filter_by(id=id).delete()
    session.commit()


def delete_brand(id):
    cars = session.query(Car).\
        join(Brand, Car.brand_id == Brand.id).filter(Brand.id == id)
    [session.delete(car) for car in cars]
    session.query(Brand).filter_by(id=id).delete()
    session.commit()

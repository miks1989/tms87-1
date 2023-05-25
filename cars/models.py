# Создать ветку cars от master. Создать пакет cars.
# Создать таблицы Brand(name), Car(model, release_year,
# brand(foreing key на таблицу Brand)). Реализовать CRUD
# (создание, чтение, обновление по id, удаление по id)
# для бренда и машины. Создать пользовательский интерфейс.
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy_utils import create_database, database_exists

e = create_engine('postgresql://postgres:postgres@localhost/cars', echo=True)

if not database_exists((e.url)):
    create_database(e.url)

Base = declarative_base()


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(Integer,
                      ForeignKey('brand.id'),
                      nullable=False
                      )
    brand = relationship('Brand',
                         foreign_keys='Car.brand_id',
                         backref='cars'
                         )

    def __init__(self, model, release_year, brand):
        self.model = model
        self.release_year = release_year
        self.brand = brand


Base.metadata.create_all(e)
session = sessionmaker(bind=e)()
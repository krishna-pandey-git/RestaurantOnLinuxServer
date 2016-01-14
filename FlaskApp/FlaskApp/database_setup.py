import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
################### Declaring Classes ###########
class User(Base):
        __tablename__='user'
        id = Column(
                Integer, primary_key = True)
        name = Column(
                String(80), nullable = False)
        email = Column(String(80),
                       nullable = False)
        picture = Column(
                String, nullable = True)

class Restaurant(Base):
	__tablename__ ='restaurant'
	id = Column(
		Integer, primary_key = True)
	name = Column(
		String(80),nullable = False)
	user_id = Column(
                Integer, ForeignKey('user.id'))
	user = relationship(User)
        menuitems = relationship("MenuItem", single_parent=True ,cascade='delete, delete-orphan')
	
	@property
        def serialize(self):
        #return object data in easily serializable format
                return {
                'name': self.name,
                'id': self.id
                }


class MenuItem(Base):
	__tablename__ = 'menu_item'
	name = Column(
		String(80),nullable=False)
	id = Column(Integer, primary_key=True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(
		Integer, ForeignKey('restaurant.id'))
	user_id = Column(
                Integer, ForeignKey('user.id'))
	user = relationship(User)
	restaurant = relationship(Restaurant)
	
        @property
        def serialize(self):
        #return object data in easily serializable format
                return {
                'name': self.name,
                'description': self.description,
                'id': self.id,
                'price': self.price,
                'course': self.course
                }

############insert at the end ################

engine = create_engine(
'postgres://catalog:catalog@localhost/catalog')

Base.metadata.create_all(engine)

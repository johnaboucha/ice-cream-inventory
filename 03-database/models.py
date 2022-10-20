from sqlalchemy import Boolean, Integer, String, Column, Float

from database import Base

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, unique=True, index=True)
	hashed_password = Column(String)

class Item(Base):
	__tablename__ = "items"

	id = Column(Integer, primary_key=True, index=True)
	flavor = Column(String, index=True)
	description = Column(String, index=True)
	price = Column(Float, index=True)
	is_vegan = Column(Boolean, index=True)
	quantity = Column(Integer, index=True)

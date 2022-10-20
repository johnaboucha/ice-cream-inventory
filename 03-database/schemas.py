from pydantic import BaseModel

class ItemBase(BaseModel):
	flavor: str
	description: str | None = None
	price: float
	is_vegan: bool
	quantity: int

class Item(ItemBase):
	id: int

	class Config:
		orm_mode = True

class ItemCreate(ItemBase):
	pass

class UserBase(BaseModel):
	username: str

class UserCreate(UserBase):
	password: str

class User(UserBase):
	id: int

	class Config:
		orm_mode = True
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    address = Column(String(200))
    phone_number = Column(String(20))
    first_name = Column(String(100))
    last_name = Column(String(100))

class Manager(Base):
    __tablename__ = 'managers'
    manager_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    phone_number = Column(String(20))

class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    price = Column(DECIMAL(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    category = relationship("Category", back_populates="products")




class Authentication(Base):
    __tablename__ = 'authentication'
    auth_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    manager_id = Column(Integer, ForeignKey('managers.manager_id'))
    is_manager = Column(Boolean, nullable=False)
    token = Column(String(100), nullable=False)

class Cart(Base):
    __tablename__ = 'cart'
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    price = Column(DECIMAL(10, 2), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="cart")

User.cart = relationship("Cart", back_populates="user")
Cart.user = relationship("User", back_populates="cart")
Product.cart = relationship("Cart", uselist=False, back_populates="product")



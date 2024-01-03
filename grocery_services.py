from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from grocery_models import User, Manager, Category, Product, Authentication, Cart


engine = create_engine('sqlite:///grocery_store.db')


Session = sessionmaker(bind=engine)
session = Session()

# CRUD operations for User table

# Create
def create_user(username, email, password, address=None, phone_number=None):
    new_user = User(username=username, email=email, password=password, address=address, phone_number=phone_number)
    session.add(new_user)
    session.commit()

# Read
def get_user_by_id(user_id):
    return session.query(User).filter_by(user_id=user_id).first()

def get_user_by_name(username):
    return session.query(User.user_id,User.username,User.password).filter_by(username=username).first()


def get_users():
    return session.query(User).all()

# Update
def update_user(user_id, new_username, new_email):
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        user.username = new_username
        user.email = new_email
        session.commit()

# Delete
def delete_user(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        session.delete(user)
        session.commit()


# CRUD operations for Manager table

# Create
def create_manager(username, email, password, phone_number=None):
    new_manager = Manager(username=username, email=email, password=password, phone_number=phone_number)
    session.add(new_manager)
    session.commit()

# Read
def get_manager_by_id(manager_id):
    return session.query(Manager).filter_by(manager_id=manager_id).first()

def get_manager_by_name(username):
    return session.query(Manager.manager_id,Manager.username,Manager.password).filter_by(username=username).first()

def get_managers():
    return session.query(Manager).all()

# Update
def update_manager(manager_id, new_username, new_email):
    manager = session.query(Manager).filter_by(manager_id=manager_id).first()
    if manager:
        manager.username = new_username
        manager.email = new_email
        session.commit()

# Delete
def delete_manager(manager_id):
    manager = session.query(Manager).filter_by(manager_id=manager_id).first()
    if manager:
        session.delete(manager)
        session.commit()


# CRUD operations for Category table

# Create
def create_category(name):
    new_category = Category(name=name)
    session.add(new_category)
    session.commit()

# Read
def get_category_by_id(category_id):
    return session.query(Category).filter_by(category_id=category_id).first()

def get_categories():
    return session.query(Category).all()

# Update
def update_category(category_id, new_name):
    category = session.query(Category).filter_by(category_id=category_id).first()
    if category:
        category.name = new_name
        session.commit()

# Delete
def delete_category(category_id):
    category = session.query(Category).filter_by(category_id=category_id).first()
    if category:
        session.delete(category)
        session.commit()


# CRUD operations for Product table

# Create
def create_product(name, description, price, category_id):
    new_product = Product(name=name, description=description, price=price, category_id=category_id)
    session.add(new_product)
    session.commit()

# Read
def get_product_by_id(product_id):
    return session.query(Product).filter_by(product_id=product_id).first()

def get_product_by_name(name):
    return session.query(Product).filter_by(name=name).all()

def get_products():
    return session.query(Product).all()

# Update
def update_product(product_id, new_name, new_description, new_price, new_category_id):
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product:
        product.name = new_name
        product.description = new_description
        product.price = new_price
        product.category_id = new_category_id
        session.commit()

# Delete
def delete_product(product_id):
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product:
        session.delete(product)
        session.commit()


# CRUD operations for Authentication table

# Create
def create_authentication(user_id, manager_id, is_manager, token):
    new_authentication = Authentication(user_id=user_id, manager_id=manager_id, is_manager=is_manager, token=token)
    session.add(new_authentication)
    session.commit()

# Read
def get_authentication_by_id(auth_id):
    return session.query(Authentication).filter_by(auth_id=auth_id).first()

def get_authentications():
    return session.query(Authentication).all()

# Update
def update_authentication(auth_id, new_token):
    authentication = session.query(Authentication).filter_by(auth_id=auth_id).first()
    if authentication:
        authentication.token = new_token
        session.commit()

# Delete
def delete_authentication(auth_id):
    authentication = session.query(Authentication).filter_by(auth_id=auth_id).first()
    if authentication:
        session.delete(authentication)
        session.commit()


#CRUD operations for Cart table


# Create
def add_to_cart(user_id, product_id):
    user = session.query(User).get(user_id)
    product = session.query(Product).get(product_id)
    
    if user and product:
        cart_item = Cart(
            product_id=product.product_id,
            name=product.name,
            description=product.description,
            price=product.price,
            user_id=user.user_id,
            quantity=1
        )
        session.add(cart_item)
        session.commit()

# Read
def get_cart_items(user_id):
    return session.query(Cart).filter_by(user_id=user_id).all()


def is_product_their(product_id):
    return session.query(Cart).filter_by(product_id=product_id).all()


# Update
def update_cart_item(user_id, product_id, new_quantity):
    cart_item = session.query(Cart).filter_by(user_id=user_id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity = new_quantity
        session.commit()

# Delete
def remove_from_cart(user_id, product_id):
    cart_item = session.query(Cart).filter_by(user_id=user_id, product_id=product_id).first()
    if cart_item:
        session.delete(cart_item)
        session.commit()


    

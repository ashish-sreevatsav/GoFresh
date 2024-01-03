from flask import Flask, render_template, request, session, redirect, url_for, g, jsonify
from grocery_services import (get_products, get_user_by_name, get_manager_by_name,
                              get_product_by_name, get_cart_items, add_to_cart, 
                              remove_from_cart, get_categories, create_product, 
                              create_category, is_product_their, update_cart_item,
                              get_user_by_id, delete_product)
import os

UPLOAD_FOLDER = "./templates/img"



app = Flask(__name__,static_folder='./templates/img')
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "12345"  



def is_authenticated_user(username, password):
    user = get_user_by_name(username)
    if user and user[2] == password:
        return True
    return False

def is_authenticated_manager(username, password):
    user = get_manager_by_name(username)
    if user and user[2] == password:
        return True
    return False

@app.route("/", methods = ["GET","POST"])
def login():
    if g.user:
        if g.user < 100 :
            return render_template("index.html",product=get_products())
        elif g.user > 100 :
            return redirect(url_for("mhome"))
    else:
        if request.method == "POST":
            session.pop('user',None)
            username = request.form["username"]
            password = request.form["password"]
            if is_authenticated_user(username,password):
                session['user'] = get_user_by_name(username)[0]
                return redirect(url_for("home"))
            else:
                return render_template("display.html",error="Wrong Credentials")
    return render_template("display.html")    


@app.route("/home", methods=["GET","POST"])
def home():
    if g.user:
        return render_template("index.html",product=get_products())
    return redirect(url_for("login"))


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
        


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/cart")
def cart():
    if "user" in session:
        user_id = session["user"]
        cart = get_cart_items(user_id)
        return render_template("cart.html",cart=cart)
    return redirect(url_for("login"))

@app.route("/add_product", methods=["POST"])
def addProduct():
    if g.user and request.method == "POST":
        file = request.files['file']
        name = request.form.get('name')
        description = request.form.get('description')
        price = float(request.form.get('price'))
        category_id = int(request.form.get('category_id'))
        
        create_product(name,description,price,category_id)
        new_filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{name}.jpg')
        file.save(new_filename)
        message = f"Added '{name} to store'"
        return jsonify({"message":message, "refresh":True})
    return jsonify({"message":"need to login to add"})

@app.route("/delete_product", methods = ["POST"])
def deleteProduct():
    if g.user:
        data = request.json
        id = int(data['id'])
        name = data['name']
        os.remove(f"./templates/img/{name}.jpg")
        delete_product(id)
        message = f"Deleted '{name}' from store"
        return jsonify({"message":message, "refresh":True})
    return jsonify({"message":"neeed to login to performe any activity"})

@app.route("/add_category", methods=["POST"])
def addCategory():
    if g.user and request.method == "POST" :
        name = request.form.get('name')
        create_category(name)
        message = f"Added {name} category to store"
        return jsonify({"message":message, "refresh":True})
    return jsonify({"message":"need to login to add"}) 


@app.route("/searchProduct", methods=["POST"])
def searchProduct():
    if "user" in session and request.method == "POST":
        name = request.form["search"].capitalize()
        return render_template("index.html",product=get_product_by_name(name))
    return redirect(url_for("login"))

@app.route("/manager-login", methods=["GET","POST"])
def manager_login():
    if request.method == "POST":
        session.pop('user',None)
        username = request.form["username"]
        password = request.form["password"]
        if is_authenticated_manager(username,password):
            session['user'] = get_manager_by_name(username)[0]
            return redirect(url_for("mhome"))
        else:
            return render_template("mdisplay.html",error="Wrong Credentials")
    return render_template("mdisplay.html")

@app.route("/mhome")
def mhome():
    if g.user:
        return render_template("mhome.html", category = get_categories(), product=get_products())
    return redirect(url_for("login"))

@app.route("/add_to_cart", methods = ["POST"])
def addtocart():
    if g.user and request.method == "POST":
        data = request.json
        product_id = int(data['id'])
        data2 = is_product_their(product_id)
        if data2:
            qty = data2[0].quantity+1
            update_cart_item(g.user,data2[0].product_id,qty)
            return jsonify({"message":"Updated quntity"})
        else: 
            add_to_cart(g.user,product_id)
            message = f"Added '{data['id']}' to cart"
            return jsonify({"message":message})
    return jsonify({"message":"need to login to add"})

@app.route("/delete_from_cart", methods=["POST"])
def deleteFromCart():
    if g.user and request.method=="POST":
        data = request.json
        product_id = int(data['id'])
        remove_from_cart(g.user, product_id)
        message = f"Deleted '{data['id']}' from cart"
        return jsonify({"message":message, "refresh":True})
    return jsonify({"message":"need to login"})

@app.route("/billing", methods=["GET","POST"])
def billing():
    if g.user:
        return render_template("billing.html", cart = get_cart_items(g.user), user = get_user_by_id(g.user))


@app.route("/increase", methods = ["POST"])
def increase():
    if g.user:
        data = request.json
        product_id = data['id']
        qty = is_product_their(product_id)[0].quantity+1
        update_cart_item(g.user,product_id,qty)
        message = f"Added '{data['id']}'"
        return jsonify({"message":message, "refresh":True})
    return jsonify({"message":"need to login to add"})

@app.route("/decrease", methods = ["POST"])
def decrease():
    if g.user:
        data = request.json
        product_id = data['id']
        qty = is_product_their(product_id)[0].quantity-1
        if qty > 0:
            update_cart_item(g.user,product_id,qty)
        elif qty == 0:
            remove_from_cart(g.user,product_id)
        message = f"deleted '{data['id']}'"
        return jsonify({"message":message, "refresh":True})
    return jsonify({"message":"need to login to add"})


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8080)

from flask import Flask 

app = Flask(__name__) # Create a Flask application instance

# GET http://127.0.0.1:5000/home
@app.route("/home", methods=["GET"]) # Define a route for the home page that accepts GET requests
def home():
    return {"message": "Welcome to Flask cohort#65"}

# GET http://127.0.0.1:5000/cohort-65
@app.route("/cohort-65", methods=["GET"]) # Define a route for the cohort-65 page that accepts GET requests
def get_students():
    students_list = ["Sergio", "Leomar", "Charles", "Aymen","Dejanirra", "Freysy", "Trishon"]
    return students_list


#  ------ Products
products = [
  {
    "_id": 1, 
    "title": "Nintendo Switch", 
    "price": 499.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2, 
    "title": "Smart Refrigerator", 
    "price": 999.99, 
    "category": "Kitchen", 
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3, 
    "title": "Bluetooth Speaker", 
    "price": 79.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/3/300/300"
  },
]

# GET http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"]) # Define a route for the products page that accepts GET requests
def get_products():
    return {"data": products} # Return a JSON response containing the list of products


# ---- Coupons ----

coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50},    
]

# GET http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["GET"]) # Define a route for the products page that accepts GET requests
def get_coupons():
    return {"data": coupons} # Return a JSON response containing the list of products

@app.route("/api/coupons/count", methods=["GET"])
def get_couponsCount():
    return {"count": len(coupons)}

if __name__ == "__main__":
    app.run()
    
# Wehn this file is run directly: __name_== "__main__" will evaluate to True, and the code inside this block will be executed.
# When this file is imported as module: __name__ == "server.py"
# When this script is run directly, it starts the Flask development server.
# The server will listen for incoming requests and route them to the appropriate functions based on the defined routes.
# In this case, when a GET request is made to the "/home" endpoint, the home() function will be called, returning a JSON response with a welcome message.
# Note: In a production environment, you would typically use a more robust server setup and not run the Flask development server directly.py
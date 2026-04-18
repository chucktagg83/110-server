from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


from flask import Flask, jsonify, request # Import the Flask class and jsonify

app = Flask(__name__) # Create a Flask application instance
CORS(app, origins=["http://localhost:5173", "http://myapp.com"]) # Enable CORS for the Flask application

# GET http://127.0.0.1:5000/home
@app.route("/home", methods=["GET"]) # Define a route for the home page that accepts GET requests
def home():
    return {"message": "Welcome to Flask cohort#65"}

# GET http://127.0.0.1:5000/cohort-65
@app.route("/cohort-65", methods=["GET"]) # Define a route for the cohort-65 page that accepts GET requests
def get_students():
    students_list = ["Sergio", "Leomar", "Charles", "Aymen","Dejanirra", "Freysy", "Trishon"]
    return students_list

#------------Path Parameters------------
@app.route("/greet/<string:name>", methods=["GET"]) # Define a route for the greet page that accepts GET requests and includes a path parameter for the name
def say_hi(name): # The function takes the name parameter from the URL and returns a JSON response with a personalized greeting message
    return jsonify({"message": f"Hello {name}"}), 200 # Concatenate the greeting message with the name parameter to create a personalized greeting

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    return jsonify({"this is the user id": user_id}), 200 # Return a JSON response containing the user ID extracted from the URL path parameter
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

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    for product in products:
       if (product["_id"]) == product_id:
           return jsonify({
               "success": True,
               "message": f"Product with id {product_id} found",
               "data": product 
           }), 200 # OK 
    
    return jsonify({
        "success": False,
        "message": f"Proudct with id {product_id} not found",
    }), 404 # Not Found

# POST http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    print(f"new product: {request.get_json()}") # Get the JSON data from the request body and parse it into a Python dictionary  
    new_product = request.get_json() # Store the new product data in a variable
    #new_product["_id"] = len(products) + 1 # Generate a new unique ID for the product by calculating the length of the products list and adding 1
    new_product["uuid"] = str(uuid.uuid4()) # Generate a new unique UUID for the product using the uuid library and convert it to a string
    products.append(new_product) # Add the new product to the products list
    return jsonify({
        "success": True,
        "message": "Product added successfully",
        "data": new_product        
    }), 201 # Created

# PUT http://127.0.0.1:5000/api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["PUT"]) # Define a route for updating a product by its ID that accepts PUT requests and includes a path parameter for the product ID
def update_product_by_id(product_id): # Define a route for updating a product by its ID that accepts PUT requests and includes a path parameter for the product ID
    updated_product = request.get_json() # Get the JSON data from the request body and parse it into a Python dictionary
    print(updated_product) # Get the JSON data from the request body and parse it into a Python dictionary
    for product in products: # Iterate through the products list to find the product with the matching ID
        if product["_id"] == product_id: # Check if the product ID matches the provided product_id
            product["title"] = updated_product["title"] # Update the product's title with the new value from the request body
            product["price"] = updated_product["price"] # Update the product's price with the new value from the request body
            product["category"] = updated_product["category"] # Update the product's category with the new value from the request body
            product["image"] = updated_product["image"] # Update the product's image with the new value from the request body
            return jsonify({
                "success": True,
                "message": f"Product with id {product_id} updated successfully",
                "data": product
            }), 200 # OK, product updated successfully, return the updated product data in the response

    return jsonify({
        "success": False,
        "message": f"Product with id {product_id} not found",
    }), 404 # Not Found, product with the specified ID does not exist in the products list  
    
# PUT http://127.0.0.1:5000/api/coupons/<int:id>
@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"])
def update_coupon_by_id(coupon_id):
    updated_data = request.get_json()
    
    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            # update fields
            coupon["code"] = updated_data.get("code", coupon["code"])
            coupon["discount"] = updated_data.get("discount", coupon["discount"])
            
            return jsonify({
                "success": True,
                "message": f"Coupon with id {coupon_id} updated",
                "data": coupon
            }), 200 # OK
    else:
        return jsonify({
            "success": False,
            "message": f"Coupon with id {coupon_id} not found",
        }), 404 # Not Found
        
    
# DELETE http://127.0.0.1:5000/api/products/
@app.route("/api/products/<int:product_id>", methods=["DELETE"]) # Define a route for deleting a product by its ID that accepts DELETE requests and includes a path parameter for the product ID
def delete_product_by_id(product_id): # Define a route for deleting a product by its ID that accepts DELETE requests and includes a path parameter for the product ID
    for product in products: # Iterate through the products list to find the product with the matching ID
        if product["_id"] == product_id: # Check if the product ID matches the provided product_id
            products.remove(product) # Remove the product from the products list
            return jsonify({
                "success": True,
                "message": f"Product with id {product_id} deleted successfully",
            }), 200 # OK 
            
    return jsonify({
        "success": False, #
        "message": f"Product with id {product_id} not found", #
    }), 404 # Not Found
    
#DELETE http://127.0.0.1:5000/api/coupons/<int:id>
@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])
def delete_coupon_by_id(coupon_id):
    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            coupons.remove(coupon)
            return jsonify({
                "success": True,
                "message": f"Coupon with id {coupon_id} deleted successfully",
                "data": coupon
            }), 200 # OK
    else:
        return jsonify({
            "success": False,
            "message": f"Coupon with id {coupon_id} not found",
        }), 404 # Not Found


# ---- Coupons ----

coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50},    
]

# GET http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json() # Get the JSON data from the request body and parse it into a Python dictionary
    print(f"new coupon: {new_coupon}") # Get the JSON data from the request body and parse it into a Python dictionary  
    coupons.append(new_coupon) # Add the new coupon to the coupons list
    return jsonify({
        "success": True,
        "message": "Coupon added successfully",
        "data": new_coupon        
    }), 201 # Created


@app.route("/api/coupons", methods=["GET"]) # Define a route for the products page that accepts GET requests
def get_coupons():
    return ({"data": coupons}) # Return a JSON response containing the list of products


#GET http://127.0.0.1:5000/api/coupons/<int:id>
@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])
def get_coupon_by_id(coupon_id):
    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            return jsonify({
                "success": True,
                "message": f"Coupon with id {coupon_id} found",
                "data": coupon
            }), 200 # OK
    else:
        return jsonify({
            "success": False,
            "message": f"Coupon with id {coupon_id} not found",
        }), 404 # Not Found


# GET http://127.0.0.1:5000/api/coupons/count
@app.route("/api/coupons/count", methods=["GET"])
def get_couponsCount():
    return ({"count": len(coupons)})


if __name__ == "__main__":
    app.run(debug=True) # Start the Flask development server with debug mode enabled, allowing for easier debugging and automatic reloading of the server when code changes are detected.
    
# Wehn this file is run directly: __name_== "__main__" will evaluate to True, and the code inside this block will be executed.
# When this file is imported as module: __name__ == "server.py"
# When this script is run directly, it starts the Flask development server.
# The server will listen for incoming requests and route them to the appropriate functions based on the defined routes.
# In this case, when a GET request is made to the "/home" endpoint, the home() function will be called, returning a JSON response with a welcome message.
# Note: In a production environment, you would typically use a more robust server setup and not run the Flask development server directly.py
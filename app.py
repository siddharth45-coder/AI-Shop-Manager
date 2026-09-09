from flask import Flask, render_template, request, redirect, url_for

from config import Config

from models.product import (
    create_product_table,
    get_all_products,
    add_product,
    delete_product
)


app = Flask(__name__)

app.config.from_object(Config)


# Create products table
create_product_table()


@app.route("/")
def home():

    products = get_all_products()

    return render_template(
        "index.html",
        products=products
    )


@app.route("/products")
def products():

    all_products = get_all_products()

    return render_template(
        "products.html",
        products=all_products
    )


@app.route("/add-product", methods=["POST"])
def add_product_route():

    name = request.form["name"]

    price = float(
        request.form["price"]
    )

    stock = int(
        request.form["stock"]
    )

    category = request.form["category"]


    add_product(
        name,
        price,
        stock,
        category
    )

    return redirect(
        url_for("products")
    )


@app.route("/delete-product/<int:product_id>")
def delete_product_route(product_id):

    delete_product(product_id)

    return redirect(
        url_for("products")
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )
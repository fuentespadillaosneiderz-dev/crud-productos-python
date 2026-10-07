from flask import Blueprint, request, jsonify
from app.models.producto import db, ProductModel

product_blueprint = Blueprint('product_blueprint', __name__)

# 1. Método GET: Consultar todos los productos
@product_blueprint.route('/products', methods=['GET'])
def get_products():
    products = ProductModel.query.all()
    result = []
    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        })
    return jsonify(result), 200

# 2. Método POST: Crear un nuevo producto
@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    new_product = ProductModel(
        name=data.get('name'),
        price=data.get('price'),
        stock=data.get('stock')
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price,
        "stock": new_product.stock
    }), 201

# 3. Método DELETE: Eliminar un producto por su ID
@product_blueprint.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = ProductModel.query.get(id)
    
    if not product:
        return jsonify({"message": "Producto no encontrado"}), 404
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({"message": "Producto eliminado exitosamente"}), 200
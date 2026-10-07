from app.models.producto import db, ProductModel

class ProductService:
    
    @staticmethod
    def get_all_products():
        # Consulta todos los productos de la base de datos
        products = ProductModel.query.all()
        return [product.to_json() for product in products]

    @staticmethod
    def create_product(data):
        # Crea y guarda un nuevo producto
        new_product = ProductModel(
            name=data.get('name'),
            price=data.get('price'),
            stock=data.get('stock')
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_json()
    
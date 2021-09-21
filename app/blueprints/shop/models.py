from app import db
from datetime import datetime as dt

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    products = db.relationship('Product', backref='group', lazy='dynamic')

    def __repr__(self):
        return f'<Category: {self.id} | {self.name}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        data={
            "id":self.id,
            "name":self.name
        }
        return data


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String)
    created_on = db.Column(db.DateTime, index=True, default=dt.utcnow)
    category_id = db.Column(db.ForeignKey('category.id'))

    def __repr__(self):
        return f'<Item: {self.id} | {self.name}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        data={
            'id':self.id,
            "name":self.name,
            "price":self.price,
            "img":self.img,
            "category_id":self.category_id,
            "created_on":self.created_on
        }
        return data

    def from_dict(self, data):
        for field in ["name","price","img","description","category_id"]:
            if field in data:
                setattr(self, field, data[field])


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

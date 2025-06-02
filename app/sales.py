from datetime import datetime
from app import db

class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    drug = db.relationship('Drug', back_populates='sales')
    customer_name = db.Column(db.String(100), nullable=True)
    customer_phone = db.Column(db.String(20), nullable=True)
    
    # Optional relationship
    drug = db.relationship('Drug', backref='sales')
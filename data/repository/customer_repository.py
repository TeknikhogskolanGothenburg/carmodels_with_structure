from data.db import session
from data.models import Customer


def get_customer_by_id(_id):
    return session.query(Customer).filter(Customer.customerNumber == _id).first()


def get_customers_by_name_pattern(pattern):
    return session.query(Customer).filter(Customer.customerName.like(f'%{pattern}%')).all()
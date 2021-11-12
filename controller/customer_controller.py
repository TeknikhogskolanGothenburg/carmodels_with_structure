from data.repository import customer_repository


def get_customer_by_id(_id):
    return customer_repository.get_customer_by_id(_id)


def get_customers_by_name_pattern(pattern):
    return customer_repository.get_customers_by_name_pattern(pattern)

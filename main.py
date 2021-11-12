from controller import customer_controller


def main():
    customer = customer_controller.get_customer_by_id(128)
    print(customer.customerName)

    customers = customer_controller.get_customers_by_name_pattern('Gifts')

    for customer in customers:
        print(customer.customerName)


if __name__ == '__main__':
    main()

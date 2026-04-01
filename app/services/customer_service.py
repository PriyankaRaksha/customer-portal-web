customers=[]

def add_customer(name,email):

    customer={
        "name":name,
        "email":email
    }

    customers.append(customer)

    return customer
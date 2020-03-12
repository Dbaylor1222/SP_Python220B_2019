'''Basic operations for customer database'''

# pylint disabled: R0913

import logging
import peewee
from customer_model import Customer

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def add_customer(customer_id, name, lastname, home_address, phone_number, email_address,
                 status, credit_limit):
    '''Adds a new customer to the database.'''
    try:
        new_customer = Customer.create(cust_id=customer_id,
                                       f_name=name,
                                       l_name=lastname,
                                       address=home_address,
                                       phone=phone_number,
                                       email=email_address,
                                       status=status,
                                       credit=credit_limit)
        new_customer.save()
        LOGGER.info('Added %s %s to the customer database', name, lastname)

    except peewee.IntegrityError:
        LOGGER.info('Customer %s %s currently exists in the database', name, lastname)
        raise ValueError

def search_customer(customer_id):
    '''Searches the database for a specific customer'''
    cust_data = {}
    try:
        LOGGER.info('Searching for customer ID: %s in the database', customer_id)
        customer = Customer.get(Customer.cust_id == customer_id)
        cust_data = {'f_name': customer.f_name,
                     'l_name': customer.l_name,
                     'email': customer.email,
                     'phone': customer.phone}
        LOGGER.info('found customer ID: %s %s', customer_id, cust_data)
    except peewee.DoesNotExist:
        LOGGER.info('Customer ID: %s does not exist in the database', customer_id)
    return cust_data

def delete_customer(customer_id):
    '''Deletes a specific customer from the database.'''
    try:
        LOGGER.info('Searching for customer ID %s to delete from the database', customer_id)
        Customer.get_by_id(customer_id)
        Customer.delete_by_id(customer_id)
        LOGGER.info('Customer %s is deleted from the database', customer_id)
    except peewee.DoesNotExist:
        LOGGER.info('Customer ID: %s is not available to delete from the database', customer_id)
        raise ValueError

def update_customer_credit(customer_id, credit_limit):
    '''Updates the customer's credit limit'''
    try:
        logging.info('Attempting to update credit limit for customer ID: %s to $%s',
                     customer_id, credit_limit)
        customer = Customer.get(Customer.cust_id == customer_id)
        customer.credit = credit_limit
        customer.save()
        LOGGER.info('Updated credit limit for cutomer ID: %s to $%s', customer_id, customer.credit)
    except peewee.DoesNotExist:
        LOGGER.info('Customer ID: %s does not exist in the database', customer_id)
        raise ValueError

def list_active_customers():
    '''Returns the number of customers with an active status in the database.'''
    active_custs = Customer.select().where(Customer.status == 'Active').count()
    LOGGER.info('There are %s active customers in the database', active_custs)
    return active_custs

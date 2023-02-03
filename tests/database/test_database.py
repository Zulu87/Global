import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users =db.get_all_users()

    print (users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user =db.get_user_address_by_name("Sergii")

    assert user[0][0] =='Maydan Nezalezhnosti 1'
    assert user[0][1] =='Kyiv'
    assert user[0][2] =='3127'
    assert user[0][3] =='Ukraine'

@pytest.mark.database
def test_product_quantity_update():
    db = Database()
    db.update_product_quantity_by_id(1, 25)
    water_quantity = db.select_product_quantity_by_id(1)

    assert water_quantity[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4,'печиво', 'солодке',30)
    product_quantity = db.select_product_quantity_by_id(4)

    assert product_quantity[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99,'test', 'data',99)
    db.delete_product_by_id(99)
    product_quantity = db.select_product_quantity_by_id(99)

    assert len(product_quantity) == 0

@pytest.mark.database    
def test_detailed_orders():
    db = Database()
    orders =db.get_detailed_orders()
    print("Ordering was", orders)

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] =='Sergii'
    assert orders[0][2] =='солодка вода'
    assert orders[0][3] =='з цукром'
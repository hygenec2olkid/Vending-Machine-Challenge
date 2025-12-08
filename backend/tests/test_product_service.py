import pytest
from unittest.mock import MagicMock, patch, ANY
from sqlalchemy.orm import Session
from collections import namedtuple
from services.product_service import ProductService
from db.schema import DBProductInventory 

MockDBProductInventory = namedtuple(
    'DBProductInventory', 
    ['id', 'name', 'price', 'quantity']
)

MOCK_PRODUCTS_DATA = [
    MockDBProductInventory(id=1, name="Soda", price=150, quantity=10),
    MockDBProductInventory(id=2, name="Chips", price=100, quantity=5),
]

@pytest.fixture
def mock_db_session():
    return MagicMock(spec=Session)

@pytest.fixture
def mock_coin_service():
    return MagicMock()

@pytest.fixture
def product_service(mock_db_session, mock_coin_service):
    with patch('services.product_service.CoinService', return_value=mock_coin_service):
        service = ProductService(session=mock_db_session)
        # Ensure the instance attribute uses the mock
        service.coin_service = mock_coin_service 
        yield service

def test_get_product_stock_success(product_service, mock_db_session):
    """Tests successful retrieval of all products."""
    
    # Setup the mock execution result chain: .execute().scalars().all()
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = MOCK_PRODUCTS_DATA
    mock_db_session.execute.return_value = mock_result
    
    # Call the method
    products = product_service.get_product_stock()
    
    # Assertions
    assert len(products) == 2
    assert products[0].name == "Soda"
    
    # Ensure the database execution method was called once
    product_service._db.execute.assert_called_once()
    

## Test Suite for buy_product

def test_buy_product_success(product_service, mock_db_session, mock_coin_service):
    """Tests a successful purchase including change processing and DB update."""
    
    PRODUCT_ID = 1
    AMOUNT_TO_BUY = 1
    BALANCE = 200 
    
    # 1. Mock product lookup (to return an object that can have its quantity modified)
    mock_product = MagicMock(spec=DBProductInventory, 
                             id=PRODUCT_ID, name="Soda", price=150, quantity=10)
    mock_db_session.execute.return_value.scalar_one_or_none.return_value = mock_product
    
    # 2. Mock the change calculation (Machine CAN provide change: 50 units)
    CHANGE_AMOUNT = 50
    CHANGE_COMBINATION = {50: 1} # One 50-coin returned
    mock_coin_service.can_change_coin.return_value = (True, CHANGE_COMBINATION)
    
    # 3. Call the method
    returned_change = product_service.buy_product(PRODUCT_ID, AMOUNT_TO_BUY, BALANCE)
    
    # 4. Assertions
    
    # Check change logic call and result
    mock_coin_service.can_change_coin.assert_called_once_with(CHANGE_AMOUNT)
    assert returned_change == CHANGE_COMBINATION
    
    # Check CoinService stock update (the machine pays out 1 coin)
    mock_coin_service.update_coin_stock.assert_called_once_with(50, -1)
    
    # Check product quantity update
    assert mock_product.quantity == 9 # Initial 10 - 1 bought
    mock_db_session.commit.assert_called_once() # Ensure transaction was committed


def test_buy_product_failure_not_found(product_service, mock_db_session):
    """Tests failure when the product ID does not exist."""
    
    # Mock lookup to return None (product not found)
    mock_db_session.execute.return_value.scalar_one_or_none.return_value = None
    
    # Assert that the correct ValueError is raised
    with pytest.raises(ValueError, match="Product not found"):
        product_service.buy_product(99, 1, 500)
        
    mock_db_session.commit.assert_not_called()


def test_buy_product_failure_out_of_stock(product_service, mock_db_session):
    """Tests failure when quantity requested exceeds stock (or stock is zero)."""
    
    # Mock product with zero stock
    mock_product = MagicMock(quantity=0)
    mock_db_session.execute.return_value.scalar_one_or_none.return_value = mock_product
    
    # Assert that the correct ValueError is raised
    with pytest.raises(ValueError, match="Product out of stock"):
        product_service.buy_product(1, 1, 500)
        
    mock_db_session.commit.assert_not_called()


def test_buy_product_failure_insufficient_balance(product_service, mock_db_session):
    """Tests failure when the balance is less than the total price."""
    
    # Mock product priced at 150
    mock_product = MagicMock(price=150, quantity=10)
    mock_db_session.execute.return_value.scalar_one_or_none.return_value = mock_product
    
    # Assert that the correct ValueError is raised (Balance 100 < Price 150)
    with pytest.raises(ValueError, match="Balance is insufficient"):
        product_service.buy_product(1, 1, 100)
        
    mock_db_session.commit.assert_not_called()


def test_buy_product_failure_cannot_make_change(product_service, mock_db_session, mock_coin_service):
    """Tests failure when the CoinService cannot provide the required change."""
    
    PRODUCT_ID = 1
    AMOUNT_TO_BUY = 1
    BALANCE = 200 # Change needed is 50
    
    # 1. Mock the product lookup
    mock_product = MagicMock(price=150, quantity=10)
    mock_db_session.execute.return_value.scalar_one_or_none.return_value = mock_product
    
    # 2. Mock change calculation (Machine CANNOT provide change)
    mock_coin_service.can_change_coin.return_value = (False, {})
    
    # 3. Assert that the correct ValueError is raised
    with pytest.raises(ValueError, match="Machine cannot provide coin to change"):
        product_service.buy_product(PRODUCT_ID, AMOUNT_TO_BUY, BALANCE)
        
    # Assert that no changes were committed to the DB
    mock_db_session.commit.assert_not_called()
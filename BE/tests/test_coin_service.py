import pytest
from unittest.mock import MagicMock, patch, call
from sqlalchemy.orm import Session
from collections import namedtuple
from services.coin_service import CoinService
from db.schema import DBCoinStock


class MockDBCoin:
    def __init__(self, coin, quantity):
        self.coin = coin
        self.quantity = quantity

@pytest.fixture
def mock_session():
    return MagicMock(spec=Session)

@pytest.fixture
def coin_service(mock_session):
    return CoinService(session=mock_session)

class TestGetCoinStock:
    def test_get_coin_stock_success(self, coin_service, mock_session):
        """Test retrieving all coins sorted descending."""
        # Setup mock return data
        mock_data = [MockDBCoin(10, 5), MockDBCoin(5, 10)]
        
        # Configure the chain: session.execute().scalars().all()
        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = mock_data
        mock_session.execute.return_value = mock_result

        # Execute
        result = coin_service.get_coin_stock()

        # Assert
        assert len(result) == 2
        assert result[0].coin == 10
        mock_session.execute.assert_called_once()


class TestGetChangeCoin:
    """Tests the logic helper method (pure logic, no DB)."""
    
    def test_coin_larger_than_value(self, coin_service):
        # Value 5, Coin 10 -> Should use 0
        assert coin_service.get_change_coin(5, 10, 100) == 0

    def test_ample_stock(self, coin_service):
        # Value 30, Coin 10, Stock 100 -> Should use 3
        assert coin_service.get_change_coin(30, 10, 100) == 3

    def test_limited_stock(self, coin_service):
        # Value 30, Coin 10, Stock 2 -> Should use 2 (all stock)
        assert coin_service.get_change_coin(30, 10, 2) == 2


class TestCanChangeCoin:
    """Tests the greedy change algorithm."""

    def test_can_change_coin_success(self, coin_service):
        # Mock get_coin_stock to avoid DB calls in this specific test
        # Inventory: 10s: 5, 5s: 10, 1s: 20
        mock_inventory = [
            MockDBCoin(10, 5), 
            MockDBCoin(5, 10), 
            MockDBCoin(1, 20)
        ]
        
        with patch.object(coin_service, 'get_coin_stock', return_value=mock_inventory):
            # Try to change 27 -> 10*2 + 5*1 + 1*2
            success, change_dict = coin_service.can_change_coin(27)

            assert success is True
            assert change_dict[10] == 2
            assert change_dict[5] == 1
            assert change_dict[1] == 2

    def test_can_change_coin_failure_insufficient_total(self, coin_service):
        # Inventory: Only one 10 coin
        mock_inventory = [MockDBCoin(10, 1)]
        
        with patch.object(coin_service, 'get_coin_stock', return_value=mock_inventory):
            # Try to change 20
            success, change_dict = coin_service.can_change_coin(20)

            assert success is False
            assert change_dict == {}

    def test_can_change_coin_failure_missing_denomination(self, coin_service):
        # Inventory: 10s: 10. No 1s or 5s.
        mock_inventory = [MockDBCoin(10, 10)]
        
        with patch.object(coin_service, 'get_coin_stock', return_value=mock_inventory):
            # Try to change 15. Can take 10, rem 5. No 5s.
            success, change_dict = coin_service.can_change_coin(15)

            assert success is False
            assert change_dict == {}


class TestUpdateCoinStock:
    def test_update_coin_stock_add_success(self, coin_service, mock_session):
        """Test adding stock to an existing coin."""
        coin_value = 10
        initial_qty = 5
        add_qty = 5
        
        # Mock DB finding the coin
        mock_coin = MockDBCoin(coin_value, initial_qty)
        mock_session.execute.return_value.scalar_one_or_none.return_value = mock_coin

        # Execute
        coin_service.update_coin_stock(coin_value, add_qty)

        # Assert
        assert mock_coin.quantity == 10 # 5 + 5
        mock_session.commit.assert_called_once()

    def test_update_coin_stock_remove_success(self, coin_service, mock_session):
        """Test removing stock (decrease quantity)."""
        coin_value = 10
        mock_coin = MockDBCoin(coin_value, 5)
        mock_session.execute.return_value.scalar_one_or_none.return_value = mock_coin

        # Remove 3
        coin_service.update_coin_stock(coin_value, -3)

        assert mock_coin.quantity == 2
        mock_session.commit.assert_called_once()

    def test_update_coin_stock_insufficient_funds(self, coin_service, mock_session):
        """Test error when trying to remove more than available."""
        coin_value = 10
        mock_coin = MockDBCoin(coin_value, 2) # Only 2 available
        mock_session.execute.return_value.scalar_one_or_none.return_value = mock_coin

        # Try to remove 5
        with pytest.raises(ValueError, match=f"Insufficient stock for coin {coin_value}"):
            coin_service.update_coin_stock(coin_value, -5)

        # Ensure NO commit happened
        mock_session.commit.assert_not_called()

    def test_update_coin_stock_not_found(self, coin_service, mock_session):
        """Test error when coin does not exist in DB."""
        mock_session.execute.return_value.scalar_one_or_none.return_value = None

        with pytest.raises(ValueError, match="Invalid operation for non-existing coin"):
            coin_service.update_coin_stock(999, 10)

        mock_session.commit.assert_not_called()
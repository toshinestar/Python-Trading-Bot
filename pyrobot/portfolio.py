from typing import Tuple
from typing import List
from typing import Iterable

class Portfolio():

    def __init__(self, account_number: str = None) -> None:
        """Initalizes a new instance of the Portfolio object.
        
        Keyword Arguments:
        ----
        account_number {str} -- An accout number to associate with the Portfolio. (default: {None})
        """
        
        self.positions: dict = {}
        self.positions_count: int = 0
        self.market_value: float = 0.00
        self.profit_loss: float = 0.00
        self.risk_tolerance: float = 0.00
        self.account_number: str = account_number

    def add_positions(self, positions: List[dict]) -> dict:
        """Add Multiple positions to the portfolio at once.

        This method will take an iterable containing the values
        normally passed through in the `add_position` endpoint and
        then adds each position to the portfolio.
        
        Arguments:
        ----
        positions {list[dict]} -- Multiple positions with the required arguments to be added.

        Usage:
        ----
            # Define mutliple positions to add.
            >>> multi_position = [
                {
                    'asset_type': 'equity',
                    'quantity': 2,
                    'purchase_price': 4.00,
                    'symbol': 'TSLA',
                    'purchase_date': '2020-01-31'
                },
                {
                    'asset_type': 'equity',
                    'quantity': 2,
                    'purchase_price': 4.00,
                    'symbol': 'SQ',
                    'purchase_date': '2020-01-31'
                }
            ]
            >>> new_positions = trading_robot.portfolio.add_positions(positions=multi_position)
            {
                'SQ': {
                    'asset_type': 'equity',
                    'purchase_date': '2020-01-31',
                    'purchase_price': 4.00,
                    'quantity': 2,
                    'symbol': 'SQ'
                },
                'TSLA': {
                    'asset_type': 'equity',
                    'purchase_date': '2020-01-31',
                    'purchase_price': 4.00,
                    'quantity': 2,
                    'symbol': 'TSLA'
                }
            }

        Returns:
        ----
        dict -- A dictionary containing multiple positions.
        """
        
        if isinstance(positions, list):

            return_dict = {}

            for position in positions:

                symbol = position['symbol']

                self.positions[symbol] = {}
                self.positions[symbol]['symbol'] = position['symbol']
                self.positions[symbol]['quantity'] = position.get('quantity',0)
                self.positions[symbol]['purchase_price'] = position.get('purchase_price',0.00)
                self.positions[symbol]['purchase_date'] = position.get('purchase_date',None)
                self.positions[symbol]['asset_type'] = position['asset_type']

                return_dict[symbol] = self.positions[symbol]

            return return_dict

        else:
            raise TypeError('Positions must be a list of dictionaries.')

    def add_position(self, symbol: str, asset_type: str, quantity: int = 0, purchase_price: float = 0.00, purchase_date: str = None) -> dict:
        """Adds a single new position to the the portfolio.
        
        Arguments:
        ----
        symbol {str} -- The Symbol of the Financial Instrument. Example: 'AAPL' or '/ES'

        asset_type {str} -- The type of the financial instrument to be added. For example,
            'equity', 'forex', 'option', 'futures'

        Keyword Arguments:
        ----
        quantity {int} -- The number of shares or contracts you own. (default: {0})

        purchase_price {float} -- The price at which the position was purchased. (default: {0.00})

        purchase_date {str} -- The date which the asset was purchased. Must be ISO Format "YYYY-MM-DD"
            For example, "2020-04-01" (default: {None})

        Usage:
        ----
            >>> portfolio = Portfolio()
            >>> new_position = Portfolio.add_position(symbol='MSFT', 
                    asset_type='equity', 
                    quantity=2, 
                    purchase_price=4.00,
                    purchase_date="2020-01-31")
            >>> new_position
            {
                'asset_type': 'equity', 
                'quantity': 2, 
                'purchase_price': 4.00,
                'symbol': 'MSFT',
                'purchase_date': '2020-01-31'
            }           
        
        Returns:
        ----
        dict -- A dictionary object that represents a position in the portfolio.
        """
        
        self.positions[symbol] = {}
        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['quantity'] = quantity
        self.positions[symbol]['purchase_price'] = purchase_price
        self.positions[symbol]['purchase_date'] = purchase_date
        self.positions[symbol]['asset_type'] = asset_type

        return self.positions[symbol]

    def remove_position(self, symbol: str) -> Tuple[bool,str]:
        """Deletes a single position from the portfolio.
        
        Arguments:
        ----
        symbol {str} -- The symbol of the instrument to be deleted. Example: 'AAPL' or '/ES'
        
        Usage:
        ----
            >>> portfolio = Portfolio()

            >>> new_position = Portfolio.add_position(symbol='MSFT', 
                    asset_type='equity', 
                    quantity=2, 
                    purchase_price=4.00,
                    purchase_date="2020-01-31")

            >>> delete_status = Portfolio.delete_position(symbol='MSFT')
            >>> delete_status
            (True, 'MSFT was successfully removed.')

            >>> delete_status = Portfolio.delete_position(symbol='AAPL')
            >>> delete_status
            (False, 'AAPL did not exist in the porfolio.')

        Returns:
        ----
        Tuple[bool, str] -- Returns True if successfully deleted, False otherwise along with a message.
        """
        
        if symbol in self.positions:
            del self.positions[symbol]
            return (True, "{symbol} was successfully removed.".format(symbol=symbol))
        else:
            return (False, "{symbol} did not exist in the porfolio.".format(symbol=symbol))

    def total_allocation(self):

        total_allocation = {
            'stocks':[],
            'fixed_income':[],
            'options':[],
            'futures':[],
            'furex':[]
        }
        
        if len(self.positions.keys()) > 0:
            for symbol in self.positions:
                total_allocation[self.positions[symbol]['asset_type']]

    def risk_exposure(self):
        pass

    def portfolio_summary(self):
        pass
    
    def in_portfolio(self, symbol: str) -> bool:
        """checks if the symbol is in the portfolio.
        
        Arguments:
        ----
        symbol {str} -- The symbol of the instrument to be deleted. Example: 'AAPL' or '/ES'
        
        Usage:
        ----
            >>> portfolio = Portfolio()
            >>> new_position = Portfolio.add_position(
                symbol='MSFT', 
                asset_type='equity'
            )
            >>> in_position_flag = Portfolio.in_portfolio(symbol='MSFT')
            >>> in_position_flag
            True

        Returns:
        ----
        bool -- `True` if the position is in the portfolio, `False` otherwise.
        """

        if symbol in self.positions:
            return True
        else:
            return False

    def is_porfitable(self, symbol: str, current_price: float) -> bool:
        """Specifies whether a position is profitable.
        
        Arguments:
        ----
        symbol {str} -- The symbol of the instrument, to check profitability.

        current_price {float} -- The current trading price of the instrument.

        Usage:
        ----

        
        Returns:
        ----
        bool -- Specifies whether the position is profitable or flat (True) or not
            profitable (False).
        """

        # Grab the purchase price.
        purchase_price = self.positions[symbol]['purchase_price']
        
        if (symbol in self.positions and purchase_price <= current_price):
            return True
        elif (symbol in self.positions and purchase_price > current_price):
            return False

    def projected_market_value(self):
        pass



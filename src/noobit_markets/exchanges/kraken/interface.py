from noobit_markets.base.models.interface import ExchangeInterface


# private endpoints
from noobit_markets.exchanges.kraken.rest.private.balances.get import get_balances_kraken

# public endpoints
from noobit_markets.exchanges.kraken.rest.public.ohlc.get import get_ohlc_kraken
from noobit_markets.exchanges.kraken.rest.public.symbols.get import get_symbols
from noobit_markets.exchanges.kraken.rest.public.orderbook.get import get_orderbook_kraken


KRAKEN = ExchangeInterface(**{
    "rest": {
        "public": {
            "ohlc": get_ohlc_kraken,
            "orderbook": get_orderbook_kraken,
            "symbols": get_symbols,
        },
        "private": {
            "balances": get_balances_kraken
        }
    }
})

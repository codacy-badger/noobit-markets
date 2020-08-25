import typing
from decimal import Decimal
from datetime import date
from datetime import datetime

from pydantic import PositiveInt, conint, validator

from noobit_markets.base.models.frozenbase import FrozenBaseModel
from noobit_markets.base import ntypes




# ============================================================
# OHLC
# ============================================================


class NoobitResponseItemOhlc(FrozenBaseModel):

    symbol: ntypes.SYMBOL
    utcTime: PositiveInt

    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal

    volume: Decimal
    trdCount: PositiveInt


class NoobitResponseOhlc(FrozenBaseModel):

    ohlc: typing.List[NoobitResponseItemOhlc]
    last: PositiveInt

    @validator('last')
    def check_year_from_timestamp(cls, v):
        # timestamp should be in milliseconds
        y = date.fromtimestamp(v/1000).year
        if not y > 2009 and y < 2050:
            # FIXME we should raise
            raise ValueError(f'TimeStamp year : {y} not within [2009, 2050]')
        # return v * 10**3
        return v


# ============================================================
# SYMBOLS
# ============================================================


class NoobitResponseItemSymbols(FrozenBaseModel):

    exchange_name: str
    ws_name: str
    base: str
    quote: str
    volume_decimals: conint(ge=0)
    price_decimals: conint(ge=0)
    leverage_available: typing.Tuple[PositiveInt, ...]
    order_min: Decimal


class NoobitResponseSymbols(FrozenBaseModel):

    asset_pairs: typing.Mapping[ntypes.SYMBOL, NoobitResponseItemSymbols]
    assets: ntypes.ASSET_TO_EXCHANGE


# ============================================================
# BALANCES
# ============================================================


class NoobitResponseBalances(FrozenBaseModel):

    data: typing.Mapping[ntypes.ASSET, Decimal]




# ============================================================
# OHLC
# ============================================================

class NoobitResponseOrderBook(FrozenBaseModel):

    utcTime: ntypes.TIMESTAMP
    symbol: ntypes.SYMBOL
    asks: ntypes.ASKS
    bids: ntypes.BIDS
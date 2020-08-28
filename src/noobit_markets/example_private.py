import asyncio

import httpx
import stackprinter
stackprinter.set_excepthook(style='darkbg2')

from noobit_markets.exchanges.kraken import interface




# ============================================================
# SYMBOLS
# ============================================================


# print symbol_mapping
func_symbols = interface.KRAKEN.rest.public.symbols
try:
    symbol_to_exch = asyncio.run(
        func_symbols(
            loop=None,
            client=httpx.AsyncClient(),
            # logger_func= lambda *args: print("========> ", *args, "\n\n")
            logger_func= lambda *args: print("")
        )
    )
    if symbol_to_exch.is_err():
        print(symbol_to_exch)
except Exception as e:
    raise e




# ============================================================
# BALANCES
# ============================================================


asset_to_exchange = {v: k for k, v in symbol_to_exch.value.assets.items()}

# get balances
func_balances = interface.KRAKEN.rest.private.balances
try:
    balances = asyncio.run(
        func_balances(
            loop=None,
            client=httpx.AsyncClient(),
            asset_to_exchange=asset_to_exchange,
            logger_func= lambda *args: print("========> ", *args, "\n\n")
        )
    )
    if balances.is_err():
        print("Balances : ", balances.value)
        print("Is Exception : ", isinstance(balances.value, Exception))
except Exception as e:
    raise e




# ============================================================
# EXPOSURE
# ============================================================


func_exposure = interface.KRAKEN.rest.private.exposure

try:
    exposure = asyncio.run(
        func_exposure(
            loop=None,
            client=httpx.AsyncClient(),
            asset_to_exchange=asset_to_exchange,
            logger_func= lambda *args: print("========> ", *args, "\n\n")
        )
    )
    if exposure.is_err():
        print("Exposure : ", exposure.value)
        print("Is Exception : ", isinstance(exposure.value, Exception))
except Exception as e:
    raise e


# ============================================================
# USER TRADES
# ============================================================

symbols_to_exchange = {k: v.exchange_name for k, v in symbol_to_exch.value.asset_pairs.items()}
symbols_from_exchange = {v: k for k, v in symbols_to_exchange.items()}

func_trades = interface.KRAKEN.rest.private.trades

try:
    trades = asyncio.run(
        func_trades(
            loop=None,
            client=httpx.AsyncClient(),
            symbols_to_exchange=symbols_to_exchange,
            logger_func= lambda *args: print("========> ", *args, "\n\n")
        )
    )
    if trades.is_err():
        print(trades)
except Exception as e:
    raise e


# ============================================================
# OPEN POSITIONS
# ============================================================


func_op = interface.KRAKEN.rest.private.open_positions

try:
    open_pos = asyncio.run(
        func_op(
            loop=None,
            client=httpx.AsyncClient(),
            symbols_to_exchange=symbols_to_exchange,
            logger_func= lambda *args: print("========> ", *args, "\n\n")
        )
    )
    if open_pos.is_err():
        print(open_pos)
    print(open_pos)
except Exception as e:
    raise e
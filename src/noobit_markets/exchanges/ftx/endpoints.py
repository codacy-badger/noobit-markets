from noobit_markets.base.models.rest import endpoints


FTX_ENDPOINTS = endpoints.RESTEndpoints(**{
    "public": {
        "url": "https://ftx.com/api",


        "endpoints": {
            "time": "Time",
            # ? needed, now that symbols returns both assets and asset_pairs mappings ?
            "assets": "Not implemented",
            "symbols": "markets",
            "instrument": "Not implemented",
            "ohlc": "candles",          #? done
            "orderbook": "orderbook",
            "trades": "trades",
            "spread": "Not implemented"
        }

    },

    "private": {
        "url": "https://ftx.com/api",

        "endpoints": {
            'balances': "wallet/balances",
            "account_balance": "Balance",
            "exposure": "TradeBalance",
            "open_positions": "OpenPositions",
            "open_orders": "OpenOrders",
            "closed_orders": "ClosedOrders",
            "trades_history": "TradesHistory",
            "closed_positions": "TradesHistory",
            "ledger": "Ledgers",
            "order_info": "QueryOrders",
            "trades_info": "QueryTrades",
            "ledger_info": "QueryLedgers",
            "volume": "TradeVolume",
            "new_order": "AddOrder",
            "remove_order": "CancelOrder",
            "ws_token": "GetWebSocketsToken",
        }
    }
})
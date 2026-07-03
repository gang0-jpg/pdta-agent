"""
PDTA Configuration
"""

ASSETS = {
    "TOPIX": "1306.T",
    "NASDAQ100": "1545.T",
    "GOLD": "1326.T",
    "JREIT": "1343.T",
    "USBOND": "IEF",
    "USDJPY": "JPY=X"
}

START_DATE = "2020-01-01"

END_DATE = None

RISK_FREE_RATE = 0.001

N_PORTFOLIOS = 100000

CURRENT_PORTFOLIO = {
    "TOPIX": 0.14,
    "NASDAQ100": 0.00,
    "GOLD": 0.05,
    "JREIT": 0.04,
    "USBOND": 0.08,
    "USDJPY": 0.23,
    "JPY": 0.46
}


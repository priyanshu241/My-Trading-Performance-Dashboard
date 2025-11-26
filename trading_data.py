"""
Trading Data Configuration - KOTAK NEO DERIVATIVES ONLY
FY 2025-26 Trading Performance Data
Clean data showing systematic trading evolution
"""

# Kotak Neo - Derivatives Only (Monthly P&L)
kotak_derivative = {
    'Apr': -5536,
    'May': 0,
    'Jun': -5303,
    'Jul': 9834,
    'Aug': 13258,
    'Sep': 6060,
    'Oct': -3492
}

# Trading metadata
TRADING_METADATA = {
    'total_net_pnl': 12592.19,
    'total_turnover': 198598.13,
    'platform': 'Kotak Neo',
    'segment': 'Derivatives Only',
    'systematic_months': ['Jul', 'Aug', 'Sep'],  # Q2 Systematic Trading
    'learning_months': ['Apr', 'Jun'],  # Q1 Learning phase
    'financial_year': '2025-26',
    'interview_date': '20th November 2025',
    'company': 'Axxela',
    'client_name': 'Priyanshu Aryan',
    'client_code': 'XFONT'
}

# Quarter definitions
QUARTERS = {
    'Q1': ['Apr', 'May', 'Jun'],
    'Q2': ['Jul', 'Aug', 'Sep'],
    'Q3': ['Oct']
}

# Trading style classification
TRADING_STYLES = {
    'systematic': {
        'platform': 'Kotak Neo',
        'segment': 'Derivatives',
        'months': ['Jul', 'Aug', 'Sep'],
        'description': 'Disciplined, rule-based trading with consistent execution'
    },
    'learning': {
        'platform': 'Kotak Neo',
        'segment': 'Derivatives',
        'months': ['Apr', 'Jun'],
        'description': 'Initial phase, understanding market dynamics and developing strategy'
    }
}

# Platform details
PLATFORM = {
    'name': 'Kotak Neo',
    'segment': 'Derivatives',
    'focus': 'Options Trading (SENSEX, NIFTY)'
}
"""
Trading Data Configuration
FY 2024-25 Trading Performance Data
"""

# Kotak Neo - Derivative Section
kotak_derivative = {
    'Apr': -5536,
    'May': 0,
    'Jun': -5303,
    'Jul': 9834,
    'Aug': 13258,
    'Sep': 6060,
    'Oct': -3492
}

# Kotak Neo - Commodity Section
kotak_commodity = {
    'Apr': -2386,
    'May': 0,
    'Jun': -2308,
    'Jul': 0,
    'Aug': -11933,
    'Sep': 0,
    'Oct': 0
}

# Groww - Derivative Section (All trades)
groww_derivative = {
    'Apr': 0,
    'May': 0,
    'Jun': -133.67,
    'Jul': -6912.59,
    'Aug': 0,
    'Sep': 0,
    'Oct': -24857.53
}

# Trading metadata
TRADING_METADATA = {
    'total_kotak_derivative': 12592.19,
    'total_kotak_commodity': -17294.05,
    'total_groww': -31905.82,
    'systematic_months': ['Jul', 'Aug', 'Sep'],  # Q2 Systematic Trading
    'emotional_months': ['Jul', 'Oct'],  # Emotional trading on Groww
    'learning_months': ['Apr', 'Jun'],  # Q1 Learning phase
    'financial_year': '2024-25',
    'interview_date': '20th November 2025',
    'company': 'Axxela'
}

# Quarter definitions
QUARTERS = {
    'Q1': ['Apr', 'May', 'Jun'],
    'Q2': ['Jul', 'Aug', 'Sep'],
    'Q3': ['Oct']  # Partial quarter
}

# Trading style classification
TRADING_STYLES = {
    'systematic': {
        'platform': 'Kotak',
        'segment': 'Derivative',
        'months': ['Jul', 'Aug', 'Sep'],
        'description': 'Disciplined, rule-based trading with consistent execution'
    },
    'emotional': {
        'platform': 'Groww',
        'segment': 'Derivative',
        'months': ['Jul', 'Oct'],
        'description': 'Guilt-trip trading, emotional decision making'
    },
    'learning': {
        'platform': 'Kotak',
        'segment': 'Both',
        'months': ['Apr', 'Jun'],
        'description': 'Initial phase, identifying what works'
    }
}

# Platform details
PLATFORMS = {
    'Kotak': {
        'full_name': 'Kotak Neo',
        'segments': ['Derivative', 'Commodity'],
        'primary_focus': 'Derivative'
    },
    'Groww': {
        'full_name': 'Groww',
        'segments': ['Derivative'],
        'primary_focus': 'Derivative'
    }
}
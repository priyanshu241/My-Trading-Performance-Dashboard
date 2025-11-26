"""
Configuration file for Trading Dashboard
Color schemes, output paths, and styling settings
"""

import os

# Output directories
OUTPUT_DIR = 'output'
CHARTS_DIR = os.path.join(OUTPUT_DIR, 'charts')
REPORT_DIR = OUTPUT_DIR

# Create directories if they don't exist
os.makedirs(CHARTS_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Month ordering (FY 2024-25: Apr to Oct)
MONTHS_ORDER = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']

# Quarter definitions
QUARTERS = {
    'Q1': ['Apr', 'May', 'Jun'],
    'Q2': ['Jul', 'Aug', 'Sep'],
    'Q3': ['Oct']  # Only October so far
}

# Color scheme
COLORS = {
    'profit': '#10b981',  # Green
    'loss': '#ef4444',  # Red
    'systematic': '#10b981',  # Green
    'learning': '#f59e0b',  # Orange/Yellow
    'neutral': '#6b7280',  # Gray
    'kotak_derivative': '#3b82f6',  # Blue
    'background': '#1f2937',  # Dark gray
    'text': '#f9fafb',  # Light gray
    'grid': '#374151'  # Medium gray
}

# Chart styling
CHART_STYLE = {
    'figure_size': (14, 8),
    'dpi': 100,
    'font_size': 10,
    'title_size': 14,
    'label_size': 11,
    'legend_size': 9,
    'background_color': '#1f2937',
    'text_color': '#f9fafb',
    'grid_color': '#374151',
    'grid_alpha': 0.3
}

# Report styling
HTML_STYLE = """
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        color: #f9fafb;
        padding: 20px;
        line-height: 1.6;
    }
    
    .container {
        max-width: 1400px;
        margin: 0 auto;
        background: #1f2937;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    }
    
    .header {
        text-align: center;
        margin-bottom: 40px;
        padding-bottom: 30px;
        border-bottom: 3px solid #10b981;
    }
    
    .header h1 {
        font-size: 3em;
        background: linear-gradient(135deg, #10b981, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .header p {
        font-size: 1.2em;
        color: #9ca3af;
    }
    
    .summary-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-bottom: 40px;
    }
    
    .card {
        background: #374151;
        padding: 25px;
        border-radius: 15px;
        border-left: 4px solid;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
    }
    
    .card.profit { border-color: #10b981; }
    .card.loss { border-color: #ef4444; }
    .card.info { border-color: #3b82f6; }
    .card.warning { border-color: #f59e0b; }
    
    .card h3 {
        font-size: 0.9em;
        color: #9ca3af;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .card .value {
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .card .subtitle {
        font-size: 0.85em;
        color: #6b7280;
    }
    
    .section {
        margin-bottom: 50px;
    }
    
    .section h2 {
        font-size: 2em;
        margin-bottom: 20px;
        color: #10b981;
        border-bottom: 2px solid #374151;
        padding-bottom: 10px;
    }
    
    .chart-container {
        background: #374151;
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .chart-container img {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
    }
    
    .insights-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 30px;
        margin-top: 30px;
    }
    
    .insight-box {
        background: #374151;
        padding: 25px;
        border-radius: 15px;
    }
    
    .insight-box h3 {
        color: #10b981;
        margin-bottom: 15px;
        font-size: 1.3em;
    }
    
    .insight-box ul {
        list-style: none;
        padding-left: 0;
    }
    
    .insight-box li {
        padding: 10px 0;
        border-bottom: 1px solid #4b5563;
    }
    
    .insight-box li:last-child {
        border-bottom: none;
    }
    
    .metric-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        background: #374151;
        border-radius: 10px;
        overflow: hidden;
    }
    
    .metric-table th {
        background: #1f2937;
        padding: 15px;
        text-align: left;
        color: #10b981;
        font-weight: bold;
    }
    
    .metric-table td {
        padding: 15px;
        border-bottom: 1px solid #4b5563;
    }
    
    .metric-table tr:last-child td {
        border-bottom: none;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(59, 130, 246, 0.1));
        border: 2px solid #10b981;
        padding: 30px;
        border-radius: 15px;
        margin: 30px 0;
    }
    
    .highlight-box h3 {
        color: #10b981;
        font-size: 1.5em;
        margin-bottom: 15px;
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        padding-top: 30px;
        border-top: 2px solid #374151;
        color: #6b7280;
    }
    
    @media print {
        body {
            background: white;
            color: black;
        }
        .container {
            box-shadow: none;
        }
    }
</style>
"""

# Currency formatting
CURRENCY_SYMBOL = '₹'
CURRENCY_FORMAT = '{:,.2f}'
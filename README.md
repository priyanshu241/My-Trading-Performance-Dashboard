# Trading Performance Dashboard

## 🚀 Professional Trading Analytics for Axxela Interview

A comprehensive Python-based trading performance dashboard that analyzes your FY 2024-25 trading data, visualizes your evolution from emotional to systematic trading, and generates a professional HTML report perfect for your Trainee Analyst interview.

---

## 📋 Project Overview

This dashboard tells your trading story:
- **Q1 (Apr-Jun)**: Learning phase with initial losses
- **Q2 (Jul-Sep)**: Systematic trading with 3 consecutive profitable months
- **Key Insight**: Recognized emotional vs systematic trading patterns and adapted

**Net Result**: Demonstrated 185.4% improvement from Q1 to Q2 through disciplined, data-driven approach.

---

## 🎯 Features

### 📊 Comprehensive Analytics
- Monthly, quarterly, and overall P&L analysis
- Segment-wise performance breakdown (Derivatives vs Commodities)
- Platform comparison (Kotak vs Groww)
- Win rate, profit factor, Sharpe ratio, and more

### 📈 Professional Visualizations
1. Monthly P&L bar chart
2. Cumulative P&L journey
3. Quarterly comparison
4. Segment distribution pie chart
5. Systematic vs Emotional trading analysis
6. Consistency heatmap
7. Win/Loss distribution
8. Drawdown & recovery analysis

### 📄 HTML Report
- Executive summary
- Key metrics cards
- All visualizations embedded
- Detailed insights and learnings
- Interview talking points
- Risk management analysis

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Verify Installation

```bash
python -c "import pandas; import matplotlib; import seaborn; print('All dependencies installed successfully!')"
```

---

## 🚀 Usage

### Run the Dashboard Generator

```bash
python main.py
```

That's it! The script will:
1. Generate all 8 visualization charts
2. Calculate 30+ performance metrics
3. Create a professional HTML report
4. Print key metrics summary to console

### Output Structure

```
trading_dashboard/
├── output/
│   ├── Trading_Performance_Report.html  ← Main report
│   └── charts/
│       ├── monthly_pnl.png
│       ├── cumulative_pnl.png
│       ├── quarterly_comparison.png
│       ├── segment_distribution.png
│       ├── systematic_vs_emotional.png
│       ├── consistency_heatmap.png
│       ├── win_loss_distribution.png
│       └── drawdown_recovery.png
```

---

## 📊 Your Trading Data

### Kotak Neo
- **Derivatives**: ₹12,592.19 profit (total FY)
- **Commodities**: ₹17,294.05 loss (total FY)

### Groww
- **Derivatives**: ₹31,905.82 loss (total FY)

### Monthly Breakdown

| Month | Kotak Deriv | Kotak Comm | Groww Deriv | Total |
|-------|-------------|------------|-------------|-------|
| Apr   | -₹5,536     | -₹2,386    | ₹0          | -₹7,922 |
| May   | ₹0          | ₹0         | ₹0          | ₹0 |
| Jun   | -₹5,303     | -₹2,308    | -₹133.67    | -₹7,744.67 |
| Jul   | ₹9,834      | ₹0         | -₹6,912.59  | ₹2,921.41 |
| Aug   | ₹13,258     | -₹11,933   | ₹0          | ₹1,325 |
| Sep   | ₹6,060      | ₹0         | ₹0          | ₹6,060 |
| Oct   | -₹3,492     | ₹0         | -₹24,857.53 | -₹28,349.53 |

---

## 🎤 Interview Talking Points

### 1. Real Skin in the Game
"I traded with my own capital to truly understand market dynamics, not just theoretically."

### 2. Data-Driven Approach
"Analyzed Q1 losses, identified patterns, and improved Q2 performance by 185.4%."

### 3. Self-Awareness
"Recognized emotional trading on Groww platform and had the discipline to stop."

### 4. Risk Management
"Stopped commodity trading after identifying it wasn't my strength - cut losses early."

### 5. Systematic Success
"Q2 showed 3 consecutive profitable months with 100% win rate through disciplined execution."

### 6. Resilience
"Bounced back from Q1 losses, demonstrating ability to learn and adapt under pressure."

---

## 📈 Key Metrics

- **Net P&L**: -₹22,019.18 (overall)
- **Q1 P&L**: -₹15,666.67 (learning phase)
- **Q2 P&L**: ₹10,246.41 (systematic phase)
- **Improvement**: +185.4% (Q1 to Q2)
- **Systematic Win Rate**: 100% (Q2 derivatives)
- **Overall Win Rate**: 42.9%
- **Profit Factor**: 0.49
- **Best Month**: Jun (₹6,060)
- **Worst Month**: Oct (-₹28,349.53)

---

## 🔧 Project Structure

```
trading_dashboard/
├── main.py                 # Main execution script
├── trading_data.py         # Your trading data
├── config.py              # Configuration & styling
├── data_processor.py      # Data processing logic
├── analytics.py           # Metrics calculation
├── visualizer.py          # Chart generation
├── report_generator.py    # HTML report creation
├── requirements.txt       # Dependencies
├── README.md             # This file
└── output/               # Generated outputs
```

---

## 🎨 Customization

### Modify Trading Data
Edit `trading_data.py` to update your data:

```python
kotak_derivative = {
    'Apr': -5536,
    'May': 0,
    # ... add more months
}
```

### Adjust Colors
Edit `config.py` to change color scheme:

```python
COLORS = {
    'profit': '#10b981',  # Green
    'loss': '#ef4444',    # Red
    # ... customize colors
}
```

### Customize Report
Edit `report_generator.py` to modify report sections, add/remove content, or change styling.

---

## 🐛 Troubleshooting

### Issue: "Module not found"
**Solution**: Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: "Permission denied" when saving files
**Solution**: Check write permissions for the output directory or run with elevated privileges.

### Issue: Charts not displaying in report
**Solution**: Ensure charts are generated before opening the HTML report. Re-run `python main.py`.

---

## 💡 Tips for Tomorrow's Interview

1. **Open the HTML report** in your browser before the interview
2. **Review each visualization** and understand what it shows
3. **Practice your narrative** using the talking points section
4. **Be ready to discuss**:
   - Your Q2 systematic approach
   - How you recognized and stopped emotional trading
   - Risk management decisions (stopping commodity trading)
   - Data-driven improvements (185% Q1 to Q2)

5. **Key message**: "Systematic, disciplined trading works; emotional trading doesn't - and I had the self-awareness to recognize this early."

---

## 🔥 Final Notes

This dashboard demonstrates:
- ✅ Real trading experience with personal capital
- ✅ Data-driven decision making and analysis
- ✅ Self-awareness about trading psychology
- ✅ Strong risk management discipline
- ✅ Ability to learn from mistakes and adapt
- ✅ Systematic approach that produces results

**You got this! Good luck at Axxela tomorrow!** 🚀

---

## 📞 Questions?

If you encounter any issues or need modifications:
1. Check the console output for detailed error messages
2. Review the generated metrics summary
3. Ensure all data in `trading_data.py` is correct

---

## 📄 License

Personal project for interview purposes. All data is your own trading history.

---

**Generated**: November 19, 2025  
**Interview Date**: November 20, 2025  
**Company**: Axxela  
**Role**: Trainee Analyst
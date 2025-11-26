# Quick Start Guide - Trading Dashboard

## ⚡ Get Running in 5 Minutes

### Step 1: Setup (2 minutes)

```bash
# Create project directory
mkdir trading_dashboard
cd trading_dashboard

# Save all the Python files I provided:
# - main.py
# - trading_data.py
# - config.py
# - data_processor.py
# - analytics.py
# - visualizer.py
# - report_generator.py
# - requirements.txt

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Run (30 seconds)

```bash
python main.py
```

### Step 3: View Report (30 seconds)

```bash
# The report will be at:
# output/Trading_Performance_Report.html

# Open it in your browser
# Windows: start output\Trading_Performance_Report.html
# Mac: open output/Trading_Performance_Report.html
# Linux: xdg-open output/Trading_Performance_Report.html
```

---

## 📂 File Checklist

Make sure you have all these files in your `trading_dashboard` folder:

- [ ] `main.py`
- [ ] `trading_data.py`
- [ ] `config.py`
- [ ] `data_processor.py`
- [ ] `analytics.py`
- [ ] `visualizer.py`
- [ ] `report_generator.py`
- [ ] `requirements.txt`
- [ ] `README.md` (optional)
- [ ] `INTERVIEW_DEMO_SCRIPT.md` (optional)

---

## 🐛 Common Issues

### Issue: "No module named 'pandas'"
```bash
pip install pandas numpy matplotlib seaborn
```

### Issue: "Permission denied"
```bash
# Run with admin/sudo if needed
sudo python main.py
```

### Issue: "Output directory not found"
```bash
# The script creates it automatically
# But you can manually create it:
mkdir output
mkdir output/charts
```

---

## ✅ Expected Output

When you run `python main.py`, you should see:

```
================================================================================
           TRADING PERFORMANCE DASHBOARD GENERATOR
                  FY 2024-25 | Axxela Interview
================================================================================

🚀 Starting dashboard generation...
📁 Output directory: /path/to/trading_dashboard/output

Step 1/3: Generating visualizations...
--------------------------------------------------------------------------------
✓ Monthly P&L chart created
✓ Cumulative P&L chart created
✓ Quarterly comparison chart created
✓ Segment distribution chart created
✓ Systematic vs Emotional chart created
✓ Consistency heatmap created
✓ Win/Loss distribution chart created
✓ Drawdown recovery chart created

✅ All visualizations saved to: output/charts

Step 2/3: Generating HTML report...
--------------------------------------------------------------------------------
✅ Report generated: output/Trading_Performance_Report.html

Step 3/3: Summary...
--------------------------------------------------------------------------------

================================================================================
KEY METRICS SUMMARY
================================================================================

📊 Overall Performance:
   Net P&L: ₹-22,019.18
   Win Rate: 42.9%
   Profit Factor: 0.49

✅ Systematic Trading (Q2):
   Total P&L: ₹29,152.00
   Win Rate: 100.0%
   Consecutive Profitable Months: 3

📈 Improvement:
   Q1 P&L: ₹-15,666.67
   Q2 P&L: ₹10,246.41
   Improvement: +185.4%

🎯 Best/Worst:
   Best Month: Sep (₹6,060.00)
   Worst Month: Oct (₹-28,349.53)

🛡️ Risk Metrics:
   Max Drawdown: ₹-22,019.18
   Volatility: ₹12,841.42
   Sharpe Ratio: -0.631

================================================================================

================================================================================
✅ DASHBOARD GENERATION COMPLETE!
================================================================================

📄 Report: /path/to/trading_dashboard/output/Trading_Performance_Report.html
📊 Charts: /path/to/trading_dashboard/output/charts

💡 Next Steps:
   1. Open the HTML report in your browser
   2. Review all visualizations and metrics
   3. Practice your interview narrative using the talking points
   4. Be ready to discuss your systematic trading approach

🎯 For Tomorrow's Interview:
   • Focus on Q2 systematic trading success
   • Highlight self-awareness and risk management
   • Emphasize data-driven decision making
   • Show resilience and learning from Q1

🔥 Good luck at Axxela tomorrow! You got this!
================================================================================
```

---

## 🚀 Ready for Interview

Once the script runs successfully:

1. **Open the HTML report** - This is your main presentation
2. **Review all 8 charts** - Know what each one shows
3. **Read the interview talking points** - Practice your narrative
4. **Check your laptop battery** - Make sure you can demo it
5. **Practice the 2-minute demo** - Time yourself

---

## 📱 Emergency Contact

If something goes wrong:

1. Check the error message in console
2. Verify all files are in the same directory
3. Make sure Python 3.8+ is installed: `python --version`
4. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

---

## ⏰ Timeline for Today (Nov 19)

- [x] **4:00 PM** - Setup project and run script
- [ ] **4:30 PM** - Review generated report
- [ ] **5:00 PM** - Practice demo script (3 times)
- [ ] **6:00 PM** - Review key numbers and metrics
- [ ] **8:00 PM** - Final review before bed
- [ ] **Tomorrow 12:00 PM** - Quick refresh before interview

---

**You're all set! Now run that script and let's get you interview-ready! 🔥**
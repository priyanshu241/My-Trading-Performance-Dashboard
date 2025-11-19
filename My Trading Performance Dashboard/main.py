"""
Main Execution Script
Trading Performance Dashboard Generator
"""

import sys
import os
from datetime import datetime
from visualizer import TradingVisualizer
from report_generator import ReportGenerator
from analytics import TradingAnalytics
from config import OUTPUT_DIR

def print_header():
    """Print dashboard header"""
    print("=" * 80)
    print("           TRADING PERFORMANCE DASHBOARD GENERATOR")
    print("                  FY 2024-25 | Axxela Interview")
    print("=" * 80)
    print()

def print_metrics_summary():
    """Print key metrics summary to console"""
    print("\n" + "=" * 80)
    print("KEY METRICS SUMMARY")
    print("=" * 80)
    
    analytics = TradingAnalytics()
    metrics = analytics.calculate_all_metrics()
    
    print(f"\n📊 Overall Performance:")
    print(f"   Net P&L: ₹{metrics['total_pnl']:,.2f}")
    print(f"   Win Rate: {metrics['win_rate']:.1f}%")
    print(f"   Profit Factor: {metrics['profit_factor']:.2f}")
    
    print(f"\n✅ Systematic Trading (Q2):")
    print(f"   Total P&L: ₹{metrics['systematic_pnl']:,.2f}")
    print(f"   Win Rate: {metrics['systematic_win_rate']:.1f}%")
    print(f"   Consecutive Profitable Months: {metrics['systematic_profitable_months']}")
    
    print(f"\n📈 Improvement:")
    print(f"   Q1 P&L: ₹{metrics['q1_pnl']:,.2f}")
    print(f"   Q2 P&L: ₹{metrics['q2_pnl']:,.2f}")
    print(f"   Improvement: +{metrics['q1_to_q2_improvement']:.1f}%")
    
    print(f"\n🎯 Best/Worst:")
    print(f"   Best Month: {metrics['best_month']} (₹{metrics['best_month_pnl']:,.2f})")
    print(f"   Worst Month: {metrics['worst_month']} (₹{metrics['worst_month_pnl']:,.2f})")
    
    print(f"\n🛡️ Risk Metrics:")
    print(f"   Max Drawdown: ₹{metrics['max_drawdown']:,.2f}")
    print(f"   Volatility: ₹{metrics['volatility']:,.2f}")
    print(f"   Sharpe Ratio: {metrics['sharpe_ratio']:.3f}")
    
    print("\n" + "=" * 80)

def main():
    """Main execution function"""
    try:
        print_header()
        
        print("🚀 Starting dashboard generation...")
        print(f"📁 Output directory: {os.path.abspath(OUTPUT_DIR)}\n")
        
        # Step 1: Generate visualizations
        print("Step 1/3: Generating visualizations...")
        print("-" * 80)
        visualizer = TradingVisualizer()
        visualizer.generate_all_visualizations()
        
        # Step 2: Generate report
        print("\nStep 2/3: Generating HTML report...")
        print("-" * 80)
        report_gen = ReportGenerator()
        report_file = report_gen.generate_full_report()
        
        # Step 3: Print summary
        print("\nStep 3/3: Summary...")
        print("-" * 80)
        print_metrics_summary()
        
        # Final output
        print("\n" + "=" * 80)
        print("✅ DASHBOARD GENERATION COMPLETE!")
        print("=" * 80)
        print(f"\n📄 Report: {os.path.abspath(report_file)}")
        print(f"📊 Charts: {os.path.abspath(os.path.join(OUTPUT_DIR, 'charts'))}")
        print("\n💡 Next Steps:")
        print("   1. Open the HTML report in your browser")
        print("   2. Review all visualizations and metrics")
        print("   3. Practice your interview narrative using the talking points")
        print("   4. Be ready to discuss your systematic trading approach")
        print("\n🎯 For Tomorrow's Interview:")
        print("   • Focus on Q2 systematic trading success")
        print("   • Highlight self-awareness and risk management")
        print("   • Emphasize data-driven decision making")
        print("   • Show resilience and learning from Q1")
        print("\n🔥 Good luck at Axxela tomorrow! You got this!")
        print("=" * 80 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
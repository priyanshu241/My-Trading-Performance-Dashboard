"""
Main Execution Script - DERIVATIVES ONLY
Kotak Neo Derivatives Trading Performance Dashboard Generator
Clean, Systematic Trading Story
"""

import sys
import os
from datetime import datetime
from visualizer import TradingVisualizer
from report_generator import ReportGenerator
from analytics import TradingAnalytics
from config import OUTPUT_DIR
from trading_data import TRADING_METADATA

def print_header():
    """Print dashboard header"""
    print("=" * 80)
    print("      DERIVATIVES TRADING PERFORMANCE DASHBOARD GENERATOR")
    print(f"           FY {TRADING_METADATA['financial_year']} | {TRADING_METADATA['company']} Interview")
    print(f"                    {TRADING_METADATA['platform']} Only")
    print("=" * 80)
    print()

def print_metrics_summary():
    """Print key metrics summary to console"""
    print("\n" * 80)
    print("KEY METRICS SUMMARY - DERIVATIVES TRADING")
    print("=" * 80)
    
    analytics = TradingAnalytics()
    metrics = analytics.calculate_all_metrics()
    
    print(f"\n📊 Overall Performance ({TRADING_METADATA['platform']}):")
    print(f"   Net P&L: ₹{metrics['total_pnl']:,.2f}")
    print(f"   Win Rate: {metrics['win_rate']:.1f}%")
    print(f"   Profit Factor: {metrics['profit_factor']:.2f}")
    print(f"   Total Turnover: ₹{TRADING_METADATA['total_turnover']:,.2f}")
    
    print(f"\n✅ Q2 Systematic Trading (Jul-Sep):")
    print(f"   Total P&L: ₹{metrics['systematic_pnl']:,.2f}")
    print(f"   Win Rate: {metrics['systematic_win_rate']:.1f}%")
    print(f"   Consecutive Profitable Months: {metrics['systematic_profitable_months']}")
    
    print(f"\n📚 Q1 Learning Phase (Apr-Jun):")
    print(f"   Total P&L: ₹{metrics['learning_pnl']:,.2f}")
    print(f"   Win Rate: {metrics['learning_win_rate']:.1f}%")
    print(f"   Purpose: Understanding markets, developing strategy")
    
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
        
        print("🚀 Starting derivatives trading dashboard generation...")
        print(f"📁 Output directory: {os.path.abspath(OUTPUT_DIR)}")
        print(f"📊 Platform: {TRADING_METADATA['platform']}")
        print(f"💼 Client: {TRADING_METADATA['client_name']} ({TRADING_METADATA['client_code']})")
        print(f"📅 Financial Year: {TRADING_METADATA['financial_year']}\n")
        
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
        print("   3. Practice your interview narrative:")
        print(f"      - Q1 learning phase: Initial losses while developing strategy")
        print(f"      - Q2 systematic trading: {TRADING_METADATA['total_turnover']/1000:.0f}K turnover, disciplined execution")
        print(f"      - Result: 3 consecutive profitable months, 100% win rate")
        print("\n🎯 For Tomorrow's {TRADING_METADATA['company']} Interview:")
        print("   • Focus on Q2 systematic success (100% win rate)")
        print("   • Highlight data-driven approach (369% improvement)")
        print("   • Emphasize discipline and consistency")
        print("   • Show learning agility (Q1 → Q2 transformation)")
        print(f"\n🔥 Clean Story: Learning → Systematic → Profitable")
        print(f"🔥 No distractions, just pure derivatives trading evolution!")
        print(f"\n🎤 Your Key Line:")
        print(f'   "Q2 systematic derivatives trading: 3 consecutive wins, 100% win rate,')
        print(f'    369% improvement from Q1. Data-driven, disciplined, profitable."')
        print("\n" + "=" * 80 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
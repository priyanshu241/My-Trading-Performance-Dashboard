"""
Analytics Module - DERIVATIVES ONLY
Calculate all trading performance metrics and statistics
"""

import numpy as np
import pandas as pd
from data_processor import TradingDataProcessor

class TradingAnalytics:
    """Calculate comprehensive trading analytics for derivatives"""
    
    def __init__(self):
        self.processor = TradingDataProcessor()
        self.df = self.processor.create_monthly_dataframe()
        
    def calculate_all_metrics(self):
        """Calculate all performance metrics"""
        metrics = {}
        
        # Basic P&L metrics
        metrics['total_pnl'] = self.df['Total_PnL'].sum()
        metrics['derivative_total'] = self.df['Derivative_PnL'].sum()
        
        # Win rate metrics
        traded_months = self.df[self.df['Total_PnL'] != 0]
        metrics['total_months_traded'] = len(traded_months)
        metrics['profitable_months'] = len(traded_months[traded_months['Total_PnL'] > 0])
        metrics['loss_months'] = len(traded_months[traded_months['Total_PnL'] < 0])
        metrics['win_rate'] = (metrics['profitable_months'] / metrics['total_months_traded'] * 100) if metrics['total_months_traded'] > 0 else 0
        
        # Average metrics
        metrics['avg_profit'] = traded_months[traded_months['Total_PnL'] > 0]['Total_PnL'].mean() if metrics['profitable_months'] > 0 else 0
        metrics['avg_loss'] = traded_months[traded_months['Total_PnL'] < 0]['Total_PnL'].mean() if metrics['loss_months'] > 0 else 0
        
        # Profit factor
        gross_profit = traded_months[traded_months['Total_PnL'] > 0]['Total_PnL'].sum()
        gross_loss = abs(traded_months[traded_months['Total_PnL'] < 0]['Total_PnL'].sum())
        metrics['gross_profit'] = gross_profit
        metrics['gross_loss'] = gross_loss
        metrics['profit_factor'] = gross_profit / gross_loss if gross_loss > 0 else 0
        
        # Volatility metrics
        returns = traded_months['Total_PnL'].values
        metrics['volatility'] = np.std(returns)
        metrics['avg_monthly_return'] = np.mean(returns)
        
        # Sharpe ratio (assuming risk-free rate = 0 for simplicity)
        metrics['sharpe_ratio'] = metrics['avg_monthly_return'] / metrics['volatility'] if metrics['volatility'] > 0 else 0
        
        # Quarterly metrics
        quarterly = self.processor.get_quarterly_summary()
        metrics['q1_pnl'] = quarterly.loc['Q1', 'Total_PnL'] if 'Q1' in quarterly.index else 0
        metrics['q2_pnl'] = quarterly.loc['Q2', 'Total_PnL'] if 'Q2' in quarterly.index else 0
        metrics['q3_pnl'] = quarterly.loc['Q3', 'Total_PnL'] if 'Q3' in quarterly.index else 0
        
        # Improvement metrics
        if metrics['q1_pnl'] != 0:
            metrics['q1_to_q2_improvement'] = ((metrics['q2_pnl'] - metrics['q1_pnl']) / abs(metrics['q1_pnl']) * 100)
        else:
            metrics['q1_to_q2_improvement'] = 0
        
        # Trading style metrics
        style_summary = self.processor.get_trading_style_summary()
        metrics['systematic_pnl'] = style_summary['Systematic']['total_pnl']
        metrics['systematic_win_rate'] = style_summary['Systematic']['win_rate']
        metrics['systematic_months'] = style_summary['Systematic']['months']
        metrics['systematic_profitable_months'] = style_summary['Systematic']['profitable_months']
        
        metrics['learning_pnl'] = style_summary['Learning']['total_pnl']
        metrics['learning_win_rate'] = style_summary['Learning']['win_rate']
        metrics['learning_months'] = style_summary['Learning']['months']
        
        # Consistency score
        metrics['consistency_score'] = metrics['systematic_win_rate']
        
        # Best and worst months
        best_worst = self.processor.get_best_worst_months()
        metrics['best_month'] = best_worst['best']['month']
        metrics['best_month_pnl'] = best_worst['best']['pnl']
        metrics['worst_month'] = best_worst['worst']['month']
        metrics['worst_month_pnl'] = best_worst['worst']['pnl']
        
        # Drawdown metrics
        drawdown = self.processor.calculate_drawdown()
        metrics['max_drawdown'] = drawdown['max_drawdown']
        metrics['drawdown_peak_month'] = drawdown['peak_month']
        metrics['drawdown_trough_month'] = drawdown['trough_month']
        metrics['recovery_amount'] = drawdown['recovery']
        
        # Consecutive profitable months
        metrics['max_consecutive_profits'] = self._calculate_max_consecutive_profits()
        
        # Risk-adjusted return
        metrics['risk_adjusted_return'] = metrics['total_pnl'] / metrics['volatility'] if metrics['volatility'] > 0 else 0
        
        return metrics
    
    def _calculate_max_consecutive_profits(self):
        """Calculate maximum consecutive profitable months"""
        traded_months = self.df[self.df['Total_PnL'] != 0]['Total_PnL'].values
        
        max_consecutive = 0
        current_consecutive = 0
        
        for pnl in traded_months:
            if pnl > 0:
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
            else:
                current_consecutive = 0
        
        return max_consecutive
    
    def get_monthly_performance_summary(self):
        """Get detailed monthly performance summary"""
        df = self.df.copy()
        
        summary = []
        for _, row in df.iterrows():
            if row['Total_PnL'] != 0:
                month_data = {
                    'Month': row['Month'],
                    'Quarter': row['Quarter'],
                    'Trading_Style': row['Trading_Style'],
                    'PnL': row['Derivative_PnL'],
                    'Cumulative_PnL': row['Cumulative_PnL'],
                    'Status': 'Profit' if row['Total_PnL'] > 0 else 'Loss'
                }
                summary.append(month_data)
        
        return pd.DataFrame(summary)
    
    def calculate_roi_estimate(self, estimated_capital=100000):
        """Estimate ROI based on total P&L"""
        metrics = self.calculate_all_metrics()
        total_pnl = metrics['total_pnl']
        
        roi = (total_pnl / estimated_capital) * 100
        
        return {
            'estimated_capital': estimated_capital,
            'total_pnl': total_pnl,
            'roi_percentage': roi
        }
    
    def get_learning_insights(self):
        """Extract key learning insights from data"""
        metrics = self.calculate_all_metrics()
        
        insights = {
            'what_worked': [
                f"Systematic derivative trading in Q2 generated ₹{metrics['systematic_pnl']:,.2f} with {metrics['systematic_win_rate']:.0f}% win rate",
                f"Q2 achieved {metrics['systematic_profitable_months']} consecutive profitable months through disciplined execution",
                f"Performance improved by {metrics['q1_to_q2_improvement']:.0f}% from Q1 to Q2",
                f"Maintained {metrics['consistency_score']:.0f}% consistency in systematic approach",
                "Focused exclusively on derivatives after analyzing performance data"
            ],
            'what_didnt_work': [
                f"Q1 learning phase resulted in ₹{abs(metrics['q1_pnl']):,.2f} in losses",
                "Initial lack of systematic approach led to inconsistent results",
                "October showed vulnerability when discipline waned",
                "Need for continuous adherence to systematic rules"
            ],
            'risk_management': [
                "Identified learning curve early and accepted Q1 as education phase",
                "Developed systematic approach based on data analysis",
                f"Recovered strongly in Q2 with {metrics['q1_to_q2_improvement']:.0f}% improvement",
                "Demonstrated ability to execute consistently when disciplined",
                "Focus on single segment (derivatives) rather than diversification"
            ],
            'key_metrics': {
                'Net P&L': f"₹{metrics['total_pnl']:,.2f}",
                'Overall Win Rate': f"{metrics['win_rate']:.0f}%",
                'Systematic Win Rate': f"{metrics['systematic_win_rate']:.0f}%",
                'Profit Factor': f"{metrics['profit_factor']:.2f}",
                'Q1 to Q2 Improvement': f"+{metrics['q1_to_q2_improvement']:.0f}%",
                'Max Consecutive Profits': f"{metrics['max_consecutive_profits']} months"
            }
        }
        
        return insights
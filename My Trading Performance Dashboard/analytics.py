"""
Analytics Module
Calculate all trading performance metrics and statistics
"""

import numpy as np
import pandas as pd
from data_processor import TradingDataProcessor

class TradingAnalytics:
    """Calculate comprehensive trading analytics"""
    
    def __init__(self):
        self.processor = TradingDataProcessor()
        self.df = self.processor.create_monthly_dataframe()
        
    def calculate_all_metrics(self):
        """Calculate all performance metrics"""
        metrics = {}
        
        # Basic P&L metrics
        metrics['total_pnl'] = self.df['Total_PnL'].sum()
        metrics['kotak_derivative_total'] = self.df['Kotak_Derivative'].sum()
        metrics['kotak_commodity_total'] = self.df['Kotak_Commodity'].sum()
        metrics['groww_total'] = self.df['Groww_Derivative'].sum()
        
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
        
        metrics['emotional_pnl'] = style_summary['Emotional']['total_pnl']
        metrics['emotional_win_rate'] = style_summary['Emotional']['win_rate']
        metrics['emotional_months'] = style_summary['Emotional']['months']
        
        # Consistency score (percentage of months that were profitable in systematic phase)
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
        
        # Platform comparison
        platform_comp = self.processor.get_platform_comparison()
        metrics['kotak_total'] = platform_comp['Kotak']['total_pnl']
        metrics['kotak_months'] = platform_comp['Kotak']['months_traded']
        metrics['kotak_avg_per_month'] = platform_comp['Kotak']['avg_per_month']
        metrics['groww_months'] = platform_comp['Groww']['months_traded']
        metrics['groww_avg_per_month'] = platform_comp['Groww']['avg_per_month']
        
        # Segment-wise win rates
        segment_summary = self.processor.get_segment_summary()
        for segment, data in segment_summary.items():
            if data['months_traded'] > 0:
                metrics[f'{segment}_win_rate'] = (data['profitable_months'] / data['months_traded'] * 100)
            else:
                metrics[f'{segment}_win_rate'] = 0
        
        # Risk-adjusted return (return per unit of volatility)
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
            if row['Total_PnL'] != 0:  # Only include months with trades
                month_data = {
                    'Month': row['Month'],
                    'Quarter': row['Quarter'],
                    'Trading_Style': row['Trading_Style'],
                    'Kotak_Derivative': row['Kotak_Derivative'],
                    'Kotak_Commodity': row['Kotak_Commodity'],
                    'Groww_Derivative': row['Groww_Derivative'],
                    'Total_PnL': row['Total_PnL'],
                    'Cumulative_PnL': row['Cumulative_PnL'],
                    'Status': 'Profit' if row['Total_PnL'] > 0 else 'Loss'
                }
                summary.append(month_data)
        
        return pd.DataFrame(summary)
    
    def calculate_roi_estimate(self, estimated_capital=100000):
        """Estimate ROI based on total P&L (assuming capital deployed)"""
        metrics = self.calculate_all_metrics()
        total_pnl = metrics['total_pnl']
        
        roi = (total_pnl / estimated_capital) * 100
        
        # Calculate segment-wise ROI
        segment_roi = {
            'Kotak_Derivative': (metrics['kotak_derivative_total'] / (estimated_capital * 0.4)) * 100,
            'Kotak_Commodity': (metrics['kotak_commodity_total'] / (estimated_capital * 0.3)) * 100,
            'Groww': (metrics['groww_total'] / (estimated_capital * 0.3)) * 100,
            'Overall': roi
        }
        
        return segment_roi
    
    def get_learning_insights(self):
        """Extract key learning insights from data"""
        metrics = self.calculate_all_metrics()
        
        insights = {
            'what_worked': [
                f"Systematic derivative trading generated ₹{metrics['systematic_pnl']:,.2f} with {metrics['systematic_win_rate']:.0f}% win rate",
                f"Q2 showed {metrics['systematic_profitable_months']} consecutive profitable months",
                f"Improved performance by {metrics['q1_to_q2_improvement']:.0f}% from Q1 to Q2",
                f"Maintained consistency in systematic approach with {metrics['consistency_score']:.0f}% success rate"
            ],
            'what_didnt_work': [
                f"Commodity trading resulted in ₹{abs(metrics['kotak_commodity_total']):,.2f} loss",
                f"Emotional trading on Groww lost ₹{abs(metrics['emotional_pnl']):,.2f}",
                f"Q1 learning phase had ₹{abs(metrics['q1_pnl']):,.2f} in losses",
                f"Platform switching (Groww) during emotional periods led to poor decisions"
            ],
            'risk_management': [
                "Identified commodity trading weakness and stopped after August",
                "Recognized emotional trading patterns and adapted strategy",
                f"Recovered ₹{metrics['recovery_amount']:,.2f} from maximum drawdown",
                "Focused on strengths (derivatives) and avoided weaknesses (commodities)"
            ],
            'key_metrics': {
                'Overall Win Rate': f"{metrics['win_rate']:.0f}%",
                'Systematic Win Rate': f"{metrics['systematic_win_rate']:.0f}%",
                'Profit Factor': f"{metrics['profit_factor']:.2f}",
                'Q1 to Q2 Improvement': f"{metrics['q1_to_q2_improvement']:.0f}%",
                'Max Consecutive Profits': f"{metrics['max_consecutive_profits']} months"
            }
        }
        
        return insights
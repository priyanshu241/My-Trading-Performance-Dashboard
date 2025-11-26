"""
Data Processing Module - DERIVATIVES ONLY
Processes Kotak Neo derivatives trading data into structured formats
"""

import pandas as pd
import numpy as np
from trading_data import *
from config import MONTHS_ORDER, QUARTERS

class TradingDataProcessor:
    """Process and structure derivatives trading data for analysis"""
    
    def __init__(self):
        self.kotak_derivative = kotak_derivative
        self.months = MONTHS_ORDER
        
    def create_monthly_dataframe(self):
        """Create comprehensive monthly dataframe"""
        data = []
        
        for month in self.months:
            row = {
                'Month': month,
                'Derivative_PnL': self.kotak_derivative.get(month, 0),
                'Total_PnL': self.kotak_derivative.get(month, 0)
            }
            
            # Add trading style classification
            if month in TRADING_STYLES['systematic']['months']:
                row['Trading_Style'] = 'Systematic'
            elif month in TRADING_STYLES['learning']['months']:
                row['Trading_Style'] = 'Learning'
            else:
                row['Trading_Style'] = 'Normal'
            
            # Add quarter classification
            for quarter, months in QUARTERS.items():
                if month in months:
                    row['Quarter'] = quarter
                    break
            
            data.append(row)
        
        df = pd.DataFrame(data)
        
        # Calculate cumulative P&L
        df['Cumulative_PnL'] = df['Total_PnL'].cumsum()
        
        return df
    
    def get_segment_summary(self):
        """Get summary statistics"""
        summary = {
            'Derivatives': {
                'total': sum(self.kotak_derivative.values()),
                'months_traded': sum(1 for v in self.kotak_derivative.values() if v != 0),
                'profitable_months': sum(1 for v in self.kotak_derivative.values() if v > 0),
                'loss_months': sum(1 for v in self.kotak_derivative.values() if v < 0),
                'avg_profit': np.mean([v for v in self.kotak_derivative.values() if v > 0]) if any(v > 0 for v in self.kotak_derivative.values()) else 0,
                'avg_loss': np.mean([v for v in self.kotak_derivative.values() if v < 0]) if any(v < 0 for v in self.kotak_derivative.values()) else 0
            }
        }
        
        return summary
    
    def get_quarterly_summary(self):
        """Get summary by quarter"""
        df = self.create_monthly_dataframe()
        quarterly = df.groupby('Quarter').agg({
            'Total_PnL': 'sum',
            'Derivative_PnL': 'sum',
            'Month': 'count'
        }).rename(columns={'Month': 'Months_Traded'})
        
        return quarterly
    
    def get_trading_style_summary(self):
        """Get summary by trading style"""
        df = self.create_monthly_dataframe()
        
        systematic_data = df[df['Trading_Style'] == 'Systematic']
        learning_data = df[df['Trading_Style'] == 'Learning']
        
        summary = {
            'Systematic': {
                'total_pnl': systematic_data['Derivative_PnL'].sum(),
                'months': len(systematic_data),
                'profitable_months': len(systematic_data[systematic_data['Derivative_PnL'] > 0]),
                'avg_pnl': systematic_data['Derivative_PnL'].mean(),
                'win_rate': (len(systematic_data[systematic_data['Derivative_PnL'] > 0]) / len(systematic_data) * 100) if len(systematic_data) > 0 else 0
            },
            'Learning': {
                'total_pnl': learning_data['Derivative_PnL'].sum(),
                'months': len(learning_data),
                'profitable_months': len(learning_data[learning_data['Derivative_PnL'] > 0]),
                'avg_pnl': learning_data['Derivative_PnL'].mean(),
                'win_rate': (len(learning_data[learning_data['Derivative_PnL'] > 0]) / len(learning_data) * 100) if len(learning_data) > 0 else 0
            }
        }
        
        return summary
    
    def get_best_worst_months(self):
        """Get best and worst performing months"""
        df = self.create_monthly_dataframe()
        df_traded = df[df['Total_PnL'] != 0].copy()
        
        best_month = df_traded.loc[df_traded['Total_PnL'].idxmax()]
        worst_month = df_traded.loc[df_traded['Total_PnL'].idxmin()]
        
        return {
            'best': {
                'month': best_month['Month'],
                'pnl': best_month['Total_PnL']
            },
            'worst': {
                'month': worst_month['Month'],
                'pnl': worst_month['Total_PnL']
            }
        }
    
    def calculate_drawdown(self):
        """Calculate maximum drawdown"""
        df = self.create_monthly_dataframe()
        cumulative = df['Cumulative_PnL'].values
        
        running_max = np.maximum.accumulate(cumulative)
        drawdown = cumulative - running_max
        max_drawdown = np.min(drawdown)
        
        # Find drawdown period
        max_dd_idx = np.argmin(drawdown)
        peak_idx = np.argmax(cumulative[:max_dd_idx+1]) if max_dd_idx > 0 else 0
        
        return {
            'max_drawdown': max_drawdown,
            'peak_month': df.iloc[peak_idx]['Month'],
            'trough_month': df.iloc[max_dd_idx]['Month'],
            'recovery': cumulative[-1] - cumulative[max_dd_idx] if max_dd_idx < len(cumulative) - 1 else 0
        }
"""
Data Processing Module
Processes raw trading data into structured formats for analysis
"""

import pandas as pd
import numpy as np
from trading_data import *
from config import MONTHS_ORDER, QUARTERS

class TradingDataProcessor:
    """Process and structure trading data for analysis"""
    
    def __init__(self):
        self.kotak_derivative = kotak_derivative
        self.kotak_commodity = kotak_commodity
        self.groww_derivative = groww_derivative
        self.months = MONTHS_ORDER
        
    def create_monthly_dataframe(self):
        """Create comprehensive monthly dataframe"""
        data = []
        
        for month in self.months:
            row = {
                'Month': month,
                'Kotak_Derivative': self.kotak_derivative.get(month, 0),
                'Kotak_Commodity': self.kotak_commodity.get(month, 0),
                'Groww_Derivative': self.groww_derivative.get(month, 0),
                'Total_Kotak': self.kotak_derivative.get(month, 0) + self.kotak_commodity.get(month, 0),
                'Total_PnL': (self.kotak_derivative.get(month, 0) + 
                             self.kotak_commodity.get(month, 0) + 
                             self.groww_derivative.get(month, 0))
            }
            
            # Add trading style classification
            if month in TRADING_STYLES['systematic']['months']:
                row['Trading_Style'] = 'Systematic'
            elif month in TRADING_STYLES['emotional']['months']:
                row['Trading_Style'] = 'Emotional'
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
        """Get summary by segment"""
        summary = {
            'Kotak_Derivative': {
                'total': sum(self.kotak_derivative.values()),
                'months_traded': sum(1 for v in self.kotak_derivative.values() if v != 0),
                'profitable_months': sum(1 for v in self.kotak_derivative.values() if v > 0),
                'loss_months': sum(1 for v in self.kotak_derivative.values() if v < 0)
            },
            'Kotak_Commodity': {
                'total': sum(self.kotak_commodity.values()),
                'months_traded': sum(1 for v in self.kotak_commodity.values() if v != 0),
                'profitable_months': sum(1 for v in self.kotak_commodity.values() if v > 0),
                'loss_months': sum(1 for v in self.kotak_commodity.values() if v < 0)
            },
            'Groww_Derivative': {
                'total': sum(self.groww_derivative.values()),
                'months_traded': sum(1 for v in self.groww_derivative.values() if v != 0),
                'profitable_months': sum(1 for v in self.groww_derivative.values() if v > 0),
                'loss_months': sum(1 for v in self.groww_derivative.values() if v < 0)
            }
        }
        
        return summary
    
    def get_quarterly_summary(self):
        """Get summary by quarter"""
        df = self.create_monthly_dataframe()
        quarterly = df.groupby('Quarter').agg({
            'Total_PnL': 'sum',
            'Kotak_Derivative': 'sum',
            'Kotak_Commodity': 'sum',
            'Groww_Derivative': 'sum',
            'Month': 'count'
        }).rename(columns={'Month': 'Months_Traded'})
        
        return quarterly
    
    def get_trading_style_summary(self):
        """Get summary by trading style"""
        df = self.create_monthly_dataframe()
        
        systematic_data = df[df['Trading_Style'] == 'Systematic']
        emotional_data = df[df['Trading_Style'] == 'Emotional']
        
        summary = {
            'Systematic': {
                'total_pnl': systematic_data['Kotak_Derivative'].sum(),
                'months': len(systematic_data),
                'profitable_months': len(systematic_data[systematic_data['Kotak_Derivative'] > 0]),
                'avg_pnl': systematic_data['Kotak_Derivative'].mean(),
                'win_rate': (len(systematic_data[systematic_data['Kotak_Derivative'] > 0]) / len(systematic_data) * 100) if len(systematic_data) > 0 else 0
            },
            'Emotional': {
                'total_pnl': emotional_data['Groww_Derivative'].sum(),
                'months': len(emotional_data),
                'profitable_months': len(emotional_data[emotional_data['Groww_Derivative'] > 0]),
                'avg_pnl': emotional_data['Groww_Derivative'].mean(),
                'win_rate': (len(emotional_data[emotional_data['Groww_Derivative'] > 0]) / len(emotional_data) * 100) if len(emotional_data) > 0 else 0
            }
        }
        
        return summary
    
    def get_platform_comparison(self):
        """Compare platforms"""
        df = self.create_monthly_dataframe()
        
        kotak_total = df['Total_Kotak'].sum()
        groww_total = df['Groww_Derivative'].sum()
        
        kotak_months = len(df[df['Total_Kotak'] != 0])
        groww_months = len(df[df['Groww_Derivative'] != 0])
        
        comparison = {
            'Kotak': {
                'total_pnl': kotak_total,
                'months_traded': kotak_months,
                'avg_per_month': kotak_total / kotak_months if kotak_months > 0 else 0,
                'profitable_months': len(df[df['Total_Kotak'] > 0])
            },
            'Groww': {
                'total_pnl': groww_total,
                'months_traded': groww_months,
                'avg_per_month': groww_total / groww_months if groww_months > 0 else 0,
                'profitable_months': len(df[df['Groww_Derivative'] > 0])
            }
        }
        
        return comparison
    
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
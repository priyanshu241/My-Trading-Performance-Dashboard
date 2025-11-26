"""
Visualization Module - DERIVATIVES ONLY
Create clean, professional visualizations for derivatives trading
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import pandas as pd
from data_processor import TradingDataProcessor
from analytics import TradingAnalytics
from config import COLORS, CHART_STYLE, CHARTS_DIR
import os

plt.style.use('dark_background')
sns.set_palette("husl")

class TradingVisualizer:
    """Create professional trading visualizations"""
    
    def __init__(self):
        self.processor = TradingDataProcessor()
        self.analytics = TradingAnalytics()
        self.df = self.processor.create_monthly_dataframe()
        self.colors = COLORS
        self.style = CHART_STYLE
        
    def _apply_style(self, ax, title):
        """Apply consistent styling"""
        ax.set_title(title, fontsize=self.style['title_size'], fontweight='bold', pad=20, color=self.style['text_color'])
        ax.set_facecolor(self.style['background_color'])
        ax.tick_params(colors=self.style['text_color'], labelsize=self.style['font_size'])
        ax.spines['bottom'].set_color(self.style['grid_color'])
        ax.spines['left'].set_color(self.style['grid_color'])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, alpha=self.style['grid_alpha'], color=self.style['grid_color'], linestyle='--')
        
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_color(self.style['text_color'])
    
    def create_monthly_pnl_chart(self):
        """Monthly P&L bar chart"""
        fig, ax = plt.subplots(figsize=self.style['figure_size'], dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        months = self.df['Month']
        pnl = self.df['Derivative_PnL']
        
        colors_list = [self.colors['profit'] if p > 0 else self.colors['loss'] if p < 0 else self.colors['neutral'] for p in pnl]
        
        bars = ax.bar(months, pnl, color=colors_list, edgecolor='white', linewidth=1.5, width=0.7)
        
        # Add value labels
        for bar, value in zip(bars, pnl):
            if value != 0:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + (abs(height) * 0.05), 
                       f'₹{value:,.0f}', ha='center', va='bottom' if value > 0 else 'top', 
                       fontsize=10, fontweight='bold', color=self.style['text_color'])
        
        ax.axhline(y=0, color=self.style['grid_color'], linestyle='-', linewidth=2)
        ax.set_xlabel('Month', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_ylabel('P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        
        self._apply_style(ax, 'Monthly Derivatives Performance - Kotak Neo')
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'monthly_pnl.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
        
    def create_cumulative_pnl_chart(self):
        """Cumulative P&L line chart"""
        fig, ax = plt.subplots(figsize=self.style['figure_size'], dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        months = self.df['Month']
        cumulative = self.df['Cumulative_PnL']
        
        ax.plot(months, cumulative, marker='o', linewidth=3, markersize=12, color=self.colors['profit'], label='Cumulative P&L')
        ax.fill_between(months, cumulative, alpha=0.3, color=self.colors['profit'])
        
        ax.axhline(y=0, color=self.colors['loss'], linestyle='--', linewidth=2, label='Break-even')
        
        # Annotate key points
        for i, (month, value) in enumerate(zip(months, cumulative)):
            if i % 2 == 0:  # Annotate every other month to avoid clutter
                ax.annotate(f'₹{value:,.0f}', (month, value), textcoords="offset points", 
                           xytext=(0,15), ha='center', fontsize=9, color=self.style['text_color'])
        
        ax.set_xlabel('Month', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_ylabel('Cumulative P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.legend(fontsize=self.style['legend_size'], framealpha=0.9, facecolor=self.style['background_color'], edgecolor=self.colors['profit'])
        
        self._apply_style(ax, 'Trading Journey: Cumulative P&L Evolution')
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'cumulative_pnl.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_quarterly_comparison_chart(self):
        """Quarterly comparison"""
        quarterly = self.processor.get_quarterly_summary()
        
        fig, ax = plt.subplots(figsize=(12, 7), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        quarters = quarterly.index
        pnl = quarterly['Total_PnL']
        colors_list = [self.colors['loss'] if p < 0 else self.colors['profit'] for p in pnl]
        
        bars = ax.bar(quarters, pnl, color=colors_list, edgecolor='white', linewidth=2, width=0.6)
        
        for bar, value in zip(bars, pnl):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + (abs(height) * 0.05), 
                   f'₹{value:,.0f}', ha='center', va='bottom' if value > 0 else 'top', 
                   fontsize=13, fontweight='bold', color=self.style['text_color'])
        
        ax.axhline(y=0, color=self.style['grid_color'], linestyle='-', linewidth=2)
        ax.set_xlabel('Quarter', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_ylabel('Total P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        
        self._apply_style(ax, 'Quarterly Performance: Q1 Learning → Q2 Systematic')
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'quarterly_comparison.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_learning_vs_systematic_chart(self):
        """Learning phase vs systematic trading comparison"""
        style_summary = self.processor.get_trading_style_summary()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        # P&L Comparison
        styles = ['Q1\nLearning Phase', 'Q2\nSystematic Trading']
        pnls = [style_summary['Learning']['total_pnl'], style_summary['Systematic']['total_pnl']]
        colors_comp = [self.colors['learning'], self.colors['systematic']]
        
        bars1 = ax1.bar(styles, pnls, color=colors_comp, edgecolor='white', linewidth=2, width=0.6)
        
        for bar, value in zip(bars1, pnls):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + (abs(height) * 0.05), 
                    f'₹{value:,.0f}', ha='center', va='bottom' if value > 0 else 'top', 
                    fontsize=13, fontweight='bold', color=self.style['text_color'])
        
        ax1.axhline(y=0, color=self.style['grid_color'], linestyle='-', linewidth=2)
        ax1.set_ylabel('Total P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        self._apply_style(ax1, 'P&L Comparison')
        
        # Win Rate Comparison
        win_rates = [style_summary['Learning']['win_rate'], style_summary['Systematic']['win_rate']]
        bars2 = ax2.bar(styles, win_rates, color=colors_comp, edgecolor='white', linewidth=2, width=0.6)
        
        for bar, value in zip(bars2, win_rates):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 5, f'{value:.0f}%', 
                    ha='center', va='bottom', fontsize=13, fontweight='bold', color=self.style['text_color'])
        
        ax2.set_ylabel('Win Rate (%)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax2.set_ylim(0, 110)
        self._apply_style(ax2, 'Win Rate Comparison')
        
        fig.suptitle('Learning Phase vs Systematic Trading Evolution', fontsize=16, fontweight='bold', color=self.style['text_color'], y=0.98)
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'learning_vs_systematic.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_consistency_heatmap(self):
        """Monthly consistency heatmap"""
        fig, ax = plt.subplots(figsize=(14, 6), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        months = self.df['Month'].values
        pnl = self.df['Derivative_PnL'].values
        
        data_matrix = pnl.reshape(1, -1)
        
        cmap = sns.diverging_palette(10, 130, as_cmap=True)
        sns.heatmap(data_matrix, annot=True, fmt='.0f', cmap=cmap, center=0, 
                   xticklabels=months, yticklabels=['P&L'], 
                   cbar_kws={'label': 'P&L (₹)'}, linewidths=2, linecolor='white', 
                   ax=ax, annot_kws={'fontsize': 11, 'fontweight': 'bold'})
        
        ax.set_title('Monthly Performance Heatmap', fontsize=self.style['title_size'], fontweight='bold', pad=20, color=self.style['text_color'])
        ax.set_xlabel('Month', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.tick_params(colors=self.style['text_color'])
        
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=self.style['font_size'], colors=self.style['text_color'])
        cbar.set_label('P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'])
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'consistency_heatmap.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_win_loss_distribution(self):
        """Win/loss distribution"""
        traded_months = self.df[self.df['Total_PnL'] != 0]
        
        wins = len(traded_months[traded_months['Total_PnL'] > 0])
        losses = len(traded_months[traded_months['Total_PnL'] < 0])
        
        fig, ax = plt.subplots(figsize=(10, 8), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        labels = ['Profitable Months', 'Loss Months']
        sizes = [wins, losses]
        colors_list = [self.colors['profit'], self.colors['loss']]
        explode = (0.1, 0)
        
        wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', 
                                          startangle=90, colors=colors_list, textprops={'color': 'white', 'fontsize': 12})
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(14)
        
        for text in texts:
            text.set_fontsize(13)
            text.set_fontweight('bold')
        
        ax.set_title('Win/Loss Month Distribution', fontsize=self.style['title_size'], fontweight='bold', pad=20, color=self.style['text_color'])
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'win_loss_distribution.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_drawdown_recovery_chart(self):
        """Drawdown and recovery"""
        fig, ax = plt.subplots(figsize=self.style['figure_size'], dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        months = self.df['Month']
        cumulative = self.df['Cumulative_PnL']
        
        running_max = np.maximum.accumulate(cumulative)
        drawdown = cumulative - running_max
        
        ax.fill_between(months, 0, drawdown, color=self.colors['loss'], alpha=0.4, label='Drawdown')
        ax.plot(months, drawdown, color=self.colors['loss'], linewidth=2, marker='o', markersize=8)
        
        ax.axhline(y=0, color=self.colors['profit'], linestyle='--', linewidth=2)
        
        min_dd_idx = np.argmin(drawdown)
        ax.annotate(f'Max DD: ₹{drawdown.iloc[min_dd_idx]:,.0f}', 
                   xy=(months.iloc[min_dd_idx], drawdown.iloc[min_dd_idx]), 
                   xytext=(10, -30), textcoords='offset points', fontsize=11, fontweight='bold', 
                   color=self.colors['loss'], 
                   bbox=dict(boxstyle='round,pad=0.5', facecolor=self.style['background_color'], 
                            edgecolor=self.colors['loss'], linewidth=2),
                   arrowprops=dict(arrowstyle='->', color=self.colors['loss'], lw=2))
        
        ax.set_xlabel('Month', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_ylabel('Drawdown (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.legend(fontsize=self.style['legend_size'], framealpha=0.9, facecolor=self.style['background_color'], edgecolor=self.colors['loss'])
        
        self._apply_style(ax, 'Drawdown Analysis & Recovery Path')
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'drawdown_recovery.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def generate_all_visualizations(self):
        """Generate all visualizations"""
        print("Generating visualizations...")
        
        self.create_monthly_pnl_chart()
        print("✓ Monthly P&L chart created")
        
        self.create_cumulative_pnl_chart()
        print("✓ Cumulative P&L chart created")
        
        self.create_quarterly_comparison_chart()
        print("✓ Quarterly comparison chart created")
        
        self.create_learning_vs_systematic_chart()
        print("✓ Learning vs Systematic chart created")
        
        self.create_consistency_heatmap()
        print("✓ Consistency heatmap created")
        
        self.create_win_loss_distribution()
        print("✓ Win/Loss distribution chart created")
        
        self.create_drawdown_recovery_chart()
        print("✓ Drawdown recovery chart created")
        
        print(f"\n✅ All visualizations saved to: {CHARTS_DIR}")
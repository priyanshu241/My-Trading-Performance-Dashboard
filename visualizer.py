"""
Visualization Module
Create all charts and visualizations for the dashboard
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

# Set style
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
        """Apply consistent styling to all charts"""
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
        """Create monthly P&L bar chart"""
        fig, ax = plt.subplots(figsize=self.style['figure_size'], dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        months = self.df['Month']
        x = np.arange(len(months))
        width = 0.25
        
        kotak_deriv = self.df['Kotak_Derivative']
        kotak_comm = self.df['Kotak_Commodity']
        groww = self.df['Groww_Derivative']
        
        ax.bar(x - width, kotak_deriv, width, label='Kotak Derivatives', color=self.colors['kotak_derivative'], edgecolor='white', linewidth=0.5)
        ax.bar(x, kotak_comm, width, label='Kotak Commodities', color=self.colors['kotak_commodity'], edgecolor='white', linewidth=0.5)
        ax.bar(x + width, groww, width, label='Groww Derivatives', color=self.colors['groww_derivative'], edgecolor='white', linewidth=0.5)
        
        ax.axhline(y=0, color=self.style['grid_color'], linestyle='-', linewidth=2)
        ax.set_xlabel('Month', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_ylabel('P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(months)
        ax.legend(fontsize=self.style['legend_size'], framealpha=0.9, facecolor=self.style['background_color'], edgecolor=self.colors['profit'])
        
        self._apply_style(ax, 'Monthly Performance by Platform & Segment')
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'monthly_pnl.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
        
    def create_cumulative_pnl_chart(self):
        """Create cumulative P&L line chart"""
        fig, ax = plt.subplots(figsize=self.style['figure_size'], dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        months = self.df['Month']
        cumulative = self.df['Cumulative_PnL']
        
        ax.plot(months, cumulative, marker='o', linewidth=3, markersize=10, color=self.colors['profit'], label='Cumulative P&L')
        ax.fill_between(months, cumulative, alpha=0.3, color=self.colors['profit'])
        
        ax.axhline(y=0, color=self.colors['loss'], linestyle='--', linewidth=2, label='Break-even')
        
        for i, (month, value) in enumerate(zip(months, cumulative)):
            ax.annotate(f'₹{value:,.0f}', (month, value), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color=self.style['text_color'])
        
        ax.set_xlabel('Month', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_ylabel('Cumulative P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.legend(fontsize=self.style['legend_size'], framealpha=0.9, facecolor=self.style['background_color'], edgecolor=self.colors['profit'])
        
        self._apply_style(ax, 'Trading Journey: Cumulative P&L Over Time')
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'cumulative_pnl.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_quarterly_comparison_chart(self):
        """Create quarterly comparison bar chart"""
        quarterly = self.processor.get_quarterly_summary()
        
        fig, ax = plt.subplots(figsize=(12, 7), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        quarters = quarterly.index
        pnl = quarterly['Total_PnL']
        colors_list = [self.colors['loss'] if p < 0 else self.colors['profit'] for p in pnl]
        
        bars = ax.bar(quarters, pnl, color=colors_list, edgecolor='white', linewidth=1.5, width=0.6)
        
        for bar, value in zip(bars, pnl):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + (abs(height) * 0.05), f'₹{value:,.0f}', ha='center', va='bottom' if value > 0 else 'top', fontsize=11, fontweight='bold', color=self.style['text_color'])
        
        ax.axhline(y=0, color=self.style['grid_color'], linestyle='-', linewidth=2)
        ax.set_xlabel('Quarter', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_ylabel('Total P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        
        self._apply_style(ax, 'Quarterly Performance Comparison')
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'quarterly_comparison.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_segment_pie_chart(self):
        """Create segment distribution pie chart"""
        segment_summary = self.processor.get_segment_summary()
        
        labels = []
        values = []
        colors_list = []
        
        for segment, data in segment_summary.items():
            labels.append(segment.replace('_', ' '))
            values.append(abs(data['total']))
            if 'Derivative' in segment:
                colors_list.append(self.colors['kotak_derivative'] if 'Kotak' in segment else self.colors['groww_derivative'])
            else:
                colors_list.append(self.colors['kotak_commodity'])
        
        fig, ax = plt.subplots(figsize=(12, 8), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors_list, textprops={'color': 'white', 'fontsize': 11}, explode=[0.05, 0.05, 0.05])
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(12)
        
        for text in texts:
            text.set_fontsize(12)
            text.set_fontweight('bold')
        
        ax.set_title('Segment-wise Exposure Distribution', fontsize=self.style['title_size'], fontweight='bold', pad=20, color=self.style['text_color'])
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'segment_distribution.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_systematic_vs_emotional_chart(self):
        """Create systematic vs emotional trading comparison"""
        style_summary = self.processor.get_trading_style_summary()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        # P&L Comparison
        styles = ['Systematic\nTrading', 'Emotional\nTrading']
        pnls = [style_summary['Systematic']['total_pnl'], style_summary['Emotional']['total_pnl']]
        colors_comp = [self.colors['systematic'], self.colors['emotional']]
        
        bars1 = ax1.bar(styles, pnls, color=colors_comp, edgecolor='white', linewidth=2, width=0.6)
        
        for bar, value in zip(bars1, pnls):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + (abs(height) * 0.05), f'₹{value:,.0f}', ha='center', va='bottom' if value > 0 else 'top', fontsize=13, fontweight='bold', color=self.style['text_color'])
        
        ax1.axhline(y=0, color=self.style['grid_color'], linestyle='-', linewidth=2)
        ax1.set_ylabel('Total P&L (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        self._apply_style(ax1, 'P&L Comparison')
        
        # Win Rate Comparison
        win_rates = [style_summary['Systematic']['win_rate'], style_summary['Emotional']['win_rate']]
        bars2 = ax2.bar(styles, win_rates, color=colors_comp, edgecolor='white', linewidth=2, width=0.6)
        
        for bar, value in zip(bars2, win_rates):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 3, f'{value:.0f}%', ha='center', va='bottom', fontsize=13, fontweight='bold', color=self.style['text_color'])
        
        ax2.set_ylabel('Win Rate (%)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax2.set_ylim(0, 110)
        self._apply_style(ax2, 'Win Rate Comparison')
        
        fig.suptitle('Systematic vs Emotional Trading Analysis', fontsize=16, fontweight='bold', color=self.style['text_color'], y=0.98)
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'systematic_vs_emotional.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def create_consistency_heatmap(self):
        """Create monthly consistency heatmap"""
        fig, ax = plt.subplots(figsize=(14, 6), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        months = self.df['Month'].values
        total_pnl = self.df['Total_PnL'].values
        
        data_matrix = total_pnl.reshape(1, -1)
        
        cmap = sns.diverging_palette(10, 130, as_cmap=True)
        sns.heatmap(data_matrix, annot=True, fmt='.0f', cmap=cmap, center=0, xticklabels=months, yticklabels=['P&L'], cbar_kws={'label': 'P&L (₹)'}, linewidths=2, linecolor='white', ax=ax, annot_kws={'fontsize': 11, 'fontweight': 'bold'})
        
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
        """Create win/loss distribution chart"""
        traded_months = self.df[self.df['Total_PnL'] != 0]
        
        wins = len(traded_months[traded_months['Total_PnL'] > 0])
        losses = len(traded_months[traded_months['Total_PnL'] < 0])
        
        fig, ax = plt.subplots(figsize=(10, 8), dpi=self.style['dpi'])
        fig.patch.set_facecolor(self.style['background_color'])
        
        labels = ['Profitable Months', 'Loss Months']
        sizes = [wins, losses]
        colors_list = [self.colors['profit'], self.colors['loss']]
        explode = (0.1, 0)
        
        wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors_list, textprops={'color': 'white', 'fontsize': 12})
        
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
        """Create drawdown and recovery visualization"""
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
        ax.annotate(f'Max DD: ₹{drawdown.iloc[min_dd_idx]:,.0f}', xy=(months.iloc[min_dd_idx], drawdown.iloc[min_dd_idx]), xytext=(10, -30), textcoords='offset points', fontsize=11, fontweight='bold', color=self.colors['loss'], bbox=dict(boxstyle='round,pad=0.5', facecolor=self.style['background_color'], edgecolor=self.colors['loss'], linewidth=2), arrowprops=dict(arrowstyle='->', color=self.colors['loss'], lw=2))
        
        ax.set_xlabel('Month', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.set_ylabel('Drawdown (₹)', fontsize=self.style['label_size'], color=self.style['text_color'], fontweight='bold')
        ax.legend(fontsize=self.style['legend_size'], framealpha=0.9, facecolor=self.style['background_color'], edgecolor=self.colors['loss'])
        
        self._apply_style(ax, 'Drawdown Analysis & Recovery')
        
        plt.tight_layout()
        plt.savefig(os.path.join(CHARTS_DIR, 'drawdown_recovery.png'), facecolor=self.style['background_color'], dpi=150, bbox_inches='tight')
        plt.close()
    
    def generate_all_visualizations(self):
        """Generate all visualizations at once"""
        print("Generating visualizations...")
        
        self.create_monthly_pnl_chart()
        print("✓ Monthly P&L chart created")
        
        self.create_cumulative_pnl_chart()
        print("✓ Cumulative P&L chart created")
        
        self.create_quarterly_comparison_chart()
        print("✓ Quarterly comparison chart created")
        
        self.create_segment_pie_chart()
        print("✓ Segment distribution chart created")
        
        self.create_systematic_vs_emotional_chart()
        print("✓ Systematic vs Emotional chart created")
        
        self.create_consistency_heatmap()
        print("✓ Consistency heatmap created")
        
        self.create_win_loss_distribution()
        print("✓ Win/Loss distribution chart created")
        
        self.create_drawdown_recovery_chart()
        print("✓ Drawdown recovery chart created")
        
        print(f"\n✅ All visualizations saved to: {CHARTS_DIR}")
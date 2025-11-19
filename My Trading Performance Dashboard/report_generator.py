"""
Report Generator Module
Generate professional HTML report with all insights
"""

import os
from analytics import TradingAnalytics
from data_processor import TradingDataProcessor
from config import HTML_STYLE, REPORT_DIR, CHARTS_DIR
from trading_data import TRADING_METADATA

class ReportGenerator:
    """Generate comprehensive HTML trading report"""
    
    def __init__(self):
        self.analytics = TradingAnalytics()
        self.processor = TradingDataProcessor()
        self.metrics = self.analytics.calculate_all_metrics()
        self.insights = self.analytics.get_learning_insights()
        
    def format_currency(self, value):
        """Format currency values"""
        return f"₹{abs(value):,.2f}"
    
    def format_percentage(self, value):
        """Format percentage values"""
        return f"{value:.1f}%"
    
    def generate_executive_summary(self):
        """Generate executive summary section"""
        html = f"""
        <div class="section">
            <h2>📊 Executive Summary</h2>
            <div class="highlight-box">
                <h3>Trading Evolution: FY {TRADING_METADATA['financial_year']}</h3>
                <p style="font-size: 1.1em; line-height: 1.8;">
                    This dashboard presents my <strong>systematic trading journey</strong> across {self.metrics['total_months_traded']} months of active trading. 
                    Starting with a learning phase in Q1 (losses of {self.format_currency(self.metrics['q1_pnl'])}), I evolved into a <strong>disciplined, 
                    systematic trader</strong> in Q2, generating {self.format_currency(self.metrics['systematic_pnl'])} with a {self.format_percentage(self.metrics['systematic_win_rate'])} win rate.
                </p>
                <p style="font-size: 1.1em; line-height: 1.8; margin-top: 15px;">
                    <strong>Key Achievement:</strong> Demonstrated {self.format_percentage(self.metrics['q1_to_q2_improvement'])} improvement from Q1 to Q2 
                    through data-driven strategy refinement and risk management discipline. Recognized emotional trading patterns early and adapted accordingly.
                </p>
            </div>
        </div>
        """
        return html
    
    def generate_summary_cards(self):
        """Generate summary metric cards"""
        html = """
        <div class="summary-cards">
        """
        
        cards = [
            {
                'title': 'NET P&L',
                'value': self.format_currency(self.metrics['total_pnl']),
                'subtitle': f"Across {self.metrics['total_months_traded']} active months",
                'type': 'profit' if self.metrics['total_pnl'] > 0 else 'loss'
            },
            {
                'title': 'SYSTEMATIC TRADING',
                'value': self.format_currency(self.metrics['systematic_pnl']),
                'subtitle': f"Q2: {self.metrics['systematic_months']} months, {self.format_percentage(self.metrics['systematic_win_rate'])} win rate",
                'type': 'profit'
            },
            {
                'title': 'Q1 TO Q2 IMPROVEMENT',
                'value': f"+{self.format_percentage(self.metrics['q1_to_q2_improvement'])}",
                'subtitle': f"From {self.format_currency(self.metrics['q1_pnl'])} to {self.format_currency(self.metrics['q2_pnl'])}",
                'type': 'info'
            },
            {
                'title': 'OVERALL WIN RATE',
                'value': self.format_percentage(self.metrics['win_rate']),
                'subtitle': f"Profit Factor: {self.metrics['profit_factor']:.2f}",
                'type': 'info'
            },
            {
                'title': 'BEST MONTH',
                'value': self.metrics['best_month'],
                'subtitle': self.format_currency(self.metrics['best_month_pnl']),
                'type': 'profit'
            },
            {
                'title': 'RISK MANAGEMENT',
                'value': 'STRONG',
                'subtitle': 'Stopped commodity & emotional trading',
                'type': 'warning'
            }
        ]
        
        for card in cards:
            html += f"""
            <div class="card {card['type']}">
                <h3>{card['title']}</h3>
                <div class="value">{card['value']}</div>
                <div class="subtitle">{card['subtitle']}</div>
            </div>
            """
        
        html += "</div>"
        return html
    
    def generate_performance_charts(self):
        """Generate performance charts section"""
        html = """
        <div class="section">
            <h2>📈 Performance Evolution</h2>
            <div class="chart-container">
                <img src="charts/monthly_pnl.png" alt="Monthly Performance">
                <p style="margin-top: 15px; color: #9ca3af;">
                    Monthly P&L breakdown showing clear evolution from Q1 learning phase to Q2 systematic profitability
                </p>
            </div>
            
            <div class="chart-container">
                <img src="charts/cumulative_pnl.png" alt="Cumulative P&L">
                <p style="margin-top: 15px; color: #9ca3af;">
                    Trading journey visualization - demonstrating recovery from initial losses and upward trajectory
                </p>
            </div>
        </div>
        """
        return html
    
    def generate_quarterly_analysis(self):
        """Generate quarterly analysis section"""
        html = f"""
        <div class="section">
            <h2>🎯 Quarterly Analysis</h2>
            <div class="chart-container">
                <img src="charts/quarterly_comparison.png" alt="Quarterly Comparison">
            </div>
            
            <div class="insights-grid">
                <div class="insight-box">
                    <h3>Q1: Learning Phase (Apr-Jun)</h3>
                    <ul>
                        <li><strong>Result:</strong> {self.format_currency(self.metrics['q1_pnl'])} loss</li>
                        <li><strong>Focus:</strong> Understanding market dynamics</li>
                        <li><strong>Key Learning:</strong> Identified that commodity trading wasn't my strength</li>
                        <li><strong>Action:</strong> Decided to focus on derivatives with systematic approach</li>
                    </ul>
                </div>
                
                <div class="insight-box">
                    <h3>Q2: Systematic Execution (Jul-Sep)</h3>
                    <ul>
                        <li><strong>Result:</strong> {self.format_currency(self.metrics['q2_pnl'])} profit</li>
                        <li><strong>Win Rate:</strong> {self.format_percentage(self.metrics['systematic_win_rate'])}</li>
                        <li><strong>Consistency:</strong> {self.metrics['systematic_profitable_months']} consecutive profitable months</li>
                        <li><strong>Strategy:</strong> Disciplined derivative trading on Kotak platform</li>
                    </ul>
                </div>
            </div>
        </div>
        """
        return html
    
    def generate_trading_style_analysis(self):
        """Generate trading style analysis section"""
        html = f"""
        <div class="section">
            <h2>🧠 Systematic vs Emotional Trading</h2>
            <div class="chart-container">
                <img src="charts/systematic_vs_emotional.png" alt="Trading Style Analysis">
            </div>
            
            <div class="insights-grid">
                <div class="insight-box" style="border: 2px solid #10b981;">
                    <h3>✓ Systematic Trading (Q2 Kotak Derivatives)</h3>
                    <ul>
                        <li><strong>Total P&L:</strong> {self.format_currency(self.metrics['systematic_pnl'])}</li>
                        <li><strong>Win Rate:</strong> {self.format_percentage(self.metrics['systematic_win_rate'])}</li>
                        <li><strong>Approach:</strong> Rule-based, disciplined execution</li>
                        <li><strong>Platform:</strong> Kotak Neo (primary)</li>
                        <li><strong>Result:</strong> 3 consecutive profitable months</li>
                    </ul>
                </div>
                
                <div class="insight-box" style="border: 2px solid #ef4444;">
                    <h3>✗ Emotional Trading (Groww Platform)</h3>
                    <ul>
                        <li><strong>Total P&L:</strong> {self.format_currency(self.metrics['emotional_pnl'])} loss</li>
                        <li><strong>Win Rate:</strong> 0%</li>
                        <li><strong>Issue:</strong> Guilt-trip trading, emotional decisions</li>
                        <li><strong>Platform:</strong> Groww (Jul & Oct)</li>
                        <li><strong>Learning:</strong> Recognized pattern and stopped</li>
                    </ul>
                </div>
            </div>
            
            <div class="highlight-box" style="margin-top: 30px;">
                <h3>💡 Key Insight: Self-Awareness</h3>
                <p style="font-size: 1.1em; line-height: 1.8;">
                    The stark contrast between systematic and emotional trading demonstrates <strong>high self-awareness</strong> and 
                    <strong>data-driven decision making</strong>. When trading systematically with discipline, I achieved consistent profitability. 
                    When trading emotionally, results were consistently negative. This recognition led to strategic adaptation - 
                    focusing exclusively on systematic approaches and avoiding emotional triggers.
                </p>
            </div>
        </div>
        """
        return html
    
    def generate_risk_management_section(self):
        """Generate risk management section"""
        html = f"""
        <div class="section">
            <h2>🛡️ Risk Management & Discipline</h2>
            
            <div class="chart-container">
                <img src="charts/drawdown_recovery.png" alt="Drawdown Analysis">
            </div>
            
            <div class="insights-grid">
                <div class="insight-box">
                    <h3>Drawdown Management</h3>
                    <ul>
                        <li><strong>Maximum Drawdown:</strong> {self.format_currency(self.metrics['max_drawdown'])}</li>
                        <li><strong>Drawdown Period:</strong> {self.metrics['drawdown_peak_month']} to {self.metrics['drawdown_trough_month']}</li>
                        <li><strong>Recovery:</strong> {self.format_currency(self.metrics['recovery_amount'])} recovered</li>
                        <li><strong>Current Status:</strong> On recovery trajectory</li>
                    </ul>
                </div>
                
                <div class="insight-box">
                    <h3>Risk Controls Implemented</h3>
                    <ul>
                        <li><strong>Stopped commodity trading</strong> after identifying consistent losses</li>
                        <li><strong>Avoided emotional trading</strong> by recognizing Groww pattern</li>
                        <li><strong>Focused on strengths:</strong> Systematic derivative trading</li>
                        <li><strong>Platform discipline:</strong> Kotak for systematic, avoided Groww</li>
                    </ul>
                </div>
            </div>
        </div>
        """
        return html
    
    def generate_detailed_metrics_table(self):
        """Generate detailed metrics table"""
        html = """
        <div class="section">
            <h2>📊 Detailed Performance Metrics</h2>
            <table class="metric-table">
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Value</th>
                        <th>Interpretation</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        metrics_data = [
            ('Total P&L', self.format_currency(self.metrics['total_pnl']), 'Overall trading result'),
            ('Win Rate', self.format_percentage(self.metrics['win_rate']), f"{self.metrics['profitable_months']} profitable out of {self.metrics['total_months_traded']} months"),
            ('Profit Factor', f"{self.metrics['profit_factor']:.2f}", 'Gross profit / Gross loss ratio'),
            ('Systematic Win Rate', self.format_percentage(self.metrics['systematic_win_rate']), 'Success rate in disciplined trading'),
            ('Q1 to Q2 Improvement', f"+{self.format_percentage(self.metrics['q1_to_q2_improvement'])}", 'Performance evolution'),
            ('Best Month', f"{self.metrics['best_month']}: {self.format_currency(self.metrics['best_month_pnl'])}", 'Highest single month profit'),
            ('Worst Month', f"{self.metrics['worst_month']}: {self.format_currency(self.metrics['worst_month_pnl'])}", 'Largest single month loss'),
            ('Monthly Volatility', self.format_currency(self.metrics['volatility']), 'Standard deviation of monthly returns'),
            ('Max Consecutive Profits', f"{self.metrics['max_consecutive_profits']} months", 'Longest winning streak'),
            ('Sharpe Ratio', f"{self.metrics['sharpe_ratio']:.3f}", 'Risk-adjusted return measure'),
        ]
        
        for metric, value, interpretation in metrics_data:
            html += f"""
                <tr>
                    <td><strong>{metric}</strong></td>
                    <td>{value}</td>
                    <td style="color: #9ca3af;">{interpretation}</td>
                </tr>
            """
        
        html += """
                </tbody>
            </table>
        </div>
        """
        return html
    
    def generate_key_learnings(self):
        """Generate key learnings section"""
        insights = self.insights
        
        html = """
        <div class="section">
            <h2>🎓 Key Learnings & Interview Talking Points</h2>
            
            <div class="insights-grid">
                <div class="insight-box" style="border: 2px solid #10b981;">
                    <h3>✓ What Worked</h3>
                    <ul>
        """
        
        for point in insights['what_worked']:
            html += f"<li>{point}</li>"
        
        html += """
                    </ul>
                </div>
                
                <div class="insight-box" style="border: 2px solid #ef4444;">
                    <h3>✗ What Didn't Work</h3>
                    <ul>
        """
        
        for point in insights['what_didnt_work']:
            html += f"<li>{point}</li>"
        
        html += """
                    </ul>
                </div>
            </div>
            
            <div class="insight-box" style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(59, 130, 246, 0.1)); border: 2px solid #10b981; margin-top: 30px;">
                <h3>🛡️ Risk Management Evolution</h3>
                <ul>
        """
        
        for point in insights['risk_management']:
            html += f"<li>{point}</li>"
        
        html += """
                </ul>
            </div>
        </div>
        """
        return html
    
    def generate_interview_highlights(self):
        """Generate interview talking points section"""
        html = f"""
        <div class="section">
            <h2>🎤 Interview Talking Points for {TRADING_METADATA['company']}</h2>
            
            <div class="highlight-box">
                <h3>Why This Matters for {TRADING_METADATA['company']}</h3>
                <p style="font-size: 1.1em; line-height: 1.8; margin-bottom: 20px;">
                    This trading journey demonstrates the exact qualities {TRADING_METADATA['company']} values in a Trainee Analyst:
                </p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 20px;">
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #10b981;">
                        <h4 style="color: #10b981; margin-bottom: 10px;">1. Real Skin in the Game</h4>
                        <p>Traded with personal capital, experiencing real risk and reward - not just theoretical knowledge</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #3b82f6;">
                        <h4 style="color: #3b82f6; margin-bottom: 10px;">2. Data-Driven Decision Making</h4>
                        <p>Used quantitative analysis to identify what works, leading to {self.format_percentage(self.metrics['q1_to_q2_improvement'])} improvement</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #f59e0b;">
                        <h4 style="color: #f59e0b; margin-bottom: 10px;">3. Self-Awareness & Adaptability</h4>
                        <p>Recognized emotional trading patterns early and had the discipline to stop and adapt strategy</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #8b5cf6;">
                        <h4 style="color: #8b5cf6; margin-bottom: 10px;">4. Risk Management</h4>
                        <p>Stopped commodity trading after identifying weakness, demonstrating ability to cut losses</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #ec4899;">
                        <h4 style="color: #ec4899; margin-bottom: 10px;">5. Systematic Approach</h4>
                        <p>Q2 showed {self.metrics['systematic_profitable_months']} consecutive profitable months through disciplined execution</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #10b981;">
                        <h4 style="color: #10b981; margin-bottom: 10px;">6. Resilience & Learning Mindset</h4>
                        <p>Bounced back from Q1 losses, demonstrating ability to learn and improve under pressure</p>
                    </div>
                </div>
            </div>
            
            <div style="background: #1f2937; border: 3px solid #10b981; padding: 30px; border-radius: 15px; margin-top: 30px;">
                <h3 style="color: #10b981; text-align: center; font-size: 1.5em; margin-bottom: 20px;">The Narrative for Tomorrow</h3>
                <p style="font-size: 1.15em; line-height: 1.9; text-align: center;">
                    "I started trading to truly understand markets, not just theoretically. Q1 was my learning phase - I took losses, 
                    but more importantly, I analyzed what went wrong. I identified that commodity trading wasn't my strength and that 
                    emotional decisions led to poor outcomes. In Q2, I became highly systematic in derivatives - this led to 
                    <strong>{self.metrics['systematic_profitable_months']} consecutive profitable months</strong> with a 
                    <strong>{self.format_percentage(self.metrics['systematic_win_rate'])} win rate</strong>. 
                    The key insight: <strong>systematic, disciplined trading works; emotional trading doesn't</strong>. 
                    I had the self-awareness to recognize this early and adapt. This is exactly the mindset {TRADING_METADATA['company']} 
                    needs - data-driven, risk-aware, and adaptable."
                </p>
            </div>
        </div>
        """
        return html
    
    def generate_additional_charts(self):
        """Generate additional visualization sections"""
        html = """
        <div class="section">
            <h2>📉 Additional Analysis</h2>
            
            <div class="chart-container">
                <img src="charts/segment_distribution.png" alt="Segment Distribution">
                <p style="margin-top: 15px; color: #9ca3af;">Exposure distribution across different segments</p>
            </div>
            
            <div class="chart-container">
                <img src="charts/consistency_heatmap.png" alt="Consistency Heatmap">
                <p style="margin-top: 15px; color: #9ca3af;">Monthly performance heatmap showing trading consistency</p>
            </div>
            
            <div class="chart-container">
                <img src="charts/win_loss_distribution.png" alt="Win Loss Distribution">
                <p style="margin-top: 15px; color: #9ca3af;">Distribution of profitable vs loss months</p>
            </div>
        </div>
        """
        return html
    
    def generate_full_report(self):
        """Generate complete HTML report"""
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Trading Performance Dashboard - FY {TRADING_METADATA['financial_year']}</title>
            {HTML_STYLE}
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Trading Performance Dashboard</h1>
                    <p>FY {TRADING_METADATA['financial_year']} | Systematic Trading Evolution</p>
                    <p style="margin-top: 10px; font-size: 0.9em;">Prepared for: <strong>{TRADING_METADATA['company']}</strong> Trainee Analyst Interview | Date: {TRADING_METADATA['interview_date']}</p>
                </div>
                
                {self.generate_summary_cards()}
                {self.generate_executive_summary()}
                {self.generate_performance_charts()}
                {self.generate_quarterly_analysis()}
                {self.generate_trading_style_analysis()}
                {self.generate_risk_management_section()}
                {self.generate_detailed_metrics_table()}
                {self.generate_key_learnings()}
                {self.generate_interview_highlights()}
                {self.generate_additional_charts()}
                
                <div class="footer">
                    <p>Generated on: {TRADING_METADATA['interview_date']}</p>
                    <p>Systematic Trading Performance Dashboard | FY {TRADING_METADATA['financial_year']}</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        output_file = os.path.join(REPORT_DIR, 'Trading_Performance_Report.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"\n✅ Report generated: {output_file}")
        return output_file
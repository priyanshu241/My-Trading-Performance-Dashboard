"""
Report Generator Module - DERIVATIVES ONLY
Generate professional HTML report with clean narrative + Kotak Screenshots
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
        """Generate executive summary"""
        html = f"""
        <div class="section">
            <h2>📊 Executive Summary</h2>
            <div class="highlight-box">
                <h3>Systematic Derivatives Trading Evolution - {TRADING_METADATA['platform']}</h3>
                <p style="font-size: 1.1em; line-height: 1.8;">
                    This dashboard presents my <strong>systematic derivatives trading journey</strong> on Kotak Neo across {self.metrics['total_months_traded']} active months of FY {TRADING_METADATA['financial_year']}. 
                    Starting with a <strong>learning phase in Q1</strong> (losses of {self.format_currency(self.metrics['q1_pnl'])}), I analyzed my performance, 
                    identified patterns, and developed a <strong>disciplined, systematic approach</strong>.
                </p>
                <p style="font-size: 1.1em; line-height: 1.8; margin-top: 15px;">
                    <strong>Result in Q2:</strong> Generated {self.format_currency(self.metrics['systematic_pnl'])} with a <strong>{self.format_percentage(self.metrics['systematic_win_rate'])} win rate</strong> 
                    and <strong>{self.metrics['systematic_profitable_months']} consecutive profitable months</strong>. This represents a <strong>{self.format_percentage(self.metrics['q1_to_q2_improvement'])} improvement</strong> from Q1 through 
                    data-driven strategy refinement and disciplined execution.
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
                'subtitle': f"Kotak Neo Derivatives | {self.metrics['total_months_traded']} active months",
                'type': 'profit' if self.metrics['total_pnl'] > 0 else 'info'
            },
            {
                'title': 'Q2 SYSTEMATIC TRADING',
                'value': self.format_currency(self.metrics['systematic_pnl']),
                'subtitle': f"{self.metrics['systematic_profitable_months']} consecutive wins | {self.format_percentage(self.metrics['systematic_win_rate'])} win rate",
                'type': 'profit'
            },
            {
                'title': 'Q1 → Q2 IMPROVEMENT',
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
                'title': 'DISCIPLINE',
                'value': 'HIGH',
                'subtitle': 'Data-driven approach, systematic execution',
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
                    Monthly P&L showing clear evolution from Q1 learning phase to Q2 systematic profitability
                </p>
            </div>
            
            <div class="chart-container">
                <img src="charts/cumulative_pnl.png" alt="Cumulative P&L">
                <p style="margin-top: 15px; color: #9ca3af;">
                    Trading journey demonstrating recovery from initial losses and upward trajectory with systematic approach
                </p>
            </div>
        </div>
        """
        return html
    
    def generate_kotak_screenshots_section(self):
        """Generate section with actual Kotak Neo screenshots"""
        html = """
        <div class="section">
            <h2>📱 Official Kotak Neo Platform Data</h2>
            <p style="font-size: 1.1em; color: #9ca3af; margin-bottom: 30px;">
                Below are the actual screenshots from Kotak Neo platform showing the derivatives trading performance. 
                This validates the data used in this dashboard and demonstrates real trading activity with personal capital.
            </p>
            
            <div class="chart-container">
                <h3 style="color: #10b981; margin-bottom: 15px;">📊 Monthly Performance View</h3>
                <img src="../kotak_monthly.png" alt="Kotak Neo Monthly View" style="border: 2px solid #10b981; border-radius: 10px; max-width: 100%;">
                <p style="margin-top: 15px; color: #9ca3af;">
                    <strong>Official Kotak Neo monthly P&L chart</strong> showing FY 2025-26 derivatives performance with detailed breakdown
                </p>
            </div>
            
            <div class="chart-container">
                <h3 style="color: #10b981; margin-bottom: 15px;">📅 Daily Trading Activity View</h3>
                <img src="../kotak_daily.png" alt="Kotak Neo Daily View" style="border: 2px solid #10b981; border-radius: 10px; max-width: 100%;">
                <p style="margin-top: 15px; color: #9ca3af;">
                    <strong>Trading activity heatmap</strong> from Kotak Neo platform showing daily trading patterns and consistency
                </p>
            </div>
            
            <div class="highlight-box" style="margin-top: 30px; background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(59, 130, 246, 0.15)); border: 3px solid #10b981;">
                <h3>✅ Data Validation & Authenticity</h3>
                <p style="font-size: 1.1em; line-height: 1.8;">
                    These official Kotak Neo screenshots validate the accuracy of all metrics and analysis presented in this dashboard. 
                    This is <strong>real trading activity with personal capital</strong>, not simulated or paper trading.
                </p>
                <div style="margin-top: 20px; padding: 20px; background: #374151; border-radius: 10px;">
                    <p style="font-size: 1.05em;">
                        <strong style="color: #10b981;">✓ Net P&L:</strong> ₹12,592.19 
                        <span style="margin: 0 15px;">|</span>
                        <strong style="color: #10b981;">✓ Total Turnover:</strong> ₹1,98,598.13 
                        <span style="margin: 0 15px;">|</span>
                        <strong style="color: #10b981;">✓ Client Code:</strong> XFONT
                    </p>
                </div>
            </div>
        </div>
        """
        return html
    
    def generate_quarterly_analysis(self):
        """Generate quarterly analysis"""
        html = f"""
        <div class="section">
            <h2>🎯 Quarterly Analysis: Learning → Systematic</h2>
            <div class="chart-container">
                <img src="charts/quarterly_comparison.png" alt="Quarterly Comparison">
            </div>
            
            <div class="insights-grid">
                <div class="insight-box">
                    <h3>Q1: Learning Phase (Apr-Jun)</h3>
                    <ul>
                        <li><strong>Result:</strong> {self.format_currency(self.metrics['q1_pnl'])} loss</li>
                        <li><strong>Purpose:</strong> Understanding market dynamics and developing strategy</li>
                        <li><strong>Key Learning:</strong> Need for systematic, rule-based approach</li>
                        <li><strong>Action:</strong> Analyzed performance data to identify patterns</li>
                        <li><strong>Outcome:</strong> Developed disciplined trading methodology</li>
                    </ul>
                </div>
                
                <div class="insight-box">
                    <h3>Q2: Systematic Execution (Jul-Sep)</h3>
                    <ul>
                        <li><strong>Result:</strong> {self.format_currency(self.metrics['q2_pnl'])} profit</li>
                        <li><strong>Win Rate:</strong> {self.format_percentage(self.metrics['systematic_win_rate'])}</li>
                        <li><strong>Consistency:</strong> {self.metrics['systematic_profitable_months']} consecutive profitable months</li>
                        <li><strong>Strategy:</strong> Disciplined, rule-based derivatives trading</li>
                        <li><strong>Improvement:</strong> +{self.format_percentage(self.metrics['q1_to_q2_improvement'])} from Q1</li>
                    </ul>
                </div>
            </div>
            
            <div class="highlight-box" style="margin-top: 30px;">
                <h3>💡 The Turning Point</h3>
                <p style="font-size: 1.1em; line-height: 1.8;">
                    Between Q1 and Q2, I conducted thorough performance analysis, identified what wasn't working, 
                    and developed a <strong>systematic, disciplined approach</strong> to derivatives trading. 
                    The result speaks for itself: <strong>{self.format_percentage(self.metrics['q1_to_q2_improvement'])} improvement</strong> 
                    and <strong>100% win rate in Q2</strong>. This demonstrates my ability to <strong>learn from data, adapt quickly, and execute consistently</strong>.
                </p>
            </div>
        </div>
        """
        return html
    
    def generate_trading_style_analysis(self):
        """Generate trading style analysis"""
        html = f"""
        <div class="section">
            <h2>🧠 Learning Phase vs Systematic Trading</h2>
            <div class="chart-container">
                <img src="charts/learning_vs_systematic.png" alt="Trading Style Analysis">
            </div>
            
            <div class="insights-grid">
                <div class="insight-box" style="border: 2px solid #f59e0b;">
                    <h3>Q1: Learning Phase</h3>
                    <ul>
                        <li><strong>Total P&L:</strong> {self.format_currency(self.metrics['learning_pnl'])} loss</li>
                        <li><strong>Win Rate:</strong> {self.format_percentage(self.metrics['learning_win_rate'])}</li>
                        <li><strong>Approach:</strong> Experimental, understanding market behavior</li>
                        <li><strong>Focus:</strong> Identifying what works and what doesn't</li>
                        <li><strong>Value:</strong> Essential education phase with measurable lessons</li>
                    </ul>
                </div>
                
                <div class="insight-box" style="border: 2px solid #10b981;">
                    <h3>Q2: Systematic Trading</h3>
                    <ul>
                        <li><strong>Total P&L:</strong> {self.format_currency(self.metrics['systematic_pnl'])} profit</li>
                        <li><strong>Win Rate:</strong> {self.format_percentage(self.metrics['systematic_win_rate'])}</li>
                        <li><strong>Approach:</strong> Rule-based, disciplined execution</li>
                        <li><strong>Platform:</strong> Kotak Neo Derivatives</li>
                        <li><strong>Result:</strong> {self.metrics['systematic_profitable_months']} consecutive profitable months</li>
                    </ul>
                </div>
            </div>
            
            <div class="highlight-box" style="margin-top: 30px;">
                <h3>💡 Key Insight: The Power of Systematic Approach</h3>
                <p style="font-size: 1.1em; line-height: 1.8;">
                    The dramatic contrast between Q1 and Q2 demonstrates a critical truth: <strong>systematic, disciplined trading works</strong>. 
                    When I developed and followed a clear methodology, results became <strong>consistently positive</strong>. 
                    This isn't luck—it's the result of <strong>data analysis, strategy development, and disciplined execution</strong>. 
                    The exact approach that drives success at {TRADING_METADATA['company']}.
                </p>
            </div>
        </div>
        """
        return html
    
    def generate_risk_management_section(self):
        """Generate risk management section"""
        html = f"""
        <div class="section">
            <h2>🛡️ Risk Management & Learning Curve</h2>
            
            <div class="chart-container">
                <img src="charts/drawdown_recovery.png" alt="Drawdown Analysis">
            </div>
            
            <div class="insights-grid">
                <div class="insight-box">
                    <h3>Drawdown Management</h3>
                    <ul>
                        <li><strong>Maximum Drawdown:</strong> {self.format_currency(self.metrics['max_drawdown'])}</li>
                        <li><strong>Drawdown Period:</strong> {self.metrics['drawdown_peak_month']} to {self.metrics['drawdown_trough_month']}</li>
                        <li><strong>Recovery Action:</strong> Implemented systematic approach</li>
                        <li><strong>Q2 Performance:</strong> {self.format_percentage(self.metrics['q1_to_q2_improvement'])} improvement</li>
                    </ul>
                </div>
                
                <div class="insight-box">
                    <h3>Risk Controls & Discipline</h3>
                    <ul>
                        <li><strong>Accepted Q1 as learning phase</strong> - understood it as education cost</li>
                        <li><strong>Analyzed performance data</strong> to identify weakness patterns</li>
                        <li><strong>Developed systematic rules</strong> based on analysis</li>
                        <li><strong>Maintained discipline</strong> in Q2 execution</li>
                        <li><strong>Focused on single segment:</strong> Derivatives (played to strengths)</li>
                    </ul>
                </div>
            </div>
        </div>
        """
        return html
    
    def generate_detailed_metrics_table(self):
        """Generate detailed metrics table"""
        html = f"""
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
                    <tr>
                        <td><strong>Net P&L</strong></td>
                        <td>{self.format_currency(self.metrics['total_pnl'])}</td>
                        <td style="color: #9ca3af;">Overall derivatives trading result</td>
                    </tr>
                    <tr>
                        <td><strong>Win Rate</strong></td>
                        <td>{self.format_percentage(self.metrics['win_rate'])}</td>
                        <td style="color: #9ca3af;">{self.metrics['profitable_months']} profitable out of {self.metrics['total_months_traded']} months</td>
                    </tr>
                    <tr>
                        <td><strong>Profit Factor</strong></td>
                        <td>{self.metrics['profit_factor']:.2f}</td>
                        <td style="color: #9ca3af;">Gross profit / Gross loss ratio</td>
                    </tr>
                    <tr>
                        <td><strong>Q2 Systematic Win Rate</strong></td>
                        <td>{self.format_percentage(self.metrics['systematic_win_rate'])}</td>
                        <td style="color: #9ca3af;">Success rate with disciplined approach</td>
                    </tr>
                    <tr>
                        <td><strong>Q1 to Q2 Improvement</strong></td>
                        <td>+{self.format_percentage(self.metrics['q1_to_q2_improvement'])}</td>
                        <td style="color: #9ca3af;">Performance evolution through systematic approach</td>
                    </tr>
                    <tr>
                        <td><strong>Best Month</strong></td>
                        <td>{self.metrics['best_month']}: {self.format_currency(self.metrics['best_month_pnl'])}</td>
                        <td style="color: #9ca3af;">Highest single month profit</td>
                    </tr>
                    <tr>
                        <td><strong>Worst Month</strong></td>
                        <td>{self.metrics['worst_month']}: {self.format_currency(self.metrics['worst_month_pnl'])}</td>
                        <td style="color: #9ca3af;">Largest single month loss (learning phase)</td>
                    </tr>
                    <tr>
                        <td><strong>Monthly Volatility</strong></td>
                        <td>{self.format_currency(self.metrics['volatility'])}</td>
                        <td style="color: #9ca3af;">Standard deviation of returns</td>
                    </tr>
                    <tr>
                        <td><strong>Max Consecutive Profits</strong></td>
                        <td>{self.metrics['max_consecutive_profits']} months</td>
                        <td style="color: #9ca3af;">Longest winning streak (Q2 systematic phase)</td>
                    </tr>
                    <tr>
                        <td><strong>Sharpe Ratio</strong></td>
                        <td>{self.metrics['sharpe_ratio']:.3f}</td>
                        <td style="color: #9ca3af;">Risk-adjusted return measure</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
        return html
    
    def generate_key_learnings(self):
        """Generate key learnings"""
        insights = self.insights
        
        html = """
        <div class="section">
            <h2>🎓 Key Learnings & Takeaways</h2>
            
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
                <h3>🛡️ Risk Management & Discipline</h3>
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
        """Generate interview talking points"""
        html = f"""
        <div class="section">
            <h2>🎤 Interview Talking Points for {TRADING_METADATA['company']}</h2>
            
            <div class="highlight-box">
                <h3>Why This Matters for {TRADING_METADATA['company']}</h3>
                <p style="font-size: 1.1em; line-height: 1.8; margin-bottom: 20px;">
                    This derivatives trading journey demonstrates the exact qualities {TRADING_METADATA['company']} values in a Trainee Analyst:
                </p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 20px;">
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #10b981;">
                        <h4 style="color: #10b981; margin-bottom: 10px;">1. Real Market Experience</h4>
                        <p>Traded derivatives with personal capital - experiencing real risk, not just theory</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #3b82f6;">
                        <h4 style="color: #3b82f6; margin-bottom: 10px;">2. Data-Driven Approach</h4>
                        <p>Analyzed Q1 performance, identified patterns, improved Q2 by {self.format_percentage(self.metrics['q1_to_q2_improvement'])}</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #f59e0b;">
                        <h4 style="color: #f59e0b; margin-bottom: 10px;">3. Systematic Execution</h4>
                        <p>Q2 showed {self.metrics['systematic_profitable_months']} consecutive wins through disciplined approach</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #8b5cf6;">
                        <h4 style="color: #8b5cf6; margin-bottom: 10px;">4. Learning Agility</h4>
                        <p>Quickly identified weakness, developed solution, executed successfully</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #ec4899;">
                        <h4 style="color: #ec4899; margin-bottom: 10px;">5. Risk Awareness</h4>
                        <p>Accepted Q1 as learning phase, managed drawdown, focused on strengths</p>
                    </div>
                    
                    <div style="background: #374151; padding: 20px; border-radius: 10px; border-left: 4px solid #10b981;">
                        <h4 style="color: #10b981; margin-bottom: 10px;">6. Discipline Under Pressure</h4>
                        <p>Maintained systematic approach even after initial losses</p>
                    </div>
                </div>
            </div>
            
            <div style="background: #1f2937; border: 3px solid #10b981; padding: 30px; border-radius: 15px; margin-top: 30px;">
                <h3 style="color: #10b981; text-align: center; font-size: 1.5em; margin-bottom: 20px;">The Narrative for Your Interview</h3>
                <p style="font-size: 1.15em; line-height: 1.9; text-align: center;">
                    "I started trading derivatives on Kotak Neo to gain real market experience. Q1 was my learning phase where I took losses 
                    of {self.format_currency(self.metrics['q1_pnl'])}, but I used this as data. I analyzed what wasn't working, developed a 
                    <strong>systematic, rule-based approach</strong>, and the results were clear: Q2 showed <strong>{self.metrics['systematic_profitable_months']} 
                    consecutive profitable months</strong> with a <strong>{self.format_percentage(self.metrics['systematic_win_rate'])} win rate</strong>, 
                    representing a <strong>{self.format_percentage(self.metrics['q1_to_q2_improvement'])} improvement</strong>. 
                    The key insight: <strong>when I'm disciplined and systematic, I'm consistently profitable</strong>. 
                    This data-driven, disciplined mindset is exactly what {TRADING_METADATA['company']} needs in a trader."
                </p>
            </div>
        </div>
        """
        return html
    
    def generate_additional_charts(self):
        """Generate additional charts section"""
        html = """
        <div class="section">
            <h2>📉 Additional Analysis</h2>
            
            <div class="chart-container">
                <img src="charts/consistency_heatmap.png" alt="Consistency Heatmap">
                <p style="margin-top: 15px; color: #9ca3af;">Monthly performance heatmap showing trading consistency evolution</p>
            </div>
            
            <div class="chart-container">
                <img src="charts/win_loss_distribution.png" alt="Win Loss Distribution">
                <p style="margin-top: 15px; color: #9ca3af;">Distribution of profitable vs loss months across the FY</p>
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
            <title>Derivatives Trading Dashboard - FY {TRADING_METADATA['financial_year']}</title>
            {HTML_STYLE}
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Derivatives Trading Performance Dashboard</h1>
                    <p>FY {TRADING_METADATA['financial_year']} | Systematic Trading Evolution | {TRADING_METADATA['platform']}</p>
                    <p style="margin-top: 10px; font-size: 0.9em;">
                        Prepared for: <strong>{TRADING_METADATA['company']}</strong> Trainee Analyst Interview | 
                        Date: {TRADING_METADATA['interview_date']}
                    </p>
                </div>
                
                {self.generate_summary_cards()}
                {self.generate_executive_summary()}
                {self.generate_performance_charts()}
                {self.generate_kotak_screenshots_section()}
                {self.generate_quarterly_analysis()}
                {self.generate_trading_style_analysis()}
                {self.generate_risk_management_section()}
                {self.generate_detailed_metrics_table()}
                {self.generate_key_learnings()}
                {self.generate_interview_highlights()}
                {self.generate_additional_charts()}
                
                <div class="footer">
                    <p>Generated on: {TRADING_METADATA['interview_date']}</p>
                    <p>Systematic Derivatives Trading Dashboard | FY {TRADING_METADATA['financial_year']} | {TRADING_METADATA['platform']}</p>
                    <p style="margin-top: 10px; font-size: 0.9em; color: #6b7280;">
                        Net P&L: {self.format_currency(self.metrics['total_pnl'])} | 
                        Q2 Win Rate: {self.format_percentage(self.metrics['systematic_win_rate'])} | 
                        Improvement: +{self.format_percentage(self.metrics['q1_to_q2_improvement'])}
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        output_file = os.path.join(REPORT_DIR, 'Derivatives_Trading_Report.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"\n✅ Report generated: {output_file}")
        return output_file
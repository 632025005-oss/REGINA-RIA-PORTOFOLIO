"""
TRANSACTION ANALYSIS TOOL
By: Regina Ria Aurellia | Former BCA Teller
Mathematical approach to banking transaction analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class TransactionAnalyzer:
    """Analisis transaksi perbankan berdasarkan pengalaman nyata di BCA"""
    
    def __init__(self):
        self.author = "Regina Ria Aurellia"
        self.background = "S1 Pendidikan Matematika | BCA Teller 2022-2025"
        
    def generate_sample_data(self):
        """Generate sample data berdasarkan pengalaman real di BCA"""
        np.random.seed(42)
        
        dates = pd.date_range('2024-01-01', periods=30, freq='D')
        
        data = {
            'date': dates,
            'transaction_count': np.random.randint(120, 220, 30),  # 120-220 transaksi/hari
            'cash_amount': np.random.randint(300, 1200, 30) * 1e6,  # Rp 300jt-1.2M/hari
            'customer_satisfaction': np.random.uniform(4.0, 5.0, 30),
            'errors': np.random.randint(0, 3, 30)  # 0-2 kesalahan/hari
        }
        
        return pd.DataFrame(data)
    
    def calculate_daily_performance(self, df):
        """Hitung performa harian dengan metrics banking"""
        results = {
            'avg_transactions': df['transaction_count'].mean(),
            'total_cash_month': df['cash_amount'].sum(),
            'avg_cash_per_day': df['cash_amount'].mean(),
            'accuracy_rate': (1 - (df['errors'].sum() / df['transaction_count'].sum())) * 100,
            'avg_satisfaction': df['customer_satisfaction'].mean()
        }
        return results
    
    def plot_performance_trend(self, df):
        """Visualisasi trend performa"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle('Banking Performance Analysis\nBy: Regina Ria Aurellia', fontsize=14)
        
        # Plot 1: Transaction Volume
        axes[0, 0].plot(df['date'], df['transaction_count'], 'b-o', linewidth=2)
        axes[0, 0].set_title('Daily Transaction Volume')
        axes[0, 0].set_ylabel('Number of Transactions')
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].axhline(y=150, color='r', linestyle='--', alpha=0.5, label='BCA Standard')
        axes[0, 0].legend()
        
        # Plot 2: Cash Flow
        axes[0, 1].bar(df['date'], df['cash_amount']/1e6, alpha=0.7)
        axes[0, 1].set_title('Daily Cash Flow (in Millions Rupiah)')
        axes[0, 1].set_ylabel('Rp (Million)')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Plot 3: Customer Satisfaction
        axes[1, 0].plot(df['date'], df['customer_satisfaction'], 'g-s', linewidth=2)
        axes[1, 0].set_title('Customer Satisfaction Trend')
        axes[1, 0].set_ylabel('Score (1-5)')
        axes[1, 0].set_ylim(3.5, 5.0)
        axes[1, 0].fill_between(df['date'], 4.5, df['customer_satisfaction'], alpha=0.3, color='green')
        
        # Plot 4: Error Rate
        error_rate = (df['errors'] / df['transaction_count']) * 100
        axes[1, 1].plot(df['date'], error_rate, 'r-^', linewidth=2)
        axes[1, 1].set_title('Transaction Error Rate')
        axes[1, 1].set_ylabel('Error Rate (%)')
        axes[1, 1].axhline(y=0.5, color='orange', linestyle='--', label='Target (<0.5%)')
        axes[1, 1].legend()
        
        plt.tight_layout()
        plt.savefig('performance_analysis.png', dpi=150, bbox_inches='tight')
        plt.show()
        
        return fig

# Contoh penggunaan
if __name__ == "__main__":
    print("=== BANKING TRANSACTION ANALYSIS ===")
    print("By: Regina Ria Aurellia")
    print("BCA Teller Experience: 2022-2025\n")
    
    analyzer = TransactionAnalyzer()
    print(f"Analyst: {analyzer.author}")
    print(f"Background: {analyzer.background}\n")
    
    # Generate sample data
    df = analyzer.generate_sample_data()
    
    # Calculate performance
    results = analyzer.calculate_daily_performance(df)
    
    print("📊 PERFORMANCE REPORT:")
    print(f"- Average Daily Transactions: {results['avg_transactions']:.0f}")
    print(f"- Total Cash Monthly: Rp {results['total_cash_month']:,.0f}")
    print(f"- Average Cash/Day: Rp {results['avg_cash_per_day']:,.0f}")
    print(f"- Transaction Accuracy: {results['accuracy_rate']:.2f}%")
    print(f"- Customer Satisfaction: {results['avg_satisfaction']:.2f}/5.0")
    
    # Generate visualization
    print("\n📈 Generating performance charts...")
    analyzer.plot_performance_trend(df)

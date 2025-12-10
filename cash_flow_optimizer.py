"""
CASH FLOW OPTIMIZATION FOR BANK TELLERS
Mathematical optimization based on real banking experience
"""

import numpy as np
from typing import List, Dict

class CashFlowOptimizer:
    """Optimasi pengelolaan cash untuk teller banking"""
    
    def __init__(self):
        self.denominations = {
            100000: "Rp 100,000",
            50000: "Rp 50,000", 
            20000: "Rp 20,000",
            10000: "Rp 10,000",
            5000: "Rp 5,000",
            2000: "Rp 2,000",
            1000: "Rp 1,000"
        }
    
    def calculate_optimal_mix(self, total_amount: float) -> Dict:
        """
        Hitung mix uang tunai optimal berdasarkan pengalaman BCA
        """
        amount = total_amount
        result = {}
        
        for denom in sorted(self.denominations.keys(), reverse=True):
            if amount >= denom:
                count = amount // denom
                
                # Batasan berdasarkan pengalaman nyata
                if denom == 100000:
                    count = min(count, 300)  # Max 300 lembar Rp100k
                elif denom == 50000:
                    count = min(count, 400)  # Max 400 lembar Rp50k
                
                result[denom] = int(count)
                amount -= count * denom
        
        # Sisa uang pecahan kecil
        if amount > 0:
            result[1000] = result.get(1000, 0) + int(amount // 1000)
        
        return result
    
    def calculate_transaction_efficiency(self, peak_hours: List[int]) -> Dict:
        """
        Optimasi jumlah teller berdasarkan jam sibuk
        Berdasarkan pengalaman di BCA Singosaren
        """
        # Data berdasarkan pengamatan real
        base_customers_per_hour = 15
        peak_multiplier = 2.5
        
        efficiency_report = {}
        
        for hour in range(8, 17):  # Jam operasional banking
            is_peak = hour in peak_hours
            customers = base_customers_per_hour * (peak_multiplier if is_peak else 1)
            
            # Formula optimal teller: customers / 8 (ideal: 8 customer/jam/teller)
            optimal_tellers = max(1, np.ceil(customers / 8))
            
            efficiency_report[hour] = {
                'hour': f"{hour}:00",
                'is_peak': is_peak,
                'estimated_customers': int(customers),
                'optimal_tellers': int(optimal_tellers),
                'wait_time_minutes': (customers * 7.5) / (optimal_tellers * 60) * 60
            }
        
        return efficiency_report

# Contoh implementasi
if __name__ == "__main__":
    print("=== CASH FLOW OPTIMIZER ===")
    print("Based on BCA Teller Experience\n")
    
    optimizer = CashFlowOptimizer()
    
    # Contoh 1: Optimasi pecahan uang
    cash_amount = 875_000_000  # Rp 875 juta
    print(f"Optimizing cash for: Rp {cash_amount:,}")
    
    mix = optimizer.calculate_optimal_mix(cash_amount)
    
    print("\n💰 OPTIMAL CASH MIX:")
    total_notes = 0
    for denom, count in mix.items():
        if count > 0:
            print(f"{optimizer.denominations[denom]}: {count:,} lembar")
            total_notes += count
    
    print(f"\nTotal lembar: {total_notes:,}")
    
    # Contoh 2: Optimasi jam operasional
    print("\n⏰ OPERATIONAL EFFICIENCY ANALYSIS:")
    peak_hours = [10, 11, 13, 14]  # Jam sibuk berdasarkan pengalaman
    efficiency = optimizer.calculate_transaction_efficiency(peak_hours)
    
    for hour_data in efficiency.values():
        peak = "📈 PEAK" if hour_data['is_peak'] else "   normal"
        print(f"{hour_data['hour']} {peak}: {hour_data['estimated_customers']} customers | "
              f"Optimal tellers: {hour_data['optimal_tellers']} | "
              f"Wait: {hour_data['wait_time_minutes']:.1f} min")

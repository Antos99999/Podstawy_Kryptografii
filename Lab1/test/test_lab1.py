'''
Lab 1
BBS (Blum-Blum-Shub) - Implementacja generatora ciągów losowych oraz wybranych testów lsowości
Testy standardu FIPS 140-2
'''

import unittest
from lab1 import main

class test_lab1(unittest.TestCase):

    def setUp(self):
        pass

    def test_single_bit(self):
        bits = main()  # Uruchamiamy algorytm i pobieramy wynik
        ones_count = bits.count('1')  # Liczba jedynek
        zeros_count = bits.count('0')  # Liczba zer

        total_bits = len(bits)
        self.assertTrue(abs(ones_count - zeros_count) / total_bits < 0.05)

    def test_extended_series(self):
        bits = main()
        series = 1
        max_series = 1
        list_bits = list(map(int,str(bits)))
        for i in range (1, len(list_bits)):
            if list_bits[i] == 1 and list_bits[i-1] == 1:
                series += 1
                max_series = max(max_series, series)
            elif list_bits[i] == 0 and list_bits[i-1] == 0:
                series += 1
                max_series = max(max_series, series)
            else:
                series = 1
        self.assertFalse(max_series>=26)

    def test_series(self):
        bits = main()
        series = 1
        series_counts = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            '6+': 0
        }
        list_bits = list(map(int, str(bits)))

        for i in range (1, len(list_bits)):
            if list_bits[i] == 1 and list_bits[i-1] == 1:
                series += 1
            elif list_bits[i] == 0 and list_bits[i-1] == 0:
                series += 1
            else:
                if series >= 6:
                    #print(series)
                    series_counts['6+'] += 1
                else:
                    #print(series)
                    series_counts[series] += 1
                series = 1
        if series >= 6:
            series_counts['6+'] += 1
        else:
            series_counts[series] += 1

        print(series_counts)

        self.assertTrue(2315 <= series_counts[1] <= 2685)
        self.assertTrue(1114 <= series_counts[2] <= 1386)
        self.assertTrue(527 <= series_counts[3] <= 723)
        self.assertTrue(240 <= series_counts[4] <= 384)
        self.assertTrue(103 <= series_counts[5] <= 209)
        self.assertTrue(103 <= series_counts['6+'] <= 209)

    def test_poker(self):
        bits = main()

if __name__ == "__main__":
    unittest.main()
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

if __name__ == "__main__":
    unittest.main()
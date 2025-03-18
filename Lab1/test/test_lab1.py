'''
Lab 1
BBS (Blum-Blum-Shub) - Implementacja generatora ciągów losowych oraz wybranych testów lsowości
Testy standardu FIPS 140-2
'''

import unittest
import math
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
            "1_0": 0,
            "1_1": 0,
            "2_0": 0,
            "2_1": 0,
            "3_0": 0,
            "3_1": 0,
            "4_0": 0,
            "4_1": 0,
            "5_0": 0,
            "5_1": 0,
            '6+_0': 0,
            '6+_1': 0,
        }
        list_bits = list(map(int, str(bits)))

        for i in range (1, len(list_bits)):
            if list_bits[i] == 1 and list_bits[i-1] == 1:
                series += 1
            elif list_bits[i] == 0 and list_bits[i-1] == 0:
                series += 1
            else:
                if series >= 6 and list_bits[i-1] == 1:
                    #print(series)
                    series_counts['6+_1'] += 1
                    series = 1
                elif series >= 6 and list_bits[i-1] == 0:
                    series_counts['6+_0'] += 1
                    series = 1
                elif series == 1 and list_bits[i-1] == 1:
                    series_counts['1_1'] += 1
                    series = 1
                elif series == 1 and list_bits[i-1] == 0:
                    series_counts['1_0'] += 1
                    series = 1
                elif series == 2 and list_bits[i-1] == 1:
                    series_counts['2_1'] += 1
                    series = 1
                elif series == 2 and list_bits[i-1] == 0:
                    series_counts['2_0'] += 1
                    series = 1
                elif series == 3 and list_bits[i-1] == 1:
                    series_counts['3_1'] += 1
                    series = 1
                elif series == 3 and list_bits[i-1] == 0:
                    series_counts['3_0'] += 1
                    series = 1
                elif series == 4 and list_bits[i-1] == 1:
                    series_counts['4_1'] += 1
                    series = 1
                elif series == 4 and list_bits[i-1] == 0:
                    series_counts['4_0'] += 1
                    series = 1
                elif series == 5 and list_bits[i-1] == 1:
                    series_counts['5_1'] += 1
                    series = 1
                elif series == 5 and list_bits[i-1] == 0:
                    series_counts['5_0'] += 1
                    series = 1
        if series >= 6 and list_bits[i-1] == 1:
            series_counts['6+_1'] += 1
        elif series >= 6 and list_bits[i-1] == 0:
            series_counts['6+_0'] += 1
        elif series == 1 and list_bits[-1] == 1:
            series_counts['1_1'] += 1
        elif series == 1 and list_bits[-1] == 0:
            series_counts['1_0'] += 1
        elif series == 2 and list_bits[-1] == 1:
            series_counts['2_1'] += 1
        elif series == 2 and list_bits[-1] == 0:
            series_counts['2_0'] += 1
        elif series == 3 and list_bits[-1] == 1:
            series_counts['3_1'] += 1
        elif series == 3 and list_bits[-1] == 0:
            series_counts['3_0'] += 1
        elif series == 4 and list_bits[-1] == 1:
            series_counts['4_1'] += 1
        elif series == 4 and list_bits[-1] == 0:
            series_counts['4_0'] += 1
        elif series == 5 and list_bits[-1] == 1:
            series_counts['5_1'] += 1
        elif series == 5 and list_bits[-1] == 0:
            series_counts['5_0'] += 1

        self.assertTrue(2315 <= series_counts["1_0"] <= 2685, "Seria 1_0 wynosi: " + str(series_counts["1_0"]))
        self.assertTrue(2315 <= series_counts["1_1"] <= 2685, "Seria 1_1 wynosi: " + str(series_counts["1_1"]))
        self.assertTrue(1114 <= series_counts["2_0"] <= 1386, "Seria 2_0 wynosi: " + str(series_counts["2_0"]))
        self.assertTrue(1114 <= series_counts["2_1"] <= 1386, "Seria 2_1 wynosi: " + str(series_counts["2_1"]))
        self.assertTrue(527 <= series_counts["3_0"] <= 723, "Seria 3_0 wynosi: " + str(series_counts["3_0"]))
        self.assertTrue(527 <= series_counts["3_1"] <= 723, "Seria 3_1 wynosi: " + str(series_counts["3_1"]))
        self.assertTrue(240 <= series_counts["4_0"] <= 384, "Seria 4_0 wynosi: " + str(series_counts["4_0"]))
        self.assertTrue(240 <= series_counts["4_1"] <= 384, "Seria 4_1 wynosi: " + str(series_counts["4_1"]))
        self.assertTrue(103 <= series_counts["5_0"] <= 209, "Seria 5_0 wynosi: " + str(series_counts["5_0"]))
        self.assertTrue(103 <= series_counts["5_1"] <= 209, "Seria 5_1 wynosi: " + str(series_counts["5_1"]))
        self.assertTrue(103 <= series_counts['6+_0'] <= 209, "Seria 6+_0 wynosi: " + str(series_counts['6+_0']))
        self.assertTrue(103 <= series_counts['6+_1'] <= 209, "Seria 6+_1 wynosi: " + str(series_counts['6+_1']))

    def test_poker(self):
        bits = main()
        character = [bits[i:i+4] for i in range(0, len(bits), 4)]

        #print(character)

        variant = {
            '0': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            '10': 0,
            '11': 0,
            '12': 0,
            '13': 0,
            '14': 0,
            '15': 0,
        }

        variant['0'] += character.count('0000')
        variant['1'] += character.count('0001')
        variant['2'] += character.count('0010')
        variant['3'] += character.count('0011')
        variant['4'] += character.count('0100')
        variant['5'] += character.count('0101')
        variant['6'] += character.count('0110')
        variant['7'] += character.count('0111')
        variant['8'] += character.count('1000')
        variant['9'] += character.count('1001')
        variant['10'] += character.count('1010')
        variant['11'] += character.count('1011')
        variant['12'] += character.count('1100')
        variant['13'] += character.count('1101')
        variant['14'] += character.count('1110')
        variant['15'] += character.count('1111')

        #print(variant)

        suma = 0

        for i in variant:
            #print(i)
            suma += math.pow(variant[str(i)],2)

        x = (16/5000) * suma - 5000

        #print(x)

        self.assertTrue(2.16<=x<=46.17, "Wartość X: " + str(x))

if __name__ == "__main__":
    unittest.main()
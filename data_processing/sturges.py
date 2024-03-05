from data_processing.utils.helpers import math

def calcular_intervalos_sturges(df):
    n = len(df['Renda_Mensal'])
    k_sturges = 1 + 3.3 * math.log10(n)
    return int(k_sturges)
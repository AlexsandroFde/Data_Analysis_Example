from data_processing.utils.helpers import pd
from data_processing.sturges import calcular_intervalos_sturges

def criar_tabelas_de_frequencia(df):
    freq_Tipo_Produto = df['Tipo_Produto'].value_counts().reset_index()
    freq_Tipo_Produto.columns = ['Categoria', 'Frequência']

    freq_Regiao = df['Regiao'].value_counts().reset_index()
    freq_Regiao.columns = ['Categoria', 'Frequência']

    renda_mensal_bins = pd.cut(df['Renda_Mensal'], bins=calcular_intervalos_sturges(df), retbins=True)[1]
    valor_compra_bins = pd.cut(df['Valor_Compra'], bins=calcular_intervalos_sturges(df), retbins=True)[1]
    idade_bins = pd.cut(df['Idade'], bins=calcular_intervalos_sturges(df), retbins=True)[1]

    return freq_Tipo_Produto, freq_Regiao, renda_mensal_bins, valor_compra_bins, idade_bins
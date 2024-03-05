from data_processing.utils.helpers import pd
from data_processing.sturges import calcular_intervalos_sturges

def criar_tabelas_de_frequencia(df):
    freq_Tipo_Produto = df['Tipo_Produto'].value_counts().reset_index()
    freq_Tipo_Produto.columns = ['Categoria', 'Frequência']

    freq_Regiao = df['Regiao'].value_counts().reset_index()
    freq_Regiao.columns = ['Categoria', 'Frequência']

    Renda_Mensal_bins = pd.cut(df['Renda_Mensal'], bins=calcular_intervalos_sturges(df), retbins=True)[1]
    df['Categoria_Renda_Mensal'] = pd.cut(df['Renda_Mensal'], bins=Renda_Mensal_bins, labels=[f'{Renda_Mensal_bins[i]:.2f}-{Renda_Mensal_bins[i+1]:.2f}' for i in range(len(Renda_Mensal_bins)-1)])
    freq_categoria_Renda_Mensal = df['Categoria_Renda_Mensal'].value_counts().reset_index()
    freq_categoria_Renda_Mensal.columns = ['Amplitude', 'Frequência']

    Valor_Compra_bins = pd.cut(df['Valor_Compra'], bins=calcular_intervalos_sturges(df), retbins=True)[1]
    df['Categoria_Valor_Compra'] = pd.cut(df['Valor_Compra'], bins=Valor_Compra_bins, labels=[f'{Valor_Compra_bins[i]:.2f}-{Valor_Compra_bins[i+1]:.2f}' for i in range(len(Valor_Compra_bins)-1)])
    freq_categoria_Valor_Compra = df['Categoria_Valor_Compra'].value_counts().reset_index()
    freq_categoria_Valor_Compra.columns = ['Amplitude', 'Frequência']

    Idade_bins = pd.cut(df['Idade'], bins=calcular_intervalos_sturges(df), retbins=True)[1]
    df['Categoria_Idade'] = pd.cut(df['Idade'], bins=Idade_bins, labels=[f'{Idade_bins[i]:.2f}-{Idade_bins[i+1]:.2f}' for i in range(len(Idade_bins)-1)])
    freq_categoria_Idade = df['Categoria_Idade'].value_counts().reset_index()
    freq_categoria_Idade.columns = ['Amplitude', 'Frequência']

    return freq_Tipo_Produto, freq_Regiao, freq_categoria_Renda_Mensal, freq_categoria_Valor_Compra, freq_categoria_Idade
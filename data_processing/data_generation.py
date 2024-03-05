from data_processing.utils.helpers import np, pd

def gerar_dados(seed):
    np.random.seed(seed)
    data = {
        'Tipo_Produto': np.random.choice(['Eletrônico', 'Vestuário', 'Alimentos'], 100),
        'Regiao': np.random.choice(['Norte', 'Sul', 'Leste'], 100),
        'Renda_Mensal': np.random.normal(3000, 1000, 100),
        'Valor_Compra': np.random.uniform(5, 150, 100),
        'Idade': np.random.poisson(25, 100)
    }
    return pd.DataFrame(data)
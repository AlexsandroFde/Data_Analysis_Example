from data_processing.frequency_tables import criar_tabelas_de_frequencia
from data_processing.utils.helpers import plt, np


def exibir_histogramas(df):
    freq_Tipo_Produto, freq_Regiao, Renda_Mensal_bins, Valor_Compra_bins, Idade_bins = criar_tabelas_de_frequencia(df)

    bin_means_Renda_Mensal = [np.mean([Renda_Mensal_bins[i], Renda_Mensal_bins[i+1]]) for i in range(len(Renda_Mensal_bins)-1)]
    bin_means_Valor_Compra = [np.mean([Valor_Compra_bins[i], Valor_Compra_bins[i+1]]) for i in range(len(Valor_Compra_bins)-1)]
    bin_means_Idade = [np.mean([Idade_bins[i], Idade_bins[i+1]]) for i in range(len(Idade_bins)-1)]

    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    axs[0, 0].bar(freq_Tipo_Produto['Categoria'], freq_Tipo_Produto['Frequência'], color='skyblue', edgecolor='black')
    axs[0, 0].set_title('Gráfico de Barras para Tipo de Produto')
    axs[0, 0].set_xlabel('Categoria')
    axs[0, 0].set_ylabel('Frequência')
    axs[0, 0].tick_params(axis='x', rotation=45)
    axs[0, 0].grid(axis='y', linestyle='--', alpha=0.7)

    axs[0, 1].bar(freq_Regiao['Categoria'], freq_Regiao['Frequência'], color='lightgreen', edgecolor='black')
    axs[0, 1].set_title('Gráfico de Barras para Região')
    axs[0, 1].set_xlabel('Categoria')
    axs[0, 1].set_ylabel('Frequência')
    axs[0, 1].tick_params(axis='x', rotation=45)
    axs[0, 1].grid(axis='y', linestyle='--', alpha=0.7)

    axs[0, 2].hist(df['Renda_Mensal'], bins=Renda_Mensal_bins, color='salmon', edgecolor='black')
    axs[0, 2].set_title('Histograma para Renda Mensal')
    axs[0, 2].set_xlabel('Renda Mensal (R$)')
    axs[0, 2].set_ylabel('Frequência')
    axs[0, 2].set_xticks(bin_means_Renda_Mensal)
    axs[0, 2].tick_params(axis='x', rotation=45)
    axs[0, 2].grid(axis='y', linestyle='--', alpha=0.7)

    axs[1, 0].hist(df['Valor_Compra'], bins=Valor_Compra_bins, color='lightblue', edgecolor='black')
    axs[1, 0].set_title('Histograma para Valor de Compra')
    axs[1, 0].set_xlabel('Valor de Compra (R$)')
    axs[1, 0].set_ylabel('Frequência')
    axs[1, 0].set_xticks(bin_means_Valor_Compra)
    axs[1, 0].tick_params(axis='x', rotation=45)
    axs[1, 0].grid(axis='y', linestyle='--', alpha=0.7)

    axs[1, 1].hist(df['Idade'], bins=Idade_bins, color='lightcoral', edgecolor='black')
    axs[1, 1].set_title('Histograma para Idade')
    axs[1, 1].set_xlabel('Idade (anos)')
    axs[1, 1].set_ylabel('Frequência')
    axs[1, 1].set_xticks(bin_means_Idade)
    axs[1, 1].tick_params(axis='x', rotation=45)
    axs[1, 1].grid(axis='y', linestyle='--', alpha=0.7)

    fig.delaxes(axs[1, 2])
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.45, bottom= 0.1)
    plt.show()
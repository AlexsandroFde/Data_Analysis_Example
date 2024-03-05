from data_processing.data_generation import gerar_dados
from data_processing.frequency_tables import criar_tabelas_de_frequencia
from visualization.histograms import exibir_histogramas


def main():
    seed = int(input("Digite a seed para gerar os dados aleatórios: "))
    df = gerar_dados(seed)

    exibir_histogramas(df)

if __name__ == "__main__":
    main()
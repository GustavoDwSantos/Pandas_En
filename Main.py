import pandas as pd
import matplotlib.pyplot as plt

def main():

    url_enem = "https://raw.githubusercontent.com/alura-cursos/imersao-dados-2-2020/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv"
    dados_enem = pd.read_csv(url_enem)
    colunas = dados_enem.columns.values
    Exercicio_1 = dados_enem[['TP_SEXO','NU_IDADE']]
    
    print(f"Idade e sexo dos participantes: \n{Exercicio_1}")

    Exercicio_2 = dados_enem['NU_IDADE'].unique()
    Exercicio_2.sort()
    Exercicio_3 = len(dados_enem['NO_MUNICIPIO_RESIDENCIA'].unique())
    print(f"Idades unicas inscritas: {Exercicio_2}\n Quantidade de municipios inscritos: {Exercicio_3}")
    Exercicio_4 = dados_enem['NU_IDADE'].value_counts()
    print(f"quantidade de inscritos de cada idade:\n {Exercicio_4}")
    exercicio5(dados_enem)
    exercicio6(dados_enem)

    
    

def exercicio5(dados):
    grafico = dados["SG_UF_RESIDENCIA"].hist(bins= 20, figsize=(10,8))
    plt.show()
    plt.close()
    return grafico

def exercicio6(dados):
    grafico = dados["NU_IDADE"].value_counts().plot.pie(figsize = (10,8))
    plt.show()
    plt.close()
    return grafico
    
if __name__ == "__main__":
    main() 
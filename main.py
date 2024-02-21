import pandas as pd

def criar_receita(nome_receita, ingredientes, planilha):
    """
    Creates a recipe dictionary with ingredients and quantities.

    Args:
        nome_receita (str): Name of the recipe.
        ingredientes (list): List of tuples containing ingredient names and quantities.
        planilha (list): List to store recipe dictionaries.

    Returns:
        None
    """

    nomes_ingredientes, quantidades = zip(*ingredientes)
    receita = {
        'Nome da Receita': [nome_receita] * len(nomes_ingredientes),
        'Ingrediente': list(nomes_ingredientes),
        'Quantidade Utilizada (g)': list(quantidades)
    }
    planilha.append(receita)

def exportar_receitas(receitas):
    """
    Exports a list of recipe DataFrames to a single Excel sheet with formatting.

    Args:
        receitas (list): List of DataFrames containing recipe information.

    Returns:
        None
    """

    df_completo = pd.concat(receitas, ignore_index=True)
    styled_df = df_completo.style.set_properties(**{'text-align': 'center',
                                                    'font-weight': 'bold',
                                                    'border': '1px solid black',
                                                    'background-color': 'lightgrey'})
    styled_df.to_excel('receitas_completas.xlsx', index=False, engine='openpyxl')

if __name__ == '__main__':
    Geral = []
    ingredientes1 = [
        ('CORANTE VERMELHO NATAL SOFTGEL DUAS ROSAS', 0.1),
        ('MARGARIN SADIA QUALY', 0.1),
        ('MASSA DE CARANGUEIJO', 0.1),
        ('PATA DE CARANGUEIJO', 0.1)
    ]
    ingredientes2 = [
        ('FARINHA DE TRIGO', 0.2),
        ('LEITE INTEGRAL', 0.3),
        ('OVOS', 2),
        ('ACUCAR REFINADO', 0.15)
    ]

    receitas = []

    criar_receita('Massa', ingredientes1, Geral)
    criar_receita('Pão de Ló', ingredientes2, Geral)

    for receita in Geral:
        df_receita = pd.DataFrame(receita)
        receitas.append(df_receita)

    exportar_receitas(receitas)

import pandas as pd

def criar_receita():
    ingredientes = [
        ('CORANTE VERMELHO NATAL SOFTGEL DUAS ROSAS', 0.100),
        ('MARGARIN SADIA QUALY', 0.100),
        ('MASSA DE CARANGUEIJO', 0.100),
        ('PATA DE CARANGUEIJO', 0.100)
    ]

    nomes_ingredientes, quantidades = zip(*ingredientes)
    receita = {
        'Nome da Receita': ['MASSA'] * len(nomes_ingredientes),
        'Ingrediente': list(nomes_ingredientes),
        'Quantidade Utilizada (g)': list(quantidades)
    }

    df = pd.DataFrame(receita)
    styled_df = df.style.set_properties(**{'text-align': 'center', 'font-weight': 'bold', 'border': '1px solid black', 'background-color': 'lightgrey'})
    styled_df.to_excel('receita.xlsx', index=False, sheet_name='Receita', engine='openpyxl')

if __name__ == '__main__':
    criar_receita()
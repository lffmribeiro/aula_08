import pandas as pd

#df_exemplo = pd.read_csv('data/exemplo.csv', sep=';')

df_clientes = pd.read_csv('data/clientes.csv')
df_vendas_1 = pd.read_csv('data/vendas.csv')
df_vendas_2 = pd.read_csv('data/vendas_2.csv')
df_vendas_3 = pd.read_csv('data/vendas_3.csv')

print(df_vendas_3.head()) # padrão limite de 5 linhas


df_concatenado = pd.concat([df_vendas_1, df_vendas_2, df_vendas_3], ignore_index=True) # union all

df_upper = df_concatenado.rename(str.upper, axis='columns') # deixando com letra maiúscula

dict = {'VENDA_ID': 'ID',
        'PRODUTO': 'PRDT'
       }
df_novo_nome = df_upper.rename(columns=dict) # Mudando o nome das colunas

print(df_novo_nome.head())


df_merge = pd.merge(df_vendas_1, df_vendas_2, on='cliente_id', how='left') # left join

print(df_merge.head())

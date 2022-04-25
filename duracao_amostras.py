import pandas as pd
import datetime as dt
import openpyxl

data_hoje = dt.datetime.today()
colunas = ['AMOSTRA','NOME','DURACAO']

df = pd.read_csv('biolaudo_amostras.csv',parse_dates=['Dt. Cadastro'], dayfirst=True)
colunas_temp = ['Cod. Amostra','Nome','Status','Dt. Cadastro','Testado']

df = df[colunas_temp]

df['tempo_liberacao'] = (data_hoje - df['Dt. Cadastro'])
#print(df.loc[df['Cod. Amostra']=='231921025'])
filtro = ((df.tempo_liberacao.dt.components.days>=1) & (df.Testado==0) & (df.Status == 'Recebido'))

df_final = df.loc[filtro,['Cod. Amostra','Nome','tempo_liberacao']]
df_final = pd.DataFrame(df_final.values, columns=colunas)
if len(df_final)>0:
    df_final['DURACAO'] = df_final['DURACAO'].map(lambda x: str(x).split('.')[0])

df_final.to_excel(R"\\ceara-fs\Ceara\Central Analítica\Biologia Molecular\Room3-record\S3. Supervisão\TESTE_TI\amostras_duracao_critica.xlsx", sheet_name='Nao_Testadas',index=False)

## --------------------------------- Amostras no Reteste ------------------------------------------ ##

## df com amostras de reteste, checar se amostra com mais de um dia está no reteste. Sempre verificar a planilha e dia correto, sempre um dia anterior
df_check = pd.read_excel(r'\\ceara-fs\Ceara\Central Analítica\Biologia Molecular\Room4-record\S4. RETESTES\2022\04_REGISTRO DE RETESTE - Abril.xlsm', sheet_name='06')
df_check['amostras'] = df_check['Unnamed: 1'].iloc[7:]
df_check.fillna(0,inplace=True)
df_check = df_check.loc[df_check.amostras!=0]

filtro02 = df['Cod. Amostra'].isin(df_check['amostras'].values)
filtro03 = df.Testado==1
filtro04 = df['tempo_liberacao'].dt.components.days>=1
df = df.loc[filtro02 & filtro03 & filtro04]
df_final = df[['Cod. Amostra','Nome','tempo_liberacao']]
df_final = pd.DataFrame(df_final.values, columns=colunas)
if len(df_final)>0:
    df_final['DURACAO'] = df_final['DURACAO'].astype(str).str.split('.')[0][0]

## Escreve em um arquivo existente
with pd.ExcelWriter(r"\\ceara-fs\Ceara\Central Analítica\Biologia Molecular\Room3-record\S3. Supervisão\TESTE_TI\amostras_duracao_critica.xlsx", mode='a') as writer:
    df_final.to_excel(writer, sheet_name="Testadas", index=False)

import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import calendar

st.title(':blue["Análise de Sazonalidade de Consumo de Energia Elétrica: Descubra Seu Padrão de Consumo"]')


'''
A gestão de energia é essencial para os gestores do agronegócio, e existem diversas oportunidades para economizar na conta de energia. Um desses benefícios é a sazonalidade, que permite economizar energia durante a entressafra. 

Para obter esse benefício, é necessário comprovar que a unidade consumidora é usada para fins agrícolas e que a relação entre os quatro menores e quatro maiores consumos elétricos da unidade é de 20% ou menos. 

Se você tem dificuldade em fazer esses cálculos, pode utilizar a calculadora de sazonalidade da Satori. 

Com o benefício da sazonalidade, é possível desenvolver um cronograma mensal de demanda contratada, que evita o pagamento por demanda não consumida. As unidades que possuem sazonalidade reconhecida também podem optar por pagar a demanda medida, sem pagar a demanda contratada cheia, ou 10% da maior demanda medida nos últimos 11 ciclos. 

É importante lembrar que é preciso ter uma boa gestão energética para aproveitar esses benefícios sem pagar multas e perder o reconhecimento da sazonalidade. 

Acesse agora mesmo a calculadora de sazonalidade da Satori e comece a economizar energia!
'''

# Define as colunas do dataframe
columns = ['Mês', 'Consumo Ponta Anual', 'Consumo Fora Ponta Anual', 'Consumo Total']

# Cria uma lista vazia para armazenar os inputs de consumo
data = []

# Cria a interface do Streamlit para coletar os inputs
with st.sidebar:
    st.title('Histórico de Consumo')
    st.subheader('Insira seus dados de consumo Ponta e Fora Ponta')
    for i in range(12):
        month_name = calendar.month_name[i+1]  # Obtém o nome do mês correspondente
        st.header(f'{month_name}')
        consumo_ponta = st.number_input(f'Consumo de Ponta em {month_name}', key=f'ponta_{i}')
        consumo_fora_ponta = st.number_input(f'Consumo Fora de Ponta em {month_name}', key=f'fora_ponta_{i}')
        consumo_total = consumo_ponta + consumo_fora_ponta
        data.append([month_name, consumo_ponta, consumo_fora_ponta, consumo_total])

# Cria o dataframe a partir dos inputs
df = pd.DataFrame(data, columns=columns)

# Mostra o dataframe na tela
st.write(df)

# Cria um gráfico de linhas com os dados do dataframe
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Mês'], y=df['Consumo Ponta Anual'], name='Consumo Ponta Anual'))
fig.add_trace(go.Scatter(x=df['Mês'], y=df['Consumo Fora Ponta Anual'], name='Consumo Fora Ponta Anual'))
fig.add_trace(go.Scatter(x=df['Mês'], y=df['Consumo Total'], name='Consumo Total'))

# Define o layout do gráfico
fig.update_layout(
    title='Consumo Mensal',
    xaxis_title='Mês',
    yaxis_title='Consumo',
)

# Mostra o gráfico na tela
st.plotly_chart(fig)

# Cria um novo DataFrame com os quatro maiores e menores valores de consumo total
df_top_bottom = pd.concat([df.nlargest(4, 'Consumo Total'), df.nsmallest(4, 'Consumo Total')])

# Cria um gráfico de barras com os quatro maiores e menores valores de consumo total
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=df_top_bottom['Mês'], y=df_top_bottom['Consumo Total'], name='Consumo Total'))

# Define o layout do gráfico
fig2.update_layout(
    title='Quatro maiores e quatro menores consumos totais do ano',
    xaxis_title='Mês',
    yaxis_title='Consumo',
)

# Mostra o gráfico na tela
st.plotly_chart(fig2)

# Soma dos quatro maiores e quatro menores consumos totais
soma_maiores = df.nlargest(4, 'Consumo Total')['Consumo Total'].sum()
soma_menores = df.nsmallest(4, 'Consumo Total')['Consumo Total'].sum()

# Diferença entre os quatro maiores e quatro menores consumos totais em porcentagem
diferenca_perc = (soma_menores * 1/ soma_maiores) 

# Mostra a soma dos quatro maiores e quatro menores consumos totais e a diferença em porcentagem na tela
st.write(f'**Soma dos quatro maiores consumos totais: :blue[ {soma_maiores}]**')
st.write(f'**Soma dos quatro menores consumos totais: :blue[{soma_menores}]**')
st.write(f'**Diferença entre os quatro maiores e quatro menores consumos totais: :blue[{diferenca_perc:.2f}% ]**')

# Verifica se a soma dos menores e maiores consumos é menor ou igual a 20%
if diferenca_perc <= 0.2:
    st.subheader(':blue[A Unidade Consumidora **encontra-se apta** à Solicitar a Sazonalidade.]')
else:
    st.subheader(':red[A Unidade Consumidora **não está apta** à Solicitar a Sazonalidade.]')

st.markdown("[Satori](https://www.satorienergia.com)")

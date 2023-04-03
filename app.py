import streamlit as st
import pandas as pd

#Planiha padrão para o usuario baixar
def download_template():
    template_url = 'https://github.com/jessiscarva/xseg/raw/main/historico%20de%20consumo.xlsx'
    df = pd.read_excel(template_url)
    df.to_excel('historico de consumo.xlsx', index=False)
    st.success('A planilha padrão foi baixada com sucesso!')


#Função para fazer o upload da planilha preenchida
def upload_data():
    uploaded_file = st.file_uploader("Selecione a planilha preenchida:", type=['xlsx'])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        df.to_excel('uploads/dados.xlsx', index=False)
        st.success('A planilha preenchida foi enviada com sucesso!')

#Criar botoões no Streamlit
def main():
    st.title('Upload e Download de Planilhas')
    st.write('Baixe a planilha padrão e preencha os dados. Em seguida, faça o upload da planilha preenchida para análise dos dados.')

    if st.button('Baixar Planilha Padrão'):
        download_template()

    if st.button('Enviar Planilha Preenchida'):
        upload_data()

if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import calendar
import streamlit_authenticator as stauth

#módulo Hasher para converter suas senhas de texto sem formatação em senhas hash
hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

#Criar objeto autenticador
authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

#Renderizar o widget de login fornecendo um nome para o formulário e sua localização ( ou seja, barra lateral ou principal )
name, authentication_status, username = authenticator.login('Login', 'main')

#Checar o status da autenticação
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Usuario ou senha incorreta')
elif authentication_status == None:
    st.warning('Faça login com o seu username e senha')

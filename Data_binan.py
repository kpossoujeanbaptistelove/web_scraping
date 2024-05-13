import streamlit as st
from binance import Client

# Créer une interface utilisateur avec Streamlit
st.title('Interface Binance')

# Ajouter un formulaire pour saisir les clés API
st.subheader('Configuration API')
api_key = st.text_input('Clé API')
api_secret = st.text_input('Clé secrète', type='password')

# Créer un client Binance
if api_key and api_secret:
    client = Client(api_key, api_secret)

    # Afficher les informations du compte
    st.subheader('Informations du compte')
    info_compte = client.get_account()
    st.write(info_compte)

    # Afficher le solde
    st.subheader('Solde')
    asset = st.text_input('Actif')
    if asset:
        solde = client.get_asset_balance(asset=asset)
        st.write(solde)

    # Afficher les ordres ouverts
    st.subheader('Ordres ouverts')
    ordres_ouverts = client.get_open_orders(symbol='BTCUSDT')
    st.write(ordres_ouverts)

    # Afficher l'historique des transactions
    st.subheader('Historique des transactions')
    historique_transactions = client.get_my_trades(symbol='BTCUSDT')
    st.write(historique_transactions)

    # Afficher les données du carnet de commandes
    st.subheader('Carnet de commandes')
    carnet_commandes = client.get_order_book(symbol='BTCUSDT')
    st.write(carnet_commandes)

    # Afficher les données historiques des prix
    st.subheader('Historique des prix')
    historique_prix = client.get_historical_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY, start_str='1 Jan, 2022')
    st.write(historique_prix)

    # Afficher les dernières informations sur les prix
    st.subheader('Prix actuel')
    prix_actuel = client.get_symbol_ticker(symbol='BTCUSDT')
    st.write(prix_actuel)

import requests

def obter_cotacoes():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        response = requests.get(url)
        dados = response.json()

        dolar = dados['USDBRL']['bid']
        euro = dados['EURBRL']['bid']
        bitcoin = dados['BTCBRL']['bid']

        return {
            "Dólar": dolar,
            "Euro": euro,
            "Bitcoin": bitcoin
        }

    except:
        return None
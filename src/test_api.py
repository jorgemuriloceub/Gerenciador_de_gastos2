from src.api_moedas import obter_cotacoes

def test_api_retorna_dados():
    dados = obter_cotacoes()

    assert dados is not None
    assert "Dólar" in dados
    assert "Euro" in dados
    assert "Bitcoin" in dados
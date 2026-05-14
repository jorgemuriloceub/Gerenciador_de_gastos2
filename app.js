// Função para buscar a cotação do Dólar via API
async function buscarCotacaoDolar() {
  const url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL';
  
  try {
    const resposta = await fetch(url);
    const dados = await resposta.json();
    
    // USDBRL é a chave que a API retorna
    const valorDolar = dados.USDBRL.bid; 
    
    console.log(`Cotação capturada: R$ ${valorDolar}`);
    return parseFloat(valorDolar);
  } catch (erro) {
    console.error("Erro ao conectar com a API:", erro);
  }
}

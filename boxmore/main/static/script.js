let carrinho = [];

// Função para adicionar ao carrinho
function adicionarAoCarrinho(produto, preco) {
    carrinho.push({ produto, preco });
    atualizarCarrinho();
    atualizarContagemCarrinho();
}

// Função para atualizar o carrinho (já existente)
function atualizarCarrinho() {
    const listaCarrinho = document.getElementById("lista-carrinho");
    const total = document.getElementById("total");

    listaCarrinho.innerHTML = "";
    let somaTotal = 0;

    carrinho.forEach((item, index) => {
        const li = document.createElement("li");
        li.textContent = `${item.produto} - R$ ${item.preco.toFixed(2)}`;
        const botaoRemover = document.createElement("button");
        botaoRemover.textContent = "Remover";
        botaoRemover.onclick = () => removerDoCarrinho(index);
        li.appendChild(botaoRemover);
        listaCarrinho.appendChild(li);
        somaTotal += item.preco;
    });

    total.textContent = `Total: R$ ${somaTotal.toFixed(2)}`;
}

// Função para remover itens do carrinho
function removerDoCarrinho(index) {
    carrinho.splice(index, 1);
    atualizarCarrinho();
    atualizarContagemCarrinho();
}

// Função para atualizar o contador do carrinho
function atualizarContagemCarrinho() {
    const contagem = carrinho.length;
    const elementoContagem = document.getElementById("carrinho-contagem");
    elementoContagem.textContent = contagem;
}

// Função para finalizar a compra
function finalizarCompra() {
    if (carrinho.length === 0) {
        alert("O carrinho está vazio!");
        return;
    }
    document.getElementById("carrinho").style.display = "none";
    document.getElementById("pagamento").style.display = "block";
}

// Função para processar o pagamento
function processarPagamento(event) {
    event.preventDefault();
    const formaPagamento = document.querySelector('input[name="forma-pagamento"]:checked').value;
    alert(`Pagamento realizado com sucesso via ${formaPagamento}! Obrigado pela compra.`);
    carrinho = [];
    atualizarCarrinho();
    atualizarContagemCarrinho();
    document.getElementById("pagamento").style.display = "none";
    document.getElementById("carrinho").style.display = "block";
}


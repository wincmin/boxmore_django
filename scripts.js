let carrinho = [];

function adicionarAoCarrinho(produto, preco) {
    carrinho.push({ produto, preco });
    atualizarCarrinho();
}

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

function removerDoCarrinho(index) {
    carrinho.splice(index, 1);
    atualizarCarrinho();
}

function finalizarCompra() {
    if (carrinho.length === 0) {
        alert("O carrinho está vazio!");
        return;
    }
    document.getElementById("carrinho").style.display = "none";
    document.getElementById("pagamento").style.display = "block";
}

function processarPagamento(event) {
    event.preventDefault();
    const formaPagamento = document.querySelector('input[name="forma-pagamento"]:checked').value;
    alert(`Pagamento realizado com sucesso via ${formaPagamento}! Obrigado pela compra.`);
    carrinho = [];
    atualizarCarrinho();
    document.getElementById("pagamento").style.display = "none";
    document.getElementById("carrinho").style.display = "block";
}
newCaroucel('#carousel-camisa','#btnLeftCamisa','#btnRightCamisa')
newCaroucel('#caroucel-tenis','#btnLeftTenis','#btnRightTenis')
newCaroucel('#caroucel-meias','#btnLeftMeias','#btnRightMeias')
newCaroucel('#caroucel-acessorios','#btnLeftAcessorios','#btnRightAcessorios')

function newCaroucel(  imgContainer , prevBtn, nextBtn){
    let imagesContainer = document.querySelector(imgContainer);
    let images = document.querySelectorAll(imgContainer+' img');
    let prevButton = document.querySelector(prevBtn);
    let nextButton = document.querySelector(nextBtn);

    let currentIndex = 0;

    var count = Math.round(images.length /4);

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex === 0) ? count - 1 : currentIndex - 1;
        
        updateCarousel(currentIndex,imagesContainer);
       
        
       
         
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
        if(currentIndex == count){
            currentIndex =0;
        }
        updateCarousel(currentIndex,imagesContainer);
       
        
       
    });
   

    
} 
function updateCarousel(currentIndex,imagesContainer ) {
    let offset = - currentIndex * 100
    console.log(offset);
    imagesContainer.style.transform = `translateX(${offset}%)`;
}
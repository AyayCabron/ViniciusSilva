// Função para atualizar o relógio
function updateClock() {
    var now = new Date();
    var hours = now.getHours().toString().padStart(2, '0');
    var minutes = now.getMinutes().toString().padStart(2, '0');
    var seconds = now.getSeconds().toString().padStart(2, '0');
    var timeString = hours + ':' + minutes + ':' + seconds;
    document.getElementById('clock').innerText = timeString;
}

// Atualiza o relógio a cada segundo
setInterval(updateClock, 1000);

// Modal para a imagem do currículo
var modal = document.getElementById("imageModal");
var img = document.getElementById("curriculum-img");
var modalImg = document.getElementById("imgModal");
var span = document.getElementsByClassName("close")[0];

var zoomed = false;

img.onclick = function() {
    modal.style.display = "block";
    modalImg.src = this.src;
}

span.onclick = function() {
    modal.style.display = "none";
}

modal.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

modalImg.onclick = function() {
    if (zoomed) {
        modalImg.style.transform = "scale(1)";
        zoomed = false;
        modalImg.style.cursor = "zoom-in";
    } else {
        modalImg.style.transform = "scale(1.5)";
        zoomed = true;
        modalImg.style.cursor = "zoom-out";
    }
}

// Chama a função para exibir a hora assim que a página carrega
updateClock();



// Alterna a exibição da seção de currículo
document.getElementById('curriculumButton').addEventListener('click', function() {
    const curriculumSection = document.getElementById('curriculum');
    curriculumSection.classList.toggle('hidden'); // Adiciona ou remove a classe 'hidden'

    // Controla a exibição com base na presença da classe 'hidden'
    curriculumSection.style.display = curriculumSection.classList.contains('hidden') ? 'none' : 'block';
});

// Modal para a imagem do currículo
var modal = document.getElementById("imageModal");
var img = document.getElementById("curriculum-img");
var modalImg = document.getElementById("imgModal");
var span = document.getElementsByClassName("close")[0];

// Quando o usuário clicar na imagem, abre o modal
img.onclick = function() {
    modal.style.display = "block";
    modalImg.src = this.src; // Define a imagem do modal
}

// Quando o usuário clicar no "X", fecha o modal
span.onclick = function() {
    modal.style.display = "none";
}

// Fecha o modal quando o usuário clicar fora da imagem
modal.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

// Adatok tömbje (csak két linkkel)
const solvedAlgorithms = [
    {
        title: "Egyenletes Pakolás",
        description: "",
        difficulty: "Haladó",
        tema: "Dinamikus Programozás",
        link: "https://mester.inf.elte.hu:8181/faces/leiras.xhtml?jfwid=103159e28015d478a1f845c79f98:29", 
        link2: "./pdf/egyenletes_pakolas.pdf",
        link3: "./code/egyenletes_pakolas.py"
    },
    {
        title: "Csapatverseny",
        description: "",
        difficulty: "Haladó",
        tema: "Gráfok",
        link: "https://mester.inf.elte.hu:8181/faces/leiras.xhtml?jfwid=a5d6364e0c638f4929107170bc48:28", 
        link2: "./pdf/csapatverseny.pdf",
        link3: "./code/csapatverseny.py"
    },
];


function createCard(algorithm) {
    const card = document.createElement('div');
    card.classList.add('algorithm-card');
    
    let linksHtml = '';

    if (algorithm.link) {
        linksHtml += `
            <a href="${algorithm.link}" target="_blank" class="task-link">Feladat Leírása 1</a>
        `;
    }

    if (algorithm.link2) {
        linksHtml += `
            <a href="${algorithm.link2}" target="_blank" class="task-link secondary-task-link">Feladat Leírása 2</a>
        `;
    }

    if (algorithm.link3) {
        linksHtml += `
            <a href="${algorithm.link3}" target="_blank" class="download-link">Kód Letöltése</a>
        `;
    }
    
    card.innerHTML = `
        <h2 class="card-title">${algorithm.title}</h2>
        <p class="card-difficulty">Nehézség: <strong>${algorithm.difficulty}</strong></p>
        <p class="card-difficulty">Témakör: ${algorithm.tema}</p>
        <div class="card-link">
            ${linksHtml}
        </div>
    `;
    
    return card;
}

function renderCards() {
    const cardContainer = document.getElementById('cardContainer');
    if (!cardContainer) return;

    solvedAlgorithms.forEach(algorithm => {
        const cardElement = createCard(algorithm);
        cardContainer.appendChild(cardElement);
    });
}

document.addEventListener('DOMContentLoaded', renderCards);
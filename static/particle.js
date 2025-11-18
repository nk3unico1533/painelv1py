// quantidade de partículas
const total = 60;

const area = document.getElementById("particles");

for (let i = 0; i < total; i++) {
    let p = document.createElement("div");
    p.classList.add("particle");

    p.style.left = Math.random() * 100 + "vw";
    p.style.top = Math.random() * 100 + "vh";
    p.style.animationDuration = 4 + Math.random() * 4 + "s";
    p.style.opacity = 0.3 + Math.random() * 0.7;

    area.appendChild(p);
}
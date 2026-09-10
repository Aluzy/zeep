// Comportements client : sélecteur de tranche d'âge + recherche/filtre wiki.
// Aucune dépendance externe (contrainte de l'environnement de build actuel).

const AGE_MODES = [
  { id: "quatre_six", label: "4-6 ans" },
  { id: "six_dix", label: "6-10 ans" },
  { id: "college", label: "Collège" },
  { id: "lycee_adultes", label: "Lycée & adultes" },
];

function initAgeSwitcher() {
  const container = document.querySelector("[data-age-switcher]");
  if (!container) return;

  const stored = localStorage.getItem("ageMode") || "lycee_adultes";
  container.innerHTML = AGE_MODES.map(
    (m) =>
      `<button type="button" data-mode="${m.id}" class="${m.id === stored ? "active" : ""}">${m.label}</button>`
  ).join("");

  function applyMode(mode) {
    localStorage.setItem("ageMode", mode);
    container.querySelectorAll("button").forEach((b) => {
      b.classList.toggle("active", b.dataset.mode === mode);
    });
    document.querySelectorAll("[data-defs]").forEach((el) => {
      let defs;
      try {
        defs = JSON.parse(el.getAttribute("data-defs"));
      } catch (e) {
        return;
      }
      const note = el.parentElement.querySelector(".age-note");
      if (defs[mode]) {
        el.innerHTML = defs[mode];
        if (note) note.classList.remove("show");
      } else {
        el.innerHTML = defs["lycee_adultes"] || "";
        if (note) {
          const modeLabel = AGE_MODES.find((m) => m.id === mode)?.label || mode;
          note.textContent = `Cette page n'existe pas encore en version « ${modeLabel} » — voici la version Lycée & adultes en attendant.`;
          note.classList.add("show");
        }
      }
    });
  }

  container.addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-mode]");
    if (!btn) return;
    applyMode(btn.dataset.mode);
  });

  applyMode(stored);
}

function initWikiSearch() {
  const searchEl = document.querySelector("#wiki-search");
  const grid = document.querySelector("#term-grid");
  if (!searchEl || !grid) return;
  const tiles = Array.from(grid.querySelectorAll(".term-tile"));
  const filterBtns = document.querySelectorAll(".domain-filters button");
  let activeDomain = "all";

  function apply() {
    const q = searchEl.value.trim().toLowerCase();
    tiles.forEach((t) => {
      const name = t.dataset.term.toLowerCase();
      const domains = (t.dataset.domains || "").split(",");
      const matchesText = !q || name.includes(q);
      const matchesDomain = activeDomain === "all" || domains.includes(activeDomain);
      t.style.display = matchesText && matchesDomain ? "" : "none";
    });
  }

  searchEl.addEventListener("input", apply);
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      activeDomain = btn.dataset.domain;
      filterBtns.forEach((b) => b.classList.toggle("active", b === btn));
      apply();
    });
  });

  // Pré-sélection du domaine si la page est ouverte avec ?domain=X
  const params = new URLSearchParams(window.location.search);
  const fromUrl = params.get("domain");
  if (fromUrl) {
    const match = Array.from(filterBtns).find((b) => b.dataset.domain === fromUrl);
    if (match) match.click();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initAgeSwitcher();
  initWikiSearch();
});

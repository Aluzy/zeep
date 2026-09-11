// Comportements client : recherche/filtre wiki.
// Aucune dépendance externe (contrainte de l'environnement de build actuel).

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
  initWikiSearch();
});

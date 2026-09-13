// Comportements client : recherche/filtre wiki, scroll-to-top.
// Aucune dépendance externe (contrainte de l'environnement de build actuel).

function initScrollToTop() {
  const btn = document.querySelector("#scroll-to-top");
  if (!btn) return;

  function updateVisibility() {
    if (window.scrollY > 300) {
      btn.classList.add("visible");
    } else {
      btn.classList.remove("visible");
    }
  }

  btn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  window.addEventListener("scroll", updateVisibility, { passive: true });
  updateVisibility(); // Vérifier l'état initial
}

function initDomainFilterTooltips() {
  const filterBtns = document.querySelectorAll(".domain-filters .domain-filter-btn");
  filterBtns.forEach((btn) => {
    btn.addEventListener("mouseover", () => {
      btn.classList.add("show-tooltip");
    });
    btn.addEventListener("mouseout", () => {
      btn.classList.remove("show-tooltip");
    });
    btn.addEventListener("focus", () => {
      btn.classList.add("show-tooltip");
    });
    btn.addEventListener("blur", () => {
      btn.classList.remove("show-tooltip");
    });
  });
}

function initWikiSearch() {
  const searchEl = document.querySelector("#wiki-search");
  const grid = document.querySelector("#term-grid");
  if (!searchEl || !grid) return;
  const tiles = Array.from(grid.querySelectorAll(".term-tile"));
  const filterBtns = document.querySelectorAll(".domain-filters button");
  let activeDomain = "all";

  initDomainFilterTooltips();

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
  initScrollToTop();
  initWikiSearch();
});

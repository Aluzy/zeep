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

/** Minuscules sans accents : « Ampère » et « ampere » se cherchent pareil. */
function sansAccents(texte) {
  return (texte || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

// Libellés des codes de niveau, pour le bandeau de filtre (?niveau=...) : copie de
// NIVEAU_LABEL (src/lib/helpers.ts), car ce script est du JS statique servi tel quel
// et ne passe pas par le build Astro/TypeScript. Garder les deux synchronisées.
const NIVEAU_LABEL = {
  C1: "Maternelle",
  C2: "CP-CE2",
  C3: "CM1-6e",
  C4: "Collège (5e-3e)",
  "2GT": "Seconde",
  "1G": "Première",
  TG: "Terminale",
  "1-TG": "Première et terminale",
  STI2D: "STI2D",
  CAP: "CAP",
  BACPRO: "Bac pro",
};

function initWikiSearch() {
  const searchEl = document.querySelector("#wiki-search");
  const grid = document.querySelector("#term-grid");
  if (!searchEl || !grid) return;
  const tiles = Array.from(grid.querySelectorAll(".term-tile"));
  const filterBtns = document.querySelectorAll(".domain-filters button");
  const banner = document.querySelector("#niveau-filter-banner");
  const bannerLabel = document.querySelector("#niveau-filter-label");
  let activeDomain = "all";
  // Codes de niveau demandés via ?niveau=C1,C2 (depuis /apprends/ ou un lien direct).
  // Tableau vide = pas de filtre.
  let activeNiveaux = [];

  initDomainFilterTooltips();

  function apply() {
    const q = sansAccents(searchEl.value.trim());
    tiles.forEach((t) => {
      // Le terme, plus ses formes équivalentes (abréviations, symboles) : taper
      // « farad », « PWM » ou « cos phi » doit ramener la bonne fiche.
      const name = sansAccents(t.dataset.term);
      const synonymes = sansAccents(t.dataset.synonymes || "");
      const domains = (t.dataset.domains || "").split(",");
      const matchesText = !q || name.includes(q) || synonymes.includes(q);
      const matchesDomain = activeDomain === "all" || domains.includes(activeDomain);
      const matchesNiveau = activeNiveaux.length === 0 || activeNiveaux.includes(t.dataset.niveau || "");
      t.style.display = matchesText && matchesDomain && matchesNiveau ? "" : "none";
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

  // Filtre par niveau depuis ?niveau=C1,C2 (liens de la page /apprends/ ou partagés) :
  // un ou plusieurs codes séparés par des virgules.
  const niveauParam = params.get("niveau");
  if (niveauParam) {
    activeNiveaux = niveauParam.split(",").map((c) => c.trim()).filter(Boolean);
    if (activeNiveaux.length && banner && bannerLabel) {
      const labels = activeNiveaux.map((c) => NIVEAU_LABEL[c] || c);
      bannerLabel.textContent = `Niveau : ${labels.join(", ")}`;
      banner.hidden = false;
    }
    apply();
  }

  // Pré-remplissage depuis la barre de recherche du header (?q=...), envoyée
  // en GET vers /wiki/ depuis n'importe quelle page.
  const q = params.get("q");
  if (q) {
    searchEl.value = q;
    apply();
  }
}

function initPostToc() {
  const toc = document.querySelector(".post-toc");
  if (!toc) return;
  const links = Array.from(toc.querySelectorAll("a[href^='#']"));
  if (!links.length) return;

  const targets = links
    .map((link) => {
      const id = decodeURIComponent(link.getAttribute("href").slice(1));
      const el = document.getElementById(id);
      return el ? { link, el } : null;
    })
    .filter(Boolean);
  if (!targets.length) return;

  function setActive(id) {
    links.forEach((l) => {
      l.classList.toggle("is-active", l.getAttribute("href") === `#${id}`);
    });
  }

  // Sans IntersectionObserver (vieux navigateur) : pas de mise en avant dynamique,
  // le sommaire reste utilisable comme simple liste de liens.
  if (!("IntersectionObserver" in window)) return;

  let current = targets[0].el.id;
  setActive(current);

  // La bande de lecture retenue est proche du haut de l'écran, sous l'en-tête
  // collant : le titre qui l'atteint devient la section "en cours".
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          current = entry.target.id;
        }
      });
      setActive(current);
    },
    { rootMargin: "-96px 0px -70% 0px", threshold: 0 }
  );
  targets.forEach(({ el }) => observer.observe(el));
}

document.addEventListener("DOMContentLoaded", () => {
  initScrollToTop();
  initWikiSearch();
  initPostToc();
});

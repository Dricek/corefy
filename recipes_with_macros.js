
// 🔥 RECETTES COREFY AVEC MACROS
// Auto-généré avec calculateur nutritionnel

const recipes = {
  "R001": {
    nom: "Bowl protéiné avocat-saumon",
    categorie: "dejeuner",
    difficulte: "facile",
    temps: "15 min",
    kcal: 641.7,
    proteines: 37.5,
    glucides: 24.3,
    lipides: 43.5,
    macros_display: "641.7 kcal • 37.5g prot • 24.3g glu • 43.5g lip",
    description: "Bowl healthy et protéiné parfait pour le déjeuner",
    ingredients: [
      ["saumon", "120g"],
      ["avocat", "80g"],
      ["quinoa cuit", "100g"],
      ["épinards", "50g"],
      ["huile olive", "1 cuillère"],
    ],
    instructions: [
      "Cuire le quinoa",
      "Griller le saumon",
      "Couper l'avocat",
      "Assembler le bowl",
    ]
  },

  "R002": {
    nom: "Smoothie protéiné banane-cacao",
    categorie: "petit_dejeuner",
    difficulte: "très facile",
    temps: "5 min",
    kcal: 403.1,
    proteines: 38.8,
    glucides: 36.1,
    lipides: 11.4,
    macros_display: "403.1 kcal • 38.8g prot • 36.1g glu • 11.4g lip",
    description: "Smoothie énergisant pour commencer la journée",
    ingredients: [
      ["banane", "100g"],
      ["protéine whey", "30g"],
      ["lait écrémé", "250ml"],
      ["cacao non sucré", "10g"],
      ["amandes", "15g"],
    ],
    instructions: [
      "Mixer tous les ingrédients",
      "Servir frais",
    ]
  },

  "R003": {
    nom: "Salade de poulet méditerranéenne",
    categorie: "dejeuner",
    difficulte: "facile",
    temps: "20 min",
    kcal: 693.3,
    proteines: 63.1,
    glucides: 6.4,
    lipides: 44.4,
    macros_display: "693.3 kcal • 63.1g prot • 6.4g glu • 44.4g lip",
    description: "Salade fraîche et équilibrée",
    ingredients: [
      ["blanc de poulet", "150g"],
      ["salade verte", "100g"],
      ["tomate", "100g"],
      ["concombre", "80g"],
      ["mozzarella", "50g"],
      ["huile olive", "2 cuillères"],
    ],
    instructions: [
      "Griller le poulet",
      "Couper les légumes",
      "Assembler",
      "Assaisonner",
    ]
  },

  "R004": {
    nom: "Overnight oats aux baies",
    categorie: "petit_dejeuner",
    difficulte: "très facile",
    temps: "5 min (+nuit)",
    kcal: 405.3,
    proteines: 26.8,
    glucides: 53.7,
    lipides: 9.6,
    macros_display: "405.3 kcal • 26.8g prot • 53.7g glu • 9.6g lip",
    description: "Petit-déjeuner préparé la veille",
    ingredients: [
      ["avoine", "50g"],
      ["yaourt grec 0%", "150g"],
      ["baies mélangées", "80g"],
      ["miel", "10g"],
      ["amandes", "10g"],
    ],
    instructions: [
      "Mélanger avoine et yaourt",
      "Ajouter les baies",
      "Réfrigérer toute la nuit",
    ]
  },

  "R005": {
    nom: "Wrap protéiné au thon",
    categorie: "dejeuner",
    difficulte: "facile",
    temps: "10 min",
    kcal: 438.5,
    proteines: 42.4,
    glucides: 35.7,
    lipides: 13.5,
    macros_display: "438.5 kcal • 42.4g prot • 35.7g glu • 13.5g lip",
    description: "Wrap rapide et nutritif",
    ingredients: [
      ["thon", "100g"],
      ["pain complet", "80g"],
      ["avocat", "60g"],
      ["salade verte", "30g"],
      ["tomate", "50g"],
    ],
    instructions: [
      "Étaler l'avocat sur le wrap",
      "Ajouter thon et légumes",
      "Rouler",
    ]
  },

};


// Fonction pour afficher les macros dans l'interface
function displayRecipeMacros(recipeId) {
  const recipe = recipes[recipeId];
  if (!recipe) return "";
  
  return `
    <div class="recipe-macros">
      <span class="kcal">${recipe.kcal} kcal</span>
      <span class="macro">🥩 ${recipe.proteines}g</span>
      <span class="macro">🍞 ${recipe.glucides}g</span>
      <span class="macro">🥑 ${recipe.lipides}g</span>
    </div>
  `;
}

// CSS pour styliser les macros
const macrosCSS = `
.recipe-macros {
  display: flex;
  gap: 8px;
  margin-top: 8px;
  font-size: 12px;
  color: var(--muted);
}

.recipe-macros .kcal {
  font-weight: 500;
  color: var(--accent);
}

.recipe-macros .macro {
  background: var(--surface2);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 11px;
}
`;

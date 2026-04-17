
# 🔥 GUIDE D'INTÉGRATION MACROS DANS COREFY

## 1. MODIFICATIONS CSS
Ajoute ce CSS dans ta section `<style>` existante :

```css
/* Macros nutritionnelles */
.recipe-macros {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 8px;
  padding: 6px 0;
  font-size: 11px;
  border-top: 0.5px solid var(--border);
  color: var(--muted);
}

.recipe-macros .kcal {
  font-weight: 500;
  color: var(--accent);
  margin-right: 4px;
}

.recipe-macros .macro {
  background: var(--surface2);
  padding: 2px 5px;
  border-radius: 3px;
  font-size: 10px;
  font-weight: 500;
}

.recipe-macros .macro.protein { background: rgba(255, 107, 53, 0.1); color: var(--accent2); }
.recipe-macros .macro.carbs { background: rgba(255, 211, 42, 0.1); color: var(--yellow); }
.recipe-macros .macro.fats { background: rgba(0, 245, 160, 0.1); color: var(--accent); }
```

## 2. AJOUT DU CALCULATEUR JS
Ajoute les fonctions JavaScript dans ta section script.

## 3. MODIFICATION DES CARTES RECETTES
Dans ta fonction qui génère les cartes de recettes, ajoute :

```javascript
// Calculer les macros
const macros = calculateRecipeMacros(recipe.ingredients);
const macrosHTML = generateMacrosHTML(macros);

// Puis ajouter ${macrosHTML} dans ton template HTML
```

## 4. EXEMPLE FINAL
Résultat attendu dans chaque carte recette :
```
Bowl protéiné avocat-saumon
15 min • facile
Bowl healthy et protéiné parfait pour le déjeuner

[641.7 kcal] [🥩 37.5g] [🍞 24.3g] [🥑 43.5g]
```

## 5. AVANTAGES
✅ Calcul automatique des macros
✅ Base de données nutritionnelle intégrée  
✅ Affichage responsive mobile
✅ Couleurs codées par type de macro
✅ Compatible avec ton design existant

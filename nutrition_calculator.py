"""
Base de données nutritionnelle pour COREFY
Calcul des macros : protéines, glucides, lipides, kcal
Valeurs pour 100g de chaque ingrédient
"""

# Base de données nutritionnelle (pour 100g)
# Format: "ingrédient": {"kcal": X, "proteines": Y, "glucides": Z, "lipides": W}

NUTRITION_DB = {
    # PROTÉINES ANIMALES
    "blanc de poulet": {"kcal": 165, "proteines": 31, "glucides": 0, "lipides": 3.6},
    "saumon": {"kcal": 208, "proteines": 25, "glucides": 0, "lipides": 12},
    "thon": {"kcal": 132, "proteines": 30, "glucides": 0, "lipides": 1},
    "crevettes": {"kcal": 85, "proteines": 20, "glucides": 0, "lipides": 1},
    "oeuf entier": {"kcal": 155, "proteines": 13, "glucides": 1, "lipides": 11},
    "blanc d'oeuf": {"kcal": 52, "proteines": 11, "glucides": 1, "lipides": 0.2},
    "boeuf maigre": {"kcal": 190, "proteines": 26, "glucides": 0, "lipides": 9},
    "jambon blanc": {"kcal": 115, "proteines": 21, "glucides": 1, "lipides": 3},
    
    # PRODUITS LAITIERS
    "yaourt grec 0%": {"kcal": 59, "proteines": 10, "glucides": 4, "lipides": 0.4},
    "fromage blanc 0%": {"kcal": 45, "proteines": 8, "glucides": 4, "lipides": 0.2},
    "lait écrémé": {"kcal": 34, "proteines": 3.4, "glucides": 5, "lipides": 0.1},
    "mozzarella": {"kcal": 280, "proteines": 28, "glucides": 2, "lipides": 17},
    "parmesan": {"kcal": 392, "proteines": 36, "glucides": 1, "lipides": 26},
    
    # LÉGUMINEUSES
    "lentilles cuites": {"kcal": 116, "proteines": 9, "glucides": 16, "lipides": 0.4},
    "haricots rouges": {"kcal": 127, "proteines": 8.7, "glucides": 22, "lipides": 0.5},
    "pois chiches": {"kcal": 164, "proteines": 8, "glucides": 27, "lipides": 2.6},
    "tofu": {"kcal": 76, "proteines": 8, "glucides": 2, "lipides": 4.8},
    
    # CÉRÉALES & FÉCULENTS
    "riz basmati cuit": {"kcal": 121, "proteines": 2.5, "glucides": 25, "lipides": 0.3},
    "quinoa cuit": {"kcal": 120, "proteines": 4.4, "glucides": 22, "lipides": 1.9},
    "avoine": {"kcal": 389, "proteines": 17, "glucides": 66, "lipides": 6.9},
    "pain complet": {"kcal": 247, "proteines": 13, "glucides": 41, "lipides": 4.2},
    "pâtes complètes cuites": {"kcal": 124, "proteines": 5, "glucides": 23, "lipides": 1.1},
    "patate douce": {"kcal": 86, "proteines": 2, "glucides": 20, "lipides": 0.1},
    
    # LÉGUMES
    "brocolis": {"kcal": 25, "proteines": 3, "glucides": 2, "lipides": 0.4},
    "épinards": {"kcal": 23, "proteines": 2.9, "glucides": 1.4, "lipides": 0.4},
    "courgette": {"kcal": 17, "proteines": 1.2, "glucides": 2.1, "lipides": 0.3},
    "tomate": {"kcal": 18, "proteines": 0.9, "glucides": 2.7, "lipides": 0.2},
    "concombre": {"kcal": 12, "proteines": 0.6, "glucides": 1.8, "lipides": 0.1},
    "salade verte": {"kcal": 13, "proteines": 1.2, "glucides": 1.3, "lipides": 0.2},
    "poivron": {"kcal": 20, "proteines": 1, "glucides": 3.9, "lipides": 0.3},
    "champignons": {"kcal": 11, "proteines": 2.5, "glucides": 0.6, "lipides": 0.1},
    
    # FRUITS
    "banane": {"kcal": 89, "proteines": 1.1, "glucides": 20, "lipides": 0.3},
    "pomme": {"kcal": 52, "proteines": 0.3, "glucides": 12, "lipides": 0.2},
    "avocat": {"kcal": 160, "proteines": 2, "glucides": 2, "lipides": 15},
    "baies mélangées": {"kcal": 43, "proteines": 1.4, "glucides": 8.1, "lipides": 0.3},
    
    # OLÉAGINEUX & GRAISSES
    "amandes": {"kcal": 575, "proteines": 21, "glucides": 7, "lipides": 53},
    "noix": {"kcal": 654, "proteines": 15, "glucides": 7, "lipides": 65},
    "graines de tournesol": {"kcal": 584, "proteines": 21, "glucides": 11, "lipides": 51},
    "huile olive": {"kcal": 884, "proteines": 0, "glucides": 0, "lipides": 100},
    "beurre de cacahuète": {"kcal": 588, "proteines": 25, "glucides": 8, "lipides": 50},
    
    # AUTRES
    "miel": {"kcal": 304, "proteines": 0.3, "glucides": 75, "lipides": 0},
    "cacao non sucré": {"kcal": 229, "proteines": 20, "glucides": 11, "lipides": 14},
    "protéine whey": {"kcal": 400, "proteines": 80, "glucides": 5, "lipides": 5}
}

def find_ingredient_match(ingredient_name):
    """
    Trouve la correspondance la plus proche pour un ingrédient
    """
    ingredient_lower = ingredient_name.lower()
    
    # Recherche exacte d'abord
    if ingredient_lower in NUTRITION_DB:
        return NUTRITION_DB[ingredient_lower]
    
    # Recherche par mots-clés
    for db_ingredient, values in NUTRITION_DB.items():
        if any(keyword in ingredient_lower for keyword in db_ingredient.split()):
            return values
    
    # Valeurs par défaut si rien trouvé (légume générique)
    return {"kcal": 25, "proteines": 2, "glucides": 4, "lipides": 0.2}

def parse_quantity(quantity_str):
    """
    Parse les quantités comme "150g", "2 cuillères", "1 tasse", etc.
    Retourne les grammes équivalents
    """
    if not quantity_str:
        return 100  # Défaut 100g
    
    quantity_lower = quantity_str.lower().strip()
    
    # Extraire les nombres
    import re
    numbers = re.findall(r'\d+(?:\.\d+)?', quantity_lower)
    if not numbers:
        return 100
    
    base_amount = float(numbers[0])
    
    # Conversions courantes
    if 'g' in quantity_lower or 'gram' in quantity_lower:
        return base_amount
    elif 'kg' in quantity_lower:
        return base_amount * 1000
    elif 'cuillère' in quantity_lower or 'càs' in quantity_lower:
        return base_amount * 15  # 1 càs ≈ 15g
    elif 'càc' in quantity_lower or 'cuillère à café' in quantity_lower:
        return base_amount * 5   # 1 càc ≈ 5g
    elif 'tasse' in quantity_lower or 'cup' in quantity_lower:
        return base_amount * 150 # 1 tasse ≈ 150g
    elif 'tranche' in quantity_lower:
        return base_amount * 30  # 1 tranche ≈ 30g
    elif 'pièce' in quantity_lower or 'unité' in quantity_lower:
        return base_amount * 100 # 1 pièce ≈ 100g (moyenne)
    else:
        return base_amount  # Assume grammes par défaut

def calculate_macros(ingredients_list):
    """
    Calcule les macros totales pour une liste d'ingrédients
    
    Args:
        ingredients_list: Liste de tuples (nom_ingredient, quantité)
    
    Returns:
        dict: {"kcal": X, "proteines": Y, "glucides": Z, "lipides": W}
    """
    total_macros = {"kcal": 0, "proteines": 0, "glucides": 0, "lipides": 0}
    
    for ingredient_name, quantity in ingredients_list:
        # Trouver les valeurs nutritionnelles
        nutrition = find_ingredient_match(ingredient_name)
        
        # Parser la quantité
        grams = parse_quantity(quantity)
        
        # Calculer pour cette quantité (base = 100g)
        multiplier = grams / 100
        
        for macro in total_macros.keys():
            total_macros[macro] += nutrition[macro] * multiplier
    
    # Arrondir les résultats
    for key in total_macros:
        total_macros[key] = round(total_macros[key], 1)
    
    return total_macros

# Test avec une recette exemple
if __name__ == "__main__":
    # Exemple : salade de poulet
    test_ingredients = [
        ("blanc de poulet", "150g"),
        ("salade verte", "100g"),
        ("tomate", "80g"),
        ("avocat", "50g"),
        ("huile olive", "1 cuillère")
    ]
    
    macros = calculate_macros(test_ingredients)
    print("Test - Salade de poulet:")
    print(f"📊 {macros['kcal']} kcal • {macros['proteines']}g protéines • {macros['glucides']}g glucides • {macros['lipides']}g lipides")

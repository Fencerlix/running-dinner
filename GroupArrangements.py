from itertools import permutations, combinations

def is_valid(history, new_groups, encounters):
    """ Prüft, ob die neuen Gruppen gültig sind, ohne Wiederholungen. """
    for group in new_groups:
        g_set = frozenset(group)
        if g_set in encounters:
            return False  # Diese Gruppe hat sich schon getroffen
    return True

def generate_valid_groups(main_groups, other_groups):
    """ Erstellt 6 gültige Gruppen mit genau einer bestimmten Hauptgruppe pro Gruppe. """
    all_combinations = list(combinations(other_groups, 2))  # Wähle 2 Gruppen aus anderen Kategorien
    valid_groups = []
    
    for main, (g1, g2) in zip(main_groups, all_combinations[:6]):
        valid_groups.append((main, g1, g2))
    
    return valid_groups

def count_valid_arrangements(v_groups, h_groups, n_groups, stage=0, history=None, encounters=None):
    """ Rekursive Funktion zur Zählung aller gültigen Gruppenkombinationen. """
    if history is None:
        history = [[] for _ in range(3)]  # 3 Stages, jede mit 6 Gruppenkombinationen
    if encounters is None:
        encounters = set()  # Speichert bereits getroffene Gruppen
    
    if stage == 3:
        print_history(history)
        return 1  # Eine vollständige Kombination gefunden, Rekursionsanker
    
    valid_count = 0
    if stage == 0:
        main_groups, other_groups = v_groups, h_groups + n_groups  # V als Hauptgruppe
    elif stage == 1:
        main_groups, other_groups = h_groups, v_groups + n_groups  # H als Hauptgruppe
    elif stage == 2:
        main_groups, other_groups = n_groups, v_groups + h_groups  # N als Hauptgruppe
    
    possible_combinations = permutations(other_groups, 12)  # 12 verfügbare Plätze
    
    
    for selection in possible_combinations:
        new_groups = generate_valid_groups(main_groups, list(selection)[:12])
        
        if is_valid(history, new_groups, encounters):
            new_history = [row[:] for row in history]  # Deepcopy des bisherigen Verlaufs
            new_history[stage] = new_groups  # Speichere Gruppen für diese Stage
            new_encounters = encounters | {frozenset(g) for g in new_groups}  # Update Begegnungen
            valid_count += count_valid_arrangements(v_groups, h_groups, n_groups, stage + 1, new_history, new_encounters)
    
    return valid_count

def print_history(history):
    print(history[1])
    print(history[2])
    print(history[3])

# Gruppen
vorspeisen = [f"V{i}" for i in range(1, 7)]
hauptspeisen = [f"H{i}" for i in range(1, 7)]
nachspeisen = [f"N{i}" for i in range(1, 7)]

# Anzahl der gültigen Kombinationen berechnen
anzahl_kombinationen = count_valid_arrangements(vorspeisen, hauptspeisen, nachspeisen)
print(f"Anzahl gültiger Kombinationen: {anzahl_kombinationen}")


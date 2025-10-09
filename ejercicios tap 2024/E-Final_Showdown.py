def can_defeat_beast_dp(weapons, initial_power, beast_health):
    """
    Verifica si es posible derrotar a The Beast usando programación dinámica optimizada.
    
    Args:
        weapons: Lista de tuplas (A, B, C) representando las armas
        initial_power: Poder inicial del héroe
        beast_health: Vida inicial de The Beast
    
    Returns:
        bool: True si es posible derrotarla, False en caso contrario
    """
    n = len(weapons)
    
    # OPTIMIZACIÓN: Ordenamos las armas por eficiencia (daño/poder_consumido)
    # Esto ayuda a encontrar soluciones más rápido
    weapons_sorted = sorted(weapons, key=lambda w: w[2] / max(1, w[1]), reverse=True)
    
    # MEMOIZACIÓN MANUAL: Diccionario para almacenar resultados ya calculados
    memo = {}
    
    def dp(power, remaining_health, used_mask):
        """
        Función de programación dinámica con memoización manual.
        
        Args:
            power: Poder actual del héroe
            remaining_health: Vida restante de The Beast
            used_mask: Máscara de bits indicando qué armas se han usado
        
        Returns:
            bool: True si es posible derrotar a The Beast desde este estado
        """
        # Creamos la clave del estado para la memoización
        state = (power, remaining_health, used_mask)
        
        # Si ya calculamos este estado, retornamos el resultado guardado
        if state in memo:
            return memo[state]
        
        # OPTIMIZACIÓN: Casos base tempranos
        if remaining_health <= 0:
            memo[state] = power >= 0
            return memo[state]
        
        if power < 0:
            memo[state] = False
            return memo[state]
        
        if used_mask == (1 << n) - 1:
            memo[state] = False
            return memo[state]
        
        # OPTIMIZACIÓN: Verificación rápida de poder insuficiente
        # Si el poder es muy bajo, es improbable que podamos continuar
        if power < 5:  # Umbral heurístico
            memo[state] = False
            return memo[state]
        
        # Probamos usar cada arma disponible (ordenadas por eficiencia)
        for i in range(n):
            if used_mask & (1 << i):
                continue
            
            A, B, C = weapons_sorted[i]
            
            # OPTIMIZACIÓN: Verificación temprana de poder insuficiente
            if power <= B:
                continue
            
            # OPTIMIZACIÓN: Si esta arma puede matar a The Beast directamente
            if C >= remaining_health and power > B:
                new_power = (power - B) // A
                if new_power >= 0:
                    memo[state] = True
                    return memo[state]
            
            # Calculamos el nuevo estado
            new_power = (power - B) // A
            new_health = remaining_health - C
            new_mask = used_mask | (1 << i)
            
            # Recursión con el nuevo estado
            if dp(new_power, new_health, new_mask):
                memo[state] = True
                return memo[state]
        
        # Si ninguna arma funciona desde este estado, perdemos
        memo[state] = False
        return memo[state]
    
    return dp(initial_power, beast_health, 0)


def solve_final_showdown():
    """
    Función principal que resuelve el problema Final Showdown.
    
    Estrategia:
    1. Leer entrada
    2. Usar búsqueda binaria para encontrar la máxima vida posible
    3. Para cada valor de vida, usar programación dinámica optimizada
    4. Retornar el máximo valor válido
    """
    # Lectura de entrada
    N, P = map(int, input().split())
    
    weapons = []
    for _ in range(N):
        A, B, C = map(int, input().split())
        weapons.append((A, B, C))
    
    # BÚSQUEDA BINARIA: Encontramos la máxima vida posible
    left = 0
    right = sum(C for _, _, C in weapons)  # Máximo daño posible
    
    # OPTIMIZACIÓN: Ajustamos el rango derecho para casos extremos
    max_possible_health = min(right, P * 100)  # Límite heurístico
    right = max_possible_health
    
    best_health = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # PROGRAMACIÓN DINÁMICA OPTIMIZADA
        if can_defeat_beast_dp(weapons, P, mid):
            best_health = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return best_health


# Ejecutamos la solución
if __name__ == "__main__":
    result = solve_final_showdown()
    print(result)

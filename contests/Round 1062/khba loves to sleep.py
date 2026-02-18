import sys

def solve():
    n, k, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort() # Ordenar las posiciones de los amigos
    
    # --- Función check(t) ---
    # ¿Podemos colocar k teleports si el tiempo mínimo debe ser 't'?
    def check(t):
        """
        Verifica si es posible colocar k teleports tal que todos los amigos
        estén a una distancia de al menos 't' de su teleport más cercano.
        
        Devuelve (bool: es_posible, list: intervalos_prohibidos_fusionados)
        """
        
        # Si t=0, |a_i - p| < 0 es imposible. No hay zonas prohibidas.
        if t == 0:
            return (x + 1) >= k, []

        # Crear los intervalos prohibidos para cada amigo
        # Prohibido: |a_i - p| < t  =>  a_i - t < p < a_i + t
        # En enteros: [a_i - t + 1, a_i + t - 1]
        intervals = []
        for pos in a:
            L = max(0, pos - t + 1)
            R = min(x, pos + t - 1)
            if R >= L: # Solo añadir si es un intervalo válido
                intervals.append((L, R))
        
        if not intervals:
            # No hay amigos, o 't' es tan grande que no crea intervalos válidos
            return (x + 1) >= k, []

        # Fusionar los intervalos prohibidos
        # Como 'a' está ordenado, los 'L' de los intervalos están casi ordenados,
        # lo que hace que la fusión sea eficiente (O(n)).
        merged = []
        curr_L, curr_R = intervals[0]
        
        for i in range(1, len(intervals)):
            next_L, next_R = intervals[i]
            
            # Si hay superposición o son adyacentes (ej: [1,2] y [3,4])
            if next_L <= curr_R + 1:
                curr_R = max(curr_R, next_R) # Fusionar
            else:
                # Hay un hueco, guardar el intervalo anterior
                merged.append((curr_L, curr_R))
                curr_L, curr_R = next_L, next_R
        
        # Añadir el último intervalo que estábamos procesando
        merged.append((curr_L, curr_R))

        # Calcular el total de posiciones prohibidas
        total_forbidden = 0
        for L, R in merged:
            total_forbidden += (R - L + 1)
        
        # Total de posiciones permitidas
        allowed_positions = (x + 1) - total_forbidden
        
        return allowed_positions >= k, merged

    # --- Búsqueda Binaria sobre el tiempo 't' ---
    low = 0
    high = x + 1  # El tiempo puede ser hasta x
    ans_t = 0     # Guardará el tiempo óptimo (el 't' máximo que funciona)

    while low <= high:
        mid_t = (low + high) // 2
        is_possible, _ = check(mid_t)
        
        if is_possible:
            ans_t = mid_t     # Este tiempo 'mid_t' funciona
            low = mid_t + 1   # Intentemos un tiempo mayor
        else:
            high = mid_t - 1  # Este tiempo 'mid_t' es demasiado grande

    # --- Obtener y mostrar las k posiciones ---
    # Ejecutamos check() una última vez con el tiempo óptimo
    # para obtener la lista final de intervalos prohibidos.
    _, final_forbidden_intervals = check(ans_t)
    
    result = []
    k_needed = k
    pos = 0            # Posición actual que estamos comprobando
    interval_idx = 0   # Índice del intervalo prohibido actual

    while k_needed > 0 and pos <= x:
        # Si ya pasamos todos los intervalos prohibidos
        if interval_idx >= len(final_forbidden_intervals):
            result.append(str(pos))
            pos += 1
            k_needed -= 1
            continue
        
        # Intervalo prohibido actual
        curr_L, curr_R = final_forbidden_intervals[interval_idx]
        
        if pos < curr_L:
            # Estamos en un hueco permitido
            result.append(str(pos))
            pos += 1
            k_needed -= 1
        else: # pos >= curr_L
            # Estamos dentro de un intervalo prohibido
            # Saltar al final de este intervalo
            pos = curr_R + 1
            interval_idx += 1 # Moverse al siguiente intervalo prohibido

    print(" ".join(result))

# --- Bucle principal para múltiples casos de prueba ---
num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()

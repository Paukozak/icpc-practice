import math

class Point3D:
    """Clase para representar puntos en 3D con coordenadas (x, y, z)"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __sub__(self, other):
        """Operación de resta entre dos puntos (vector resultante)"""
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __add__(self, other):
        """Operación de suma entre dos puntos"""
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, scalar):
        """Multiplicación por escalar"""
        return Point3D(self.x * scalar, self.y * scalar, self.z * scalar)

def cross_product(a, b):
    """Producto cruz entre dos vectores 3D"""
    return Point3D(
        a.y * b.z - a.z * b.y,
        a.z * b.x - a.x * b.z,
        a.x * b.y - a.y * b.x
    )

def dot_product(a, b):
    """Producto punto entre dos vectores 3D"""
    return a.x * b.x + a.y * b.y + a.z * b.z

def point_in_polygon(point, polygon):
    """
    Algoritmo Ray Casting para determinar si un punto está dentro de un polígono
    Cuenta el número de intersecciones con los bordes del polígono
    """
    x, y = point.x, point.y
    n = len(polygon)
    inside = False
    
    # Algoritmo de Ray Casting: trazamos un rayo horizontal desde el punto
    # y contamos las intersecciones con los bordes del polígono
    for i in range(n):
        j = (i + 1) % n
        xi, yi = polygon[i].x, polygon[i].y
        xj, yj = polygon[j].x, polygon[j].y
        
        # Verificamos si el rayo horizontal intersecta con el borde
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
    
    return inside

def ray_triangle_intersection(ray_origin, ray_direction, triangle):
    """
    Algoritmo Möller–Trumbore para intersección rayo-triángulo
    Determina si un rayo intersecta con un triángulo 3D
    """
    # Vértices del triángulo
    v0, v1, v2 = triangle
    
    # Vectores de dos bordes del triángulo
    edge1 = v1 - v0
    edge2 = v2 - v0
    
    # Vector perpendicular al plano del triángulo
    h = cross_product(ray_direction, edge2)
    
    # Producto punto entre edge1 y h
    a = dot_product(edge1, h)
    
    # Si a es muy cercano a 0, el rayo es paralelo al triángulo
    if abs(a) < 1e-8:
        return False
    
    # Vector del origen del rayo al primer vértice del triángulo
    s = ray_origin - v0
    
    # Coordenada baricéntrica u
    u = dot_product(s, h) / a
    if u < 0.0 or u > 1.0:
        return False
    
    # Vector perpendicular para calcular v
    q = cross_product(s, edge1)
    
    # Coordenada baricéntrica v
    v = dot_product(ray_direction, q) / a
    if v < 0.0 or u + v > 1.0:
        return False
    
    # Parámetro t del rayo
    t = dot_product(edge2, q) / a
    
    return t > 1e-8

def ray_pyramid_intersection(ray_origin, ray_direction, base_polygon, apex):
    """
    Verifica si un rayo intersecta con la pirámide
    La pirámide se compone de triángulos formados por la base y el vértice
    """
    n = len(base_polygon)
    
    # Verificamos intersección con cada triángulo de la pirámide
    for i in range(n):
        j = (i + 1) % n
        
        # Triángulo formado por dos vértices consecutivos de la base y el vértice
        triangle = (base_polygon[i], base_polygon[j], apex)
        
        if ray_triangle_intersection(ray_origin, ray_direction, triangle):
            return True
    
    return False

def solve_discovering_ngipto():
    """
    Función principal que resuelve el problema Discovering Ngipto
    Utiliza ray casting para determinar si existe sombra
    """
    # Lectura de entrada
    N = int(input())  # Número de vértices del polígono base
    
    # Coordenadas del vértice de la pirámide
    x_apex, y_apex, z_apex = map(int, input().split())
    apex = Point3D(x_apex, y_apex, z_apex)
    
    # Coordenadas del sol
    x_sun, y_sun, z_sun = map(int, input().split())
    sun = Point3D(x_sun, y_sun, z_sun)
    
    # Lectura de los vértices del polígono base
    base_polygon = []
    for _ in range(N):
        x, y = map(int, input().split())
        base_polygon.append(Point3D(x, y, 0))  # Z = 0 para puntos en el desierto
    
    # Estrategia: buscamos puntos candidatos fuera del polígono base
    # y verificamos si están en sombra
    
    # Encontramos los límites del polígono para generar puntos candidatos
    min_x = min(p.x for p in base_polygon) - 1
    max_x = max(p.x for p in base_polygon) + 1
    min_y = min(p.y for p in base_polygon) - 1
    max_y = max(p.y for p in base_polygon) + 1
    
    # Generamos puntos candidatos muy cerca del polígono base
    # Para polígonos no convexos, los puntos en sombra suelen estar cerca
    candidate_points = []
    
    # Puntos en los bordes de la cuadrícula
    for x in range(min_x, max_x + 1):
        candidate_points.append(Point3D(x, min_y, 0))
        candidate_points.append(Point3D(x, max_y, 0))
    
    for y in range(min_y + 1, max_y):
        candidate_points.append(Point3D(min_x, y, 0))
        candidate_points.append(Point3D(max_x, y, 0))
    
    # Puntos adicionales muy cerca del polígono (importante para polígonos no convexos)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # Solo agregamos puntos que estén muy cerca del polígono
            point = Point3D(x, y, 0)
            if not point_in_polygon(point, base_polygon):
                # Verificamos si está muy cerca de algún borde del polígono
                min_distance = float('inf')
                for i in range(len(base_polygon)):
                    j = (i + 1) % len(base_polygon)
                    p1, p2 = base_polygon[i], base_polygon[j]
                    # Distancia al segmento de línea
                    dist = point_to_line_distance(point, p1, p2)
                    min_distance = min(min_distance, dist)
                
                # Solo agregamos puntos muy cerca (distancia < 2)
                if min_distance < 2:
                    candidate_points.append(point)
    
    # Verificamos cada punto candidato
    for point in candidate_points:
        # Solo consideramos puntos fuera del polígono base
        if not point_in_polygon(point, base_polygon):
            # Vector dirección del rayo (del sol al punto)
            # Para que un punto esté en sombra, el rayo del sol al punto debe intersectar la pirámide
            ray_direction = point - sun
            
            # Debug: imprimimos información del punto candidato
            print(f"Verificando punto candidato: ({point.x}, {point.y})")
            
            # Verificamos si este rayo intersecta con la pirámide
            if ray_pyramid_intersection(sun, ray_direction, base_polygon, apex):
                print(f"¡Punto ({point.x}, {point.y}) está en sombra!")
                return "S"  # Existe sombra
            else:
                print(f"Punto ({point.x}, {point.y}) NO está en sombra")
    
    return "N"  # No existe sombra

# Ejecución del programa
if __name__ == "__main__":
    result = solve_discovering_ngipto()
    print(result)

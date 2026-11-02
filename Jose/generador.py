import json
import random

def generar_instancias():
    random.seed(42)
    
    configuraciones = [
        {"tipo": "Pequeña", "cat": (3,4), 
         "alt": (5,10), "libres": (2,4), "cant": 5},
        {"tipo": "Mediana", "cat": (5,5), 
         "alt": (11,25), "libres": (5,8), "cant": 5},
        {"tipo": "Grande", "cat": (5,5), 
         "alt": (26,50), "libres": (9,15), "cant": 5}
    ]
    
    id_instancia = 1
    
    for config in configuraciones:
        for _ in range(config["cant"]):
            c_min, c_max = config["cat"]
            a_min, a_max = config["alt"]
            l_min, l_max = config["libres"]
            
            num_cat = random.randint(c_min, c_max)
            num_alt = random.randint(a_min, a_max)
            num_libres = random.randint(l_min, l_max)
            num_fijos = random.randint(2, 4)
            
            categorias = [f"CAT-{c+1}" for c in range(num_cat)]
            catalogo = {}
            
            # Generar catálogo asegurando que menor U -> mayor C
            for cat in categorias:
                alternativas = []
                for j in range(num_alt):
                    u_val = round(random.uniform(0.3, 3.5), 2)
                    ruido = random.uniform(-0.1, 0.1)
                    c_val = round((15000 / u_val) * (1 + ruido), 0)
                    
                    alternativas.append({
                        "id_alt": f"ALT-{cat}-{j+1}", 
                        "U": u_val, 
                        "C": c_val
                    })
                catalogo[cat] = alternativas
                
            elementos = []
            area_total = 0
            u_min_ponderado = 0
            
            # Generar elementos libres
            for i in range(num_libres):
                area = round(random.uniform(5.0, 40.0), 2)
                cat_asignada = random.choice(categorias)
                elementos.append({
                    "id_elem": f"ELEM-O-{i+1}",
                    "tipo": "optimizable",
                    "categoria": cat_asignada,
                    "area": area
                })
                
                # Identificar el mejor U para factibilidad
                mejor_u = min([alt["U"] for alt in catalogo[cat_asignada]])
                u_min_ponderado += (mejor_u * area)
                area_total += area
                
            # Generar elementos fijos
            for i in range(num_fijos):
                area = round(random.uniform(5.0, 40.0), 2)
                u_fijo = round(random.uniform(0.8, 3.0), 2)
                c_fijo = round((15000 / u_fijo), 0)
                elementos.append({
                    "id_elem": f"ELEM-F-{i+1}",
                    "tipo": "fijo",
                    "area": area,
                    "U_fijo": u_fijo,
                    "C_fijo": c_fijo
                })
                u_min_ponderado += (u_fijo * area)
                area_total += area
                
            # Calcular U_max garantizando factibilidad
            u_min_global = u_min_ponderado / area_total
            holgura = random.uniform(1.1, 1.5)
            u_max = round(u_min_global * holgura, 2)
            
            # Validación
            assert u_max >= u_min_global, "Error de factibilidad"
            
            instancia_data = {
                "metadata": {
                    "id": f"INST-{id_instancia:02d}",
                    "tamano": config["tipo"],
                    "U_max": u_max
                },
                "catalogo": catalogo,
                "elementos": elementos
            }
            
            # Guardar a JSON
            filename = f"instancia_{id_instancia:02d}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(instancia_data, f, indent=4, ensure_ascii=False)
                
            id_instancia += 1

if __name__ == "__main__":
    generar_instancias()
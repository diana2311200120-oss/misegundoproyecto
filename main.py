
import csv

usuarios = {
    "ana_gomez": [
        {"producto": "Ratón inalámbrico", "categoria": "Informática", "precio": 25.50},
        {"producto": "Teclado mecánico", "categoria": "Informática", "precio": 89.99},
        {"producto": "Alfombrilla XXL", "categoria": "Accesorios", "precio": 15.00}
    ],
    "carlos_ruiz": [
        {"producto": "Monitor 24 pulgadas", "categoria": "Informática", "precio": 145.00},
        {"producto": "Cable HDMI", "categoria": "Accesorios", "precio": 9.95}
    ],
    "laura_m": [
        {"producto": "Silla ergonómica", "categoria": "Mobiliario", "precio": 210.00},
        {"producto": "Lámpara LED", "categoria": "Iluminación", "precio": 32.50},
        {"producto": "Soporte portátil", "categoria": "Accesorios", "precio": 22.00},
        {"producto": "Webcam HD", "categoria": "Informática", "precio": 55.00}
    ],
    "david_perez": []
}

gastos = {}
categorias = {}
productos = []

# Recorrer usuarios y sus compras
for usuario, compras in usuarios.items():
    total = 0

    for compra in compras:
        precio = compra["precio"]
        total += precio

        # Calcular precio con IVA
        compra["precioIVA"] = round(precio * 1.21, 2)

        # Acumular gasto por categoría
        categoria = compra["categoria"]
        categorias[categoria] = categorias.get(categoria, 0) + precio

        # Guardar productos
        productos.append((compra["producto"], precio, usuario))

    gastos[usuario] = total

# 1. Gasto total por usuario
print("\n--- GASTO TOTAL POR USUARIO ---")
for usuario, total in gastos.items():
    print(f"{usuario}: {total:.2f} €")

# 2. Cliente VIP
vip = max(gastos, key=gastos.get)
print("\n--- CLIENTE VIP ---")
print(f"{vip}: {gastos[vip]:.2f} €")

# 3. Cliente con más artículos
articulos = {usuario: len(compras) for usuario, compras in usuarios.items()}
mas_articulos = max(articulos, key=articulos.get)

print("\n--- CLIENTE CON MÁS ARTÍCULOS ---")
print(f"{mas_articulos}: {articulos[mas_articulos]} artículos")

# 4. Producto más caro y más barato
caro = max(productos, key=lambda x: x[1])
barato = min(productos, key=lambda x: x[1])

print("\n--- PRODUCTO MÁS CARO ---")
print(f"{caro[0]}: {caro[1]:.2f} € - Usuario: {caro[2]}")

print("\n--- PRODUCTO MÁS BARATO ---")
print(f"{barato[0]}: {barato[1]:.2f} € - Usuario: {barato[2]}")

# 5. Resumen por categorías
print("\n--- GASTO POR CATEGORÍAS ---")
for categoria, total in categorias.items():
    print(f"{categoria}: {total:.2f} €")

# 6. Mostrar productos con IVA
print("\n--- PRODUCTOS CON IVA ---")
for usuario, compras in usuarios.items():
    for compra in compras:
        print(f"{compra['producto']}: {compra['precioIVA']:.2f} €")

# 7. Crear fichero CSV
with open("contabilidad_a.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["producto", "precioIVA"])

    for usuario, compras in usuarios.items():
        for compra in compras:
            escritor.writerow([compra["producto"], compra["precioIVA"]])

print("\nArchivo contabilidad_a.csv creado correctamente.")

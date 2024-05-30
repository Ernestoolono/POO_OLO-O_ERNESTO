productos = {
    "Papas" : 17.50,
    "Jugos" : 8.65,
    "Galletas" : 24.0,
    "Cheetos" : 12.04,
    "Pan" : 5.0,
}

descuento = 0.1

for producto, precio in productos.items():
    precio_descuento = precio *(1 - descuento)
    productos[producto] = precio_descuento
    print(f"{producto}: {precio:.2f} -> {precio_descuento:.2f}")
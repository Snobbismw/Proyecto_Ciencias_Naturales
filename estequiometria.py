from chempy import balance_stoichiometry

class InterfazQuimica:
    def __init__(self):
        self.reactivos = set()
        self.productos = set()

    def solicitar_datos(self):
        print("Usa mayúsculas correctas (Ej: Na, O, H)")
        reac_input = input("Reactivos: ") 
        self.reactivos = {r.strip() for r in reac_input.split(",") if r.strip()}

        prod_input = input("Productos: ")
        self.productos = {p.strip() for p in prod_input.split(",") if p.strip()}

    def ejecutar_balanceo(self):
        try:
            reac_bal, prod_bal = balance_stoichiometry(self.reactivos, self.productos)
            
            print("\nResultado del Balanceo:")
            self._imprimir_formateado(reac_bal, prod_bal)
        except Exception as e:
            print(f"\nError: No se pudo balancear. Revisa que los elementos existan en ambos lados.")
            print(f"Detalle: {e}")

    def _imprimir_formateado(self, r, p):
        r_str = " + ".join([f"{val if val > 1 else ''}{key}" for key, val in r.items()])
        p_str = " + ".join([f"{val if val > 1 else ''}{key}" for key, val in p.items()])
        print(f"Ecuación: {r_str} --> {p_str}")


app = InterfazQuimica()
app.solicitar_datos()
app.ejecutar_balanceo()
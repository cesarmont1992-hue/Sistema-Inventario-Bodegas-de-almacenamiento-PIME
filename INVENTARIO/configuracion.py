import tkinter as tk
from tkinter import ttk, messagebox

from database.conexion import conectar_bd


# ============================================================
# VENTANA DE CONFIGURACIÓN
# ============================================================

class ConfiguracionVentana(tk.Toplevel):

    def __init__(self, ventana_principal=None):

        if ventana_principal is None:
            super().__init__()
        else:
            super().__init__(ventana_principal)

        self.title("Configuración del sistema")
        self.geometry("850x700")
        self.resizable(False, False)
        self.configure(bg="#F5F1EA")

        self.centrar_ventana()

        # Crear tabla
        self.crear_tabla_configuracion()

        # Crear interfaz
        self.crear_interfaz()

        # Cargar configuración automáticamente
        self.cargar_configuracion()


    # ========================================================
    # CENTRAR VENTANA
    # ========================================================

    def centrar_ventana(self):

        self.update_idletasks()

        ancho = 850
        alto = 700

        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()

        x = (pantalla_ancho - ancho) // 2
        y = (pantalla_alto - alto) // 2

        self.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )


    # ========================================================
    # CREAR TABLA
    # ========================================================

    def crear_tabla_configuracion(self):

        conexion = conectar_bd()
        cursor = conexion.cursor()

        try:

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS configuracion (

                    id INTEGER PRIMARY KEY,

                    nombre_empresa TEXT DEFAULT '',

                    nit TEXT DEFAULT '',

                    telefono TEXT DEFAULT '',

                    direccion TEXT DEFAULT '',

                    iva REAL DEFAULT 19,

                    moneda TEXT DEFAULT 'COP',

                    prefijo_factura TEXT DEFAULT 'FAC',

                    numero_factura INTEGER DEFAULT 1,

                    stock_minimo_alerta REAL DEFAULT 5

                )
            """)

            cursor.execute("""
                SELECT COUNT(*)
                FROM configuracion
            """)

            cantidad = cursor.fetchone()[0]

            if cantidad == 0:

                cursor.execute("""
                    INSERT INTO configuracion
                    (
                        id,
                        nombre_empresa,
                        nit,
                        telefono,
                        direccion,
                        iva,
                        moneda,
                        prefijo_factura,
                        numero_factura,
                        stock_minimo_alerta
                    )
                    VALUES
                    (
                        1,
                        '',
                        '',
                        '',
                        '',
                        19,
                        'COP',
                        'FAC',
                        1,
                        5
                    )
                """)

            conexion.commit()

        except Exception as error:

            conexion.rollback()

            messagebox.showerror(
                "Error de base de datos",
                f"No fue posible crear la configuración.\n\n{error}",
                parent=self
            )

        finally:

            conexion.close()


    # ========================================================
    # INTERFAZ
    # ========================================================

    def crear_interfaz(self):

        # ====================================================
        # ENCABEZADO
        # ====================================================

        encabezado = tk.Frame(
            self,
            bg="#F5F1EA"
        )

        encabezado.pack(
            fill="x",
            padx=30,
            pady=(20, 10)
        )

        tk.Label(
            encabezado,
            text="⚙️ Configuración del sistema",
            bg="#F5F1EA",
            fg="#241F1A",
            font=("Arial", 23, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            encabezado,
            text="Información general de la empresa y parámetros del sistema",
            bg="#F5F1EA",
            fg="#6E6259",
            font=("Arial", 10)
        ).pack(
            anchor="w",
            pady=(3, 0)
        )


        # ====================================================
        # CONTENEDOR DEL FORMULARIO
        # ====================================================

        contenedor = tk.Frame(
            self,
            bg="white",
            bd=1,
            relief="solid"
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=5
        )


        contenedor.columnconfigure(
            1,
            weight=1
        )


        # ====================================================
        # INFORMACIÓN EMPRESA
        # ====================================================

        tk.Label(
            contenedor,
            text="🏢 Información de la empresa",
            bg="white",
            fg="#241F1A",
            font=("Arial", 14, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=25,
            pady=(20, 12)
        )


        # ====================================================
        # NOMBRE EMPRESA
        # ====================================================

        tk.Label(
            contenedor,
            text="Nombre de la empresa:",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.entrada_empresa = ttk.Entry(
            contenedor,
            width=45
        )

        self.entrada_empresa.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # NIT
        # ====================================================

        tk.Label(
            contenedor,
            text="NIT:",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.entrada_nit = ttk.Entry(
            contenedor,
            width=45
        )

        self.entrada_nit.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # TELÉFONO
        # ====================================================

        tk.Label(
            contenedor,
            text="Teléfono:",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.entrada_telefono = ttk.Entry(
            contenedor,
            width=45
        )

        self.entrada_telefono.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # DIRECCIÓN
        # ====================================================

        tk.Label(
            contenedor,
            text="Dirección:",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=4,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.entrada_direccion = ttk.Entry(
            contenedor,
            width=45
        )

        self.entrada_direccion.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # SEPARADOR
        # ====================================================

        ttk.Separator(
            contenedor,
            orient="horizontal"
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=25,
            pady=15
        )


        # ====================================================
        # PARÁMETROS
        # ====================================================

        tk.Label(
            contenedor,
            text="💰 Parámetros del sistema",
            bg="white",
            fg="#241F1A",
            font=("Arial", 14, "bold")
        ).grid(
            row=6,
            column=0,
            columnspan=2,
            sticky="w",
            padx=25,
            pady=(0, 10)
        )


        # ====================================================
        # IVA
        # ====================================================

        tk.Label(
            contenedor,
            text="IVA (%):",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=7,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.entrada_iva = ttk.Entry(
            contenedor,
            width=45
        )

        self.entrada_iva.grid(
            row=7,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # MONEDA
        # ====================================================

        tk.Label(
            contenedor,
            text="Moneda:",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=8,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.combo_moneda = ttk.Combobox(
            contenedor,
            state="readonly",
            values=[
                "COP",
                "USD",
                "EUR"
            ]
        )

        self.combo_moneda.grid(
            row=8,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # PREFIJO
        # ====================================================

        tk.Label(
            contenedor,
            text="Prefijo factura:",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=9,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.entrada_prefijo = ttk.Entry(
            contenedor,
            width=45
        )

        self.entrada_prefijo.grid(
            row=9,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # NÚMERO FACTURA
        # ====================================================

        tk.Label(
            contenedor,
            text="Próximo número de factura:",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=10,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.entrada_numero_factura = ttk.Entry(
            contenedor,
            width=45
        )

        self.entrada_numero_factura.grid(
            row=10,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # STOCK MÍNIMO
        # ====================================================

        tk.Label(
            contenedor,
            text="Alerta de stock mínimo:",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=11,
            column=0,
            sticky="w",
            padx=25,
            pady=5
        )

        self.entrada_stock_minimo = ttk.Entry(
            contenedor,
            width=45
        )

        self.entrada_stock_minimo.grid(
            row=11,
            column=1,
            sticky="ew",
            padx=(5, 25),
            pady=5
        )


        # ====================================================
        # BOTONES
        # ====================================================

        # IMPORTANTE:
        # Este contenedor está FUERA del formulario.
        # Por eso los botones siempre quedan visibles.

        contenedor_botones = tk.Frame(
            self,
            bg="#F5F1EA"
        )

        contenedor_botones.pack(
            fill="x",
            padx=30,
            pady=(10, 18)
        )


        # ====================================================
        # BOTÓN GUARDAR
        # ====================================================

        tk.Button(
            contenedor_botones,
            text="💾 Guardar",
            command=self.guardar_configuracion,
            bg="#477A5B",
            fg="white",
            activebackground="#3C674D",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10
        ).pack(
            side="left",
            padx=5
        )


        # ====================================================
        # BOTÓN CARGAR
        # ====================================================

        tk.Button(
            contenedor_botones,
            text="📂 Cargar",
            command=self.cargar_configuracion,
            bg="#3D6F8E",
            fg="white",
            activebackground="#315A73",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10
        ).pack(
            side="left",
            padx=5
        )


        # ====================================================
        # BOTÓN RESTABLECER
        # ====================================================

        tk.Button(
            contenedor_botones,
            text="🔄 Restablecer",
            command=self.restablecer_configuracion,
            bg="#B88935",
            fg="white",
            activebackground="#96732D",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10
        ).pack(
            side="left",
            padx=5
        )


        # ====================================================
        # BOTÓN CERRAR
        # ====================================================

        tk.Button(
            contenedor_botones,
            text="✖ Cerrar",
            command=self.destroy,
            bg="#8A4B4B",
            fg="white",
            activebackground="#703D3D",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10
        ).pack(
            side="right",
            padx=5
        )


    # ========================================================
    # CARGAR CONFIGURACIÓN
    # ========================================================

    def cargar_configuracion(self):

        conexion = conectar_bd()
        cursor = conexion.cursor()

        try:

            cursor.execute("""
                SELECT
                    nombre_empresa,
                    nit,
                    telefono,
                    direccion,
                    iva,
                    moneda,
                    prefijo_factura,
                    numero_factura,
                    stock_minimo_alerta
                FROM configuracion
                WHERE id = 1
            """)

            datos = cursor.fetchone()

            if datos:

                (
                    nombre_empresa,
                    nit,
                    telefono,
                    direccion,
                    iva,
                    moneda,
                    prefijo_factura,
                    numero_factura,
                    stock_minimo_alerta
                ) = datos


                # Empresa

                self.entrada_empresa.delete(
                    0,
                    tk.END
                )

                self.entrada_empresa.insert(
                    0,
                    nombre_empresa or ""
                )


                # NIT

                self.entrada_nit.delete(
                    0,
                    tk.END
                )

                self.entrada_nit.insert(
                    0,
                    nit or ""
                )


                # Teléfono

                self.entrada_telefono.delete(
                    0,
                    tk.END
                )

                self.entrada_telefono.insert(
                    0,
                    telefono or ""
                )


                # Dirección

                self.entrada_direccion.delete(
                    0,
                    tk.END
                )

                self.entrada_direccion.insert(
                    0,
                    direccion or ""
                )


                # IVA

                self.entrada_iva.delete(
                    0,
                    tk.END
                )

                self.entrada_iva.insert(
                    0,
                    iva
                )


                # Moneda

                self.combo_moneda.set(
                    moneda or "COP"
                )


                # Prefijo

                self.entrada_prefijo.delete(
                    0,
                    tk.END
                )

                self.entrada_prefijo.insert(
                    0,
                    prefijo_factura or "FAC"
                )


                # Número factura

                self.entrada_numero_factura.delete(
                    0,
                    tk.END
                )

                self.entrada_numero_factura.insert(
                    0,
                    numero_factura
                )


                # Stock mínimo

                self.entrada_stock_minimo.delete(
                    0,
                    tk.END
                )

                self.entrada_stock_minimo.insert(
                    0,
                    stock_minimo_alerta
                )


        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No fue posible cargar la configuración.\n\n{error}",
                parent=self
            )

        finally:

            conexion.close()


    # ========================================================
    # GUARDAR CONFIGURACIÓN
    # ========================================================

    def guardar_configuracion(self):

        nombre_empresa = self.entrada_empresa.get().strip()

        nit = self.entrada_nit.get().strip()

        telefono = self.entrada_telefono.get().strip()

        direccion = self.entrada_direccion.get().strip()

        iva = self.entrada_iva.get().strip()

        moneda = self.combo_moneda.get().strip()

        prefijo = self.entrada_prefijo.get().strip()

        numero_factura = self.entrada_numero_factura.get().strip()

        stock_minimo = self.entrada_stock_minimo.get().strip()


        # ====================================================
        # VALIDAR EMPRESA
        # ====================================================

        if not nombre_empresa:

            messagebox.showwarning(
                "Dato faltante",
                "Debes ingresar el nombre de la empresa.",
                parent=self
            )

            self.entrada_empresa.focus()

            return


        # ====================================================
        # VALIDAR IVA
        # ====================================================

        try:

            iva = float(
                iva.replace(",", ".")
            )

        except ValueError:

            messagebox.showwarning(
                "IVA incorrecto",
                "El IVA debe ser un número.\n\nEjemplo: 19",
                parent=self
            )

            self.entrada_iva.focus()

            return


        if iva < 0 or iva > 100:

            messagebox.showwarning(
                "IVA incorrecto",
                "El IVA debe estar entre 0 y 100.",
                parent=self
            )

            self.entrada_iva.focus()

            return


        # ====================================================
        # MONEDA
        # ====================================================

        if not moneda:

            moneda = "COP"


        # ====================================================
        # PREFIJO
        # ====================================================

        if not prefijo:

            prefijo = "FAC"


        # ====================================================
        # NÚMERO FACTURA
        # ====================================================

        try:

            numero_factura = int(
                numero_factura
            )

        except ValueError:

            messagebox.showwarning(
                "Número incorrecto",
                "El número de factura debe ser un número entero.",
                parent=self
            )

            self.entrada_numero_factura.focus()

            return


        if numero_factura < 1:

            messagebox.showwarning(
                "Número incorrecto",
                "El número de factura debe ser mayor que cero.",
                parent=self
            )

            self.entrada_numero_factura.focus()

            return


        # ====================================================
        # STOCK MÍNIMO
        # ====================================================

        try:

            stock_minimo = float(
                stock_minimo.replace(",", ".")
            )

        except ValueError:

            messagebox.showwarning(
                "Stock incorrecto",
                "La alerta de stock mínimo debe ser un número.",
                parent=self
            )

            self.entrada_stock_minimo.focus()

            return


        if stock_minimo < 0:

            messagebox.showwarning(
                "Stock incorrecto",
                "El stock mínimo no puede ser negativo.",
                parent=self
            )

            self.entrada_stock_minimo.focus()

            return


        # ====================================================
        # GUARDAR EN BASE DE DATOS
        # ====================================================

        conexion = conectar_bd()
        cursor = conexion.cursor()

        try:

            cursor.execute("""
                UPDATE configuracion

                SET
                    nombre_empresa = ?,
                    nit = ?,
                    telefono = ?,
                    direccion = ?,
                    iva = ?,
                    moneda = ?,
                    prefijo_factura = ?,
                    numero_factura = ?,
                    stock_minimo_alerta = ?

                WHERE id = 1
            """, (
                nombre_empresa,
                nit,
                telefono,
                direccion,
                iva,
                moneda,
                prefijo,
                numero_factura,
                stock_minimo
            ))

            conexion.commit()

            messagebox.showinfo(
                "Configuración guardada",
                "La configuración fue guardada correctamente.",
                parent=self
            )

        except Exception as error:

            conexion.rollback()

            messagebox.showerror(
                "Error al guardar",
                f"No fue posible guardar la configuración.\n\n{error}",
                parent=self
            )

        finally:

            conexion.close()


    # ========================================================
    # RESTABLECER CONFIGURACIÓN
    # ========================================================

    def restablecer_configuracion(self):

        respuesta = messagebox.askyesno(
            "Restablecer configuración",
            "¿Deseas restablecer la configuración a sus valores iniciales?\n\n"
            "Los datos actuales serán reemplazados.",
            parent=self
        )

        if not respuesta:

            return


        conexion = conectar_bd()
        cursor = conexion.cursor()

        try:

            cursor.execute("""
                UPDATE configuracion

                SET
                    nombre_empresa = '',
                    nit = '',
                    telefono = '',
                    direccion = '',
                    iva = 19,
                    moneda = 'COP',
                    prefijo_factura = 'FAC',
                    numero_factura = 1,
                    stock_minimo_alerta = 5

                WHERE id = 1
            """)

            conexion.commit()

            self.cargar_configuracion()

            messagebox.showinfo(
                "Configuración restablecida",
                "La configuración volvió a sus valores iniciales.",
                parent=self
            )

        except Exception as error:

            conexion.rollback()

            messagebox.showerror(
                "Error",
                f"No fue posible restablecer la configuración.\n\n{error}",
                parent=self
            )

        finally:

            conexion.close()


# ============================================================
# PRUEBA DIRECTA
# ============================================================

if __name__ == "__main__":

    ventana = tk.Tk()

    ventana.withdraw()

    ConfiguracionVentana(ventana)

    ventana.mainloop()
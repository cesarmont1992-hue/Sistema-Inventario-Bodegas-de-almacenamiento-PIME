import tkinter as tk
from tkinter import ttk, messagebox

from database.conexion import conectar_bd


# ============================================================
# VENTANA DE INVENTARIO
# ============================================================

class InventarioVentana(tk.Toplevel):

    def __init__(self, ventana_principal):

        super().__init__(ventana_principal)

        self.ventana_principal = ventana_principal

        self.title("Inventario - Perfumería")
        self.geometry("1100x650")
        self.minsize(950, 550)
        self.configure(bg="#F5F1EA")

        self.centrar_ventana()

        self.crear_interfaz()

        self.cargar_productos()


    # ========================================================
    # CENTRAR VENTANA
    # ========================================================

    def centrar_ventana(self):

        self.update_idletasks()

        ancho = self.winfo_width()
        alto = self.winfo_height()

        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        pos_x = (ancho_pantalla - ancho) // 2
        pos_y = (alto_pantalla - alto) // 2

        self.geometry(
            f"{ancho}x{alto}+{pos_x}+{pos_y}"
        )


    # ========================================================
    # INTERFAZ PRINCIPAL
    # ========================================================

    def crear_interfaz(self):

        encabezado = tk.Frame(
            self,
            bg="#F5F1EA"
        )

        encabezado.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        tk.Label(
            encabezado,
            text="🧴 Inventario de Perfumería",
            bg="#F5F1EA",
            fg="#241F1A",
            font=("Arial", 24, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            encabezado,
            text="Administración de perfumes, fragancias y existencias",
            bg="#F5F1EA",
            fg="#666666",
            font=("Arial", 11)
        ).pack(
            anchor="w",
            pady=(3, 0)
        )


        # ----------------------------------------------------
        # HERRAMIENTAS
        # ----------------------------------------------------

        herramientas = tk.Frame(
            self,
            bg="#FFFFFF"
        )

        herramientas.pack(
            fill="x",
            padx=25,
            pady=10
        )


        # ----------------------------------------------------
        # BUSQUEDAS INDEPENDIENTES
        # ----------------------------------------------------

        panel_busquedas = tk.Frame(
            herramientas,
            bg="#FFFFFF"
        )

        panel_busquedas.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(15, 10),
            pady=10
        )


        # BUSCAR POR CÓDIGO DE PRODUCTO

        fila_codigo = tk.Frame(
            panel_busquedas,
            bg="#FFFFFF"
        )

        fila_codigo.pack(
            fill="x",
            pady=(0, 6)
        )

        tk.Label(
            fila_codigo,
            text="Código de producto:",
            bg="#FFFFFF",
            fg="#333333",
            font=("Arial", 10, "bold"),
            width=19,
            anchor="w"
        ).pack(
            side="left"
        )

        self.entrada_codigo_busqueda = tk.Entry(
            fila_codigo,
            width=25,
            font=("Arial", 11)
        )

        self.entrada_codigo_busqueda.pack(
            side="left",
            padx=(0, 6),
            ipady=3
        )

        tk.Button(
            fila_codigo,
            text="🔍 Buscar",
            command=self.buscar_por_codigo_producto,
            bg="#5B6F8C",
            fg="white",
            activebackground="#4A5C75",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6
        ).pack(
            side="left"
        )

        self.entrada_codigo_busqueda.bind(
            "<Return>",
            self.buscar_por_codigo_producto
        )


        # BUSCAR POR CÓDIGO DE BARRAS

        fila_barras = tk.Frame(
            panel_busquedas,
            bg="#FFFFFF"
        )

        fila_barras.pack(
            fill="x"
        )

        tk.Label(
            fila_barras,
            text="Código de barras:",
            bg="#FFFFFF",
            fg="#333333",
            font=("Arial", 10, "bold"),
            width=19,
            anchor="w"
        ).pack(
            side="left"
        )

        self.entrada_barras_busqueda = tk.Entry(
            fila_barras,
            width=25,
            font=("Arial", 11)
        )

        self.entrada_barras_busqueda.pack(
            side="left",
            padx=(0, 6),
            ipady=3
        )

        tk.Button(
            fila_barras,
            text="📷 Buscar",
            command=self.buscar_codigo_barras,
            bg="#4F6D7A",
            fg="white",
            activebackground="#405863",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6
        ).pack(
            side="left"
        )

        self.entrada_barras_busqueda.bind(
            "<Return>",
            self.buscar_codigo_barras
        )


        # ----------------------------------------------------
        # BOTONES DE ACCIONES
        # ----------------------------------------------------

        panel_acciones = tk.Frame(
            herramientas,
            bg="#FFFFFF"
        )

        panel_acciones.pack(
            side="right",
            padx=(10, 15),
            pady=10
        )

        # Botones de acciones en una sola fila,
        # con el mismo ancho para conservar la simetría.

        tk.Button(
            panel_acciones,
            text="➕ Nuevo perfume",
            command=self.nuevo_producto,
            bg="#477A5B",
            fg="white",
            activebackground="#3C674D",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=14,
            padx=8,
            pady=8
        ).pack(
            side="left",
            padx=4
        )

        tk.Button(
            panel_acciones,
            text="⚙️ Marcas",
            command=self.gestionar_marcas,
            bg="#6B5B45",
            fg="white",
            activebackground="#594B39",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=14,
            padx=8,
            pady=8
        ).pack(
            side="left",
            padx=4
        )

        tk.Button(
            panel_acciones,
            text="✏️ Editar",
            command=self.editar_producto,
            bg="#5B6F8C",
            fg="white",
            activebackground="#4A5C75",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=14,
            padx=8,
            pady=8
        ).pack(
            side="left",
            padx=4
        )

        tk.Button(
            panel_acciones,
            text="🗑️ Eliminar",
            command=self.eliminar_producto,
            bg="#8C3B3B",
            fg="white",
            activebackground="#A94A4A",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=14,
            padx=8,
            pady=8
        ).pack(
            side="left",
            padx=4
        )


        # ----------------------------------------------------
        # TABLA
        # ----------------------------------------------------

        contenedor_tabla = tk.Frame(
            self,
            bg="#FFFFFF"
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(5, 25)
        )

        columnas = (
            "id",
            "codigo",
            "barras",
            "nombre",
            "marca",
            "tipo",
            "genero",
            "presentacion",
            "precio",
            "stock"
        )

        self.tabla = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "id": "ID",
            "codigo": "Código",
            "barras": "Código de barras",
            "nombre": "Perfume",
            "marca": "Marca",
            "tipo": "Tipo",
            "genero": "Género",
            "presentacion": "Presentación",
            "precio": "Precio venta",
            "stock": "Stock"
        }

        for columna, texto in encabezados.items():

            self.tabla.heading(
                columna,
                text=texto
            )

        anchos = {
            "id": 45,
            "codigo": 90,
            "barras": 120,
            "nombre": 190,
            "marca": 120,
            "tipo": 120,
            "genero": 90,
            "presentacion": 90,
            "precio": 110,
            "stock": 70
        }

        for columna, ancho in anchos.items():

            self.tabla.column(
                columna,
                width=ancho
            )

        scrollbar = ttk.Scrollbar(
            contenedor_tabla,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )


    # ========================================================
    # CARGAR PRODUCTOS
    # ========================================================

    def cargar_productos(self):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        conexion = conectar_bd()
        cursor = conexion.cursor()

        consulta = """
            SELECT
                p.id_producto,
                p.codigo,
                p.codigo_barras,
                p.nombre,
                COALESCE(m.nombre, ''),
                COALESCE(t.nombre, ''),
                COALESCE(g.nombre, ''),
                COALESCE(pr.nombre, ''),
                p.precio_venta,
                COALESCE(i.stock_actual, 0)

            FROM productos p

            LEFT JOIN marcas m
                ON p.id_marca = m.id_marca

            LEFT JOIN tipos_fragancia t
                ON p.id_tipo = t.id_tipo

            LEFT JOIN generos g
                ON p.id_genero = g.id_genero

            LEFT JOIN presentaciones pr
                ON p.id_presentacion = pr.id_presentacion

            LEFT JOIN inventario i
                ON p.id_producto = i.id_producto

            WHERE p.activo = 1

            ORDER BY p.id_producto DESC
        """

        cursor.execute(consulta)

        productos = cursor.fetchall()

        for producto in productos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    producto[0],
                    producto[1] or "",
                    producto[2] or "",
                    producto[3],
                    producto[4],
                    producto[5],
                    producto[6],
                    producto[7],
                    f"$ {producto[8]:,.0f}",
                    producto[9]
                )
            )

        conexion.close()


    # ========================================================
    # MOSTRAR RESULTADOS DE BÚSQUEDA
    # ========================================================

    def mostrar_resultados_busqueda(self, productos):

        for fila in self.tabla.get_children():

            self.tabla.delete(fila)

        for producto in productos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    producto[0],
                    producto[1] or "",
                    producto[2] or "",
                    producto[3],
                    producto[4],
                    producto[5],
                    producto[6],
                    producto[7],
                    f"$ {producto[8]:,.0f}",
                    producto[9]
                )
            )

        filas = self.tabla.get_children()

        if len(filas) == 1:

            self.tabla.selection_set(filas[0])
            self.tabla.focus(filas[0])
            self.tabla.see(filas[0])


    # ========================================================
    # BUSCAR POR CÓDIGO DE PRODUCTO
    # ========================================================

    def buscar_por_codigo_producto(self, evento=None):

        codigo = self.entrada_codigo_busqueda.get().strip()

        if not codigo:

            self.cargar_productos()
            self.entrada_codigo_busqueda.focus_set()
            return

        conexion = conectar_bd()
        cursor = conexion.cursor()

        consulta = """
            SELECT
                p.id_producto,
                p.codigo,
                p.codigo_barras,
                p.nombre,
                COALESCE(m.nombre, ''),
                COALESCE(t.nombre, ''),
                COALESCE(g.nombre, ''),
                COALESCE(pr.nombre, ''),
                p.precio_venta,
                COALESCE(i.stock_actual, 0)

            FROM productos p

            LEFT JOIN marcas m
                ON p.id_marca = m.id_marca

            LEFT JOIN tipos_fragancia t
                ON p.id_tipo = t.id_tipo

            LEFT JOIN generos g
                ON p.id_genero = g.id_genero

            LEFT JOIN presentaciones pr
                ON p.id_presentacion = pr.id_presentacion

            LEFT JOIN inventario i
                ON p.id_producto = i.id_producto

            WHERE p.activo = 1
            AND p.codigo = ?

            ORDER BY p.id_producto DESC
        """

        try:

            cursor.execute(
                consulta,
                (codigo,)
            )

            productos = cursor.fetchall()

            self.mostrar_resultados_busqueda(productos)

            if not productos:

                messagebox.showinfo(
                    "Código no encontrado",
                    f"No se encontró un producto con el código:\n\n{codigo}",
                    parent=self
                )

                self.entrada_codigo_busqueda.select_range(
                    0,
                    tk.END
                )
                self.entrada_codigo_busqueda.focus_set()

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No fue posible buscar el código de producto.\n\n{error}",
                parent=self
            )

        finally:

            conexion.close()


    # ========================================================
    # BUSCAR POR CÓDIGO DE BARRAS
    # ========================================================

    def buscar_codigo_barras(self, evento=None):

        codigo_barras = self.entrada_barras_busqueda.get().strip()

        if not codigo_barras:

            self.cargar_productos()
            self.entrada_barras_busqueda.focus_set()
            return

        conexion = conectar_bd()
        cursor = conexion.cursor()

        consulta = """
            SELECT
                p.id_producto,
                p.codigo,
                p.codigo_barras,
                p.nombre,
                COALESCE(m.nombre, ''),
                COALESCE(t.nombre, ''),
                COALESCE(g.nombre, ''),
                COALESCE(pr.nombre, ''),
                p.precio_venta,
                COALESCE(i.stock_actual, 0)

            FROM productos p

            LEFT JOIN marcas m
                ON p.id_marca = m.id_marca

            LEFT JOIN tipos_fragancia t
                ON p.id_tipo = t.id_tipo

            LEFT JOIN generos g
                ON p.id_genero = g.id_genero

            LEFT JOIN presentaciones pr
                ON p.id_presentacion = pr.id_presentacion

            LEFT JOIN inventario i
                ON p.id_producto = i.id_producto

            WHERE p.activo = 1
            AND p.codigo_barras = ?

            ORDER BY p.id_producto DESC
        """

        try:

            cursor.execute(
                consulta,
                (codigo_barras,)
            )

            productos = cursor.fetchall()

            self.mostrar_resultados_busqueda(productos)

            if not productos:

                messagebox.showinfo(
                    "Código no encontrado",
                    f"No se encontró un producto con el código de barras:\n\n{codigo_barras}",
                    parent=self
                )

                self.entrada_barras_busqueda.select_range(
                    0,
                    tk.END
                )
                self.entrada_barras_busqueda.focus_set()

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No fue posible buscar el código de barras.\n\n{error}",
                parent=self
            )

        finally:

            conexion.close()


    # ========================================================
    # OBTENER MARCAS
    # ========================================================

    def obtener_marcas(self):

        conexion = conectar_bd()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT nombre
            FROM marcas
            WHERE activo = 1
            ORDER BY nombre
        """)

        marcas = [
            fila[0]
            for fila in cursor.fetchall()
        ]

        conexion.close()

        return marcas


    # ========================================================
    # OBTENER TIPOS
    # ========================================================

    def obtener_tipos(self):

        conexion = conectar_bd()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT nombre
            FROM tipos_fragancia
            WHERE activo = 1
            ORDER BY nombre
        """)

        tipos = [
            fila[0]
            for fila in cursor.fetchall()
        ]

        conexion.close()

        return tipos


    # ========================================================
    # OBTENER GÉNEROS
    # ========================================================

    def obtener_generos(self):

        conexion = conectar_bd()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT nombre
            FROM generos
            WHERE activo = 1
            ORDER BY nombre
        """)

        generos = [
            fila[0]
            for fila in cursor.fetchall()
        ]

        conexion.close()

        return generos


    # ========================================================
    # OBTENER PRESENTACIONES
    # ========================================================

    def obtener_presentaciones(self):

        conexion = conectar_bd()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT nombre
            FROM presentaciones
            WHERE activo = 1
            ORDER BY nombre
        """)

        presentaciones = [
            fila[0]
            for fila in cursor.fetchall()
        ]

        conexion.close()

        return presentaciones


    # ========================================================
    # GESTIONAR MARCAS
    # ========================================================

    def gestionar_marcas(self):

        ventana = tk.Toplevel(self)

        ventana.title("Gestión de marcas")
        ventana.geometry("500x500")
        ventana.resizable(False, False)
        ventana.configure(bg="#F5F1EA")

        ventana.update_idletasks()

        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()

        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()

        x = (pantalla_ancho - ancho) // 2
        y = (pantalla_alto - alto) // 2

        ventana.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )

        tk.Label(
            ventana,
            text="⚙️ Gestión de marcas",
            bg="#F5F1EA",
            fg="#241F1A",
            font=("Arial", 20, "bold")
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            ventana,
            text="Administra las marcas de tus perfumes",
            bg="#F5F1EA",
            fg="#666666",
            font=("Arial", 10)
        ).pack(
            pady=(0, 15)
        )

        contenedor = tk.Frame(
            ventana,
            bg="#FFFFFF"
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        tabla_marcas = ttk.Treeview(
            contenedor,
            columns=("id", "nombre"),
            show="headings",
            height=12
        )

        tabla_marcas.heading(
            "id",
            text="ID"
        )

        tabla_marcas.heading(
            "nombre",
            text="Marca"
        )

        tabla_marcas.column(
            "id",
            width=60
        )

        tabla_marcas.column(
            "nombre",
            width=300
        )

        tabla_marcas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            contenedor,
            orient="vertical",
            command=tabla_marcas.yview
        )

        tabla_marcas.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )


        def cargar_marcas():

            for fila in tabla_marcas.get_children():

                tabla_marcas.delete(fila)

            conexion = conectar_bd()
            cursor = conexion.cursor()

            cursor.execute("""
                SELECT id_marca, nombre
                FROM marcas
                WHERE activo = 1
                ORDER BY nombre
            """)

            marcas = cursor.fetchall()

            conexion.close()

            for marca in marcas:

                tabla_marcas.insert(
                    "",
                    "end",
                    values=(
                        marca[0],
                        marca[1]
                    )
                )


        def agregar_marca():

            dialogo = tk.Toplevel(ventana)

            dialogo.title("Nueva marca")
            dialogo.geometry("400x220")
            dialogo.resizable(False, False)
            dialogo.configure(bg="#F5F1EA")

            tk.Label(
                dialogo,
                text="Nueva marca",
                bg="#F5F1EA",
                fg="#241F1A",
                font=("Arial", 18, "bold")
            ).pack(
                pady=(25, 15)
            )

            entrada = tk.Entry(
                dialogo,
                width=32,
                font=("Arial", 11)
            )

            entrada.pack(
                pady=5
            )

            entrada.focus()


            def guardar():

                nombre = entrada.get().strip()

                if not nombre:

                    messagebox.showwarning(
                        "Dato faltante",
                        "Escribe el nombre de la marca.",
                        parent=dialogo
                    )

                    return

                conexion = conectar_bd()
                cursor = conexion.cursor()

                try:

                    cursor.execute(
                        """
                        INSERT INTO marcas
                        (
                            nombre,
                            activo
                        )
                        VALUES (?, 1)
                        """,
                        (nombre,)
                    )

                    conexion.commit()

                    messagebox.showinfo(
                        "Marca guardada",
                        "La marca fue agregada correctamente.",
                        parent=dialogo
                    )

                    dialogo.destroy()

                    cargar_marcas()

                except Exception as error:

                    conexion.rollback()

                    messagebox.showerror(
                        "Error",
                        f"No fue posible agregar la marca.\n\n{error}",
                        parent=dialogo
                    )

                finally:

                    conexion.close()


            tk.Button(
                dialogo,
                text="💾 Guardar",
                command=guardar,
                bg="#477A5B",
                fg="white",
                activebackground="#3C674D",
                activeforeground="white",
                font=("Arial", 10, "bold"),
                relief="flat",
                cursor="hand2",
                padx=20,
                pady=8
            ).pack(
                pady=20
            )


        def editar_marca():

            seleccion = tabla_marcas.selection()

            if not seleccion:

                messagebox.showwarning(
                    "Selecciona una marca",
                    "Selecciona primero la marca que deseas editar.",
                    parent=ventana
                )

                return

            datos = tabla_marcas.item(
                seleccion[0],
                "values"
            )

            id_marca = datos[0]
            nombre_actual = datos[1]

            dialogo = tk.Toplevel(ventana)

            dialogo.title("Editar marca")
            dialogo.geometry("400x220")
            dialogo.resizable(False, False)
            dialogo.configure(bg="#F5F1EA")

            tk.Label(
                dialogo,
                text="Editar marca",
                bg="#F5F1EA",
                fg="#241F1A",
                font=("Arial", 18, "bold")
            ).pack(
                pady=(25, 15)
            )

            entrada = tk.Entry(
                dialogo,
                width=32,
                font=("Arial", 11)
            )

            entrada.pack(
                pady=5
            )

            entrada.insert(
                0,
                nombre_actual
            )

            entrada.select_range(
                0,
                tk.END
            )

            entrada.focus()


            def guardar_cambios():

                nuevo_nombre = entrada.get().strip()

                if not nuevo_nombre:

                    messagebox.showwarning(
                        "Dato faltante",
                        "El nombre de la marca no puede quedar vacío.",
                        parent=dialogo
                    )

                    return

                conexion = conectar_bd()
                cursor = conexion.cursor()

                try:

                    cursor.execute(
                        """
                        UPDATE marcas
                        SET nombre = ?
                        WHERE id_marca = ?
                        """,
                        (
                            nuevo_nombre,
                            id_marca
                        )
                    )

                    conexion.commit()

                    messagebox.showinfo(
                        "Marca actualizada",
                        "La marca fue actualizada correctamente.",
                        parent=dialogo
                    )

                    dialogo.destroy()

                    cargar_marcas()

                    self.cargar_productos()

                except Exception as error:

                    conexion.rollback()

                    messagebox.showerror(
                        "Error",
                        f"No fue posible actualizar la marca.\n\n{error}",
                        parent=dialogo
                    )

                finally:

                    conexion.close()


            tk.Button(
                dialogo,
                text="💾 Guardar cambios",
                command=guardar_cambios,
                bg="#477A5B",
                fg="white",
                activebackground="#3C674D",
                activeforeground="white",
                font=("Arial", 10, "bold"),
                relief="flat",
                cursor="hand2",
                padx=20,
                pady=8
            ).pack(
                pady=20
            )


        def desactivar_marca():

            seleccion = tabla_marcas.selection()

            if not seleccion:

                messagebox.showwarning(
                    "Selecciona una marca",
                    "Selecciona primero la marca que deseas desactivar.",
                    parent=ventana
                )

                return

            datos = tabla_marcas.item(
                seleccion[0],
                "values"
            )

            id_marca = datos[0]
            nombre = datos[1]

            respuesta = messagebox.askyesno(
                "Desactivar marca",
                f"¿Deseas desactivar la marca '{nombre}'?",
                parent=ventana
            )

            if not respuesta:

                return

            conexion = conectar_bd()
            cursor = conexion.cursor()

            try:

                cursor.execute(
                    """
                    UPDATE marcas
                    SET activo = 0
                    WHERE id_marca = ?
                    """,
                    (id_marca,)
                )

                conexion.commit()

                messagebox.showinfo(
                    "Marca desactivada",
                    f"La marca '{nombre}' fue desactivada.",
                    parent=ventana
                )

                cargar_marcas()

                self.cargar_productos()

            except Exception as error:

                conexion.rollback()

                messagebox.showerror(
                    "Error",
                    f"No fue posible desactivar la marca.\n\n{error}",
                    parent=ventana
                )

            finally:

                conexion.close()


        botones = tk.Frame(
            ventana,
            bg="#F5F1EA"
        )

        botones.pack(
            pady=15
        )

        tk.Button(
            botones,
            text="➕ Nueva",
            command=agregar_marca,
            bg="#477A5B",
            fg="white",
            activebackground="#3C674D",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            botones,
            text="✏️ Editar",
            command=editar_marca,
            bg="#6B5B45",
            fg="white",
            activebackground="#594B39",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            botones,
            text="🗑️ Desactivar",
            command=desactivar_marca,
            bg="#8C3B3B",
            fg="white",
            activebackground="#A94A4A",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        cargar_marcas()


    # ========================================================
    # ELIMINAR PRODUCTO
    # ========================================================

    def eliminar_producto(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Selecciona un producto",
                "Selecciona primero el perfume que deseas eliminar.",
                parent=self
            )

            return

        datos = self.tabla.item(
            seleccion[0],
            "values"
        )

        id_producto = datos[0]
        codigo = datos[1]
        nombre = datos[3]
        marca = datos[4]
        stock = datos[9]

        respuesta = messagebox.askyesno(
            "Eliminar producto",
            (
                f"¿Deseas eliminar este perfume?\n\n"
                f"Producto: {nombre}\n"
                f"Marca: {marca}\n"
                f"Código: {codigo}\n"
                f"Stock actual: {stock}\n\n"
                f"El producto será retirado del inventario activo."
            ),
            parent=self
        )

        if not respuesta:

            return

        conexion = conectar_bd()
        cursor = conexion.cursor()

        try:

            cursor.execute(
                """
                UPDATE productos
                SET activo = 0
                WHERE id_producto = ?
                """,
                (id_producto,)
            )

            conexion.commit()

            messagebox.showinfo(
                "Producto eliminado",
                f"El perfume '{nombre}' fue retirado del inventario activo.",
                parent=self
            )

            self.cargar_productos()

        except Exception as error:

            conexion.rollback()

            messagebox.showerror(
                "Error",
                f"No fue posible eliminar el producto.\n\n{error}",
                parent=self
            )

        finally:

            conexion.close()


    # ========================================================
    # EDITAR PRODUCTO
    # ========================================================

    def editar_producto(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Selecciona un producto",
                "Selecciona primero el perfume que deseas editar.",
                parent=self
            )

            return

        datos = self.tabla.item(
            seleccion[0],
            "values"
        )

        id_producto = datos[0]

        conexion = conectar_bd()
        cursor = conexion.cursor()

        try:

            cursor.execute(
                """
                SELECT
                    p.codigo,
                    p.codigo_barras,
                    p.nombre,
                    COALESCE(m.nombre, ''),
                    COALESCE(t.nombre, ''),
                    COALESCE(g.nombre, ''),
                    COALESCE(pr.nombre, ''),
                    COALESCE(p.descripcion, ''),
                    COALESCE(p.precio_compra, 0),
                    COALESCE(p.precio_venta, 0),
                    COALESCE(p.iva, 0),
                    COALESCE(i.stock_actual, 0),
                    COALESCE(i.stock_minimo, 0),
                    COALESCE(i.stock_maximo, 0),
                    COALESCE(i.ubicacion, '')

                FROM productos p

                LEFT JOIN marcas m
                    ON p.id_marca = m.id_marca

                LEFT JOIN tipos_fragancia t
                    ON p.id_tipo = t.id_tipo

                LEFT JOIN generos g
                    ON p.id_genero = g.id_genero

                LEFT JOIN presentaciones pr
                    ON p.id_presentacion = pr.id_presentacion

                LEFT JOIN inventario i
                    ON p.id_producto = i.id_producto

                WHERE p.id_producto = ?
                """,
                (id_producto,)
            )

            producto = cursor.fetchone()

        finally:

            conexion.close()

        if not producto:

            messagebox.showerror(
                "Error",
                "No fue posible encontrar el producto.",
                parent=self
            )

            return

        (
            codigo_actual,
            barras_actual,
            nombre_actual,
            marca_actual,
            tipo_actual,
            genero_actual,
            presentacion_actual,
            descripcion_actual,
            precio_compra_actual,
            precio_venta_actual,
            iva_actual,
            stock_actual,
            stock_minimo_actual,
            stock_maximo_actual,
            ubicacion_actual
        ) = producto


        ventana = tk.Toplevel(self)

        ventana.title("Editar perfume")
        ventana.geometry("680x760")
        ventana.resizable(False, False)

        ventana.configure(
            bg="#F5F1EA"
        )

        ventana.update_idletasks()

        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()

        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()

        x = (pantalla_ancho - ancho) // 2
        y = (pantalla_alto - alto) // 2

        ventana.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )


        tk.Label(
            ventana,
            text="✏️ Editar perfume",
            bg="#F5F1EA",
            fg="#241F1A",
            font=("Arial", 22, "bold")
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            ventana,
            text="Modifica la información del perfume",
            bg="#F5F1EA",
            fg="#666666",
            font=("Arial", 10)
        ).pack(
            pady=(0, 15)
        )


        formulario = tk.Frame(
            ventana,
            bg="#FFFFFF"
        )

        formulario.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=5
        )


        def crear_campo(texto, fila, valor=""):

            tk.Label(
                formulario,
                text=texto,
                bg="#FFFFFF",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).grid(
                row=fila,
                column=0,
                sticky="w",
                padx=20,
                pady=6
            )

            entrada = tk.Entry(
                formulario,
                width=38,
                font=("Arial", 10)
            )

            entrada.grid(
                row=fila,
                column=1,
                padx=20,
                pady=6
            )

            entrada.insert(
                0,
                str(valor)
            )

            return entrada


        def crear_lista(texto, fila, opciones, valor=""):

            tk.Label(
                formulario,
                text=texto,
                bg="#FFFFFF",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).grid(
                row=fila,
                column=0,
                sticky="w",
                padx=20,
                pady=6
            )

            lista = ttk.Combobox(
                formulario,
                values=opciones,
                width=35,
                font=("Arial", 10),
                state="readonly"
            )

            lista.grid(
                row=fila,
                column=1,
                padx=20,
                pady=6
            )

            if valor in opciones:

                lista.set(valor)

            return lista


        entrada_codigo = crear_campo(
            "Código interno:",
            0,
            codigo_actual or ""
        )

        entrada_barras = crear_campo(
            "Código de barras:",
            1,
            barras_actual or ""
        )

        entrada_nombre = crear_campo(
            "Nombre del perfume:",
            2,
            nombre_actual or ""
        )

        lista_marca = crear_lista(
            "Marca:",
            3,
            self.obtener_marcas(),
            marca_actual or ""
        )

        lista_tipo = crear_lista(
            "Tipo de fragancia:",
            4,
            self.obtener_tipos(),
            tipo_actual or ""
        )

        lista_genero = crear_lista(
            "Género:",
            5,
            self.obtener_generos(),
            genero_actual or ""
        )

        lista_presentacion = crear_lista(
            "Presentación:",
            6,
            self.obtener_presentaciones(),
            presentacion_actual or ""
        )

        entrada_descripcion = crear_campo(
            "Descripción:",
            7,
            descripcion_actual or ""
        )

        entrada_precio_compra = crear_campo(
            "Precio de compra:",
            8,
            precio_compra_actual
        )

        entrada_precio_venta = crear_campo(
            "Precio de venta:",
            9,
            precio_venta_actual
        )

        entrada_iva = crear_campo(
            "IVA (%):",
            10,
            iva_actual
        )


        tk.Label(
            formulario,
            text="Stock actual:",
            bg="#FFFFFF",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).grid(
            row=11,
            column=0,
            sticky="w",
            padx=20,
            pady=6
        )

        entrada_stock = tk.Entry(
            formulario,
            width=38,
            font=("Arial", 10),
            state="readonly"
        )

        entrada_stock.grid(
            row=11,
            column=1,
            padx=20,
            pady=6
        )

        entrada_stock.config(
            state="normal"
        )

        entrada_stock.insert(
            0,
            str(stock_actual)
        )

        entrada_stock.config(
            state="readonly"
        )

        tk.Label(
            formulario,
            text="El stock actual se modifica mediante movimientos.",
            bg="#FFFFFF",
            fg="#777777",
            font=("Arial", 8, "italic")
        ).grid(
            row=12,
            column=1,
            sticky="w",
            padx=20
        )

        entrada_stock_minimo = crear_campo(
            "Stock mínimo:",
            13,
            stock_minimo_actual
        )

        entrada_stock_maximo = crear_campo(
            "Stock máximo:",
            14,
            stock_maximo_actual
        )

        entrada_ubicacion = crear_campo(
            "Ubicación:",
            15,
            ubicacion_actual or ""
        )


        def guardar_cambios():

            codigo = entrada_codigo.get().strip()
            barras = entrada_barras.get().strip()
            nombre = entrada_nombre.get().strip()

            marca = lista_marca.get().strip()
            tipo = lista_tipo.get().strip()
            genero = lista_genero.get().strip()
            presentacion = lista_presentacion.get().strip()

            descripcion = entrada_descripcion.get().strip()

            precio_compra = entrada_precio_compra.get().strip()
            precio_venta = entrada_precio_venta.get().strip()
            iva = entrada_iva.get().strip()

            stock_minimo = entrada_stock_minimo.get().strip()
            stock_maximo = entrada_stock_maximo.get().strip()

            ubicacion = entrada_ubicacion.get().strip()


            if not nombre:

                messagebox.showwarning(
                    "Dato faltante",
                    "El nombre del perfume es obligatorio.",
                    parent=ventana
                )

                return

            if not marca:

                messagebox.showwarning(
                    "Dato faltante",
                    "Selecciona una marca.",
                    parent=ventana
                )

                return

            if not tipo:

                messagebox.showwarning(
                    "Dato faltante",
                    "Selecciona el tipo de fragancia.",
                    parent=ventana
                )

                return

            if not genero:

                messagebox.showwarning(
                    "Dato faltante",
                    "Selecciona el género.",
                    parent=ventana
                )

                return

            if not presentacion:

                messagebox.showwarning(
                    "Dato faltante",
                    "Selecciona la presentación.",
                    parent=ventana
                )

                return


            try:

                precio_compra = float(
                    precio_compra or 0
                )

                precio_venta = float(
                    precio_venta or 0
                )

                iva = float(
                    iva or 0
                )

                stock_minimo = float(
                    stock_minimo or 0
                )

                stock_maximo = float(
                    stock_maximo or 0
                )

            except ValueError:

                messagebox.showerror(
                    "Datos incorrectos",
                    "Los precios, IVA y cantidades deben ser números.",
                    parent=ventana
                )

                return


            if stock_minimo < 0 or stock_maximo < 0:

                messagebox.showwarning(
                    "Stock incorrecto",
                    "El stock mínimo y máximo no pueden ser negativos.",
                    parent=ventana
                )

                return

            if stock_maximo < stock_minimo:

                messagebox.showwarning(
                    "Stock incorrecto",
                    "El stock máximo no puede ser menor que el stock mínimo.",
                    parent=ventana
                )

                return


            conexion = conectar_bd()
            cursor = conexion.cursor()

            try:

                cursor.execute(
                    """
                    SELECT id_marca
                    FROM marcas
                    WHERE nombre = ?
                    AND activo = 1
                    """,
                    (marca,)
                )

                resultado = cursor.fetchone()

                id_marca = (
                    resultado[0]
                    if resultado
                    else None
                )


                cursor.execute(
                    """
                    SELECT id_tipo
                    FROM tipos_fragancia
                    WHERE nombre = ?
                    AND activo = 1
                    """,
                    (tipo,)
                )

                resultado = cursor.fetchone()

                id_tipo = (
                    resultado[0]
                    if resultado
                    else None
                )


                cursor.execute(
                    """
                    SELECT id_genero
                    FROM generos
                    WHERE nombre = ?
                    AND activo = 1
                    """,
                    (genero,)
                )

                resultado = cursor.fetchone()

                id_genero = (
                    resultado[0]
                    if resultado
                    else None
                )


                cursor.execute(
                    """
                    SELECT id_presentacion
                    FROM presentaciones
                    WHERE nombre = ?
                    AND activo = 1
                    """,
                    (presentacion,)
                )

                resultado = cursor.fetchone()

                id_presentacion = (
                    resultado[0]
                    if resultado
                    else None
                )


                cursor.execute(
                    """
                    UPDATE productos

                    SET
                        codigo = ?,
                        codigo_barras = ?,
                        nombre = ?,
                        id_marca = ?,
                        id_tipo = ?,
                        id_genero = ?,
                        id_presentacion = ?,
                        descripcion = ?,
                        precio_compra = ?,
                        precio_venta = ?,
                        iva = ?

                    WHERE id_producto = ?
                    """,
                    (
                        codigo or None,
                        barras or None,
                        nombre,
                        id_marca,
                        id_tipo,
                        id_genero,
                        id_presentacion,
                        descripcion,
                        precio_compra,
                        precio_venta,
                        iva,
                        id_producto
                    )
                )


                cursor.execute(
                    """
                    UPDATE inventario

                    SET
                        stock_minimo = ?,
                        stock_maximo = ?,
                        ubicacion = ?

                    WHERE id_producto = ?
                    """,
                    (
                        stock_minimo,
                        stock_maximo,
                        ubicacion,
                        id_producto
                    )
                )

                conexion.commit()

                messagebox.showinfo(
                    "Producto actualizado",
                    "El perfume fue actualizado correctamente.",
                    parent=ventana
                )

                ventana.destroy()

                self.cargar_productos()

            except Exception as error:

                conexion.rollback()

                messagebox.showerror(
                    "Error",
                    f"No fue posible actualizar el perfume.\n\n{error}",
                    parent=ventana
                )

            finally:

                conexion.close()


        tk.Button(
            ventana,
            text="💾 Guardar cambios",
            command=guardar_cambios,
            bg="#477A5B",
            fg="white",
            activebackground="#3C674D",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        ).pack(
            pady=12
        )


    # ========================================================
    # NUEVO PERFUME
    # ========================================================

    def nuevo_producto(self):

        ventana = tk.Toplevel(self)

        ventana.title("Nuevo perfume")
        ventana.geometry("700x600")
        ventana.resizable(False, False)

        ventana.configure(
            bg="#F5F1EA"
        )


        ventana.update_idletasks()

        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()

        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()

        x = (pantalla_ancho - ancho) // 2
        y = (pantalla_alto - alto) // 2

        ventana.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )


        # ----------------------------------------------------
        # TÍTULO
        # ----------------------------------------------------

        tk.Label(
            ventana,
            text="🧴 Nuevo perfume",
            bg="#F5F1EA",
            fg="#241F1A",
            font=("Arial", 22, "bold")
        ).pack(
            pady=(15, 5)
        )


        tk.Label(
            ventana,
            text="Registra la información del perfume o fragancia",
            bg="#F5F1EA",
            fg="#666666",
            font=("Arial", 10)
        ).pack(
            pady=(0, 10)
        )


        # ----------------------------------------------------
        # CONTENEDOR DEL SCROLL
        # ----------------------------------------------------

        contenedor_scroll = tk.Frame(
            ventana,
            bg="#F5F1EA"
        )

        contenedor_scroll.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )


        canvas = tk.Canvas(
            contenedor_scroll,
            bg="#FFFFFF",
            highlightthickness=0
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )


        scrollbar = ttk.Scrollbar(
            contenedor_scroll,
            orient="vertical",
            command=canvas.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )


        canvas.configure(
            yscrollcommand=scrollbar.set
        )


        formulario = tk.Frame(
            canvas,
            bg="#FFFFFF"
        )


        ventana_canvas = canvas.create_window(
            (0, 0),
            window=formulario,
            anchor="nw"
        )


        # ----------------------------------------------------
        # ACTUALIZAR ÁREA DEL SCROLL
        # ----------------------------------------------------

        def actualizar_scroll(event=None):

            canvas.configure(
                scrollregion=canvas.bbox("all")
            )


        formulario.bind(
            "<Configure>",
            actualizar_scroll
        )


        # ----------------------------------------------------
        # AJUSTAR ANCHO DEL FORMULARIO
        # ----------------------------------------------------

        def ajustar_ancho(event):

            canvas.itemconfig(
                ventana_canvas,
                width=event.width
            )


        canvas.bind(
            "<Configure>",
            ajustar_ancho
        )


        # ----------------------------------------------------
        # RUEDA DEL MOUSE
        # ----------------------------------------------------

        def desplazar_rueda(event):

            canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )


        canvas.bind_all(
            "<MouseWheel>",
            desplazar_rueda
        )


        # ----------------------------------------------------
        # CERRAR VENTANA
        # ----------------------------------------------------

        def cerrar_ventana():

            canvas.unbind_all(
                "<MouseWheel>"
            )

            ventana.destroy()


        ventana.protocol(
            "WM_DELETE_WINDOW",
            cerrar_ventana
        )


        # ----------------------------------------------------
        # CREAR CAMPO
        # ----------------------------------------------------

        def crear_campo(texto, fila):

            tk.Label(
                formulario,
                text=texto,
                bg="#FFFFFF",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).grid(
                row=fila,
                column=0,
                sticky="w",
                padx=20,
                pady=6
            )


            entrada = tk.Entry(
                formulario,
                width=38,
                font=("Arial", 10)
            )


            entrada.grid(
                row=fila,
                column=1,
                padx=20,
                pady=6
            )


            return entrada


        # ----------------------------------------------------
        # CREAR LISTA
        # ----------------------------------------------------

        def crear_lista(texto, fila, opciones):

            tk.Label(
                formulario,
                text=texto,
                bg="#FFFFFF",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).grid(
                row=fila,
                column=0,
                sticky="w",
                padx=20,
                pady=6
            )


            lista = ttk.Combobox(
                formulario,
                values=opciones,
                width=35,
                font=("Arial", 10),
                state="readonly"
            )


            lista.grid(
                row=fila,
                column=1,
                padx=20,
                pady=6
            )


            return lista


        # ----------------------------------------------------
        # DATOS
        # ----------------------------------------------------

        entrada_codigo = crear_campo(
            "Código interno:",
            0
        )


        entrada_barras = crear_campo(
            "Código de barras:",
            1
        )


        entrada_nombre = crear_campo(
            "Nombre del perfume:",
            2
        )


        lista_marca = crear_lista(
            "Marca:",
            3,
            self.obtener_marcas()
        )


        lista_tipo = crear_lista(
            "Tipo de fragancia:",
            4,
            self.obtener_tipos()
        )


        lista_genero = crear_lista(
            "Género:",
            5,
            self.obtener_generos()
        )


        lista_presentacion = crear_lista(
            "Presentación:",
            6,
            self.obtener_presentaciones()
        )


        entrada_descripcion = crear_campo(
            "Descripción:",
            7
        )


        entrada_precio_compra = crear_campo(
            "Precio de compra:",
            8
        )


        entrada_precio_venta = crear_campo(
            "Precio de venta:",
            9
        )


        entrada_iva = crear_campo(
            "IVA (%):",
            10
        )


        entrada_stock = crear_campo(
            "Stock inicial:",
            11
        )


        entrada_stock_minimo = crear_campo(
            "Stock mínimo:",
            12
        )


        entrada_stock_maximo = crear_campo(
            "Stock máximo:",
            13
        )


        entrada_ubicacion = crear_campo(
            "Ubicación:",
            14
        )


        # ----------------------------------------------------
        # GUARDAR PRODUCTO
        # ----------------------------------------------------

        def guardar_producto():

            codigo = entrada_codigo.get().strip()
            barras = entrada_barras.get().strip()
            nombre = entrada_nombre.get().strip()

            marca = lista_marca.get().strip()
            tipo = lista_tipo.get().strip()
            genero = lista_genero.get().strip()
            presentacion = lista_presentacion.get().strip()

            descripcion = entrada_descripcion.get().strip()

            precio_compra = entrada_precio_compra.get().strip()
            precio_venta = entrada_precio_venta.get().strip()
            iva = entrada_iva.get().strip()

            stock = entrada_stock.get().strip()
            stock_minimo = entrada_stock_minimo.get().strip()
            stock_maximo = entrada_stock_maximo.get().strip()

            ubicacion = entrada_ubicacion.get().strip()


            # ------------------------------------------------
            # VALIDACIONES
            # ------------------------------------------------

            if not nombre:

                messagebox.showwarning(
                    "Dato faltante",
                    "El nombre del perfume es obligatorio.",
                    parent=ventana
                )

                return


            if not marca:

                messagebox.showwarning(
                    "Dato faltante",
                    "Selecciona una marca.",
                    parent=ventana
                )

                return


            if not tipo:

                messagebox.showwarning(
                    "Dato faltante",
                    "Selecciona el tipo de fragancia.",
                    parent=ventana
                )

                return


            if not genero:

                messagebox.showwarning(
                    "Dato faltante",
                    "Selecciona el género.",
                    parent=ventana
                )

                return


            if not presentacion:

                messagebox.showwarning(
                    "Dato faltante",
                    "Selecciona la presentación.",
                    parent=ventana
                )

                return


            # ------------------------------------------------
            # CONVERTIR NÚMEROS
            # ------------------------------------------------

            try:

                precio_compra = float(
                    precio_compra or 0
                )

                precio_venta = float(
                    precio_venta or 0
                )

                iva = float(
                    iva or 0
                )

                stock = float(
                    stock or 0
                )

                stock_minimo = float(
                    stock_minimo or 0
                )

                stock_maximo = float(
                    stock_maximo or 0
                )

            except ValueError:

                messagebox.showerror(
                    "Datos incorrectos",
                    "Los precios, IVA y cantidades deben ser números.",
                    parent=ventana
                )

                return


            if stock < 0:

                messagebox.showwarning(
                    "Stock incorrecto",
                    "El stock no puede ser negativo.",
                    parent=ventana
                )

                return


            if stock_maximo < stock_minimo:

                messagebox.showwarning(
                    "Stock incorrecto",
                    "El stock máximo no puede ser menor que el stock mínimo.",
                    parent=ventana
                )

                return


            # ------------------------------------------------
            # CONEXIÓN
            # ------------------------------------------------

            conexion = conectar_bd()
            cursor = conexion.cursor()


            try:

                # --------------------------------------------
                # MARCA
                # --------------------------------------------

                cursor.execute(
                    """
                    SELECT id_marca
                    FROM marcas
                    WHERE nombre = ?
                    AND activo = 1
                    """,
                    (marca,)
                )

                resultado = cursor.fetchone()

                id_marca = (
                    resultado[0]
                    if resultado
                    else None
                )


                # --------------------------------------------
                # TIPO
                # --------------------------------------------

                cursor.execute(
                    """
                    SELECT id_tipo
                    FROM tipos_fragancia
                    WHERE nombre = ?
                    AND activo = 1
                    """,
                    (tipo,)
                )

                resultado = cursor.fetchone()

                id_tipo = (
                    resultado[0]
                    if resultado
                    else None
                )


                # --------------------------------------------
                # GÉNERO
                # --------------------------------------------

                cursor.execute(
                    """
                    SELECT id_genero
                    FROM generos
                    WHERE nombre = ?
                    AND activo = 1
                    """,
                    (genero,)
                )

                resultado = cursor.fetchone()

                id_genero = (
                    resultado[0]
                    if resultado
                    else None
                )


                # --------------------------------------------
                # PRESENTACIÓN
                # --------------------------------------------

                cursor.execute(
                    """
                    SELECT id_presentacion
                    FROM presentaciones
                    WHERE nombre = ?
                    AND activo = 1
                    """,
                    (presentacion,)
                )

                resultado = cursor.fetchone()

                id_presentacion = (
                    resultado[0]
                    if resultado
                    else None
                )


                # --------------------------------------------
                # INSERTAR PRODUCTO
                # --------------------------------------------

                cursor.execute(
                    """
                    INSERT INTO productos
                    (
                        codigo,
                        codigo_barras,
                        nombre,
                        id_marca,
                        id_tipo,
                        id_genero,
                        id_presentacion,
                        descripcion,
                        precio_compra,
                        precio_venta,
                        iva
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        codigo or None,
                        barras or None,
                        nombre,
                        id_marca,
                        id_tipo,
                        id_genero,
                        id_presentacion,
                        descripcion,
                        precio_compra,
                        precio_venta,
                        iva
                    )
                )


                id_producto = cursor.lastrowid


                # --------------------------------------------
                # INVENTARIO
                # --------------------------------------------

                cursor.execute(
                    """
                    INSERT INTO inventario
                    (
                        id_producto,
                        stock_actual,
                        stock_minimo,
                        stock_maximo,
                        ubicacion
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        id_producto,
                        stock,
                        stock_minimo,
                        stock_maximo,
                        ubicacion
                    )
                )


                # --------------------------------------------
                # MOVIMIENTO INICIAL
                # --------------------------------------------

                if stock > 0:

                    cursor.execute(
                        """
                        INSERT INTO movimientos_inventario
                        (
                            id_producto,
                            tipo_movimiento,
                            cantidad,
                            stock_anterior,
                            stock_nuevo,
                            motivo
                        )
                        VALUES (?, ?, ?, ?, ?, ?)
                        """,
                        (
                            id_producto,
                            "ENTRADA",
                            stock,
                            0,
                            stock,
                            "Stock inicial"
                        )
                    )


                conexion.commit()


                messagebox.showinfo(
                    "Perfume guardado",
                    "El perfume fue registrado correctamente.",
                    parent=ventana
                )


                cerrar_ventana()

                self.cargar_productos()


            except Exception as error:

                conexion.rollback()

                messagebox.showerror(
                    "Error",
                    f"No fue posible guardar el perfume.\n\n{error}",
                    parent=ventana
                )


            finally:

                conexion.close()


        # ----------------------------------------------------
        # BOTONES
        # ----------------------------------------------------

        zona_botones = tk.Frame(
            formulario,
            bg="#FFFFFF"
        )

        zona_botones.grid(
            row=15,
            column=0,
            columnspan=2,
            pady=20
        )


        tk.Button(
            zona_botones,
            text="💾 Guardar perfume",
            command=guardar_producto,
            bg="#477A5B",
            fg="white",
            activebackground="#3C674D",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        ).pack(
            side="left",
            padx=5
        )


        tk.Button(
            zona_botones,
            text="❌ Cancelar",
            command=cerrar_ventana,
            bg="#8C3B3B",
            fg="white",
            activebackground="#A94A4A",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        ).pack(
            side="left",
            padx=5
        )


        # ----------------------------------------------------
        # POSICIÓN INICIAL
        # ----------------------------------------------------

        ventana.after(
            100,
            lambda: canvas.yview_moveto(0)
        )


# ============================================================
# PRUEBA DIRECTA
# ============================================================

if __name__ == "__main__":

    ventana = tk.Tk()

    ventana.withdraw()

    InventarioVentana(ventana)

    ventana.mainloop()
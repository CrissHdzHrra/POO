#commit_01_12_25

from tkinter import messagebox
from model import operaciones

class Controlador:
    @staticmethod
    def respuesta_sql(titulo, respuesta):
        if respuesta:
            messagebox.showinfo(icon="info", title=titulo, message="acción realizada con exito")
        else:
            messagebox.showinfo(icon="info", title=titulo, message="no fue posible realizar la accion, vuelva a intentar")

    @staticmethod
    def insertar(tipo, marca, color, modelo, velocidad, caballaje, plazas, extra1, extra2):
        if not all([str(marca).strip(), str(color).strip(), str(modelo).strip()]):
            messagebox.showerror("error, todos los campos de texto son obligatorios.")
            return False
        
        try:
            vel = int(velocidad)
            cab = int(caballaje)
            pla = int(plazas)
            ex1 = int(extra1) if extra1 else 0
            ex2 = extra2 
        except ValueError:
            messagebox.showerror("error, verifique que los campos numericos sean correctos.")
            return False

        try:
            respuesta = operaciones.Operaciones.insertar(tipo, marca, color, modelo, vel, cab, pla, ex1, ex2)
            Controlador.respuesta_sql(f"Insertar {tipo}", respuesta)
            return respuesta
        except Exception as e:
            messagebox.showerror(f"error, ocurrió un error al insertar: {e}")
            return False

    @staticmethod
    def consultar(tipo):
        try:
            registros = operaciones.Operaciones.consultar_todos(tipo)
            if not registros:
                messagebox.showinfo("consulta", f"no hay {tipo} registrados.")
                return None
            else:
                texto = ""
                for auto in registros:
                    texto += f"ID: {auto['id']} | Marca: {auto['marca']} | Modelo: {auto['modelo']}\n"
                messagebox.showinfo(f"listado de {tipo}", texto)
                return registros
        except Exception as e:
            messagebox.showerror(f"error, al consultar: {e}")
            return None

    @staticmethod
    def actualizar(id_vehiculo, marca, color, modelo, velocidad):
        if not str(id_vehiculo).strip():
            messagebox.showerror("error, el ID es obligatorio.")
            return False

        try:
            val_id = int(id_vehiculo)
            val_vel = int(velocidad)
        except ValueError:
            messagebox.showerror("error, ID y Velocidad deben ser numeros.")
            return False

        try:
            respuesta = operaciones.Operaciones.actualizar(val_id, marca, color, modelo, val_vel)
            Controlador.respuesta_sql("actualizar vehiculo", respuesta)
            return respuesta
        except Exception as e:
            messagebox.showerror(f"error, al actualizar: {e}")
            return False

    @staticmethod
    def eliminar(id_vehiculo):
        if not str(id_vehiculo).strip():
            messagebox.showerror("error, el ID es obligatorio.")
            return False
        
        try:
            val_id = int(id_vehiculo)
            respuesta = operaciones.Operaciones.eliminar(val_id)
            Controlador.respuesta_sql("eliminar vehiculo", respuesta)
            return respuesta
        except ValueError:
            messagebox.showerror("error, el ID debe ser un numero.")
            return False
        except Exception as e:
            messagebox.showerror(f"error, al eliminar: {e}")
            return False

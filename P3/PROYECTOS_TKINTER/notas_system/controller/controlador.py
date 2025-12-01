from tkinter import messagebox
from model import nota, usuario
from view import interfaz

class Controlador:
    #SQL
    @staticmethod
    def respuesta_sql(titulo, respuesta):
        if respuesta:
            messagebox.showinfo(icon="info",title=titulo, message="acción realizada con exito")
        else:
            messagebox.showinfo(icon="info",title=titulo, message="no fue posible realizar la accin, vuelva a intentar")
    #REGISTRAR
    @staticmethod
    def registrar(nombre, apellidos, email, password):
        if not all([str(nombre).strip(), str(apellidos).strip(), str(email).strip(), password]):
            messagebox.showerror("error, todos los campos son obligatorios, por favor, verifica de nuevo.")
            return False
        if "@" not in email or "." not in email:
            messagebox.showerror("error, correo electrónico inválido.")
            return False
        if len(password) < 6:
            messagebox.showerror("error, la contraseña debe tener al menos 6 caracteres.")
            return False
        try:
            registrado = usuario.Usuario.registrar(nombre, apellidos, email, password)
            if registrado:
                messagebox.showinfo("el usuario fue registrado correctamente.")
                return True
            else:
                messagebox.showerror("no se pudo registrar el usuario. Verifique los datos porfavor.")
                return False
        except Exception as e:
            messagebox.showerror(f"error, ocurrió un error al registrar: {e}")
            return False
    #LOGIN
    @staticmethod
    def login(email, password, ventana):
        if not all([str(email).strip(), password]):
            messagebox.showerror("error, todos los campos son obligatorios, vuelva a intentarlo.")
            return None
        if "@" not in email or "." not in email:
            messagebox.showerror("error, el correo electrónico es inválido.")
            return None
        if len(password) < 6:
            messagebox.showerror("error la contraseña debe tener al menos 6 caracteres.")
            return None
        try:
            registro = usuario.Usuario.iniciar_sesion(email, password)
            if registro:
                messagebox.showinfo(f"bienvenido {registro[1]} {registro[2]}, haz iniciado seción correctamente")
                interfaz.Vistas.menu_notas(ventana, registro[0], registro[1], registro[2])
                return registro
            else:
                messagebox.showerror("error, el email o contraseña estan incorrectos.")
                return None
        except Exception as e:
            messagebox.showerror(f"error, ha ocurrido un error al iniciar sesión: {e}")
            return None
    #CREAR NOTAS
    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        respuesta=nota.Nota.crear(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql("Crear Notas", respuesta)
    #MOSTRAR NOTAS
    @staticmethod
    def mostrar_nota(usuario_id):
        registros=nota.Nota.mostrar(usuario_id)
        return registros
    #CAMBIAR NOTA
    @staticmethod
    def cambiar_nota(id,titulo,descripcion):
        respuesta=nota.Nota.actualizar(id,titulo,descripcion)
        Controlador.respuesta_sql("Cambiar Notas", respuesta)
    #ELIMINAR NOTA
    @staticmethod
    def eliminar_nota(id):
        respuesta = nota.Nota.eliminar(id)
        Controlador.respuesta_sql("Borrar Nota", respuesta)
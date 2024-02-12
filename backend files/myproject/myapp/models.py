from django.db import models


class Usuario(models.Model):
    ID_usuario = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo_electronico = models.EmailField()
    Contraseña = models.CharField(max_length=255)  # Hashed password
    Telefono = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=255)
    Fecha_de_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"


class Profesional(models.Model):
    ID_profesional = models.AutoField(primary_key=True)
    ID_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Especialidad = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Tarifa_por_sesion = models.DecimalField(max_digits=10, decimal_places=2)
    Horarios_de_disponibilidad = models.CharField(max_length=255)

    def __str__(self):
        return f"Professional: {self.ID_usuario.Nombre} {self.ID_usuario.Apellido}"


class Turno(models.Model):
    ID_turno = models.AutoField(primary_key=True)
    ID_profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    ID_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Fecha_y_hora_del_turno = models.DateTimeField()
    Estado_del_turno = models.CharField(max_length=20, choices=[('confirmado', 'Confirmado'), ('pendiente', 'Pendiente'), ('cancelado', 'Cancelado'), ('completado', 'Completado')])
    Mensaje_al_profesional = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment {self.ID_turno}"


class Pago(models.Model):
    ID_pago = models.AutoField(primary_key=True)
    ID_turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    Metodo_de_pago = models.CharField(max_length=100)
    Fecha_y_hora_del_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.ID_pago}"


class Valoracion(models.Model):
    ID_valoracion = models.AutoField(primary_key=True)
    ID_turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    Puntuacion = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    Comentario = models.TextField()
    Fecha_de_la_valoracion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.ID_valoracion}"


class Mensajes(models.Model):
    ID_mensaje = models.AutoField(primary_key=True)
    ID_turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    Remitente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sender')
    Destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recipient')
    Contenido_del_mensaje = models.TextField()
    Fecha_y_hora_del_mensaje = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.ID_mensaje}"


class HistoralDeCitas(models.Model):
    ID_historial = models.AutoField(primary_key=True)
    ID_turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    Estado_anterior = models.CharField(max_length=20)
    Estado_actual = models.CharField(max_length=20)
    Fecha_y_hora_del_cambio_de_estado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment History {self.ID_historial}"


# python manage.py makemigrations
# python manage.py migrate

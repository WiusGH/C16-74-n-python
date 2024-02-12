from datetime import datetime
from main import db, Usuario, Profesional, Turno, Pago, Valoracion, Mensaje, Cita

# Create sample data for Usuario table
usuarios_data = [
    Usuario(nombre='John', apellido='Doe', correo_electronico='john@example.com', contrasena='password1', telefono='123456789', direccion='123 Main St', fecha_registro=datetime.now()),
    Usuario(nombre='Jane', apellido='Smith', correo_electronico='jane@example.com', contrasena='password2', telefono='987654321', direccion='456 Elm St', fecha_registro=datetime.now()),
    Usuario(nombre='Alice', apellido='Johnson', correo_electronico='alice@example.com', contrasena='password3', telefono='555666777', direccion='789 Oak St', fecha_registro=datetime.now())
]

# Add Usuario data to the database
db.session.add_all(usuarios_data)
db.session.commit()

# Create sample data for Profesional table
profesionales_data = [
    Profesional(id_usuario=1, especialidad='Psychologist', descripcion='Experienced psychologist specializing in cognitive behavioral therapy.', tarifa_por_sesion=100.0, horarios_disponibilidad='Mon-Fri 9am-5pm'),
    Profesional(id_usuario=2, especialidad='Therapist', descripcion='Compassionate therapist with expertise in family counseling.', tarifa_por_sesion=120.0, horarios_disponibilidad='Tue-Sat 10am-6pm'),
    Profesional(id_usuario=3, especialidad='Psychiatrist', descripcion='Board-certified psychiatrist offering medication management and psychotherapy.', tarifa_por_sesion=150.0, horarios_disponibilidad='Mon-Sat 8am-4pm')
]

# Add Profesional data to the database
db.session.add_all(profesionales_data)
db.session.commit()

# Create sample data for Turno table
turnos_data = [
    Turno(id_profesional=1, id_usuario=2, fecha_hora_turno=datetime.now(), estado_turno='pending', mensaje_profesional='Please bring any relevant documents to the appointment.'),
    Turno(id_profesional=2, id_usuario=3, fecha_hora_turno=datetime.now(), estado_turno='confirmed', mensaje_profesional='Remember to arrive 15 minutes early for your appointment.'),
    Turno(id_profesional=3, id_usuario=1, fecha_hora_turno=datetime.now(), estado_turno='completed', mensaje_profesional='Follow-up appointment scheduled for next month.')
]

# Add Turno data to the database
db.session.add_all(turnos_data)
db.session.commit()

# Create sample data for Pago table
pagos_data = [
    Pago(id_turno=1, monto=100.0, metodo_pago='credit card'),
    Pago(id_turno=2, monto=120.0, metodo_pago='cash'),
    Pago(id_turno=3, monto=150.0, metodo_pago='bank transfer')
]

# Add Pago data to the database
db.session.add_all(pagos_data)
db.session.commit()

# Create sample data for Valoracion table
valoraciones_data = [
    Valoracion(id_turno=1, puntuacion=5, comentario='Great experience, would highly recommend.'),
    Valoracion(id_turno=2, puntuacion=4, comentario='Very helpful, but wait time was a bit long.'),
    Valoracion(id_turno=3, puntuacion=5, comentario='Excellent care and attention from the psychiatrist.')
]

# Add Valoracion data to the database
db.session.add_all(valoraciones_data)
db.session.commit()

# Create sample data for Mensaje table
mensajes_data = [
    Mensaje(id_turno=1, remitente=2, destinatario=1, contenido_mensaje='Looking forward to meeting you.'),
    Mensaje(id_turno=2, remitente=3, destinatario=2, contenido_mensaje='I have some questions before the appointment.'),
    Mensaje(id_turno=3, remitente=1, destinatario=3, contenido_mensaje='Thank you for your help.')
]

# Add Mensaje data to the database
db.session.add_all(mensajes_data)
db.session.commit()

# Create sample data for Cita table
citas_data = [
    Cita(id_turno=1, estado_anterior='pending', estado_actual='confirmed', fecha_hora_cambio_estado=datetime.now()),
    Cita(id_turno=2, estado_anterior='confirmed', estado_actual='completed', fecha_hora_cambio_estado=datetime.now()),
    Cita(id_turno=3, estado_anterior='completed', estado_actual='pending', fecha_hora_cambio_estado=datetime.now())
]

# Add Cita data to the database
db.session.add_all(citas_data)
db.session.commit()

print("Sample data added to tables successfully.")

from crontab import CronTab

# Crear objeto crontab para el usuario actual
cron = CronTab(user=True)

# Crear nueva tarea
job = cron.new(command='export DISPLAY=:0 && export XDG_RUNTIME_DIR=/run/user/1000 && dunstify -u critical --icon="info" --appname="Nombre del proceso" "Título" "Mensaje"')

# Configurar para que se ejecute cada minuto
#MINUTO,HORA,DIA,MES,DIA DE LA SEMANA

job.minute.on(35)
job.hour.on(18)
job.day.on(19)
job.month.on(23)
# Guardar cambios
cron.write()

print("Tarea programada con éxito.")

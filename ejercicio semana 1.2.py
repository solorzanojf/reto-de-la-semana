# crear variable de tipo diccionario empleado
empleado = {
   "nombre" : (),
   "horas_t" : (),
   "bonificacion" : ()
}
# modificar valores del la variable diccionario empleado
empleado ["nombre"] =  input("Indique el nombre del Trabajado: ")
empleado ["horas_t"] =  float(input("indique las horas laboradas: "))
empleado ["bonificacion"] =  float(input("indique el monto de la bonificacion para el trabajados: "))
#condicion para definir horas extras
if empleado ["horas_t"]<=8:
    horas_d = empleado ["horas_t"]
    horas_n = 0
else:
    horas_d = 8
    horas_n = empleado ["horas_t"]-horas_d
# termoinos de pagos y prestaciones sociales
phoras_d = 3785
phoras_n = 4731
auxilio_t = 106454/30
salud_pension = 258927/30

def calcularpago(empleado: dict)->str:
    resultado= (horas_d*phoras_d)+(horas_n*phoras_n)+empleado ["bonificacion"]+auxilio_t-salud_pension
    resultado= round (resultado,2)
    return str(resultado)
print("El empleado "+ empleado ["nombre"]+" total a pagar $"+calcularpago(empleado))
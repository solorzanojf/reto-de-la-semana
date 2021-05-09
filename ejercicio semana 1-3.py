# crear variable de tipo diccionario empleado
empleado = {
   "nombre" : (),
   "horas_t" : (),
   "bonificacion" : ()
}
# modificar valores del la variable diccionario empleado
empleado["nombre"] =  input("\nIndique el nombre del Trabajado: \t\t\t\t")
empleado["horas_t"] =  float(input("\nindique las horas laboradas: \t\t\t\t\t"))
empleado["bonificacion"] =  float(input("\nindique el monto de la bonificacion para el trabajados: \t"))

def calcularpago(empleado: dict)->str:
    phoras_d = 3785
    phoras_n = 4731
    auxilio_t = 106454/30
    salud_pension = 258927/30
    if empleado["horas_t"]<=8:
        horas_d = empleado["horas_t"]
        horas_n = 0
    else:
        horas_d = 8
        horas_n = empleado["horas_t"]-horas_d
    resultado= (horas_d*phoras_d)+(horas_n*phoras_n)+empleado["bonificacion"]+auxilio_t-salud_pension
    resultado= round (resultado,2)
    return "El empleado "+ empleado["nombre"]+" total a pagar "+str(resultado)
print(calcularpago(empleado))
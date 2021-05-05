nombre_empleado = input("Indique el nombre del Trabajado: ")
horas_trabajadas = float(input("indique las horas laboradas: "))
bono = float(input("indique el monto de la bonificacion para el trabajados: "))
if horas_trabajadas <=8:
    horas_d = horas_trabajadas
    horas_n = 0
else:
    horas_d = 8
    horas_n = horas_trabajadas-horas_d
phoras_d = 3785
phoras_n = 4731
auxilio_t = 106454/30
salud_pension = 258927/30
total_pagar = (horas_d*phoras_d)+(horas_n*phoras_n)+bono+auxilio_t-salud_pension
print("el empleado ", nombre_empleado, " total a pagar ", round (total_pagar, 2))
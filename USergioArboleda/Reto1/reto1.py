salarioBase, numeroHorasExtra, bonificaciones = input().split()
salarioBase = float(salarioBase)
numeroHorasExtra = int(numeroHorasExtra)
bonificaciones = int(bonificaciones)
bonificacion = 0

if bonificaciones == 1 :
    bonificacion = salarioBase*0.05

horaLaboral = salarioBase/192
horaExtraValor = horaLaboral + horaLaboral*0.25
horasExtra = horaExtraValor*numeroHorasExtra

salarioBruto = salarioBase + horasExtra + bonificacion

aporteSalud = salarioBruto*0.035
aportePension = salarioBruto*0.04
aporteCajaCompensacion = salarioBruto*0.01

salarioNeto = salarioBruto - (aporteSalud + aportePension + aporteCajaCompensacion)
print(round(salarioNeto,1))
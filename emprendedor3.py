

p = float(input("precio de suscripcion"))
u_pre = float(input("numero de usuarios premiun"))
u = float(input("numero de usuarios"))
gt = float(input("gastos totales"))
ut = float(input("utilidades anteriores"))




utilidades = p * (u + u_pre * 1.5)-gt



 



print(f" la razon es de : {utilidades/ut:.2f}")
p = float(input("precio de suscripcion"))
u_pre = float(input("numero de usuarios premiun"))
u = float(input("numero de usuarios"))
gt = float(input("gastos totales"))



utilidades = p * (u + u_pre * 1.5)-gt

 



print(f"las utilidades son: {utilidades}")
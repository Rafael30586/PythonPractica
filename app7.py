class Persona:
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad 
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre: ",self.nombre, " Edad: ",self.edad, "años Lugar de residencia: ",self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
    
        print("Salario: $",self.salario, " Antigüedad: ",self.antiguedad, " años")

e = Empleado(500000000,3,"Fernando Rafael",39,"Rio Ceballos")
p = Persona("Mario", 31, "San Miguel")
e.descripcion()
p.descripcion()

print(isinstance(e,Empleado)) # La función isInstance tiene dos parámetros: variable del objeto y clase a la que pertenece (o no) 
print(isinstance(e,Persona)) # Da true porque Empleado hereda de Persona
print(isinstance(p,Empleado))

a = 14
a = 2
a = "No da error"
print(a) # Python es de tipado dinámico

def restar_dos_numeros(x,y):
    return x - y

print(restar_dos_numeros(y=4,x=8)) # A las funcionaes se les pueden pasar los argumentos en diferente orden, siempre y cuansdo aclaremos su nombre
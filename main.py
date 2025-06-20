import module  # Así es como se importan los módulos                                  
from module2 import incrementar # Así se importa una función específica de un módulo
import module3 as m3 # Así se importa un módulo con un alias
import os # Módulo que ya viene con python
import user
from post import Post


module.saludar("Sonic", "the hedgehog")
print(module.juego)

incrementar(45, 8)

print(m3.un_personaje)

print(os.name)

app_user_one = user.User("fraq86@gmail.com","F. Rafael Alvarez",1234, "Desarrollador web") # Utilización del constructor del módulo user

app_user_one.get_user_info()
app_user_one.change_job_title("Desarrollador backend")
app_user_one.get_user_info()

new_post = Post("On a secret mission today", app_user_one.name)
new_post.get_post_info()
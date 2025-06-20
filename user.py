class User:
    def __init__(self, user_email, name, password, current_job_title): # Este es el constructor de la clase
        self.email = user_email #self es una palabra reservada del lenguaje. Es muy parecido al this de java
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User: {self.name} currently work as {self.current_job_title}, you can contact him/her at {self.email}")


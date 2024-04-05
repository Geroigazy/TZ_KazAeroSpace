# Создать image проекта
docker build -t my-django-app .

# Запустить контейнер
docker run -p 8000:8000 my-django-app

# Админ панель
http://localhost:8000/admin/
login: nura
password: 1234

# Endpoints
http://localhost:8000/api/users/
http://localhost:8000/api/users/1/

http://localhost:8000/api/trainers/
http://localhost:8000/api/trainers/1/

http://localhost:8000/api/gyms/
http://localhost:8000/api/gyms/1/

http://localhost:8000/api/schedules/
http://localhost:8000/api/schedules/1/

http://localhost:8000/api/appointments/
http://localhost:8000/api/appointments/1/


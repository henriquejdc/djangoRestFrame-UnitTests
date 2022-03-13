Rest Full Project Django REST Framework

Implementado:
- 2 modelos de serializer (ModelSerializer and Serializer)
- View com def e api_view ou csrf
- Class para view usando APIView
- Class para view usando GenericAPIView
- Class usando ViewSet e Router
- Class usando GenericViewSet e Router
- Class usando ModelViewSet e Router
- Unit Tests na Api com model, view e form test básicos

Instalar: 
- pip install -r requeriments.txt

Criar o Banco de Dados:
- python manage.py migrate

Criar o super usuário para autenticar:
- python manage.py createsuperuser

Utilizar o /admin para criar um Token

Rodar os testes:
- python manage.py test api_basic.tests # Todos os testes
- python manage.py test api_basic.tests.unit_tests # Um único teste

Seguido o tutorial abaixo:
- https://www.youtube.com/watch?v=B38aDwUpcFc&ab_channel=ParwizForogh
- https://www.youtube.com/watch?v=swEjbCW9XDY&ab_channel=VeryAcademy

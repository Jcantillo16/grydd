import sys, os, django
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Desktop/grydd')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grydd.settings")
django.setup()

from apps.usuarios.models import Role


def load_roles():
    roles = [
        {
            'nombre': 'Administrador Del Sistema',
            'descripcion': 'Administrador del sistema'
        },
        {
            'nombre': 'Administrador De La Empresa',
            'descripcion': 'Administrador de la empresa'
        },
        {
            'nombre': 'Empleado',
            'descripcion': 'Empleado de la empresa'
        }
    ]
    for role in roles:
        Role.objects.create(**role)
    print('Roles cargados')
    return True if len(roles) > 0 else False

load_roles()

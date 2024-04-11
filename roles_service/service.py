
from auth_modules.models import db, Role


def create_role(name):
    role = Role(name=name)
    db.session.add(role)
    db.session.commit()
    return {"id": role.id, "name": role.name}

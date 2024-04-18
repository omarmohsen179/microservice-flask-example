
import requests
from users_modules.models import db, User, Role, UserRoles


def create_user(username):
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return {"id": user.id, "username": user.username}


def assign_role_to_user(user_id, role_id):
    role_response = requests.get(f'http://localhost:5001/roles/{role_id}')
    if role_response.status_code == 404:
        return {"error": "Role not found"}
    role_data = role_response.json()
    # Now that we have the role, proceed to assign it to the user
    user_role = UserRoles(user_id=user_id, role_id=role_id)
    db.session.add(user_role)
    db.session.commit()
    return {"user_id": user_id, "role_id": role_id, "role_name": role_data['name']}

from prisma.models import User
from fastapi import HTTPException, status
from app.services.security import hashed_password

class ServiceAuth():
    @staticmethod
    async def inscription(name, firsname, email, password, conf_password):
        exist_user = await User.prisma().find_first(where={"email":email})
        if exist_user:
            raise HTTPException(status_code=409, detail="identifiant incorrect")
        if password != conf_password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="mot de passe incorrect")

        recup_hashed = hashed_password(password)
        print(recup_hashed)
        user_use = await User.prisma().create(data={
            "name": name,
            "firsname": firsname,
            "email": email,
            "password": recup_hashed
        })
        print(user_use)
        return user_use
    
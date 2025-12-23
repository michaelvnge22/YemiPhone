import bcrypt

def hashed_password(password:str):
    recup = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return recup.decode()

def decode_password(password, hash_password):
    verify = bcrypt.checkpw(password.encode(), hash_password.encode())
    return verify

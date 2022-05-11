from passlib.context import CryptContext

hasher = CryptContext(schemes = ["bcrypt"],deprecated = "auto")

class Hasher:
    @staticmethod
    def hash_pass(data):
        pass_hasher = hasher.hash(data)
        return pass_hasher
        
    @staticmethod
    def verify_hash(p_text,hash_pass):
        return hasher.verify(p_text,hash_pass)
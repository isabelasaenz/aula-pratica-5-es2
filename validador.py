import re

class ValidadorSenha:
    def __init__(self, senha: str):
        self.senha = senha

    def validar(self):
        if len(self.senha) < 8:
            return False, "A senha deve ter pelo menos 8 caracteres."
        if not re.search(r"[A-Z]", self.senha):
            return False, "A senha deve conter pelo menos uma letra maiúscula."
        if not re.search(r"[a-z]", self.senha):
            return False, "A senha deve conter pelo menos uma letra minúscula."
        if not re.search(r"\d", self.senha):
            return False, "A senha deve conter pelo menos um número."
        if not re.search(r"[!@#$%^&*()_\-+=]", self.senha):
            return False, "A senha deve conter pelo menos um caractere especial."

        return True, "Senha válida"

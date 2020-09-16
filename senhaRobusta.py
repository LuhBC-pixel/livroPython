#! python3
# Detecção de senhas robustas - detecta se a senha é robusta ou não
import pyperclip, re

# senha robusta deve ter pelo menos 8 caracteres
# deve conter tantos letras maiúsculas quanto minúsculas e ter pelo menos um dígito

senha = re.compile(r'(?=.*[0-9])([a-zA-Z0-9]{7,})')


testaSenha = str(pyperclip.paste())

print(f'Sua senha é: {"válida" if senha.match(testaSenha) else "inválida"}')
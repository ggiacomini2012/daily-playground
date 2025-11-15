import re

def validar_email(email: str) -> bool:
    """
    Verifica se a string fornecida é um endereço de e-mail válido.
    
    Args:
        email (str): A string a ser validada como e-mail.

    Returns:
        bool: True se o e-mail for válido, False caso contrário.
    """
    
    # 
    # Expressão Regular Simplificada para validação básica.
    # Esta regex verifica o padrão: nome@dominio.com
    # [a-zA-Z0-9._%+-]+   -> Parte local (antes do @): letras, números e alguns caracteres especiais
    # @                   -> O símbolo @
    # [a-zA-Z0-9.-]+      -> O domínio: letras, números, pontos e hífens
    # \.                  -> Um ponto obrigatório
    # [a-zA-Z]{2,}        -> A extensão (TLD): pelo menos 2 letras (ex: com, br, net)
    # 
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # re.fullmatch() verifica se a string inteira corresponde ao padrão regex
    if re.fullmatch(regex, email):
        return True
    else:
        return False

# --- Exemplos de Uso (Testes) ---

print("--- Casos de Sucesso (Resultado Esperado: True) ---")
print(f"teste@dominio.com.br: {validar_email('teste@dominio.com.br')}")
print(f"usuario.nome123@servidor.net: {validar_email('usuario.nome123@servidor.net')}")
print(f"a@b.co: {validar_email('a@b.co')}")

print("\n--- Casos de Falha (Resultado Esperado: False) ---")
# O caso de falha do seu teste: formato inválido (sem @)
print(f"teste-email.com (Sem @): {validar_email('teste-email.com')}")
print(f"usuario@.com (Domínio inválido): {validar_email('usuario@.com')}")
print(f"@dominio.com (Sem parte local): {validar_email('@dominio.com')}")
print(f"usuario@dominio (Sem TLD/extensão): {validar_email('usuario@dominio')}")
print(f"usuario@dominio..com (Pontos duplos): {validar_email('usuario@dominio..com')}")
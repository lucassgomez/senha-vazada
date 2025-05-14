import os
import hashlib
import requests
import csv

# Caminho absoluto para o CSV
caminho_csv = r"C:\Users\lucas\OneDrive\Anexos\PROGRAMAÇÃO\PESSOAL\senha-vazada\verificador-senhas\usuarios.csv"

# Função para gerar o hash SHA1 da senha
def hash_senha(senha):
    sha1 = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()
    return sha1[:5], sha1[5:]

# Função que verifica se a senha foi vazada na API do HaveIBeenPwned
def verificar_senha_vazada(senha):
    prefixo, sufixo = hash_senha(senha)
    url = f"https://api.pwnedpasswords.com/range/{prefixo}"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Levanta um erro se a resposta for um status de erro (404, 500, etc.)
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return 0  # Retorna 0 se houver erro na requisição

    # Verifica se o sufixo da senha está nos dados recebidos da API
    for linha in resposta.text.splitlines():
        hash_final, count = linha.split(':')
        if hash_final == sufixo:
            return int(count)  # Retorna o número de vezes que a senha foi vazada
    return 0  # Retorna 0 se não encontrar a senha

# Função que verifica as senhas de um arquivo CSV
def verificar_csv(caminho_csv):
    try:
        with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile)
            
            for linha in leitor:
                usuario = linha["usuario"]
                senha = linha["senha"]
                print(f"Verificando {usuario}...")
                vazamentos = verificar_senha_vazada(senha)
                
                # Exibe o resultado para cada usuário
                if vazamentos:
                    print(f"⚠️ [{usuario}] - SENHA COMPROMETIDA ({vazamentos} vezes).")
                else:
                    print(f"✅ [{usuario}] - Senha segura (não encontrada em vazamentos).")
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Executar a verificação do CSV
if __name__ == "__main__":
    verificar_csv(caminho_csv)

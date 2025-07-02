from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(texto):
    bloco = AES.block_size
    padding = bloco - len(texto) % bloco
    return texto + bytes([padding]) * padding

def unpad(texto):
    padding = texto[-1]
    return texto[:-padding]

def pad_chave(chave, tamanho):
    """Aplica padding na chave para garantir que tenha um tamanho válido."""
    return chave.ljust(tamanho, b"\0")  # Preenchendo com bytes nulos

def obter_chave():
    while True:
        try:
            tamanho = int(input("Escolha o tamanho da chave (16, 24 ou 32 bytes): "))
            if tamanho not in [16, 24, 32]:
                print("Tamanho inválido. Escolha 16, 24 ou 32.")
                continue
            chave_input = input(f"Digite sua chave (qualquer tamanho, será ajustada para {tamanho} bytes): ").encode()
            chave = pad_chave(chave_input, tamanho)
            return chave
        except ValueError:
            print("Entrada inválida. Digite um número.")

def cifrar(chave):
    texto_plano = input("Digite a mensagem para criptografar: ")
    if not texto_plano:
        print("Erro: A mensagem não pode ser vazia!")
        return
    
    texto_plano_bytes = texto_plano.encode()
    texto_plano_preenchido = pad(texto_plano_bytes)
    
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    mensagem_cifrada = cipher.encrypt(texto_plano_preenchido)

    mensagem_cifrada_base64 = base64.b64encode(iv + mensagem_cifrada).decode()
    print("\nMensagem cifrada (em Base64):")
    print(mensagem_cifrada_base64)

def decifrar(chave):
    mensagem_cifrada_base64 = input("Digite a mensagem cifrada em Base64: ")
    try:
        mensagem_cifrada_completa = base64.b64decode(mensagem_cifrada_base64)
    except Exception:
        print("Erro ao decodificar Base64.Verifique se a mensagem está correta.")
        return
    
    iv = mensagem_cifrada_completa[:AES.block_size]
    mensagem_cifrada = mensagem_cifrada_completa[AES.block_size:]

    decipher = AES.new(chave, AES.MODE_CBC, iv)
    mensagem_preenchida_decifrada = decipher.decrypt(mensagem_cifrada)
    
    try:
        mensagem_decifrada = unpad(mensagem_preenchida_decifrada)
        print("\nMensagem decifrada:")
        print(mensagem_decifrada.decode())
    except Exception:
        print("Erro: A chave pode estar incorreta ou a mensagem cifrada está inválida.")

def main():
    print("### Criptografia e Descriptografia com AES ###")
    
    opcao = input("Escolha uma opção (1 - Cifrar, 2 - Decifrar): ")
    if opcao not in ["1", "2"]:
        print("Opção inválida.")
        return

    chave = obter_chave()

    if opcao == "1":
        cifrar(chave)
    elif opcao == "2":
        decifrar(chave)

if __name__ == "__main__":
    main()

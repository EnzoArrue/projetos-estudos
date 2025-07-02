import subprocess
import time
import re

# Arquivo de log do SSH
LOG_FILE = "/var/log/auth.log"

# Expressão regular para identificar tentativas de login falhas
SSH_FAIL_REGEX = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

# Configuração do Fail2Ban
FAIL2BAN_JAIL = "sshd"

# Lista para evitar bloqueios repetidos
blocked_ips = set()

def monitor_ssh_log():
    """Monitora o log do SSH e detecta tentativas de Brute Force."""
    with subprocess.Popen(["tail", "-F", LOG_FILE], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
        for line in proc.stdout:
            match = re.search(SSH_FAIL_REGEX, line)
            if match:
                ip = match.group(1)
                if ip not in blocked_ips:
                    print(f"[ALERTA] Ataque de Brute Force detectado! IP: {ip}")
                    block_ip(ip)
                    blocked_ips.add(ip)

def block_ip(ip):
    """Bloqueia o IP usando Fail2Ban."""
    try:
        subprocess.run(["fail2ban-client", "set", FAIL2BAN_JAIL, "banip", ip], check=True)
        print(f"[BLOQUEADO] IP {ip} foi banido com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao banir {ip}: {e}")

if __name__ == "__main__":
    print("[IPS SSH ATIVO] Monitorando tentativas de Brute Force...")
    monitor_ssh_log()

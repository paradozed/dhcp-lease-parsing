import re

def extract_leases(file_path):
    leases = []
    with open(file_path, 'r') as file:
        data = file.read()

    # Utilisation d'une expression régulière pour extraire les informations nécessaires
    lease_pattern = re.compile(r'lease (\d+\.\d+\.\d+\.\d+) {([^}]+)}', re.DOTALL)
    matches = lease_pattern.findall(data)

    for match in matches:
        ip_address, lease_data = match
        # Utilisation d'une expression régulière pour extraire le client-hostname
        hostname_match = re.search(r'client-hostname "(.*?)"', lease_data)
        client_hostname = hostname_match.group(1) if hostname_match else None

        # Afficher uniquement les entrées avec un client-hostname commençant par "pokaiok"
        if client_hostname and client_hostname.startswith("pokaiok"):
            leases.append({'ip_address': ip_address, 'client_hostname': client_hostname})

    return leases

if __name__ == "__main__":
    file_path = "/var/lib/dhcp/dhcpd.leases"
    leases = extract_leases(file_path)

    for lease in leases:
        print(f"{lease['ip_address']},{lease['client_hostname']}")

import re,sys

def create_ansible_inventory(file_path, output_file="ansible_inventory.txt"):
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

    with open(output_file, 'w') as output:
        for lease in leases:
            output.write(f"{lease['ip_address']} ansible_hostname={lease['client_hostname']}\n")

    
        # Ajouter la section [install] avec les hosts pokaiok
        output.write("\n[install]\n")
        for lease in leases:
            output.write(f"{lease['client_hostname']}\n")

    print(f"Fichier d'inventaire Ansible généré avec succès : {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    create_ansible_inventory(file_path)

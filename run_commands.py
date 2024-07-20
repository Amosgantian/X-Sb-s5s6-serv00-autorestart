import json
import paramiko

# Load JSON data
with open('ACCOUNTS.json', 'r') as file:
    accounts = json.load(file)

# Function to execute command on remote server
def execute_command(host, port, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=port, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"Output: {stdout.read().decode()}")
        print(f"Error: {stderr.read().decode()}")
        ssh.close()
    except Exception as e:
        print(f"Failed to execute command on {host}: {e}")

# Execute commands based on JSON data
for account in accounts:
    command = account.get('command')
    if command:
        print(f"Executing command on {account['host']}: {command}")
        execute_command(account['host'], account['port'], account['username'], account['password'], command)

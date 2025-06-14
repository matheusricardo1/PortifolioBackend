import requests
from decouple import config
import time

USERNAME = 'matheusricardo'
API_TOKEN = config('PA_API_TOKEN')

if not API_TOKEN:
    print('Erro: Por favor, defina a variável de ambiente PA_API_TOKEN ou adicione-a ao seu arquivo .env com o seu token de API do PythonAnywhere.')
    exit(1)

DOMAIN_NAME = 'matheusricardo.pythonanywhere.com'
BASE_URL = f'https://www.pythonanywhere.com/api/v0/user/{USERNAME}/'
HEADERS = {'Authorization': f'Token {API_TOKEN}'}

def list_consoles():
    """Lista os consoles existentes."""
    response = requests.get(BASE_URL + 'consoles/', headers=HEADERS)
    if response.status_code == 200:
        consoles = response.json()
        return consoles
    else:
        print(f'Falha ao listar consoles: {response.status_code}')
        print(response.text)
        return []

def get_active_console():
    """Obtém um console bash."""
    consoles = list_consoles()
    for console in consoles:
        console_id = console['id']
        executable = console.get('executable', '').lower()
        print(f"Verificando console ID {console_id}: executable={executable}")
        if 'bash' in executable:
            print(f'Usando o console com ID: {console_id}')
            return console_id
    print('Nenhum console bash encontrado.')
    return None

def send_command(console_id, command):
    """Envia um comando para o console."""
    data = {'input': command + '\n'}
    response = requests.post(BASE_URL + f'consoles/{console_id}/send_input/', headers=HEADERS, data=data)
    if response.status_code == 200:
        print(f'Comando "{command}" enviado com sucesso.')
    else:
        print(f'Falha ao enviar o comando "{command}" para o console {console_id}: {response.status_code}')
        print(response.text)

def get_output(console_id):
    """Recupera a saída mais recente do console."""
    response = requests.get(BASE_URL + f'consoles/{console_id}/get_latest_output/', headers=HEADERS)
    if response.status_code == 200:
        output = response.json().get('output', '')
        return output
    else:
        print(f'Falha ao obter a saída do console {console_id}: {response.status_code}')
        print(response.text)
        return ''

def reload_webapp():
    """Recarrega o aplicativo web no PythonAnywhere."""
    response = requests.post(BASE_URL + f'webapps/{DOMAIN_NAME}/reload/', headers=HEADERS)
    if response.status_code == 200:
        print(f'O web app {DOMAIN_NAME} foi recarregado com sucesso.')
    else:
        print(f'Falha ao recarregar o web app: {response.status_code}')
        print(response.text)

def main():
    console_id = get_active_console()
    if not console_id:
        print('Por favor, abra um console bash no PythonAnywhere e tente novamente.')
        return

    # Altere para o diretório do seu projeto no PythonAnywhere
    project_directory = '/home/matheusricardo/PortifolioBackend'  # Atualize este caminho
    send_command(console_id, f'cd {project_directory}')

    # 'git stash'
    send_command(console_id, 'git stash')

    # 'git pull'
    send_command(console_id, 'git pull')

    # Aguarde os comandos serem executados
    time.sleep(5)  # Ajuste se necessário

    # Opcionalmente, obtenha e imprima a saída DESCOMENTAR PARA VER OS LOGS
    #output = get_output(console_id)
    #print('Saída do console:')
    #print(output)

    # Recarregue o aplicativo web
    reload_webapp()

if __name__ == '__main__':
    main()

import netmiko
from getpass import getpass
from netmiko import ConnectHandler
from pprint import pprint
import pyperclip


user = 'dhimes'
email = 'dhimes@gmail.com'


def pull_key():
    command = f'ssh-keygen -t ed25519 -C "{email}"'
    commands = [
        "eval `ssh-agent -s`",
        "ssh-add ~/.ssh/id_ed25519",
    ]
    connection = make_conn(user, email)
    output = connection.send_command(command, expect_string=':')
    output = connection.send_command("", expect_string=':')
    output = connection.send_command("", expect_string=':')
    output = connection.send_command("", expect_string=':')
    for command in commands:
        output = connection.send_command(command)
    output = connection.send_command('more ~/.ssh/id_ed25519.pub')
    pyperclip.copy(output)
    print(output)


def make_conn(user, email):
    user_input = input(f'user: [{user}]:')
    if user_input != '':
        user = user_input
    user_input = input(f'email: [{email}]:')
    if len(user_input) > 3:
        email = user_input
    server = input('server name:')
    password = getpass()

    conn_data = {
        'device_type': 'linux',
        # 'verbose': True,
        'ip': server,
        'username': user,
        'password': password,
    }
    return ConnectHandler(**conn_data)


pull_key()

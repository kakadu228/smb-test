from smb.SMBConnection import SMBConnection
from smb.smb_structs import OperationFailure

def main():
    username = "Username"  # Замените на ваше имя пользователя
    password = "Pass"    # Замените на ваш пароль
    local_name = "KaliMachine"     # Имя вашей машины
    remote_name = "Hostname_server"  # Имя удалённой машины

    conn = SMBConnection(username, password, local_name, remote_name, domain="none", use_ntlm_v2=True)

    try:
        conn.connect("IP", 445)  # Замените на IP адрес вашего Windows Server
        print("Подключение успешно!")
        # Ваш код для обработки запросов будет здесь
    except OperationFailure as e:
        print(f"Ошибка подключения: {e}")

if __name__ == "__main__":
    main()

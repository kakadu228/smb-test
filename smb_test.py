from smb.SMBConnection import SMBConnection
from smb.smb_structs import OperationFailure

def main():
    username = "test"  # Замените на ваше имя пользователя
    password = "P@ssw0rd"    # Замените на ваш пароль
    local_name = "KaliMachine"     # Имя вашей машины
    remote_name = "WS19"  # Имя удалённой машины

    conn = SMBConnection(username, password, local_name, remote_name, domain="WORKGROUP", use_ntlm_v2=True)

    try:
        conn.connect("192.168.1.14", 445)  # Замените на IP адрес вашего Windows Server
        print("Подключение успешно!")
        # Ваш код для обработки запросов будет здесь
    except OperationFailure as e:
        print(f"Ошибка подключения: {e}")

if __name__ == "__main__":
    main()

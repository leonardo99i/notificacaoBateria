import bluetooth
import time
from win10toast import ToastNotifier

# Endereços MAC dos dispositivos Bluetooth a serem conectados
addrs = ['11:22:33:44:55:66', '77:88:99:AA:BB:CC', 'DD:EE:FF:00:11:22']

# UUID do perfil de bateria (Battery Service) Bluetooth
uuid = '0000180f-0000-1000-8000-00805f9b34fb'

# Intervalo de tempo para verificar a porcentagem de bateria (em segundos)
interval = 600 # 10 minutos

# Loop infinito para verificar a porcentagem de bateria e enviar a notificação
while True:
    for addr in addrs:
        # Conectando ao dispositivo Bluetooth
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((addr, 1))

        # Obtendo o nível de bateria do perfil de bateria Bluetooth
        level = None
        for svc in bluetooth.find_service(uuid=uuid, address=addr):
            for chn in svc['channels']:
                try:
                    # Lendo o valor da porcentagem de bateria
                    sock.send(chr(0x16))
                    sock.send(chr(chn))
                    data = sock.recv(1024)
                    level = ord(data[-1])
                except:
                    pass

        # Fechando a conexão Bluetooth
        sock.close()

        # Enviando a notificação de desktop com o nível de bateria ou com a mensagem de erro, conforme o caso
        toaster = ToastNotifier()
        device_name = ''
        if addr == '11:22:33:44:55:66':
            device_name = 'MX Keys Mini'
        elif addr == '77:88:99:AA:BB:CC':
            device_name = 'MX Master 3'
        elif addr == 'DD:EE:FF:00:11:22':
            device_name = 'Fone de ouvido'
        if level is not None:
            toaster.show_toast(
                'Nível de Bateria Bluetooth - ' + device_name,
                'O dispositivo Bluetooth ' + device_name + ' está com %d%% de carga na bateria.' % level,
                duration=10)
        else:
            toaster.show_toast(
                'Erro de Leitura Bluetooth - ' + device_name,
                'Não foi possível obter a porcentagem de bateria do dispositivo Bluetooth ' + device_name + '.',
                duration=10)

    # Aguardando o intervalo de tempo definido
    time.sleep(interval)

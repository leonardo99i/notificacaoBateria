import time
from plyer import notification
from pygatt import BLEAddressType, GATTToolBackend

# Endereços MAC dos dispositivos Bluetooth
fone_endereco = "00:11:22:33:44:55"
teclado_endereco = "11:22:33:44:55:66"
mouse_endereco = "22:33:44:55:66:77"

while True:
    try:
        # Inicializa o backend do GATTTool
        with GATTToolBackend() as backend:

            # Conecta aos dispositivos Bluetooth
            fone = backend.connect(fone_endereco, address_type=BLEAddressType.public)
            teclado = backend.connect(teclado_endereco, address_type=BLEAddressType.public)
            mouse = backend.connect(mouse_endereco, address_type=BLEAddressType.public)

            # Lê o valor do nível de bateria de cada dispositivo
            fone_bateria = int(fone.char_read("2a19"), 16)
            teclado_bateria = int(teclado.char_read("2a19"), 16)
            mouse_bateria = int(mouse.char_read("2a19"), 16)

            # Exibe a notificação com as informações de bateria
            mensagem = f"AirPods: {fone_bateria}%\nMxKeys Mini: {teclado_bateria}%\nMX Master 3: {mouse_bateria}%"
            notification.notify(
                title="Bateria dos dispositivos Bluetooth",
                message=mensagem,
                timeout=10
            )

        # Aguarda 30 minutos antes de enviar a próxima notificação
        time.sleep(30*60)
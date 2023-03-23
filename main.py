import asyncio
from bleak import BleakClient
from plyer import notification

# Endereços MAC dos dispositivos
DEVICE_MACS = {
    "MX Master 3": "00:12:4B:00:22:CA",
    "MX Keys Mini": "00:12:4B:00:1E:0C",
    "AirPods de Leonardo": "11:22:33:44:55:66"
}

async def get_battery_level(device_name: str) -> int:
    async with BleakClient(DEVICE_MACS[device_name]) as client:
        battery_service = await client.get_service_by_uuid("0000180f-0000-1000-8000-00805f9b34fb")
        battery_level_char = await battery_service.get_characteristic("00002a19-0000-1000-8000-00805f9b34fb")
        battery_level = await battery_level_char.read_value()
        return battery_level[0]

async def send_notification(device_name: str, battery_level: int):
    notification_title = f"{device_name}: bateria"
    notification_text = f"{battery_level}% de bateria restante"
    notification.notify(title=notification_title, message=notification_text)

async def get_and_send_battery_levels():
    while True:
        for device_name in DEVICE_MACS:
            try:
                battery_level = await get_battery_level(device_name)
                await send_notification(device_name, battery_level)
            except:
                print(f"Erro ao obter a bateria de {device_name}")
        await asyncio.sleep(3600) # Espera uma hora (3600 segundos) antes de repetir

asyncio.run(get_and_send_battery_levels())

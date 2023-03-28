    import asyncio
    from bleak import discover, BleakClient
    from plyer import notification

    devices = {
        "MX Master 3": "38:68:A4:07:AC:F1",
        "MX Keys Mini": "52:D0:92:2B:00:85",
        "1MORE ComfoBuds Mini": "A4:05:6E:5B:D5:C2"
    }

    async def get_battery_level(address):
        try:
            async with BleakClient(address) as client:
                battery_level = await client.read_gatt_char("00002a19-0000-1000-8000-00805f9b34fb")
                return battery_level[0]
        except Exception as e:
            return f"Erro ao conectar ao dispositivo {address}: {e}"

    async def scan_devices():
        devices_data = []
        for device_name, device_address in devices.items():
            battery_level = await get_battery_level(device_address)
            if isinstance(battery_level, str):
                notification.notify(title="Erro", message=battery_level)
            else:
                devices_data.append((device_name, battery_level))
        return devices_data

    async def send_notification(devices_data):
        if not devices_data:
            return
        message = "\n".join([f"{name}: {level}%" for name, level in devices_data])
        notification.notify(title="Bateria dos dispositivos Bluetooth", message=message)

    async def main():
        while True:
            devices_data = await scan_devices()
            await send_notification(devices_data)
            await asyncio.sleep(3600)

    if __name__ == "__main__":
        print("Scanning...")
        asyncio.run(main())

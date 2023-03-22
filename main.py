import wmi
import psutil
import pyautogui
import time

def is_bluetooth_connected(device_name):
    wmi_obj = wmi.WMI()
    for controller in wmi_obj.query("SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%(COM%'"):
        if device_name in controller.Description:
            for connected_device in controller[0].Associators_():
                if connected_device.ClassGuid == "{e0cbf06c-cd8b-4647-bb8a-263b43f0f974}":
                    return True
    return False

def main():
    devices = {
        "MX Master 3": "mouse",
        "MX Keys Mini": "keyboard",
        "AirPods de Leonardo": "headphones"
    }

    while True:
        for device_name, device_type in devices.items():
            if is_bluetooth_connected(device_name):
                battery = psutil.sensors_battery()
                message = f"{device_type.title()} battery: {battery.percent}%"
                pyautogui.alert(message, title="Battery Alert", button="OK")
        time.sleep(3600) # 1 hour

if __name__ == "__main__":
    main()

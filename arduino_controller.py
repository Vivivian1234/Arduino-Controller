import serial
import pyautogui

# Update 'COM3' to match your Arduino's COM port
ser = serial.Serial('COM3', 9600, timeout=1)

print("Listening for button input...")

# Map Arduino labels to PC keyboard keys
key_mapping = {
    "Up": "up",
    "Down": "down",
    "Left": "left",
    "Right": "right",
    "Space": "space"
}

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line and ':' in line:
            key = line.split(':')[0]
            print(f"Received: {key}")
            
            if key in key_mapping:
                pyautogui.press(key_mapping[key])
                print(f"Pressed: {key_mapping[key]}")
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    ser.close()



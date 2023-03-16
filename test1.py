import serial

ser = serial.Serial('COM16', 57600)  # Replace 'COM3' with the appropriate port name

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print(data)
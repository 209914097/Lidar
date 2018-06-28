import time
import serial
import binascii

def SetAngle(SetAng):#沿着传感器Y轴负方向看，后仰时角度SetAng为正数，精度(误差)0.1°。
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM3'
    ser.open()
    def loop():
        ser.write(binascii.unhexlify(b'7704000408'))
        bit = binascii.hexlify(ser.read(17)).decode()
        if (bit[16:18] == '00'):
            Angle = int(bit[18:24]) / 10000
            # print('y轴：%f' % (Angle))
        elif (bit[16:18] == '10'):
            Angle = 0 - int(bit[18:24]) / 10000
            # print('y轴：%.4f' % (Angle))

        direction=int((Angle-SetAng)*10)
        # print('△Angle:%d' % (direction))

        import ctypes
        IODLL = ctypes.cdll.LoadLibrary("IODLL.dll")//坚果云

        if (direction>0):
            IODLL.PyLibInitialize()
            IODLL.PyGPIOSetDirection(9, 0)
            IODLL.PyGPIOSetLevel(9, 1)
        elif (direction<0):
            IODLL.PyLibInitialize()
            IODLL.PyGPIOSetDirection(9, 0)
            IODLL.PyGPIOSetLevel(9, 0)

        for i in range (abs(direction)*70):
            IODLL.plug(8,ctypes.c_float(1))

    loop();loop();loop()#校正三次

if __name__ == '__main__':
    SetAngle(10.0)

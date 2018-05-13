import time
import serial
import binascii# hex显示非常感谢http://www.cnblogs.com/r00tgrok/p/hex2char.html
# 编码对照表http://www.w3school.com.cn/tags/html_ref_urlencode.html

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM4'
ser.open()
while True:
    ser.write(binascii.unhexlify(b'7704000408'))
    """
    # ser.write也可以这样写ser.write([0x74,0x04,0x00,0x04,0x08])
    # 在python环境中serial库，接收到所有字符都是相当于串口助手中以 非hex显示的，故binascii.hexlify转换相当于串口助手中以hex显示
    """
    bit=binascii.hexlify(ser.read(17)).decode()
    if (bit[8:10]=='00'):print('x轴：%f'%(int(bit[10:16]) / 10000))
    elif (bit[8:10]=='10'):print('x轴：%.4f'%(0-int(bit[10:16]) / 10000))
    if (bit[16:18]=='00'):print('y轴：%f'%(int(bit[18:24]) / 10000))
    elif (bit[16:18]=='10'):print('y轴：%.4f'%(0-int(bit[18:24]) / 10000))
    time.sleep(0.8)

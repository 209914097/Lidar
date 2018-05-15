from scapy.all import *
import numpy as np
import pandas as pd
import os
from pandas import DataFrame,Series

def csv(ch1,ch1_x, ch1_y, ch1_z,ch2, ch2_x, ch2_y, ch2_z,ch3, ch3_x, ch3_y, ch3_z,ch4, ch4_x, ch4_y, ch4_z,ch5, ch5_x, ch5_y, ch5_z, ch6,ch6_x,
        ch6_y, ch6_z,ch7, ch7_x, ch7_y, ch7_z,ch8, ch8_x, ch8_y, ch8_z, ch9,ch9_x, ch9_y, ch9_z, ch10,ch10_x, ch10_y, ch10_z,ch11, ch11_x,
        ch11_y, ch11_z,ch12, ch12_x, ch12_y, ch12_z,ch13, ch13_x, ch13_y, ch13_z,ch14, ch14_x, ch14_y, ch14_z,ch15, ch15_x, ch15_y, ch15_z,
        ch16,ch16_x, ch16_y, ch16_z, azimuth):
    ch1=DataFrame({'dis':ch1,'x':ch1_x,'y':ch1_y,'z':ch1_z,'azimuth':azimuth,'ID':[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]})
    ch2=DataFrame({'dis':ch2,'x':ch2_x,'y':ch2_y,'z':ch2_z,'azimuth':azimuth,'ID':[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]})
    ch3=DataFrame({'dis':ch3,'x':ch3_x,'y':ch3_y,'z':ch3_z,'azimuth':azimuth,'ID':[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]})
    ch4=DataFrame({'dis':ch4,'x':ch4_x,'y':ch4_y,'z':ch4_z,'azimuth':azimuth,'ID':[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]})
    ch5=DataFrame({'dis':ch5,'x':ch5_x,'y':ch5_y,'z':ch5_z,'azimuth':azimuth,'ID':[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]})
    ch6=DataFrame({'dis':ch6,'x':ch6_x,'y':ch6_y,'z':ch6_z,'azimuth':azimuth,'ID':[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]})
    ch7=DataFrame({'dis':ch7,'x':ch7_x,'y':ch7_y,'z':ch7_z,'azimuth':azimuth,'ID':[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]})
    ch8=DataFrame({'dis':ch8,'x':ch8_x,'y':ch8_y,'z':ch8_z,'azimuth':azimuth,'ID':[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]})
    ch9=DataFrame({'dis':ch9,'x':ch9_x,'y':ch9_y,'z':ch9_z,'azimuth':azimuth,'ID':[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]})
    ch10=DataFrame({'dis':ch10,'x':ch10_x,'y':ch10_y,'z':ch10_z,'azimuth':azimuth,'ID':[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]})
    ch11=DataFrame({'dis':ch11,'x':ch11_x,'y':ch11_y,'z':ch11_z,'azimuth':azimuth,'ID':[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11]})
    ch12=DataFrame({'dis':ch12,'x':ch12_x,'y':ch12_y,'z':ch12_z,'azimuth':azimuth,'ID':[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]})
    ch13=DataFrame({'dis':ch13,'x':ch13_x,'y':ch13_y,'z':ch13_z,'azimuth':azimuth,'ID':[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13]})
    ch14=DataFrame({'dis':ch14,'x':ch14_x,'y':ch14_y,'z':ch14_z,'azimuth':azimuth,'ID':[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14]})
    ch15=DataFrame({'dis':ch15,'x':ch15_x,'y':ch15_y,'z':ch15_z,'azimuth':azimuth,'ID':[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]})
    ch16=DataFrame({'dis':ch16,'x':ch16_x,'y':ch16_y,'z':ch16_z,'azimuth':azimuth,'ID':[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16]})

    if(os.path.exists('kk.csv')):
        df = pd.read_csv('kk.csv')
        pd.concat([df[['dis','x','y','z','azimuth','ID']],ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15, ch16],
                  axis=0).to_csv('kk.csv')
    else:
        pd.concat([ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13, ch14, ch15, ch16],
                  axis=0).to_csv('kk.csv')


def interpolation(a):
    b = []
    for i in range(len(a) - 1):
        if float(a[i + 1]) < float(a[i]):
            b.append(round(float(a[i]) + ((float(a[i + 1]) + 360 - float(a[i])) / 2), 3))
        else:
            b.append(round(float(a[i]) + ((float(a[i + 1]) - float(a[i])) / 2), 3))
        if b[i] > 360: b[i] = round((b[i] - 360), 3)

    b.append(round(b[-1] + 0.36, 3))
    if b[-1] > 360:
        b[-1] = round((b[-1] - 360), 3)
    # b = [str(x) for x in b]
    return b

def coordinate(ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10,ch11,ch12,ch13,ch14,ch15,ch16,azimuth):
    azimuth_sin=[np.sin(math.radians(x))for x in azimuth]
    azimuth_cos=[np.cos(math.radians(x))for x in azimuth]
    omega=[-14.996,-12.9698,-10.9997,-8.996,-6.9839,-5.0042,-3.0053,-1.0026,14.976,12.9902,10.9825,9.01,6.991,5.0006,3.0053,0.9775]
    omega_cos=[0.9659438929131666, 0.9744884987523434, 0.9816281825077715, 0.9876992593741064, 0.992580357498133, 0.996188306565623, 0.9986246892778983, 0.9998469021618591, 0.966034155413497, 0.9744085266704574, 0.9816854169504129, 0.9876610225871372, 0.992565282587893, 0.9961937853443192, 0.9986246892778983, 0.9998544716056567]
    omega_sin=[-0.258751610127854, -0.22443744295327367, -0.1908038555860158, -0.1563655110049578, -0.12159043510440477, -0.08722876739881417, -0.05242833169786284, -0.017497778068476105, 0.2584144163442347, 0.22478439258967362, 0.19050916551938907, 0.15660684679199197, 0.12171343311736861, 0.0871661748693627, 0.05242833169786284, 0.017059765829958468]
    ch1_z = [x * omega_sin[0] for x in ch1]
    ch1_y = list(np.multiply([x * omega_cos[0] for x in ch1], azimuth_cos))
    ch1_x = list(np.multiply([x * omega_cos[0] for x in ch1], azimuth_sin))

    ch2_z = [x * omega_sin[1] for x in ch2]
    ch2_y = list(np.multiply([x * omega_cos[1] for x in ch2], azimuth_cos))
    ch2_x = list(np.multiply([x * omega_cos[1] for x in ch2], azimuth_sin))

    ch3_z = [x * omega_sin[2] for x in ch3]
    ch3_y = list(np.multiply([x * omega_cos[2] for x in ch3], azimuth_cos))
    ch3_x = list(np.multiply([x * omega_cos[2] for x in ch3], azimuth_sin))

    ch4_z = [x * omega_sin[3] for x in ch4]
    ch4_y = list(np.multiply([x * omega_cos[3] for x in ch4], azimuth_cos))
    ch4_x = list(np.multiply([x * omega_cos[3] for x in ch4], azimuth_sin))

    ch5_z = [x * omega_sin[4] for x in ch5]
    ch5_y = list(np.multiply([x * omega_cos[4] for x in ch5], azimuth_cos))
    ch5_x = list(np.multiply([x * omega_cos[4] for x in ch5], azimuth_sin))

    ch6_z = [x * omega_sin[5] for x in ch6]
    ch6_y = list(np.multiply([x * omega_cos[5] for x in ch6], azimuth_cos))
    ch6_x = list(np.multiply([x * omega_cos[5] for x in ch6], azimuth_sin))

    ch7_z = [x * omega_sin[6] for x in ch7]
    ch7_y = list(np.multiply([x * omega_cos[6] for x in ch7], azimuth_cos))
    ch7_x = list(np.multiply([x * omega_cos[6] for x in ch7], azimuth_sin))

    ch8_z = [x * omega_sin[7] for x in ch8]
    ch8_y = list(np.multiply([x * omega_cos[7] for x in ch8], azimuth_cos))
    ch8_x = list(np.multiply([x * omega_cos[7] for x in ch8], azimuth_sin))

    ch9_z = [x * omega_sin[8] for x in ch9]
    ch9_y = list(np.multiply([x * omega_cos[8] for x in ch9], azimuth_cos))
    ch9_x = list(np.multiply([x * omega_cos[8] for x in ch9], azimuth_sin))

    ch10_z = [x * omega_sin[9] for x in ch10]
    ch10_y = list(np.multiply([x * omega_cos[9] for x in ch10], azimuth_cos))
    ch10_x = list(np.multiply([x * omega_cos[9] for x in ch10], azimuth_sin))

    ch11_z = [x * omega_sin[10] for x in ch11]
    ch11_y = list(np.multiply([x * omega_cos[10] for x in ch11], azimuth_cos))
    ch11_x = list(np.multiply([x * omega_cos[10] for x in ch11], azimuth_sin))

    ch12_z = [x * omega_sin[11] for x in ch12]
    ch12_y = list(np.multiply([x * omega_cos[11] for x in ch12], azimuth_cos))
    ch12_x = list(np.multiply([x * omega_cos[11] for x in ch12], azimuth_sin))

    ch13_z = [x * omega_sin[12] for x in ch13]
    ch13_y = list(np.multiply([x * omega_cos[12] for x in ch13], azimuth_cos))
    ch13_x = list(np.multiply([x * omega_cos[12] for x in ch13], azimuth_sin))

    ch14_z = [x * omega_sin[13] for x in ch14]
    ch14_y = list(np.multiply([x * omega_cos[13] for x in ch14], azimuth_cos))
    ch14_x = list(np.multiply([x * omega_cos[13] for x in ch14], azimuth_sin))

    ch15_z = [x * omega_sin[14] for x in ch15]
    ch15_y = list(np.multiply([x * omega_cos[14] for x in ch15], azimuth_cos))
    ch15_x = list(np.multiply([x * omega_cos[14] for x in ch15], azimuth_sin))

    ch16_z = [x * omega_sin[15] for x in ch16]
    ch16_y = list(np.multiply([x * omega_cos[15] for x in ch16], azimuth_cos))
    ch16_x = list(np.multiply([x * omega_cos[15] for x in ch16], azimuth_sin))
    csv(ch1,ch1_x, ch1_y, ch1_z,ch2, ch2_x, ch2_y, ch2_z,ch3, ch3_x, ch3_y, ch3_z,ch4, ch4_x, ch4_y, ch4_z,ch5, ch5_x, ch5_y, ch5_z, ch6,ch6_x,
        ch6_y, ch6_z,ch7, ch7_x, ch7_y, ch7_z,ch8, ch8_x, ch8_y, ch8_z, ch9,ch9_x, ch9_y, ch9_z, ch10,ch10_x, ch10_y, ch10_z,ch11, ch11_x,
        ch11_y, ch11_z,ch12, ch12_x, ch12_y, ch12_z,ch13, ch13_x, ch13_y, ch13_z,ch14, ch14_x, ch14_y, ch14_z,ch15, ch15_x, ch15_y, ch15_z,
        ch16,ch16_x, ch16_y, ch16_z, azimuth)

def ok(x):
    x=list(x)
    azimuth=[];azimuth_2=[]
    ch1=[];ch1_2=[]
    ch2 = [];ch2_2 = []
    ch3 = [];ch3_2 = []
    ch4 = [];ch4_2 = []
    ch5 = [];ch5_2 = []
    ch6 = [];ch6_2 = []
    ch7 = [];ch7_2 = []
    ch8 = [];ch8_2 = []
    ch9 = [];ch9_2 = []
    ch10 = []; ch10_2 = []
    ch11 = [];ch11_2 = []
    ch12 = [];ch12_2 = []
    ch13 = [];ch13_2 = []
    ch14 = [];ch14_2 = []
    ch15 = [];ch15_2 = []
    ch16 = [];ch16_2 = []
    for i in range(12):
        azimuth.append((round(int(x[i * 200 + 88] + x[i * 200 + 89] + x[i * 200 + 90] + x[i * 200 + 91], 16) / 100, 2)))
        ch1.append((round(int(x[i * 200 + 92] + x[i * 200 + 93] + x[i * 200 + 94] + x[i * 200 + 95], 16) / 100, 2)));
        ch1_2.append(
            (round(int(x[i * 200 + 188] + x[i * 200 + 189] + x[i * 200 + 190] + x[i * 200 + 191], 16) / 100, 2)))
        ch2.append((round(int(x[i * 200 + 98] + x[i * 200 + 99] + x[i * 200 + 100] + x[i * 200 + 101], 16) / 100, 2)));
        ch2_2.append(
            (round(int(x[i * 200 + 194] + x[i * 200 + 195] + x[i * 200 + 196] + x[i * 200 + 197], 16) / 100, 2)))
        ch3.append(
            (round(int(x[i * 200 + 104] + x[i * 200 + 105] + x[i * 200 + 106] + x[i * 200 + 107], 16) / 100, 2)));
        ch3_2.append(
            (round(int(x[i * 200 + 200] + x[i * 200 + 201] + x[i * 200 + 202] + x[i * 200 + 203], 16) / 100, 2)))
        ch4.append(
            (round(int(x[i * 200 + 110] + x[i * 200 + 111] + x[i * 200 + 112] + x[i * 200 + 113], 16) / 100, 2)));
        ch4_2.append(
            (round(int(x[i * 200 + 206] + x[i * 200 + 207] + x[i * 200 + 208] + x[i * 200 + 209], 16) / 100, 2)))
        ch5.append(
            (round(int(x[i * 200 + 116] + x[i * 200 + 117] + x[i * 200 + 118] + x[i * 200 + 119], 16) / 100, 2)));
        ch5_2.append(
            (round(int(x[i * 200 + 212] + x[i * 200 + 213] + x[i * 200 + 214] + x[i * 200 + 215], 16) / 100, 2)))
        ch6.append(
            (round(int(x[i * 200 + 122] + x[i * 200 + 123] + x[i * 200 + 124] + x[i * 200 + 125], 16) / 100, 2)));
        ch6_2.append(
            (round(int(x[i * 200 + 218] + x[i * 200 + 219] + x[i * 200 + 220] + x[i * 200 + 221], 16) / 100, 2)))
        ch7.append(
            (round(int(x[i * 200 + 128] + x[i * 200 + 129] + x[i * 200 + 130] + x[i * 200 + 131], 16) / 100, 2)));
        ch7_2.append(
            (round(int(x[i * 200 + 224] + x[i * 200 + 225] + x[i * 200 + 226] + x[i * 200 + 227], 16) / 100, 2)))
        ch8.append(
            (round(int(x[i * 200 + 134] + x[i * 200 + 135] + x[i * 200 + 136] + x[i * 200 + 137], 16) / 100, 2)));
        ch8_2.append(
            (round(int(x[i * 200 + 230] + x[i * 200 + 231] + x[i * 200 + 232] + x[i * 200 + 233], 16) / 100, 2)))
        ch9.append(
            (round(int(x[i * 200 + 140] + x[i * 200 + 141] + x[i * 200 + 142] + x[i * 200 + 143], 16) / 100, 2)));
        ch9_2.append(
            (round(int(x[i * 200 + 236] + x[i * 200 + 237] + x[i * 200 + 238] + x[i * 200 + 239], 16) / 100, 2)))
        ch10.append(
            (round(int(x[i * 200 + 146] + x[i * 200 + 147] + x[i * 200 + 148] + x[i * 200 + 149], 16) / 100, 2)));
        ch10_2.append(
            (round(int(x[i * 200 + 242] + x[i * 200 + 243] + x[i * 200 + 244] + x[i * 200 + 245], 16) / 100, 2)))
        ch11.append(
            (round(int(x[i * 200 + 152] + x[i * 200 + 153] + x[i * 200 + 154] + x[i * 200 + 155], 16) / 100, 2)));
        ch11_2.append(
            (round(int(x[i * 200 + 248] + x[i * 200 + 249] + x[i * 200 + 250] + x[i * 200 + 251], 16) / 100, 2)))
        ch12.append(
            (round(int(x[i * 200 + 158] + x[i * 200 + 159] + x[i * 200 + 160] + x[i * 200 + 161], 16) / 100, 2)));
        ch12_2.append(
            (round(int(x[i * 200 + 254] + x[i * 200 + 255] + x[i * 200 + 256] + x[i * 200 + 257], 16) / 100, 2)))
        ch13.append(
            (round(int(x[i * 200 + 164] + x[i * 200 + 165] + x[i * 200 + 166] + x[i * 200 + 167], 16) / 100, 2)));
        ch13_2.append(
            (round(int(x[i * 200 + 260] + x[i * 200 + 261] + x[i * 200 + 262] + x[i * 200 + 263], 16) / 100, 2)))
        ch14.append(
            (round(int(x[i * 200 + 170] + x[i * 200 + 171] + x[i * 200 + 172] + x[i * 200 + 173], 16) / 100, 2)));
        ch14_2.append(
            (round(int(x[i * 200 + 266] + x[i * 200 + 267] + x[i * 200 + 268] + x[i * 200 + 269], 16) / 100, 2)))
        ch15.append(
            (round(int(x[i * 200 + 176] + x[i * 200 + 177] + x[i * 200 + 178] + x[i * 200 + 179], 16) / 100, 2)));
        ch15_2.append(
            (round(int(x[i * 200 + 272] + x[i * 200 + 273] + x[i * 200 + 274] + x[i * 200 + 275], 16) / 100, 2)))
        ch16.append(
            (round(int(x[i * 200 + 182] + x[i * 200 + 183] + x[i * 200 + 184] + x[i * 200 + 185], 16) / 100, 2)));
        ch16_2.append(
            (round(int(x[i * 200 + 278] + x[i * 200 + 279] + x[i * 200 + 280] + x[i * 200 + 281], 16) / 100, 2)))

    azimuth_2 = interpolation(azimuth)
    azimuth=azimuth+azimuth_2;ch1=ch1+ch1_2;ch2=ch2+ch2_2;ch3=ch3+ch3_2;ch4=ch4+ch4_2;ch5=ch5+ch5_2;ch6=ch6+ch6_2;ch7=ch7+ch7_2;ch8=ch8+ch8_2;ch9=ch9+ch9_2;ch10=ch10+ch10_2;ch11=ch11+ch11_2;ch12=ch12+ch12_2;ch13=ch13+ch13_2;ch14=ch14+ch14_2;ch15=ch15+ch15_2;ch16=ch16+ch16_2;
    ch1 = [x if x < 150 else 0 for x in ch1]
    ch2 = [x if x < 150 else 0 for x in ch2]
    ch3 = [x if x < 150 else 0 for x in ch3]
    ch4 = [x if x < 150 else 0 for x in ch4]
    ch5 = [x if x < 150 else 0 for x in ch5]
    ch6 = [x if x < 150 else 0 for x in ch6]
    ch7 = [x if x < 150 else 0 for x in ch7]
    ch8 = [x if x < 150 else 0 for x in ch8]
    ch9 = [x if x < 150 else 0 for x in ch9]
    ch10 = [x if x < 150 else 0 for x in ch10]
    ch11 = [x if x < 150 else 0 for x in ch11]
    ch12 = [x if x < 150 else 0 for x in ch12]
    ch13 = [x if x < 150 else 0 for x in ch13]
    ch14 = [x if x < 150 else 0 for x in ch14]
    ch15 = [x if x < 150 else 0 for x in ch15]
    ch16 = [x if x < 150 else 0 for x in ch16]
    coordinate (ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10,ch11,ch12,ch13,ch14,ch15,ch16,azimuth)

if __name__ == "__main__":
    dpkt = sniff(filter="udp and ip src 192.168.1.200 and udp port 6699", count=83,
                 prn=lambda x: ok(hexdump(x[0][Raw].load, dump=True)))
    wrpcap("demo.pcap", dpkt)



#Jamee Bashir 

from mpu6050 import mpu6050
import time
import urllib.request
mpu = mpu6050(0x68)

while True:
    print("Temp : "+str(mpu.get_temp()))
    temp=str(mpu.get_temp())
    print()

    accel_data = mpu.get_accel_data()
    print("Acc X : "+str(accel_data['x']))
    print("Acc Y : "+str(accel_data['y']))
    print("Acc Z : "+str(accel_data['z']))
    acc_x=str(accel_data['x'])
    acc_y=str(accel_data['y'])
    acc_z=str(accel_data['z'])
    print()

    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str(gyro_data['x']))
    print("Gyro Y : "+str(gyro_data['y']))
    print("Gyro Z : "+str(gyro_data['z']))
    gyro_x=str(gyro_data['x'])
    gyro_y=str(gyro_data['y'])
    gyro_z=str(gyro_data['z'])
    print()
    print("-------------------------------")

    URL='url-goes-here-(like : things-speak)'
    KEY='url-key-goes-here'
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}&field7={}'.fromat(temp,acc_x,acc_y,acc_x,gyro_x,gyro_y,gyro_z)
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)
    time.sleep(1)

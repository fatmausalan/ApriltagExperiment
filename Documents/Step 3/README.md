# Step 3 - Basic Car with Raspberry Pi Zero
In this step, motor driver and motor connections were made with Raspberry Pi. We made our power supply with LiPo. We connected the positive and negative terminals we received from the LiPo to the 12V input of the motor driver and the GND input. In order to power the Raspberry, we cut the micro usb cable and separated the red and black wires. We connected the black one to GND and the red one to the 5V output of the motor driver. In this way, we have made the power supply of the motors and Raspberry.
The connections with the motor driver and Raspberry Pi are as follows.
* IN1 --> GPIO 23
* IN2 --> GPIO 24
* ENA --> GPIO 25
* IN3 --> GPIO 17
* IN4 --> GPIO 27
* ENB --> GPIO 22

------------------------------------------------------------------------------------------------------------------------------------------
# Adım 3 - Raspberry Pi Zero ile Basit Araba
Bu adımda Raspberry Pi ile motor sürücü ve motorların bağlantıları yapıldı. Güç beslememizi LiPo ile yaptık. LiPo üzerinden aldığımız pozitif ve negatif uçları motor sürücünün 12V girişi ile GND girişine bağladık. Raspberry'e güç beslemesi yapabilmek için micro usb kablosunu keserek kırmızı ve siyah kabloyu ayırdık. Bu kablolardan siyahı GND'ye kırmızı olanı motor sürücünün 5V çıkışına bağladık. Bu şekilde motorların ve Raspberry'nin güç beslemesini yapmış olduk.
Motor sürücü ve Raspberry Pi ile olan bağlantılar da aşağıdaki gibidir.
* IN1 --> GPIO 23
* IN2 --> GPIO 24
* ENA --> GPIO 25
* IN3 --> GPIO 17
* IN4 --> GPIO 27
* ENB --> GPIO 22

# Step 1 - Needed Componnets for our Project
#### Just to Run AprilTag 
* Raspberry Pi Zero WH
* Raspberry Pi Power Adapter
* 16 GB Sd Card
* Micro-USB OTG Cable
* HDMI to Mini HDMI Adapter
* Raspberry Pi Camera V2.1
* Raspberry Pi Zero Camera Cable
#### For Car 
* 2 pieces 6 V 250 RPM Motor and Wheel set
* Jumper cable 
* L298N Dual Motor Driver Board with Voltage Regulator
* LiPo baterry 

  When we use the car with Raspberry Pi Zero, we powered it with LiPo baterry and the micro usb cable we obtained by cutting.
  During the project, we preferred Raspberry Pi Zero because the linux operating system is supported, as stated on apriltag's github page. We preferred the full version of the Raspberry Pi operating system in order to be easy to use in the initial stages. We used the Raspberry Pi with an external monitor while making the first installs, then we ran it using the VNC connection.
  Initially, the phone camera was tried using the IP Webcam application for the camera, but the tag detection was too late due to the slow transmission. That's why we decided to use the Raspberry Pi's own camera.
  We decided to create a basic tool to transmit our commands. We powered the motors and Raspberry P with a LiPo battery.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Adım 1 - Projemiz için Gerekli Parçalar
#### Sadece AprilTag Çalıştırmak için Kullanılanlar
* Raspberry Pi Zero WH
* Raspberry Pi Power Adaptör
* 16 GB Sd Kart
* Micro-USB OTG Kablo
* HDMI to Mini HDMI Adaptör
* Raspberry Pi Kamera V2.1
* Raspberry Pi Zero Kamera Kablosu
#### For Car 
* 2 adet 6 V 250 RPM Motor ve Tekerlek Seti
* Jumper Kablo 
* L298N Voltaj Regulatörlü Çift Motor Sürücü Kartı
* LiPo Pil 
  Arabayı Raspberry Pi Zero ile kullandığımızda LiPo pil ve keserek elde ettiğimiz mikro usb kablo ile besledik.
  Proje süresince AprilTag'ın github sayfasında belirtildiği gibi linux işletim sistemi desteklendiği için Raspberry Pi Zero tercih ettik. İlk aşamalarda kullanımı kolay olması için Raspberry Pi işletim sisteminin tam sürümünü tercih ettik. İlk kurulumları yaparken Raspberry Pi'yi harici bir monitör ile kullandık, ardından VNC bağlantısını kullanarak çalıştırdık.
  Başlangıçta telefon kamerası, kamera için IP Webcam uygulaması kullanılarak denendi, ancak yavaş iletim nedeniyle etiket algılaması çok geç oldu. Bu yüzden Raspberry Pi'nin kendi kamerasını kullanmaya karar verdik.
  Komutlarımızı iletmek için temel bir araç oluşturmaya karar verdik. Motorları ve Raspberry Pi'yi bir LiPo pil ile çalıştırdık.

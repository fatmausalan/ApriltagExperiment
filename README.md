# Apriltag Experiment
In this repository, we want to share our experiment with apriltag. And also, we answer the questions of what is apriltag, how we use it, which component do we use and why. 
You can reach our steps from Documeents folder. And, under Code folder, test and project codes can be found. Under Imagesfolder, you can find all tags which are we use in all project. 
* [Step 0](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%200) --> What is AprilTag?
* [Step 1](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%201) --> Needed Componnets for our Project
* [Step 2](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%202) --> AprilTag Usage with Raspberry Pi Zero W
* [Step 3](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%203) --> Basic Car with Raspberry Pi Zero
* [Step 4](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%204) --> Giving Basic Command to Car with AprilTag

## Introduction
We start the our project with searching what is AprilTag, how did AprilTag originate and envolve, what is the science behind it. AprilTag is a visual fiducial system, useful for a wide variety of tasks including augmented reality, robotics, and camera calibration. Targets can be created from an ordinary printer, and the AprilTag detection software computes the precise 3D position, orientation, and identity of the tags relative to the camera. The AprilTag library is implemented in C with no external dependencies. It is designed to be easily included in other applications, as well as be portable to embedded devices. Real-time performance can be achieved even on cell-phone grade processors.
You can easily reach more information from [Project Page](https://april.eecs.umich.edu/software/apriltag). 
You can reach github repo from [here](https://github.com/AprilRobotics/apriltag).
* With a QR code, a human is typically involved in aligning the camera with the tag and photographs it at fairly high resolution obtaining hundreds of bytes, such as a web address. In contrast, a visual fiducial has a small information payload (perhaps 12 bits), but is designed to be automatically detected and localized even when it is at very low resolution, unevenly lit, oddly rotated, or tucked away in the corner of an otherwise cluttered image. Visual fiducial systems are perhaps best known for their application to augmented reality, which spurred the development of several popular systems including ARToolkit and ARTag. Real-world objects can be augmented with visual fiducials, allowing virtually-generated imagery to be super-imposed. Similarly, visual fiducials can be used for basic motion capture. For more [here](https://april.eecs.umich.edu/media/pdfs/olson2011tags.pdf).
* We use AprilTag3 in our project. This work is based on the earlier AprilTag system. The design of AprilTags as a black-and-white square tag with an encoded binary payload is based on the earlier ARTag and ARToolkit. AprilTag introduced an improved method of generating binary payloads, guaranteeing a minimum Hamming distance between tags under all possible rotations, making them more robust than earlier designs. The tag generation process, a lexicode-based process with minimum complexity heuristics, was empirically shown to reduce the false positive rate compared to ARTag designs of similar bit length. For more [here](https://april.eecs.umich.edu/media/pdfs/wang2016iros.pdf). 
## What We Did in Our Project?
After doing our research on AprilTag, we decided to continue our project on Raspberry Pi Zero. First of all, we started by making the necessary installations for the Raspberry Pi. At this stage, we had a hard time choosing the camera. First, we wanted to use the phone cameras that we could easily reach, but it didn't work. The details are mentioned in the steps. After the necessary installations were made on Raspberry, apriltag was tested using the raspberry camera and it was observed that it detected successfully. Then the basic 2WD vehicle was created. Our aim is to give direction to this tool using AprilTag. During the development phase, the tool is to ensure that it reaches the desired point by using the tags that come in a certain order. The next step is to map in an indoor environment using tags.
### Step 0
First of all, we started by understanding and summarizing the articles mentioned in the introduction section. After reviewing these articles, we reviewed AprilTag's github page. And in this step, we've summarized what we've learned about AprilTag.
### Step 1
In this step, we mentioned which components we use and why. We initially tried to work through windows but we were unsuccessful. At the same time, as stated on the github page, linux operating systems are supported, although there have been successful ones on windows.
### Step 2
This step briefly summarizes how you can work with the Raspberry Pi Zero. It also explains the setup required for AprilTag and how to do your first test.
### Step 3 
How to connect and test the car to be created using Raspberry Pi is explained in this section.
### Step 4
How to steer the car using AprilTag is explained in this step. At the same time, the processing time of the information received from the tags is examined.

Note: As a result of the studies, we have created a repo and tool that needs to be continued to be developed. Due to the delay in recognizing the tags, the vehicle has not been able to operate in a controlled manner yet. However, the research process continues. If it is desired to add to the repo, it can be done in accordance with the general structure.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# AprilTag Deneyleri
Bu repository'de AprilTag ile yaptığımız deneyi paylaşmak istiyoruz. Ayrıca AprilTag nedir, nasıl kullanırız, hangi bileşeni neden kullanırız sorularına da cevap veriyoruz.
Adımlarımıza Documents klasöründen ulaşabilirsiniz. Ve Code klasörü altında test ve proje kodlarını bulabilrsiniz. Images klasörü altında projede kullandığımız tüm tagleri bulabilirsiniz.
* [Adım 0](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%200) --> What is AprilTag?
* [Adım 1](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%201) --> Needed Componnets for our Project
* [Adım 2](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%202) --> AprilTag Usage with Raspberry Pi Zero W
* [Adım 3](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%203) --> Basic Car with Raspberry Pi Zero
* [Adım 4](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%204) --> Giving Basic Command to Car with AprilTag

## Giriş
AprilTag'in ne olduğunu, AprilTag'in nasıl ortaya çıktığını ve neler içerdiğini, arkasındaki bilimin ne olduğunu araştırarak projemize başlıyoruz. AprilTag, artırılmış gerçeklik, robotik ve kamera kalibrasyonu gibi çok çeşitli görevler için kullanışlı bir görsel referans sistemidir. Hedefler sıradan bir yazıcıdan çıktı alınarak oluşturulabilir ve AprilTag detection yazılımı, etiketlerin kameraya göre kesin 3D konumunu, yönünü ve kimliğini hesaplar. AprilTag kitaplığı, C dilinde harici bağımlılık olmadan uygulanır. Diğer uygulamalara kolayca dahil edilecek ve gömülü cihazlara taşınabilir olacak şekilde tasarlanmıştır. Cep telefonu sınıfı işlemcilerde bile gerçek zamanlı performans elde edilebilir.
Daha fazla bilgi için: [Resmî Sayfası](https://april.eecs.umich.edu/software/apriltag).  
Github repositorysine buradan ulaşabilirsiniz: [AprilTag Repository](https://github.com/AprilRobotics/apriltag).
* Bir QR kodunu kullanırken kişi kamerayı etiketle hizalar ve bir web adresi gibi yüzlerce bayt elde ederek oldukça yüksek çözünürlükte fotoğraflama yapar. Buna karşılık, görsel bir referans noktasının(a fiducial system, AprilTag) küçük bir bilgi yükü vardır (12 bit kadar), ancak çok düşük çözünürlükte, eşit olmayan şekilde aydınlatıldığında, garip bir şekilde döndürüldüğünde veya başka bir şekilde köşeye sıkıştırıldığında bile otomatik olarak algılanacak ve konumlandırılacak şekilde tasarlanmıştır. Görsel referans sistemleri belki de en iyi, ARToolkit ve ARTag dahil olmak üzere birçok popüler sistemin gelişimini teşvik eden artırılmış gerçekliğe uygulamalarıyla bilinir. Gerçek dünyadaki nesneler, sanal olarak oluşturulmuş görüntülerin üst üste bindirilmesine izin vererek görsel referanslarla genişletilebilir. Benzer şekilde, temel hareket yakalama için görsel referanslar kullanılabilir. Bu konu hakkında [daha fazla bilgi için](https://april.eecs.umich.edu/media/pdfs/olson2011tags.pdf).
*  Projemizde AprilTag3 kullanıyoruz. Bu çalışma, önceki AprilTag sistemine dayanmaktadır. AprilTag'in kodlanmış binary prensibe sahip siyah-beyaz kare etiket olarak tasarımı, önceki ARTag ve ARToolkit'e dayanmaktadır. AprilTag, binary elementler oluşturmak için geliştirilmiş bir yöntem sunarak, etiketler arasında olası tüm dönüşlerde minimum Hamming mesafesini garanti ederek onları önceki tasarımlardan daha sağlam hale getirdi. Minimum karmaşıklık heuristic yöntemine sahip lexicode tabanlı bir süreç olan etiket oluşturma sürecinin, benzer bit uzunluğundaki ARTag tasarımlarına kıyasla yanlış pozitif oranı azalttığı deneysel olarak gösterildi. Bu konu hakkında [daha fazla bilgi için](https://april.eecs.umich.edu/media/pdfs/wang2016iros.pdf).

## Peki biz projemizde ne yaptık?
AprilTag üzerinde araştırmamızı yaptıktan sonra projemize Raspberry Pi Zero üzerinde devam etme kararı aldık. Öncelikle Raspberry Pi için gerekli kurulumları yaparak başladık. Bu aşamada kamera seçiminde zorlandık. Önce kolayca ulaşabildiğimiz telefon kameralarını kullanmak istedik ama olmadı. Ayrıntılar adımlarda belirtilmiştir. Raspberry üzerinde gerekli kurulumlar yapıldıktan sonra AprilTag, Raspberry kamerası kullanılarak test edilmiş ve başarılı bir şekilde tespit edildiği gözlemlenmiştir. Ardından temel 2WD araç kuruldu. Amacımız AprilTag kullanarak bu araca yön vermek ve geliştirme aşamasında aracın, belirli bir sırayla gelen etiketleri kullanarak istenilen noktaya ulaşmasını sağlamaktır. Bir sonraki adım, tagleri kullanarak bir iç mekan ortamında haritalama yapmaktır.
### Adım 0
Öncelikle giriş bölümünde bahsedilen makaleleri anlayarak ve özetleyerek başladık. Bu yazıları inceledikten sonra AprilTag'in github sayfasını inceledik. Ve bu adımda, AprilTag hakkında öğrendiklerimizi özetledik.
### Adım 1
Bu adımda hangi bileşenleri ve neden kullandığımızdan bahsettik. Başlangıçta Windows'da çalışmayı denedik ama başarısız olduk. Aynı zamanda github sayfasında da belirtildiği gibi Windows üzerinde başarılı olanlar olsa da Linux işletim sistemleri desteklenmektedir.
### Adım 2
Bu adım, Raspberry Pi Zero ile nasıl çalışabileceğinizi kısaca özetlemektedir. Ayrıca AprilTag için gereken kurulumu ve ilk testinizi nasıl yapacağınızı da açıklar.
### Adım 3 
Raspberry Pi kullanılarak oluşturulacak arabanın nasıl bağlanacağı ve test edileceği bu bölümde anlatılmaktadır.
### Adım 4
AprilTag kullanarak arabanın nasıl yönlendirileceği bu adımda açıklanmaktadır. Aynı zamanda taglerden alınan bilgilerin işlenme süresi incelenir.

Not: Çalışmaların sonucunda geliştirilmeye devam edilmesi gereken bir repo ve araç oluşturmuş olduk. Aracın tag'leri tanıma süresindeki gecikmeden ötürü kontrollü bir şekilde çalışması henüz sağlanamadı. Ancak araştırma süreci devam etmektedir. Eğer repoya ekleme yapılmak isteniyorsa genel yapıya uygun olacak şekilde yapılabilir. 

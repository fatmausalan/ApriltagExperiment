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
Bu repository'de AprilTag ile yapt??????m??z deneyi payla??mak istiyoruz. Ayr??ca AprilTag nedir, nas??l kullan??r??z, hangi bile??eni neden kullan??r??z sorular??na da cevap veriyoruz.
Ad??mlar??m??za Documents klas??r??nden ula??abilirsiniz. Ve Code klas??r?? alt??nda test ve proje kodlar??n?? bulabilrsiniz. Images klas??r?? alt??nda projede kulland??????m??z t??m tagleri bulabilirsiniz.
* [Ad??m 0](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%200) --> What is AprilTag?
* [Ad??m 1](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%201) --> Needed Componnets for our Project
* [Ad??m 2](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%202) --> AprilTag Usage with Raspberry Pi Zero W
* [Ad??m 3](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%203) --> Basic Car with Raspberry Pi Zero
* [Ad??m 4](https://github.com/fux00/ApriltagExperiment/tree/main/Documents/Step%204) --> Giving Basic Command to Car with AprilTag

## Giri??
AprilTag'in ne oldu??unu, AprilTag'in nas??l ortaya ????kt??????n?? ve neler i??erdi??ini, arkas??ndaki bilimin ne oldu??unu ara??t??rarak projemize ba??l??yoruz. AprilTag, art??r??lm???? ger??eklik, robotik ve kamera kalibrasyonu gibi ??ok ??e??itli g??revler i??in kullan????l?? bir g??rsel referans sistemidir. Hedefler s??radan bir yaz??c??dan ????kt?? al??narak olu??turulabilir ve AprilTag detection yaz??l??m??, etiketlerin kameraya g??re kesin 3D konumunu, y??n??n?? ve kimli??ini hesaplar. AprilTag kitapl??????, C dilinde harici ba????ml??l??k olmadan uygulan??r. Di??er uygulamalara kolayca dahil edilecek ve g??m??l?? cihazlara ta????nabilir olacak ??ekilde tasarlanm????t??r. Cep telefonu s??n??f?? i??lemcilerde bile ger??ek zamanl?? performans elde edilebilir.
Daha fazla bilgi i??in: [Resm?? Sayfas??](https://april.eecs.umich.edu/software/apriltag).  
Github repositorysine buradan ula??abilirsiniz: [AprilTag Repository](https://github.com/AprilRobotics/apriltag).
* Bir QR kodunu kullan??rken ki??i kameray?? etiketle hizalar ve bir web adresi gibi y??zlerce bayt elde ederek olduk??a y??ksek ????z??n??rl??kte foto??raflama yapar. Buna kar????l??k, g??rsel bir referans noktas??n??n(a fiducial system, AprilTag) k??????k bir bilgi y??k?? vard??r (12 bit kadar), ancak ??ok d??????k ????z??n??rl??kte, e??it olmayan ??ekilde ayd??nlat??ld??????nda, garip bir ??ekilde d??nd??r??ld??????nde veya ba??ka bir ??ekilde k????eye s??k????t??r??ld??????nda bile otomatik olarak alg??lanacak ve konumland??r??lacak ??ekilde tasarlanm????t??r. G??rsel referans sistemleri belki de en iyi, ARToolkit ve ARTag dahil olmak ??zere bir??ok pop??ler sistemin geli??imini te??vik eden art??r??lm???? ger??ekli??e uygulamalar??yla bilinir. Ger??ek d??nyadaki nesneler, sanal olarak olu??turulmu?? g??r??nt??lerin ??st ??ste bindirilmesine izin vererek g??rsel referanslarla geni??letilebilir. Benzer ??ekilde, temel hareket yakalama i??in g??rsel referanslar kullan??labilir. Bu konu hakk??nda [daha fazla bilgi i??in](https://april.eecs.umich.edu/media/pdfs/olson2011tags.pdf).
*  Projemizde AprilTag3 kullan??yoruz. Bu ??al????ma, ??nceki AprilTag sistemine dayanmaktad??r. AprilTag'in kodlanm???? binary prensibe sahip siyah-beyaz kare etiket olarak tasar??m??, ??nceki ARTag ve ARToolkit'e dayanmaktad??r. AprilTag, binary elementler olu??turmak i??in geli??tirilmi?? bir y??ntem sunarak, etiketler aras??nda olas?? t??m d??n????lerde minimum Hamming mesafesini garanti ederek onlar?? ??nceki tasar??mlardan daha sa??lam hale getirdi. Minimum karma????kl??k heuristic y??ntemine sahip lexicode tabanl?? bir s??re?? olan etiket olu??turma s??recinin, benzer bit uzunlu??undaki ARTag tasar??mlar??na k??yasla yanl???? pozitif oran?? azaltt?????? deneysel olarak g??sterildi. Bu konu hakk??nda [daha fazla bilgi i??in](https://april.eecs.umich.edu/media/pdfs/wang2016iros.pdf).

## Peki biz projemizde ne yapt??k?
AprilTag ??zerinde ara??t??rmam??z?? yapt??ktan sonra projemize Raspberry Pi Zero ??zerinde devam etme karar?? ald??k. ??ncelikle Raspberry Pi i??in gerekli kurulumlar?? yaparak ba??lad??k. Bu a??amada kamera se??iminde zorland??k. ??nce kolayca ula??abildi??imiz telefon kameralar??n?? kullanmak istedik ama olmad??. Ayr??nt??lar ad??mlarda belirtilmi??tir. Raspberry ??zerinde gerekli kurulumlar yap??ld??ktan sonra AprilTag, Raspberry kameras?? kullan??larak test edilmi?? ve ba??ar??l?? bir ??ekilde tespit edildi??i g??zlemlenmi??tir. Ard??ndan temel 2WD ara?? kuruldu. Amac??m??z AprilTag kullanarak bu araca y??n vermek ve geli??tirme a??amas??nda arac??n, belirli bir s??rayla gelen etiketleri kullanarak istenilen noktaya ula??mas??n?? sa??lamakt??r. Bir sonraki ad??m, tagleri kullanarak bir i?? mekan ortam??nda haritalama yapmakt??r.
### Ad??m 0
??ncelikle giri?? b??l??m??nde bahsedilen makaleleri anlayarak ve ??zetleyerek ba??lad??k. Bu yaz??lar?? inceledikten sonra AprilTag'in github sayfas??n?? inceledik. Ve bu ad??mda, AprilTag hakk??nda ????rendiklerimizi ??zetledik.
### Ad??m 1
Bu ad??mda hangi bile??enleri ve neden kulland??????m??zdan bahsettik. Ba??lang????ta Windows'da ??al????may?? denedik ama ba??ar??s??z olduk. Ayn?? zamanda github sayfas??nda da belirtildi??i gibi Windows ??zerinde ba??ar??l?? olanlar olsa da Linux i??letim sistemleri desteklenmektedir.
### Ad??m 2
Bu ad??m, Raspberry Pi Zero ile nas??l ??al????abilece??inizi k??saca ??zetlemektedir. Ayr??ca AprilTag i??in gereken kurulumu ve ilk testinizi nas??l yapaca????n??z?? da a????klar.
### Ad??m 3 
Raspberry Pi kullan??larak olu??turulacak araban??n nas??l ba??lanaca???? ve test edilece??i bu b??l??mde anlat??lmaktad??r.
### Ad??m 4
AprilTag kullanarak araban??n nas??l y??nlendirilece??i bu ad??mda a????klanmaktad??r. Ayn?? zamanda taglerden al??nan bilgilerin i??lenme s??resi incelenir.

Not: ??al????malar??n sonucunda geli??tirilmeye devam edilmesi gereken bir repo ve ara?? olu??turmu?? olduk. Arac??n tag'leri tan??ma s??resindeki gecikmeden ??t??r?? kontroll?? bir ??ekilde ??al????mas?? hen??z sa??lanamad??. Ancak ara??t??rma s??reci devam etmektedir. E??er repoya ekleme yap??lmak isteniyorsa genel yap??ya uygun olacak ??ekilde yap??labilir. 

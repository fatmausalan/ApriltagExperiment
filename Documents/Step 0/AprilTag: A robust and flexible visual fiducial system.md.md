

## AprilTag: A robust and flexible visual fiducial system
  
  &emsp;AprilTags are unlike 2D barcode systems in which the position of the barcode in the image is unimportant, visual fiducial systems provide camera-relative position and orientation of a tag. Fiducial systems also are designed to detect multiple markers in a single image.
    
![image](https://user-images.githubusercontent.com/49456613/121807772-41ed6080-cc5e-11eb-9f83-43c6a475d455.png)  
Fig. 1. Example detections. This paper describes a visual fiducial system based on 2D planar targets. The detector is robust to lighting variation and occlusions and produces accurate localizations of the tags.
    

### Detector
  
  &emsp;In this section, we will examine the detector whose job is to estimate the position of possible tags in an image.
![Screenshot_10](https://user-images.githubusercontent.com/49456613/121805023-f2a13300-cc51-11eb-8ad9-4374cf5761b4.jpg)

1. Detecting line segments
  
  &emsp; A graph is created in which each node represents a pixel. Edges are added between adjacent pixels with an edge weight equal to the pixels’ difference in gradient direction. These edges are then sorted and processed in terms of increasing edge weight: for each edge, we test whether the connected components that the pixels belong to should be joined together. 
  &emsp;Gradient-based clustering method has used is sensitive to noise in the image: even modest amounts of noise will cause local gradient directions to vary, inhibiting the growth of the components. The solution to this problem is to low-pass filter the image.
  
  ![image](https://user-images.githubusercontent.com/49456613/121805136-7a873d00-cc52-11eb-8642-59b659e65f07.png)
    
  &emsp;Once the clustering operation is complete, line segments are fit to each connected component using a traditional least-squares procedure, weighting each point by its gradient magnitude (see Fig. 3). We adjust each line segment so that the dark side of the line is on its left, and the light side is on its right. In the next phase of processing, this allows us to enforce a winding rule around each quad.

2. Quad detection
  
  &emsp; At this point, a set of directed line segments have been computed for an image. The next task is to find sequences of line segments that form a 4-sided shape, i.e., a quad. The challenge is to do this while being as robust as possible to occlusions and noise in the line segmentations.
  &emsp; Once four lines have been found, a candidate quad detection is created. The corners of this quad are the intersections of the lines that comprise it. Because the lines are fit using data from many pixels, these corner estimates are accurate to a small fraction of a pixel.
  
3. Homography and extrinsics estimation
    
  &emsp; Computation of the tag’s position and orientation requires additional information: the camera’s focal length and the physical size of the tag. The 3 × 3 homography matrix (computed by the DLT (Direct Linear Transform)) can be written as the product of the 3 × 4 camera projection matrix P (which we assume is known) and the 4×3 truncated extrinsics matrix E. Extrinsics matrix are typically 4 × 4, but every position on the tag is at z = 0 in the tag’s coordinate system. Thus, we can rewrite every tag coordinate as a 2D homogeneous point with z implicitly zero, and remove the third column of the extrinsics matrix, forming the truncated extrinsics matrix.
  
### Payload Decoding
  &emsp; The final task is to read the bits from the payload field. We do this by computing the tag-relative coordinates of each bit field, transforming them into image coordinates using the homography, and then thresholding the resulting pixels. In order to be robust to lighting (which can vary not only from tag to tag, but also within a tag), we use a spatially-varying threshold.
  
  &emsp; Specifically, we build spatially-varying model of the intensity of “black” pixels, and a second model for the intensity of “white” models. We use the border of the tag, which contains known examples of both white and black pixels, to learn this model (see Fig. 4). We use the following intensity model:
    
  &emsp; &emsp; I(x, y) = Ax + Bxy + Cy + D (4)
    
    
  &emsp; This model has four parameters which are easily computed using least squares regression. We build two such models, one for black, the other for white. The threshold used when decoding data bits is then just the average of the predicted intensity values of the black and white models.


### Coding System
  &emsp; Once the data payload is decoded from a quad, it is the job of the coding system to determine it is valid or not. The goals of a coding system are to:
      
    - Maximize the number of distinguishable codes  
    - Maximize the number of bit errors that can be detected or corrected
    - Minimize the false positive/inter-tag confusion rate
    - Minimize the total number of bits per tag (and thus the size of the tag)
  &emsp; These goals are often in conflict, and so a given code represents a trade-off. In this section, we describe a new coding system based on lexicodes that provides significant advantages over previous methods. Our procedure can generate lexicodes with a variety of properties, allowing the user to use a code that best fits their needs.
  
### Conclusion

  We have described a visual fiducial system that significantly improves upon previous methods. We described a new approach for detecting edges using a graph-based clustering method along with a coding system that is demonstrably stronger than previous methods.
    
  &emsp; In contrast to other systems (with the notable exception of ARToolkit), our implementation is fully open. Our source code and benchmarking software are freely available:
  
  http://april.eecs.umich.edu/
  
  
## References 
* https://april.eecs.umich.edu/media/pdfs/olson2011tags.pdf



  
## AprilTag: Sağlam ve esnek bir görsel referans sistem
  
  &emsp; AprilTags, barkodun görüntüdeki konumunun önemsiz olduğu 2D barkod sistemlerinden farklıdır, görsel referans sistemleri, bir etiketin kameraya göre konumunu ve yönünü sağlar. Fiducial sistemleri ayrıca tek bir görüntüde birden fazla işaretleyiciyi tespit etmek için tasarlanmıştır.  
  ![image](https://user-images.githubusercontent.com/49456613/121807772-41ed6080-cc5e-11eb-9f83-43c6a475d455.png)  
  Şekil 1. Örnek tespitler. Bu makale, 2B düzlemsel hedeflere dayalı görsel bir referans sistemi açıklamaktadır. Dedektör, aydınlatma varyasyonlarına ve tıkanıklıklara karşı dayanıklıdır ve etiketlerin doğru lokalizasyonlarını üretir.

  
### Algılayıcı  
  &emsp; Bu bölümde, işi bir görüntüdeki olası etiketlerin konumunu tahmin etmek olan dedektörü inceleyeceğiz.  
  ![image](https://user-images.githubusercontent.com/49456613/121807935-e8396600-cc5e-11eb-8723-cc9e813855c6.png)  
  Şekil 3. Erken işleme adımları. Etiket algılama algoritması, her pikseldeki gradyanı hesaplayarak, büyüklüklerini (birinci) ve yönünü (ikinci) hesaplayarak başlar. Grafiğe dayalı bir yöntem kullanılarak, benzer gradyan yönlerine ve büyüklüğüne sahip pikseller, bileşenler halinde kümelenir (üçüncü). Ağırlıklı en küçük kareler kullanılarak, her bileşendeki (dördüncü) piksellere bir çizgi parçası sığdırılır. Doğru parçasının yönü, gradyan yönü ile belirlenir, böylece bölümler solda karanlık, sağda açık olur. Çizgilerin yönü, orta noktalarında kısa dikey “çentikler” ile görselleştirilir; bu "çentiklerin" her zaman daha açık olan bölgeyi gösterdiğine dikkat edin.  
  
1. Çizgi segmentlerini tespit etme
  
  &emsp; Her düğümün bir pikseli temsil ettiği bir grafik oluşturulur. Kenarlar, piksellerin gradyan yönündeki farkına eşit bir kenar ağırlığına sahip bitişik pikseller arasına eklenir. Bu kenarlar daha sonra artan kenar ağırlığına göre sıralanır ve işlenir: her kenar için piksellerin ait olduğu bağlı bileşenlerin bir araya getirilmesi gerekip gerekmediğini test ederiz. 
  &emsp; Gradyan tabanlı kümeleme yönteminin kullandığı görüntüdeki gürültüye duyarlıdır: küçük miktarlardaki gürültü bile, bileşenlerin büyümesini engelleyerek yerel gradyan yönlerinin değişmesine neden olur. Bu sorunun çözümü, görüntüyü alçak geçiren filtre uygulamaktır.  
  
  ![image](https://user-images.githubusercontent.com/49456613/121808008-53833800-cc5f-11eb-9103-53b146e853fd.png)  
    
  &emsp;Kümeleme işlemi tamamlandıktan sonra, çizgi parçaları, her noktayı gradyan büyüklüğüne göre ağırlıklandıran geleneksel bir en küçük kareler prosedürü kullanılarak her bağlı bileşene uydurulur. Her çizgi parçasını, çizginin karanlık tarafı solunda ve aydınlık tarafı sağında olacak şekilde ayarlıyoruz. İşlemin bir sonraki aşamasında, bu, her dörtlü etrafında bir sarma kuralı uygulamamızı sağlar.  
  
2. Quad tespiti
  
  &emsp; Bu noktada, bir görüntü için bir dizi yönlendirilmiş çizgi parçası hesaplanmıştır. Bir sonraki görev, 4 kenarlı bir şekil, yani bir dörtlü(quad) oluşturan doğru parçalarının dizilerini bulmaktır. Buradaki zorluk, çizgi segmentasyonlarındaki tıkanıklıklara ve gürültüye karşı mümkün olduğunca sağlam olurken bunu yapmaktır.  
  &emsp; Dört satır bulunduğunda, bir aday dörtlü algılama oluşturulur. Bu dörtlünün köşeleri, onu oluşturan çizgilerin kesişme noktalarıdır. Çizgiler, birçok pikselden alınan veriler kullanılarak sığdırıldığından, bu köşe tahminleri, pikselin küçük bir bölümü için doğrudur.  
  
3. Homografi ve dışsal tahmin
    
  &emsp; Etiketin konumunun ve yönünün hesaplanması ek bilgi gerektirir: kameranın odak uzaklığı ve etiketin fiziksel boyutu. 3 × 3 homografi matrisi (DLT (Doğrudan Doğrusal Dönüşüm) ile hesaplanır) 3 × 4 kamera projeksiyon matrisi P (ki bunun bilindiğini varsayıyoruz) ve 4×3 kesik dışsal matris E'nin çarpımı olarak yazılabilir. matris tipik olarak 4 × 4'tür, ancak etiket üzerindeki her konum, etiketin koordinat sisteminde z = 0'dadır. Böylece, her etiket koordinatını, z örtük olarak sıfır olan bir 2B homojen nokta olarak yeniden yazabilir ve dışsal matrisin üçüncü sütununu kaldırarak, kesik dışsal matrisi oluşturabiliriz.
  
### Yük Kodu Çözme  
  &emsp; Son görev, faydalı yük alanındaki bitleri okumaktır. Bunu, her bit alanının etikete göre koordinatlarını hesaplayarak, homografiyi kullanarak bunları görüntü koordinatlarına dönüştürerek ve ardından ortaya çıkan pikselleri eşikleyerek yapıyoruz. Aydınlatmaya karşı dayanıklı olmak için (bu sadece etiketten etikete değil, aynı zamanda bir etiket içinde de değişebilir), uzamsal olarak değişen bir eşik kullanırız.  
  
  &emsp; Spesifik olarak, "siyah" piksellerin yoğunluğunun uzamsal olarak değişen modelini ve "beyaz" modellerin yoğunluğunun ikinci bir modelini oluşturuyoruz. Bu modeli öğrenmek için hem beyaz hem de siyah piksellerin bilinen örneklerini içeren etiketin kenarlığını kullanıyoruz (bkz. Şekil 4). Aşağıdaki yoğunluk modelini kullanıyoruz:  
    
  &emsp; &emsp; I(x, y) = Ax + Bxy + Cy + D  
    
    
  &emsp; Bu model, en küçük kareler regresyonu kullanılarak kolayca hesaplanan dört parametreye sahiptir. Biri siyah, diğeri beyaz olmak üzere iki model yapıyoruz. Veri bitlerinin kodunu çözerken kullanılan eşik, siyah beyaz modellerin tahmin edilen yoğunluk değerlerinin yalnızca ortalamasıdır.  
  
### Kodlama Sistemi
  &emsp; Veri yükünün kodu bir dörtlüden çözüldüğünde, bunun geçerli olup olmadığını belirlemek kodlama sisteminin işidir. Bir kodlama sisteminin amaçları şunlardır:
      
    - Ayırt edilebilir kodların sayısını en üst düzeye çıkarma  
    - Tespit edilebilecek veya düzeltilebilecek bit hatalarının sayısını en üst düzeye çıkarma
    - Yanlış pozitif/etiketler arası karışıklık oranını en aza indirgeme
    - Etiket başına toplam bit sayısını (ve dolayısıyla etiketin boyutunu) en aza indirme
    
  &emsp; Bu hedefler genellikle çatışır ve bu nedenle belirli bir kod bir takası temsil eder. Bu bölümde, önceki yöntemlere göre önemli avantajlar sağlayan sözlük kodlarına dayalı yeni bir kodlama sistemi anlatılmaktadır. Prosedürümüz, kullanıcının ihtiyaçlarına en uygun kodu kullanmasına izin vererek, çeşitli özelliklere sahip sözlük kodları üretebilir.  
  
### Sonuç  

  Önceki yöntemleri önemli ölçüde geliştiren görsel bir referans sistemi tanımladık. Önceki yöntemlerden belirgin şekilde daha güçlü olan bir kodlama sistemi ile birlikte grafik tabanlı bir kümeleme yöntemi kullanarak kenarları algılamak için yeni bir yaklaşım tanımladık.  
    
  &emsp; Diğer sistemlerin aksine (ARToolkit'in dikkate değer istisnası dışında), uygulama tamamen açıktır. Kaynak kod ve kıyaslama yazılımı ücretsiz olarak mevcuttur:  
  
  http://april.eecs.umich.edu/
  
  
## Kaynakça 
* https://april.eecs.umich.edu/media/pdfs/olson2011tags.pdf

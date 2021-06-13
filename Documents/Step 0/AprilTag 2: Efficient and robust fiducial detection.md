## AprilTag 2: Efficient and robust fiducial detection
  
  Fiducials are artificial visual features designed for automatic detection, and often carry a unique payload to make them distinguishable from each other. Although these types of fiducials were first developed and popularized by augmented reality applications [1], [2], they have since been widely adopted by the robotics community. Their uses range from ground truthing to object detection and tracking, where they can be used as a simplifying assumption in lieu of more sophisticated perception.
  
### Prior Work
  
  ![image](https://user-images.githubusercontent.com/49456613/121806236-c25c9300-cc57-11eb-9661-7d5a27a7bf1d.png)
  
  Fig. 2: A comparison of visual fiducial tags. ARToolkit tags allow arbitrary pixel patterns inside the black border, while ARTags and AprilTags use 2D binary codes. RUNE-tags and reacTIVision markers are two different existing approaches to fiducial markers.

### Tag Detector
  
  Our system features an improved quad detector which finds candidate tags in a grayscale image. Each candidate is then decoded to determine if they are valid AprilTag detections. The method leads to fewer false positives than the previous state of the art detector while reliably detecting valid unoccluded quads, contributing to an overall lower false positive rate.

  1. Lessons Learned  
  &emsp; The improvements to the tag detector were inspired by user feedback about common use cases. We learned that in most deployments, detection of partially occluded tags is of limited utility. Occluded tags often have one or more bit errors, and most users disable decoding of tags with bit errors due to the impact on false positive rates. No known users accept tags with more than two bit errors, which enables a faster decode algorithm. In our experience, the increased detection speed is a favorable tradeoff against the ability to recover partially occluded tag borders.
  
  2. Adaptive thresholding  
  &emsp; The first step is to threshold the grayscale input image into a black-and-white image. Some thresholding methods attempt to find a global threshold value for the entire image [13], while others find local or adaptive thresholds [14]. We adopt an adaptive thresholding approach, where the idea is to find the minimum and maximum values in a region around each pixel.
  ![image](https://user-images.githubusercontent.com/49456613/121806700-a0fca680-cc59-11eb-8352-ec7abe0d28e6.png)  
  Fig. 3: Intermediate steps of the AprilTag detector. The input image (a) is binarized using adaptive thresholding (b). The
connected black and white regions are segmented into connected components (c). Component boundaries are segmented
using a novel algorithm, which efficiently clusters pixels which border the same black and white region. Finally, quads are
fit to each cluster of border pixels (d), poor quad fits and undecodable tags are discarded, and valid tag detections are output
(e)

  3.  Continuous boundary segmentation  
  &emsp; Given the binarized image, the next step is to find edges which might form the boundary of a tag. A straightforward approach is to identify edge pixels which have an oppositecolored neighbor, then form connected groups of edge pixels. However, this approach breaks down when the white space between tag boundaries approaches only a single pixel wide, which may happen for physically small or faraway tags. If two tag boundaries are incorrectly merged, the tags will not be detected. Our proposed solution is to segment the edges based on the identities of the black and white components from which they arise.

  4. Fitting quads  
  &emsp; First the points are sorted by angle in a consistent winding order around their centroid. This ordering allows us to define “neighboring points” as ranges of sorted points. Cumulative first and second moment statistics are computed in a single pass through these points, enabling the first and second moments to be computed for any range of points in constant time.  
  &emsp; Corner points are identified by attempting to fit a line to windows of neighboring points, and finding the peaks in the mean squared error function as the window is swept across the points. Line fits are computed using principal component analysis (PCA), in which an ellipse is fit to the sample mean and covariance. The best fit line is the eigenvector corresponding to the first principal component. Using the precomputed statistics, all the candidate line fits may be computed in O(n) time, where n is the number of points. The strongest peaks in the mean squared error are identified as candidate corners.  
  &emsp; Finally, we iterate through all permutations of four candidate corners, fitting lines to each side of the candidate quad. At this step we select the four corners which result in the smallest mean squared line fit errors. Prefiltering is performed to reject poor quad fits, such as those without at least four corners, whose mean squared errors are too large, or whose corner angles deviate too far from 90◦.

  5. Quick decoding  
  &emsp; The idea is to use the image gradient along the edges of the candidate quads to fit new edges, approximating the behavior of the original AprilTag detector. Along each edge, at evenly-spaced sample points, we sample the image gradient along the normal to the edge to find the location with the largest gradient. Knowing tags are dark on the inside and the winding order of the points in the quad, we reject points whose gradient is not the expected sign (i.e. from noisy individual pixels). We compute a weighted average of the points along the normal, weighted by the gradient magnitude. The line fit along these weighted average points are then used as the edges of the quad. The quad corners are computed as the intersections of these lines.  
  &emsp; A straightforward approach to decoding tags is to XOR the detected code (in each of its four possible rotations) with each the codes in a tag family. A tag is identified as the code with the smallest Hamming distance from the detected code. However, if we limit the number of bit errors corrected to two bits or fewer, it is possible to enumerate all O(n^2) possible codes within two bit errors of valid codes in a tag family. These codes can be precomputed and stored in a hash table, speeding up decoding from O(n) comparisons to O(1), where n is the size of the tag family.  
  
  6. Edge refinement  
  &emsp; Edge refinement is not crucial if one is only interested in detecting tags, although it can help with the decoding of very small tags. However, the edge refinement step improves localization accuracy when tags are used for pose estimation.  
      
  ![image](https://user-images.githubusercontent.com/49456613/121807439-d5be2d00-cc5c-11eb-8ace-da6d59508ade.png)  
  Fig. 8: AprilTag mosaic for distance test on real images. Images were taken with a Point Grey Chameleon at 1296 x 964 pixels, and each tag is 0.167m wide. This experiment shows that the tag detection and localization performance observed in simulated images translates to real imagery. (Rectification was performed before tag detection and localization.)

### Conclusion  
&emsp; This paper describes a new AprilTag detection algorithm which improves upon the previous detector, reducing the rate of false positives, increasing the detection rate, and reducing the amount of computing time needed for detection. These improvements make robust tag detection viable on computation-limited systems such as smartphones, and extends the usefulness of tag tracking in real-time applications. A free AprilTag detector app is available in the iPhone App Store.

## References  
* https://april.eecs.umich.edu/media/pdfs/wang2016iros.pdf
  
 
## AprilTag 2: Verimli ve sağlam referans algılama
  
  Referans değerleri, otomatik algılama için tasarlanmış yapay görsel özelliklerdir ve genellikle birbirlerinden ayırt edilebilmeleri için benzersiz bir yük taşırlar. Bu tür referanslar ilk olarak artırılmış gerçeklik uygulamaları [1], [2] tarafından geliştirilmiş ve popüler hale getirilmiş olsa da, o zamandan beri robotik topluluğu tarafından geniş çapta benimsenmiştir. Kullanımları, daha karmaşık algılama yerine basitleştirici bir varsayım olarak kullanılabilecekleri, temel doğrulamadan nesne algılama ve izlemeye kadar uzanır.
  
 ### Önceki Çalışmalar
 
   ![image](https://user-images.githubusercontent.com/49456613/121806245-c5578380-cc57-11eb-8480-1b9fa38551f3.png)
   
   Şekil 2: Görsel referans etiketlerinin karşılaştırması. ARToolkit etiketleri siyah kenarlık içinde rastgele piksel desenlerine izin verirken, ARTag'ler ve AprilTag'ler 2B ikili kodlar kullanır. RUNE etiketleri ve reacTIVision belirteçleri, referans belirteçlerine yönelik mevcut iki farklı yaklaşımdır.

### Tag Algılayıcı
  
  Sistemimiz, gri tonlamalı bir görüntüde aday etiketleri bulan gelişmiş bir dörtlü dedektöre sahiptir. Daha sonra, geçerli AprilTag algılamaları olup olmadığını belirlemek için her aday tagin kodu çözülür. Yöntem, önceki son teknoloji ürünü dedektöre göre daha az hatalı pozitife yol açarken, geçerli kapatılmamış dörtlüleri güvenilir bir şekilde tespit ederek genel olarak daha düşük bir hatalı pozitif oranına katkıda bulunur.
  
  1. Çıkarılan Dersler  
    &emsp; Etiket algılayıcıdaki iyileştirmeler, yaygın kullanım durumları hakkındaki kullanıcı geri bildirimlerinden ilham almıştır. Çoğu dağıtımda, kısmen tıkanmış etiketlerin algılanmasının sınırlı fayda sağladığını öğrendik. Tıkalı etiketler genellikle bir veya daha fazla bit hatasına sahiptir ve çoğu kullanıcı, yanlış pozitif oranlar üzerindeki etkisinden dolayı bit hataları olan etiketlerin kodunun çözülmesini devre dışı bırakır. Bilinen hiçbir kullanıcı, daha hızlı bir kod çözme algoritması sağlayan iki bitten fazla hata içeren etiketleri kabul etmez. Deneyimlerimize göre, artan algılama hızı, kısmen tıkanmış etiket sınırlarını kurtarma yeteneğine karşı olumlu bir ödünleşimdir.
    
  2. Uyarlanabilir Eşikleme  
    &emsp; İlk adım, gri tonlamalı giriş görüntüsünü siyah beyaz bir görüntüye eşlemektir. Bazı eşikleme yöntemleri, tüm görüntü için genel bir eşik değeri bulmaya çalışırken [13], diğerleri yerel veya uyarlanabilir eşikler bulur [14]. Her pikselin etrafındaki bir bölgedeki minimum ve maksimum değerleri bulmak olan uyarlanabilir bir eşikleme yaklaşımı benimsiyoruz.
    ![image](https://user-images.githubusercontent.com/49456613/121806700-a0fca680-cc59-11eb-8352-ec7abe0d28e6.png)   
    Şekil 3: AprilTag dedektörünün ara adımları. Giriş görüntüsü (a), uyarlamalı eşikleme (b) kullanılarak ikili hale getirilir. Bağlı siyah ve beyaz bölgeler, bağlı bileşenlere (c) bölünür. Bileşen sınırları, aynı siyah beyaz bölgeyi sınırlayan pikselleri verimli bir şekilde kümeleyen yeni bir algoritma kullanılarak bölümlere ayrılır. Son olarak, dörtlüler her kenar piksel kümesine sığdırılır (d), zayıf dörtlü uyumlar ve kodu çözülemeyen etiketler atılır ve geçerli etiket algılamaları çıktılanır (e)
    
  3. Kenar Segmentasyonu  
    &emsp; İkilileştirilmiş görüntü göz önüne alındığında, bir sonraki adım, bir etiketin sınırını oluşturabilecek kenarları bulmaktır. Basit bir yaklaşım, zıt renkli bir komşuya sahip olan kenar piksellerini belirlemek ve ardından bağlantılı kenar piksel grupları oluşturmaktır. Bununla birlikte, bu yaklaşım, etiket sınırları arasındaki beyaz boşluk, fiziksel olarak küçük veya uzaktaki etiketler için olabilen, yalnızca tek bir piksel genişliğine yaklaştığında bozulur. İki etiket sınırı hatalı bir şekilde birleştirilirse, etiketler algılanmayacaktır. Önerilen çözümümüz, ortaya çıktıkları siyah ve beyaz bileşenlerin kimliklerine dayalı olarak kenarları bölümlere ayırmaktır. 
    
  4. Quadları uyumlama  
    &emsp; İlk önce noktalar, ağırlık merkezlerinin etrafında tutarlı bir sarma düzeninde açılarına göre sıralanır. Bu sıralama, "komşu noktaları" sıralanmış noktaların aralıkları olarak tanımlamamızı sağlar. Kümülatif birinci ve ikinci an istatistikleri, bu noktalardan tek bir geçişte hesaplanır ve sabit zamanda herhangi bir nokta aralığı için birinci ve ikinci anların hesaplanmasını sağlar.  
    &emsp; Köşe noktaları, komşu noktaların pencerelerine bir çizgi sığdırmaya çalışılarak ve pencere noktalar boyunca süpürülürken ortalama kare hata fonksiyonundaki tepe noktaları bulunarak tanımlanır. Çizgi uyumu, bir elipsin numune ortalamasına ve kovaryansa uygun olduğu temel bileşen analizi (PCA) kullanılarak hesaplanır. En uygun doğru, birinci ana bileşene karşılık gelen özvektördür. Önceden hesaplanmış istatistikler kullanılarak, tüm aday çizgi uyumu O(n) zamanında hesaplanabilir, burada n nokta sayısıdır. Ortalama kare hatasındaki en güçlü tepe noktaları aday köşeler olarak tanımlanır.  
    &emsp; Son olarak, dört aday köşenin tüm permütasyonlarını yineliyoruz, aday dörtlü'nün her iki tarafına çizgiler uyduruyoruz. Bu adımda, en küçük ortalama kare çizgi sığdırma hatalarıyla sonuçlanan dört köşeyi seçiyoruz. Ön filtreleme, en az dört köşesi olmayan, ortalama kare hataları çok büyük olan veya köşe açıları 90°'den çok sapanlar gibi zayıf dörtlü uyumu reddetmek için gerçekleştirilir.
    
  5. Hızlı çözümleme  
    &emsp; Etiketlerin kodunu çözmeye yönelik basit bir yaklaşım, algılanan kodu (olası dört rotasyonunun her birinde) bir etiket ailesindeki her bir kodla XOR yapmaktır. Bir etiket, tespit edilen koddan en küçük Hamming mesafesine sahip kod olarak tanımlanır. Bununla birlikte, düzeltilen bit hatalarının sayısını iki veya daha az bit ile sınırlarsak, bir etiket ailesindeki geçerli kodların iki bitlik hataları içinde olası tüm O(n^2) olası kodları numaralandırmak mümkündür. Bu kodlar önceden hesaplanabilir ve bir karma tablosunda saklanabilir, bu da O(n) karşılaştırmalarından O(1)'e kod çözmeyi hızlandırır, burada n etiket ailesinin boyutudur.
    
  6. Kenar İyileştirme  
    &emsp; Buradaki fikir, orijinal AprilTag dedektörünün davranışına yaklaşarak yeni kenarlara sığdırmak için aday dörtlülerin kenarları boyunca görüntü gradyanını kullanmaktır. Her kenar boyunca, eşit aralıklı örnek noktalarında, en büyük gradyanlı konumu bulmak için normalden kenara doğru görüntü gradyanını örnekliyoruz. Etiketlerin iç kısımlarının karanlık olduğunu ve dörtlüdeki noktaların sarma sırasını bilerek, gradyanı beklenen işaret olmayan noktaları (yani gürültülü bireysel piksellerden) reddederiz. Gradyan büyüklüğü ile ağırlıklandırılmış, normal boyunca noktaların ağırlıklı ortalamasını hesaplıyoruz. Bu ağırlıklı ortalama noktalar boyunca geçen çizgi, daha sonra dörtlü kenarları olarak kullanılır. Dört köşeler bu çizgilerin kesişim noktaları olarak hesaplanır.  
    &emsp; Çok küçük etiketlerin kodunun çözülmesine yardımcı olabilmesine rağmen, yalnızca etiketleri algılamakla ilgileniyorsanız, kenar iyileştirme çok önemli değildir. Bununla birlikte, kenar iyileştirme adımı, poz tahmini için etiketler kullanıldığında yerelleştirme doğruluğunu artırır.  
      
  ![image](https://user-images.githubusercontent.com/49456613/121807456-e2428580-cc5c-11eb-8fab-09bb75f88ad0.png)  
  Şekil 8: Gerçek görüntüler üzerinde mesafe testi için AprilTag mozaiği. Görüntüler Nokta Grisi Bukalemun ile 1296 x 964 pikselde çekildi ve her bir etiket 0.167m genişliğinde. Bu deney, simüle edilmiş görüntülerde gözlemlenen etiket algılama ve yerelleştirme performansının gerçek görüntülere dönüştüğünü göstermektedir. (Rektifikasyon, etiket tespiti ve lokalizasyonundan önce yapılmıştır.)

  
### Sonuç  
&emsp; Bu belge, önceki dedektörü geliştiren, yanlış pozitiflerin oranını azaltan, algılama oranını artıran ve algılama için gereken hesaplama süresini azaltan yeni bir AprilTag algılama algoritmasını açıklamaktadır. Bu iyileştirmeler, akıllı telefonlar gibi hesaplama sınırlı sistemlerde sağlam etiket algılamayı mümkün kılar ve gerçek zamanlı uygulamalarda etiket izlemenin kullanışlılığını genişletir. iPhone App Store'da ücretsiz bir AprilTag dedektör uygulaması mevcuttur.  
  
## Kaynakça  
* https://april.eecs.umich.edu/media/pdfs/wang2016iros.pdf

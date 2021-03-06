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
  &emsp; First the points are sorted by angle in a consistent winding order around their centroid. This ordering allows us to define ???neighboring points??? as ranges of sorted points. Cumulative first and second moment statistics are computed in a single pass through these points, enabling the first and second moments to be computed for any range of points in constant time.  
  &emsp; Corner points are identified by attempting to fit a line to windows of neighboring points, and finding the peaks in the mean squared error function as the window is swept across the points. Line fits are computed using principal component analysis (PCA), in which an ellipse is fit to the sample mean and covariance. The best fit line is the eigenvector corresponding to the first principal component. Using the precomputed statistics, all the candidate line fits may be computed in O(n) time, where n is the number of points. The strongest peaks in the mean squared error are identified as candidate corners.  
  &emsp; Finally, we iterate through all permutations of four candidate corners, fitting lines to each side of the candidate quad. At this step we select the four corners which result in the smallest mean squared line fit errors. Prefiltering is performed to reject poor quad fits, such as those without at least four corners, whose mean squared errors are too large, or whose corner angles deviate too far from 90???.

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
  
 
## AprilTag 2: Verimli ve sa??lam referans alg??lama
  
  Referans de??erleri, otomatik alg??lama i??in tasarlanm???? yapay g??rsel ??zelliklerdir ve genellikle birbirlerinden ay??rt edilebilmeleri i??in benzersiz bir y??k ta????rlar. Bu t??r referanslar ilk olarak art??r??lm???? ger??eklik uygulamalar?? [1], [2] taraf??ndan geli??tirilmi?? ve pop??ler hale getirilmi?? olsa da, o zamandan beri robotik toplulu??u taraf??ndan geni?? ??apta benimsenmi??tir. Kullan??mlar??, daha karma????k alg??lama yerine basitle??tirici bir varsay??m olarak kullan??labilecekleri, temel do??rulamadan nesne alg??lama ve izlemeye kadar uzan??r.
  
 ### ??nceki ??al????malar
 
   ![image](https://user-images.githubusercontent.com/49456613/121806245-c5578380-cc57-11eb-8480-1b9fa38551f3.png)
   
   ??ekil 2: G??rsel referans etiketlerinin kar????la??t??rmas??. ARToolkit etiketleri siyah kenarl??k i??inde rastgele piksel desenlerine izin verirken, ARTag'ler ve AprilTag'ler 2B ikili kodlar kullan??r. RUNE etiketleri ve reacTIVision belirte??leri, referans belirte??lerine y??nelik mevcut iki farkl?? yakla????md??r.

### Tag Alg??lay??c??
  
  Sistemimiz, gri tonlamal?? bir g??r??nt??de aday etiketleri bulan geli??mi?? bir d??rtl?? dedekt??re sahiptir. Daha sonra, ge??erli AprilTag alg??lamalar?? olup olmad??????n?? belirlemek i??in her aday tagin kodu ????z??l??r. Y??ntem, ??nceki son teknoloji ??r??n?? dedekt??re g??re daha az hatal?? pozitife yol a??arken, ge??erli kapat??lmam???? d??rtl??leri g??venilir bir ??ekilde tespit ederek genel olarak daha d??????k bir hatal?? pozitif oran??na katk??da bulunur.
  
  1. ????kar??lan Dersler  
    &emsp; Etiket alg??lay??c??daki iyile??tirmeler, yayg??n kullan??m durumlar?? hakk??ndaki kullan??c?? geri bildirimlerinden ilham alm????t??r. ??o??u da????t??mda, k??smen t??kanm???? etiketlerin alg??lanmas??n??n s??n??rl?? fayda sa??lad??????n?? ????rendik. T??kal?? etiketler genellikle bir veya daha fazla bit hatas??na sahiptir ve ??o??u kullan??c??, yanl???? pozitif oranlar ??zerindeki etkisinden dolay?? bit hatalar?? olan etiketlerin kodunun ????z??lmesini devre d?????? b??rak??r. Bilinen hi??bir kullan??c??, daha h??zl?? bir kod ????zme algoritmas?? sa??layan iki bitten fazla hata i??eren etiketleri kabul etmez. Deneyimlerimize g??re, artan alg??lama h??z??, k??smen t??kanm???? etiket s??n??rlar??n?? kurtarma yetene??ine kar???? olumlu bir ??d??nle??imdir.
    
  2. Uyarlanabilir E??ikleme  
    &emsp; ??lk ad??m, gri tonlamal?? giri?? g??r??nt??s??n?? siyah beyaz bir g??r??nt??ye e??lemektir. Baz?? e??ikleme y??ntemleri, t??m g??r??nt?? i??in genel bir e??ik de??eri bulmaya ??al??????rken [13], di??erleri yerel veya uyarlanabilir e??ikler bulur [14]. Her pikselin etraf??ndaki bir b??lgedeki minimum ve maksimum de??erleri bulmak olan uyarlanabilir bir e??ikleme yakla????m?? benimsiyoruz.
    ![image](https://user-images.githubusercontent.com/49456613/121806700-a0fca680-cc59-11eb-8352-ec7abe0d28e6.png)   
    ??ekil 3: AprilTag dedekt??r??n??n ara ad??mlar??. Giri?? g??r??nt??s?? (a), uyarlamal?? e??ikleme (b) kullan??larak ikili hale getirilir. Ba??l?? siyah ve beyaz b??lgeler, ba??l?? bile??enlere (c) b??l??n??r. Bile??en s??n??rlar??, ayn?? siyah beyaz b??lgeyi s??n??rlayan pikselleri verimli bir ??ekilde k??meleyen yeni bir algoritma kullan??larak b??l??mlere ayr??l??r. Son olarak, d??rtl??ler her kenar piksel k??mesine s????d??r??l??r (d), zay??f d??rtl?? uyumlar ve kodu ????z??lemeyen etiketler at??l??r ve ge??erli etiket alg??lamalar?? ????kt??lan??r (e)
    
  3. Kenar Segmentasyonu  
    &emsp; ??kilile??tirilmi?? g??r??nt?? g??z ??n??ne al??nd??????nda, bir sonraki ad??m, bir etiketin s??n??r??n?? olu??turabilecek kenarlar?? bulmakt??r. Basit bir yakla????m, z??t renkli bir kom??uya sahip olan kenar piksellerini belirlemek ve ard??ndan ba??lant??l?? kenar piksel gruplar?? olu??turmakt??r. Bununla birlikte, bu yakla????m, etiket s??n??rlar?? aras??ndaki beyaz bo??luk, fiziksel olarak k??????k veya uzaktaki etiketler i??in olabilen, yaln??zca tek bir piksel geni??li??ine yakla??t??????nda bozulur. ??ki etiket s??n??r?? hatal?? bir ??ekilde birle??tirilirse, etiketler alg??lanmayacakt??r. ??nerilen ????z??m??m??z, ortaya ????kt??klar?? siyah ve beyaz bile??enlerin kimliklerine dayal?? olarak kenarlar?? b??l??mlere ay??rmakt??r. 
    
  4. Quadlar?? uyumlama  
    &emsp; ??lk ??nce noktalar, a????rl??k merkezlerinin etraf??nda tutarl?? bir sarma d??zeninde a????lar??na g??re s??ralan??r. Bu s??ralama, "kom??u noktalar??" s??ralanm???? noktalar??n aral??klar?? olarak tan??mlamam??z?? sa??lar. K??m??latif birinci ve ikinci an istatistikleri, bu noktalardan tek bir ge??i??te hesaplan??r ve sabit zamanda herhangi bir nokta aral?????? i??in birinci ve ikinci anlar??n hesaplanmas??n?? sa??lar.  
    &emsp; K????e noktalar??, kom??u noktalar??n pencerelerine bir ??izgi s????d??rmaya ??al??????larak ve pencere noktalar boyunca s??p??r??l??rken ortalama kare hata fonksiyonundaki tepe noktalar?? bulunarak tan??mlan??r. ??izgi uyumu, bir elipsin numune ortalamas??na ve kovaryansa uygun oldu??u temel bile??en analizi (PCA) kullan??larak hesaplan??r. En uygun do??ru, birinci ana bile??ene kar????l??k gelen ??zvekt??rd??r. ??nceden hesaplanm???? istatistikler kullan??larak, t??m aday ??izgi uyumu O(n) zaman??nda hesaplanabilir, burada n nokta say??s??d??r. Ortalama kare hatas??ndaki en g????l?? tepe noktalar?? aday k????eler olarak tan??mlan??r.  
    &emsp; Son olarak, d??rt aday k????enin t??m perm??tasyonlar??n?? yineliyoruz, aday d??rtl??'n??n her iki taraf??na ??izgiler uyduruyoruz. Bu ad??mda, en k??????k ortalama kare ??izgi s????d??rma hatalar??yla sonu??lanan d??rt k????eyi se??iyoruz. ??n filtreleme, en az d??rt k????esi olmayan, ortalama kare hatalar?? ??ok b??y??k olan veya k????e a????lar?? 90??'den ??ok sapanlar gibi zay??f d??rtl?? uyumu reddetmek i??in ger??ekle??tirilir.
    
  5. H??zl?? ????z??mleme  
    &emsp; Etiketlerin kodunu ????zmeye y??nelik basit bir yakla????m, alg??lanan kodu (olas?? d??rt rotasyonunun her birinde) bir etiket ailesindeki her bir kodla XOR yapmakt??r. Bir etiket, tespit edilen koddan en k??????k Hamming mesafesine sahip kod olarak tan??mlan??r. Bununla birlikte, d??zeltilen bit hatalar??n??n say??s??n?? iki veya daha az bit ile s??n??rlarsak, bir etiket ailesindeki ge??erli kodlar??n iki bitlik hatalar?? i??inde olas?? t??m O(n^2) olas?? kodlar?? numaraland??rmak m??mk??nd??r. Bu kodlar ??nceden hesaplanabilir ve bir karma tablosunda saklanabilir, bu da O(n) kar????la??t??rmalar??ndan O(1)'e kod ????zmeyi h??zland??r??r, burada n etiket ailesinin boyutudur.
    
  6. Kenar ??yile??tirme  
    &emsp; Buradaki fikir, orijinal AprilTag dedekt??r??n??n davran??????na yakla??arak yeni kenarlara s????d??rmak i??in aday d??rtl??lerin kenarlar?? boyunca g??r??nt?? gradyan??n?? kullanmakt??r. Her kenar boyunca, e??it aral??kl?? ??rnek noktalar??nda, en b??y??k gradyanl?? konumu bulmak i??in normalden kenara do??ru g??r??nt?? gradyan??n?? ??rnekliyoruz. Etiketlerin i?? k??s??mlar??n??n karanl??k oldu??unu ve d??rtl??deki noktalar??n sarma s??ras??n?? bilerek, gradyan?? beklenen i??aret olmayan noktalar?? (yani g??r??lt??l?? bireysel piksellerden) reddederiz. Gradyan b??y??kl?????? ile a????rl??kland??r??lm????, normal boyunca noktalar??n a????rl??kl?? ortalamas??n?? hesapl??yoruz. Bu a????rl??kl?? ortalama noktalar boyunca ge??en ??izgi, daha sonra d??rtl?? kenarlar?? olarak kullan??l??r. D??rt k????eler bu ??izgilerin kesi??im noktalar?? olarak hesaplan??r.  
    &emsp; ??ok k??????k etiketlerin kodunun ????z??lmesine yard??mc?? olabilmesine ra??men, yaln??zca etiketleri alg??lamakla ilgileniyorsan??z, kenar iyile??tirme ??ok ??nemli de??ildir. Bununla birlikte, kenar iyile??tirme ad??m??, poz tahmini i??in etiketler kullan??ld??????nda yerelle??tirme do??rulu??unu art??r??r.  
      
  ![image](https://user-images.githubusercontent.com/49456613/121807456-e2428580-cc5c-11eb-8fab-09bb75f88ad0.png)  
  ??ekil 8: Ger??ek g??r??nt??ler ??zerinde mesafe testi i??in AprilTag mozai??i. G??r??nt??ler Nokta Grisi Bukalemun ile 1296 x 964 pikselde ??ekildi ve her bir etiket 0.167m geni??li??inde. Bu deney, sim??le edilmi?? g??r??nt??lerde g??zlemlenen etiket alg??lama ve yerelle??tirme performans??n??n ger??ek g??r??nt??lere d??n????t??????n?? g??stermektedir. (Rektifikasyon, etiket tespiti ve lokalizasyonundan ??nce yap??lm????t??r.)

  
### Sonu??  
&emsp; Bu belge, ??nceki dedekt??r?? geli??tiren, yanl???? pozitiflerin oran??n?? azaltan, alg??lama oran??n?? art??ran ve alg??lama i??in gereken hesaplama s??resini azaltan yeni bir AprilTag alg??lama algoritmas??n?? a????klamaktad??r. Bu iyile??tirmeler, ak??ll?? telefonlar gibi hesaplama s??n??rl?? sistemlerde sa??lam etiket alg??lamay?? m??mk??n k??lar ve ger??ek zamanl?? uygulamalarda etiket izlemenin kullan????l??l??????n?? geni??letir. iPhone App Store'da ??cretsiz bir AprilTag dedekt??r uygulamas?? mevcuttur.  
  
## Kaynak??a  
* https://april.eecs.umich.edu/media/pdfs/wang2016iros.pdf

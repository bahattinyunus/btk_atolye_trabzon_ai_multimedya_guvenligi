

### 1️⃣ Temel fikir

Destek vektör makineleri, **veri sınıflandırmak** için kullanılan güçlü bir makine öğrenmesi algoritmasıdır. Amaç, iki sınıfı **en iyi şekilde ayıran bir çizgi veya yüzeyi** bulmaktır.

* 2 boyutlu veri için bu bir doğru (line),
* 3 boyutlu veri için bu bir düzlem (plane),
* Daha yüksek boyutlarda ise bir **hiperdüzlem (hyperplane)** olur.

Örnek:
Elimizde iki tür çiçek olsun: kırmızı ve mavi. SVM, kırmızı ve mavi çiçekleri ayıracak **en geniş boşluğu (margin) sağlayan çizgiyi** bulur.

---

### 2️⃣ Margin ve Destek Vektörler

SVM’in kalbi burası:

* **Margin**: Sınıflar arasındaki boşluk. SVM, **maksimum margin**i bulmayı amaçlar.
* **Destek Vektörler**: Bu boşluğa en yakın olan veri noktalarıdır. Bu noktalar, SVM’in “karar sınırını” belirler.

Yani karar sınırını sadece bu kritik noktalar belirler, diğerleri değil.

---

### 3️⃣ Lineer ve Lineer Olmayan SVM

* **Lineer SVM**: Veri lineer olarak ayrılabiliyorsa direkt bir doğru/hiperdüzlem çizer.
* **Lineer olmayan SVM**: Veri lineer olarak ayrılamıyorsa, SVM **kernel** adı verilen bir yöntemle veriyi daha yüksek boyuta taşır ve orada lineer ayırabilir.

Örnek kernel’lar:

* **Polynomial kernel**: Polinomlarla dönüştürür.
* **RBF (Radial Basis Function)**: Karmaşık sınırlar çizebilir.
* **Sigmoid kernel**: Sinüs benzeri bir dönüşüm uygular.

---

### 4️⃣ SVM’in matematiği (kısaca)

SVM, bir hiperdüzlem (w \cdot x + b = 0) bulur. Burada:

* (w) → hiperdüzlemin normal vektörü (eğim),
* (b) → ofset (başlangıç noktası).

Amaç:

[
\text{margin} = \frac{2}{||w||} \quad \text{maksimize etmek}
]

ve

[
y_i (w \cdot x_i + b) \ge 1
]

şartını sağlamak. Buradaki (y_i), sınıf etiketidir (+1 veya -1).

---

### 5️⃣ Avantajlar ve Dezavantajlar

**Avantajlar:**

* Karmaşık sınıflandırmalarda bile güçlüdür.
* Yüksek boyutlu veri ile iyi çalışır.
* Sınıflar arasında net ayrım yapar.

**Dezavantajlar:**

* Büyük veri setlerinde yavaş olabilir.
* Doğru kernel seçimi gerekir, yanlış kernel performansı düşürür.
* Gürültülü verilerde margin esnemesi gerekir (Soft margin SVM).

---

### 6️⃣ Kısa Özet

* SVM, **verileri ayırmak için en geniş boşluğu bulur**.
* Bu boşluğu belirleyen noktalara **destek vektörler** denir.
* Lineer veya lineer olmayan olabilir, kernel’lar kullanılır.
* Matematiksel olarak **hiperdüzlem ve margin** kavramına dayanır.


### 1️⃣ Soft Margin SVM
Gerçek hayat verisi çoğu zaman **mükemmel ayrılabilir değildir**. Gürültü, hatalı etiketler veya çakışan sınıflar olabilir. Bu durumda **hard margin SVM** çalışmaz. İşte soft margin devreye giriyor:

- Amaç: **Hala geniş margin bulmak**, ama bazı noktaların sınırı çiğnemesine izin vermek.  
- Matematiksel olarak: Bir **ceza terimi \(C\)** eklenir:
  - Büyük \(C\) → SVM daha az hata toleransı, margin küçülür.  
  - Küçük \(C\) → SVM daha esnek, margin genişler ama hataları tolere eder.  

---

### 2️⃣ Kernel Trick
Bazen veri **2D veya 3D’de lineer olarak ayrılamaz**. Çözüm: **veriyi daha yüksek boyuta taşımak**. Ama doğrudan dönüştürmek pahalıdır. Kernel trick burda devreye girer:

- Kernel, veri noktaları arasındaki **iç çarpımı (dot product)** hesaplar ve yüksek boyutlu uzaya geçişi gizli tutar.  
- Popüler kernel’lar:
  - **Linear** → Basit lineer SVM.
  - **Polynomial** → Polinom tabanlı dönüşüm.
  - **RBF (Gaussian)** → Karmaşık, esnek sınırlar.  
  - **Sigmoid** → Yapay sinir ağı benzeri etki.

---

### 3️⃣ Multi-class SVM
SVM doğal olarak **iki sınıflı**dır. Ama çoğu veri seti birden fazla sınıf içerir. Çözüm:

1. **One-vs-Rest (OvR)**: Her sınıf diğerlerinden ayrı bir SVM ile karşılaştırılır.
2. **One-vs-One (OvO)**: Her sınıf çifti için ayrı SVM eğitilir.

---

### 4️⃣ SVM’in Avantajları
- **Yüksek boyutlu veride güçlü**, feature sayısı örnek sayısından fazla olsa bile çalışır.  
- Overfitting riski düşüktür (özellikle iyi C ve kernel seçilirse).  
- Küçük veri setlerinde etkili.

---

### 5️⃣ Dezavantajları
- Büyük veri setlerinde **hesaplama maliyeti yüksek**.  
- Kernel ve C parametresi yanlış seçilirse performans düşer.  
- Gürültü ve çakışan sınıflarda **hard margin SVM** başarısız olur.  

---

### 6️⃣ Kullanım Alanları
- **Metin sınıflandırma** (spam filtreleme, duygu analizi)  
- **Görüntü işleme** (yüz tanıma, obje tespiti)  
- **Biyoinformatik** (hastalık sınıflandırma, gen veri analizi)  
- **Finansal tahminler**  

---

💡 Özetle Part 2:  
- Soft margin ile hatalara izin veriyoruz.  
- Kernel trick ile lineer olmayan veriyi yüksek boyutta ayırıyoruz.  
- Multi-class SVM ile birden fazla sınıfı yönetiyoruz.  
- Parametre seçimi ve kernel tipi **performansın kilit noktasıdır**.  

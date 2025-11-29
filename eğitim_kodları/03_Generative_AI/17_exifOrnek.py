from PIL import Image, ExifTags  # Pillow'dan Image (görüntü açmak için) ve ExifTags (EXIF etiket isimleri için) sınıflarını içe aktarıyoruz.
import os                        # Dosya ve klasör yolu işlemleri için os modülünü içe aktarıyoruz.

IMAGE_PATH = os.path.join("..", "veriler", "ornek_exifli.jpg")  # Analiz etmek istediğimiz görüntü dosyasının yolunu bir değişkende tutuyoruz.

if not os.path.exists(IMAGE_PATH):                         # Belirtilen dosya yolunda gerçekten bir dosya var mı diye kontrol ediyoruz.
    raise FileNotFoundError(f"Görüntü dosyası yok: {IMAGE_PATH}")  # Eğer dosya yoksa, kullanıcıya anlamlı bir hata mesajı verip programı durduruyoruz.

img = Image.open(IMAGE_PATH)  # Pillow'un Image sınıfını kullanarak görüntü dosyasını açıyoruz.

exif_raw = img.getexif()  # Görüntünün EXIF verisini ham (raw) haliyle alıyoruz; bu bir sözlük benzeri yapı döndürür.

if not exif_raw or len(exif_raw) == 0:                             # Eğer exif_raw boşsa veya içinde hiç veri yoksa (uzunluğu 0 ise),
    print("Bu görüntüde EXIF verisi bulunmuyor veya tamamen silinmiş.")  # Kullanıcıya EXIF olmadığı bilgisini veriyoruz.
    print("- EXIF'in olmaması tek başına sahtecilik anlamına gelmez.")   # EXIF yokluğunun kesin sahtecilik kanıtı olmadığını hatırlatıyoruz.
    print("- Sosyal medya, mesajlaşma uygulamaları veya düzenleme işlemleri EXIF'i silebilir.")  # EXIF'in yok olmasının muhtemel sebeplerini açıklıyoruz.
    raise SystemExit  # Daha analiz edecek bir şey olmadığından programı burada düzgün şekilde sonlandırıyoruz.

tag_id_to_name = {id_: name for id_, name in ExifTags.TAGS.items()}  # EXIF tag ID'lerini (sayıları) anlaşılır isimlere çevirmek için bir sözlük oluşturuyoruz.

exif = {}                                    # İnsan tarafından okunabilir EXIF verilerini tutmak için boş bir sözlük oluşturuyoruz.
for tag_id, value in exif_raw.items():       # Ham EXIF verisi içindeki her (tag_id, value) çifti için döngüye giriyoruz.
    tag_name = tag_id_to_name.get(tag_id, str(tag_id))  # Tag ID'ye karşılık gelen ismi buluyoruz; eğer yoksa ID'yi stringe çevirip kullanıyoruz.
    exif[tag_name] = value                   # Bu isim–değer çiftini yeni EXIF sözlüğümüze ekliyoruz.

camera_make = exif.get("Make", "Bilinmiyor")                 # EXIF'ten kamera markasını ("Make") alıyoruz; yoksa "Bilinmiyor" yazıyoruz.
camera_model = exif.get("Model", "Bilinmiyor")               # EXIF'ten kamera modelini ("Model") alıyoruz; yoksa "Bilinmiyor".
datetime_original = exif.get("DateTimeOriginal", "Bilinmiyor")  # EXIF'ten orijinal çekim zamanını ("DateTimeOriginal") alıyoruz; yoksa "Bilinmiyor".
software = exif.get("Software", "Bilinmiyor")                # EXIF'ten kullanılan yazılım bilgisini ("Software") alıyoruz; yoksa "Bilinmiyor".
gps_info = exif.get("GPSInfo", None)                         # EXIF'ten GPS bilgisi ("GPSInfo") varsa alıyoruz; yoksa None olarak kalıyor.

print("=== Temel EXIF Bilgileri ===")  # Ekrana başlık olarak temel EXIF bilgilerinin yazdırılacağını belirtiyoruz.
print(f"Dosya      : {IMAGE_PATH}")  # Üzerinde çalıştığımız dosyanın yolunu yazdırıyoruz.
print(f"Kamera     : {camera_make} / {camera_model}")  # Kamera marka/model bilgisini kullanıcıya gösteriyoruz.
print(f"Çekim Zamanı (DateTimeOriginal): {datetime_original}")  # EXIF'te kayıtlı olan çekim tarih ve saat bilgisini yazdırıyoruz.
print(f"Yazılım    : {software}")  # EXIF'teki software alanını (hangi yazılımla kaydedildiği) yazdırıyoruz.

if gps_info is not None:                             # GPSInfo alanı boş değilse,
    print("GPS        : VAR (GPSInfo alanı mevcut)") # Görüntüde GPS bilgisi olduğunu kullanıcıya bildiriyoruz.
else:                                                # Eğer gps_info None ise,
    print("GPS        : YOK (GPSInfo alanı bulunamadı)")  # Görüntüde GPS bilgisi bulunmadığını yazdırıyoruz.

print("\n=== Basit Sahtecilik İpuçları (Kaba Analiz) ===")  # EXIF'e dayalı basit sahtecilik ipuçları analizine geçtiğimizi gösteren başlık yazdırıyoruz.

software_str = str(software).lower()  # Yazılım bilgisini küçük harfe çevirip string olarak saklıyoruz; böylece karşılaştırmaları kolay yapabiliyoruz.

if software_str == "bilinmiyor":  # Eğer yazılım bilgisi hiç yoksa veya "Bilinmiyor" olarak kalmışsa,
    print("- Yazılım bilgisi bulunmuyor veya belirtilmemiş.")  # Yazılım alanının dolu olmadığını kullanıcıya bildiriyoruz.
elif any(tool in software_str for tool in ["photoshop", "gimp", "snapseed", "lightroom", "picsart"]):  # Eğer yazılım adında bilinen düzenleme programlarından biri geçiyorsa,
    print("- UYARI: EXIF 'Software' alanında bir düzenleme yazılımı görünüyor.")  # EXIF'te düzenleme yazılımı tespit edildiğini söylüyoruz.
    print("  Bu, görüntü üzerinde sonradan işlem yapılmış olabileceğine işaret eder.")  # Bu durumun sonradan düzenleme olasılığını artırdığını belirtiyoruz.
    print("  (Bu her zaman sahtecilik demek değildir; basit parlaklık/renk düzeltmeleri de olabilir.)")  # Ancak bunun otomatik olarak sahtecilik anlamına gelmediğini vurguluyoruz.
else:  # Yazılım alanı var ama bilinen düzenleme programlarından birini içermiyorsa,
    print("- Yazılım alanı mevcut ama bilinen bir düzenleme programı içermiyor.")  # Yazılım bilgisinin görece temiz göründüğünü belirtiyoruz.
    print(f"  (Software: {software})")  # Yazılım alanındaki gerçek değeri parantez içinde gösteriyoruz.

if datetime_original == "Bilinmiyor":  # Eğer orijinal çekim zamanı bilgisi hiç yoksa,
    print("- Çekim zamanı (DateTimeOriginal) alanı bulunmuyor.")  # Bu alanın eksik olduğunu kullanıcıya bildiriyoruz.
    print("  Bu, EXIF'in eksik kaydedilmiş veya sonradan temizlenmiş olabileceğini düşündürebilir.")  # Bunun EXIF üzerinde işlem yapılmış olabileceğine dair bir ipucu olabileceğini söylüyoruz.
else:  # datetime_original alanı varsa,
    print(f"- Çekim zamanı EXIF'te mevcut: {datetime_original}")  # Mevcut çekim zamanını kullanıcıya gösteriyoruz.
    print("  (Bu zamanın doğru olup olmadığı, cihaz saati ve olayla ilgili iddialarla karşılaştırılmalıdır.)")  # Bu tarihin gerçek olup olmadığının ayrıca doğrulanması gerektiğini hatırlatıyoruz.

if gps_info is None:  # GPS bilgisi yoksa,
    print("- GPS bilgisi yok. Bu normal olabilir (GPS kapalıyken çekilmiş olabilir).")  # GPS yokluğunun normal bir durum olabileceğini açıklıyoruz.
else:  # GPS bilgisi varsa,
    print("- GPS bilgisi mevcut. Çekim yeri yaklaşık olarak harita üzerinde bulunabilir.")  # GPS ile konum çıkarılabileceğini belirtiyoruz.
    print("  Ancak sahtecilik amacıyla GPS de manipüle edilebilir veya sahte konum eklenmiş olabilir.")  # GPS bilgisinin de değiştirilebileceğini ve tek başına güvenilemeyeceğini vurguluyoruz.

if camera_make == "Bilinmiyor" and camera_model == "Bilinmiyor":  # Hem marka hem model bilgisi yoksa,
    print("- Kamera marka/model bilgisi bulunmuyor.")  # Kamera bilgisi olmadığını kullanıcıya söylüyoruz.
    print("  Bu, ekran görüntüsü veya EXIF'i kırpılmış/düzenlenmiş bir dosya olabilir.")  # Bu durumun ekran görüntüsü ya da EXIF'i temizlenmiş bir dosya olabileceğini ima ediyoruz.
else:  # Kamera bilgisi varsa,
    print(f"- Kamera bilgisi: {camera_make} / {camera_model}")  # Kamera marka/model bilgisini kullanıcıya gösteriyoruz.
    print("  Bu bilgi, aynı olayla ilgili farklı fotoğrafların aynı cihazdan çıkıp çıkmadığını karşılaştırmak için kullanılabilir.")  # Bu bilginin karşılaştırma amaçlı nasıl kullanılabileceğini açıklıyoruz.

print("\nNOT:")  # Analizin doğası hakkında not kısmını başlatıyoruz.
print("- Bu analiz, sadece EXIF üzerinden çok basit ipuçları verir.")  # Analizin sınırlı ve kaba bir analiz olduğunu belirtiyoruz.
print("- EXIF bilgisi manipüle edilebilir, eksik olabilir veya tamamen silinmiş olabilir.")  # EXIF'in güvenilirliğinin sınırlı olduğunu hatırlatıyoruz.
print("- Gerçek sahtecilik tespiti için EXIF analizi, görüntü içeriği analizi (ışık, gölge, JPEG artefaktları,")  # Sahtecilik tespitinde başka yöntemlere de ihtiyaç olduğunu anlatıyoruz (1. satır).
print("  copy-move/splicing tespiti, derin öğrenme tabanlı yöntemler vb.) ile birlikte değerlendirilmelidir.")  # Diğer tekniklerin de birlikte kullanılması gerektiğini tamamlıyoruz (2. satır).

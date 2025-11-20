

# **Erişim Kontrolü **

*Eğitim README – Temel Kavramlar ve Modeller*

## 🎯 **Nedir Bu Erişim Kontrolü?**

Erişim kontrolü, bir sistemde **kimlerin hangi kaynaklara hangi koşullarla erişeceğini** belirleyen güvenlik mekanizmasıdır.
Amaç:

* Yetkisiz erişimi önlemek
* Veri bütünlüğünü korumak
* Sistem güvenliğini sürdürülebilir kılmak

Temelde üç soru sorar:

1. **Kim?** (Kullanıcı, süreç, servis)
2. **Neye?** (Dosya, veri, API, servis, cihaz)
3. **Ne kadar?** (Okuma, yazma, silme, çalıştırma, yönetme)

---

## 🔑 **Erişim Kontrolünün Ayakları**

Erişim kontrolü 3 temel mekanizma üzerine kuruludur:

### 1. **Kimlik Doğrulama (Authentication)**

Kimin erişmeye çalıştığını doğrulama süreci.
Örnek: Parola, OTP, biyometrik, token.

### 2. **Yetkilendirme (Authorization)**

Kişinin hangi haklara sahip olduğunu belirleme.
Örnek: Rol bazlı yetki, ACL, politika kuralları.

### 3. **Hesaplama / İzleme (Accounting / Auditing)**

Yapılan işlemlerin izlenmesi ve kayıt altına alınması.
Örnek: Loglama, oturum takibi.

---

## 🧠 **Erişim Kontrolü Modelleri**

Aşağıda dünyada en çok kullanılan erişim kontrol modelleri var. Part 2’de bunların teknik uygulamasını (JWT, OAuth2, RBAC schema, IAM policy vs.) vereceğim.

---

### 🔹 **1. DAC – Discretionary Access Control (İhtiyari Erişim Kontrolü)**

Kaynağın sahibinin (owner) yetkilendirme yaptığı modeldir.

**Örnek:**
Windows'da bir dosyayı sağ tıklayıp "Bu kullanıcı erişebilir" demen gibi.

**Avantaj:** Esnek.
**Dezavantaj:** Kullanıcılar yanlış izin verebilir → güvenlik riski.

---

### 🔹 **2. MAC – Mandatory Access Control (Zorunlu Erişim Kontrolü)**

Politikaların tamamen sistem yöneticileri tarafından belirlendiği, kullanıcıların değiştiremediği model.

**Kullanım alanı:**

* Askeri sistemler
* Kritik altyapılar
* Gizlilik seviyelerine göre erişim ("Secret", “Confidential”)

**Özellik:**
Etiket-tabanlı sınıflandırma (labeling).

---

### 🔹 **3. RBAC – Role Based Access Control (Rol Tabanlı Erişim)**

Yetkiler tek tek kullanıcılara verilmez; rol tanımlanır ve kullanıcı role atanır.

**Örnek:**

* Admin → full access
* Editor → read+write
* Viewer → read-only

**Neden popüler:**
✔️ Büyük sistemlerde yönetimi çok kolay
✔️ Hataları azaltır
✔️ Kurumsal mimarilere uygun

---

### 🔹 **4. ABAC – Attribute Based Access Control (Özellik Tabanlı Erişim)**

Kararlar **kullanıcı + kaynak + ortam** attribute’larına göre verilir.

**Attribute örnekleri:**

* `role = student`
* `department = IT`
* `access_time < 18:00`
* `location = campus`

**Politika örneği:**

> "Kullanıcı departmanı IT ise ve istek kampüs içinden geliyorsa erişime izin ver."

Bu model **Zero Trust** ile çok uyumludur.

---

### 🔹 **5. PBAC / Policy Based Access Control**

Modern cloud sistemlerinde artık ABAC+RBAC karışımı politika tabanlı modeller kullanılıyor.

**Örnek:**
AWS IAM Policy
GCP IAM Binding
Kubernetes RBAC + Admission Policies

---

## ⚙️ **Erişim Kontrolünde Kullanılan Kavramlar**

### • **ACL (Access Control List)**

Her kaynak için izin tablosu.
"Kim, ne yapabilir?" listesi.

---

### • **Capability Tokens**

Kullanıcıya özel anahtar/jeton verilmesi.
Bu token belirli kaynaklara erişim hakkı taşır.

---

### • **Least Privilege (En Az Yetki)**

Modern güvenliğin kutsal yasası:

> "Kullanıcıya işini yapması için gereken minimum yetki verilir."

---

### • **Separation of Duties (Görev Ayrımı)**

Tek bir kişiye çok fazla güç verilmez.
Örnek:
Hem finans kaydı oluşturup hem onaylama yetkisi bir kişide olmaz.

---

### • **Zero Trust Access**

Hiç kimseye içerde/dışarda diye güvenmemek.
Her istek doğrulanır, yetkilendirilir, loglanır.

---

## 🧩 **Sistemlerde Erişim Kontrolünün Yeri**

Erişim kontrolü şu katmanlarda uygulanabilir:

* **Uygulama Seviyesi (App Layer)**

  * JWT, session, middleware kontrolleri
* **Veritabanı Seviyesi**

  * DB user permissions, row-level security
* **Dosya Sistemi Seviyesi**

  * chmod, NTFS izinleri
* **Network Seviyesi**

  * Firewall kuralları, NAC
* **Cloud**

  * IAM policies

Part 2’de bunların hepsinin teknik örneklerini vereceğim.

---

## 📌 **Özet**

Erişim kontrolü sistem güvenliğinin bel kemiğidir.
Part 1’de temel yapıyı anlattık:

* Modeller (DAC, MAC, RBAC, ABAC…)
* Kavramlar (ACL, token, least privilege…)
* Katmanlar
* Temel mantık



# 🔐 **Erişim Kontrolü – Teknik Derinlik / Eğitim README**

Bu doküman, erişim kontrolünün mimarisini, modellerini, saldırı vektörlerini, politika motorlarını ve modern sistemlerdeki uygulama tekniklerini derin teknik seviye bir anlatımla sunar.
Kimlik doğrulamadan bağımsız olarak **"kimin neye, ne kadar, hangi koşulda erişebileceği"** sorusuna sistematik bir yaklaşım sağlar.

---

# 🧱 **1. Erişim Kontrolünün Temel Mimarisi**

Modern güvenlik mimarisinde erişim kontrolü üç kritik bileşeni kapsar:

1. **Identification** → “Ben Bahattin’im” demek
2. **Authentication (AuthN)** → Kanıtlama
3. **Authorization (AuthZ)** → Ne yapabilirsin?

Bu README’nin odağı AuthZ (yetkilendirme).

Erişim Kontrolü = Kimlik + Rol + Yetki + Politika + Zaman + Durum + Ortam değişkenleriyle alınan kararlar.

---

# 🧠 **2. Politika Motorları (PDP-PIP-PEP)**

Modern sistemler aşağıdaki üçlü mimariyi kullanır:

### **PEP – Policy Enforcement Point**

* “Bu isteğe izin vereyim mi, engelleyeyim mi?” diye karar uygulayan nokta
* API Gateway, Reverse Proxy, mikroservis sidecar’ı olabilir

### **PDP – Policy Decision Point**

* Asıl kararı veren beyin
* RBAC/ABAC politikalarını değerlendirir

### **PIP – Policy Information Point**

* PDP’nin ihtiyacı olan ek bilgileri sağlar
  (kullanıcı departmanı, dosya etiketi, MFA durumu, cihaz türü, konum)

Bu mimari, **Zero Trust** ve modern API güvenliğinin temelidir.

---

# 🗂️ **3. Erişim Kontrolü Modelleri (Teknik Karşılaştırma)**

## **3.1. DAC (Discretionary Access Control)**

Kaynağın sahibi izinleri belirler.
*Unix file permissions → klasik örnek.*

Avantaj → Esnek
Dezavantaj → Güvenlik zayıf

---

## **3.2. MAC (Mandatory Access Control)**

Sistem politikayı zorunlu uygulatır.
*Askerî, devlet kurumları → SELinux, AppArmor*

Özellik:

* Veriler hassasiyet etiketine sahip (Secret, Top Secret vb.)
* Kullanıcı clearance seviyesine göre erişir

Çok güçlü ama kullanım zor.

---

## **3.3. RBAC (Role-Based Access Control)**

Kullanıcı → Rol → Yetki zinciri
En yaygın model.

Örnek:

* admin
* editor
* viewer

Dezavantaj:
Rol patlaması → 3000 rol olan şirketler var.

---

## **3.4. ABAC (Attribute-Based Access Control)**

Erişim kararı **attribute (özellik) tabanlı** verilir:

* Kullanıcı özellikleri
* Kaynak özellikleri
* Ortam koşulları
* Policy kuralları

Örnek politika:

> Departmanı “Finans” olan kullanıcı, “mesai saatleri içinde”, “kurumsal cihazdan” geliyorsa “bütçe dosyalarına okuma erişimi” alabilir.

ABAC = Modern kurumsal dünyanın **en güçlü modeli**

---

## **3.5. PBAC (Policy-Based Access Control)**

ABAC’ın soyutlanmış, politikaların tamamen dışarıdan yönetildiği hali.
XACML ve OPA (Open Policy Agent) bunun örneğidir.

---

## **3.6. ReBAC (Relationship-Based Access Control)**

Sosyal medya uygulamalarında kullanılır.

Örnek:

* “Arkadaşımın arkadaşı → görebilir”
* “Bir projenin üyesiysem → repo erişimim olsun”

GitHub, Google Docs gibi sistemler ReBAC kullanır.

---

# 🧱 **4. Politika Dilleri ve Değerlendirme Motorları**

## **4.1. XACML**

En kapsamlı fakat karmaşık ABAC dili.
Kurumsal yapılarda güçlüdür.

## **4.2. OPA (Open Policy Agent)**

Modern mikroservis mimarilerinin gözbebeği.
Docker, Kubernetes, API Gateway seviyesinde çalışır.
Rego dili kullanır.

Örnek karar:

```rego
allow {
    input.user.department == "finance"
    input.resource.type == "report"
    input.action == "read"
}
```

## **4.3. AWS IAM Policy Language**

JSON tabanlı, dünya çapında en kullanılan politika dili.

---

# 📜 **5. Politika Değerlendirme Mantıkları**

Politika motorları şu kombinasyonlar üzerinden çalışır:

* **Deny > Allow** ilkesi (genelde)
* Permit-override
* Deny-override
* First-applicable
* Only-one-applicable

Politika çakışması → Güvenlik zafiyeti üretebilir.

---

# 🕵️‍♂️ **6. Erişim Kontrolünde Saldırı Vektörleri**

## **6.1. IDOR (Insecure Direct Object Reference)**

Klasik ama öldürücü:
`/user/123/edit` → 123 yerine 124 yazarsın, erişim açılır.

Kök sebep: PEP yok, PDP yok, AuthZ yok.

---

## **6.2. Broken Access Control (OWASP A01)**

2021 ve 2023’te 1 numaralı OWASP zafiyeti.
Genellikle şu hatalarda olur:

* Rol kontrolü istemcide yapılması
* Endpoint gizleyip korumamak
* Admin endpoint’inin herkese açık olması
* JWT içinde “role” alanını değiştirilebilir bırakmak
* “isAdmin = true” gibi tek bit ile kontrol yapmak

---

## **6.3. Privilege Escalation**

Yetki yükseltme:

* Vertical → user → admin
* Horizontal → bir kullanıcının diğerinin verisine erişmesi

---

## **6.4. Confused Deputy Attack**

Hizmet/servis yanlışlıkla saldırgan adına işlem yapar.

Örnek:

* Google Cloud IAM’de yanlış tasarlanmış servis hesapları

---

## **6.5. Time-of-Check to Time-of-Use (TOCTOU)**

Check ile usage arasındaki süre farkından yararlanmak.
Dosya, veritabanı ve API seviyesinde olabilir.

---

## **6.6. CSRF (Cross-Site Request Forgery)**

Yetkili kullanıcının oturumu kullanılarak yetkisiz istek gönderme.

---

# 🔐 **7. Zero Trust Model ve Modern Yaklaşım**

Zero Trust prensibi:

> “Kimseye güvenme, her isteği doğrula.”

Temel özellikler:

* Her istek ayrı ayrı yetkilendirilir
* Cihaz durumu kontrol edilir
* Kullanıcı davranış analizi yapılır
* Mikrosegmentasyon
* En az yetki (least privilege)

Günümüzde bütün kurumsal ağlar buna geçiyor.

---

# 🛡️ **8. Least Privilege & Just-in-Time Access**

Güncel kurumsal güvenliğin iki vazgeçilmezi:

### **Least Privilege**

Kullanıcı sadece işini yapacak kadar yetki alır.

### **Just-in-Time Access**

Yönetici yetkileri **süreli** olarak verilir.
Süre bitince yetkiler otomatik kapanır.
Microsoft Entra, AWS SSO, HashiCorp Vault bunu destekliyor.

---

# 🏗️ **9. Modern Sistemlerde Erişim Kontrol Mimarisi**

## **9.1. API Gateway + PDP + PEP**

* İstek gelir
* Token doğrulanır
* PDP politika kararı verir
* PEP uygulama erişimi açar/kapatır

## **9.2. Mikroservislerde Sidecar Pattern**

* Her servis kendi isteğini kontrol etmez
* Yanında çalışan sidecar (envoy/istio) PEP görevi görür

## **9.3. Cloud IAM Sistemleri**

* AWS IAM
* GCP IAM
* Azure Entra ID
  Hepsi ABAC + PBAC hibrit çalışır.

---

# 🔍 **10. Auditing & Logging (İleri Seviye Gereksinim)**

Her erişim kontrolü sistemi şu logları tutmalıdır:

* Kim erişti?
* Neye erişti?
* O anki rol/attribute değerleri neydi?
* Deny edilen istekler neden reddedildi?

Bu loglar olmadan kimse güvenlik garantisi veremez.

---

# 📚 **11. Özet**

Bu eğitim dosyasında şunların teknik tarafına indik:

* Erişim kontrolü modelleri (DAC, MAC, RBAC, ABAC, ReBAC)
* Politika motorları (OPA, XACML, IAM)
* Zero Trust prensipleri
* IDOR, Privilege Escalation, Confused Deputy gibi saldırılar
* Least Privilege & JIT Access
* PEP–PDP–PIP mimarisi
* Modern API ve mikroservis yetkilendirme yapıları

Bu seviye, bir **siber güvenlik uzmanı** veya **cloud architect** seviyesinde bilginin temelidir.

---


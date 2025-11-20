

# **Güvenlik Duvarları (Firewalls) – Teknik Eğitim README**

## 🎯 **1. Güvenlik Duvarı Nedir? (Firewall Basics)**

Güvenlik duvarı, bir ağdaki trafiği **belirli kurallara göre filtreleyen ve kontrol eden** bir güvenlik bileşenidir.
Amaçları:

* Yetkisiz erişimi engellemek
* Saldırı yüzeyini azaltmak
* Network segmentleri arasında güvenlik sınırları oluşturmak
* Trafiği izlemek, loglamak ve gerektiğinde engellemek

Firewall bir nevi dijital “kapı görevlisi”dir:
Kural uygunsa → **Geç**
Kural uygun değilse → **Drop / Reject**

---

# **🧱 2. Firewall Mimari Türleri**

### **1. Packet-Filtering Firewall (Stateless)**

* En basit firewall türü
* Her paketi **bağımsız** birim olarak değerlendirir
* Header bilgilerine göre karar verir:

  * IP adresi
  * Port
  * Protokol
  * Flag'ler (SYN, ACK vs.)

**Avantaj:** Hızlıdır
**Dezavantaj:** Bağlam bilmez → Spoofing ve state-based saldırılara açık

---

### **2. Stateful Inspection Firewall**

* Trafiğin **durumunu (state)** takip eder
* Bağlantı tabloları (state table) tutar
* TCP handshake (SYN, SYN-ACK, ACK) ilişkisini takip eder

Örnek:

* Beklenen paketse → allow
* Beklenmeyen paketse → drop

**Modern firewallların çoğu stateful’dır.**

---

### **3. Application Layer Firewall (Layer 7)**

* HTTP, DNS, SMTP gibi uygulama protokollerini analiz eder
* İçeriğe bakabilir (deep packet inspection)
* SQL injection, XSS gibi saldırıları tespit edebilir

NGFW (Next-Gen Firewall) sınıfı buraya girer.

---

### **4. NGFW – Next Generation Firewall**

* Stateful Firewall

- DPI (Deep Packet Inspection)
- IPS/IDS
- Malware Analysis
- TLS inspection
- URL Filtering
- App-ID (Facebook, Telegram tespiti gibi)

En gelişmiş firewall’lardır.

---

### **5. WAF – Web Application Firewall**

Ağ firewall’ı değildir; **web uygulamalarını** korur.

Koruduğu saldırılar:

* SQL Injection
* XSS
* CSRF
* RCE
* Directory Traversal

Örnek teknolojiler:

* ModSecurity
* AWS WAF
* Cloudflare WAF

---

### **6. Proxied Firewall (Forward / Reverse Proxy)**

Gelen trafik firewall tarafından **karşılanır** → sonra hedefe yönlendirilir.

Avantaj:

* IP gizleme
* Cache
* TLS termination
* Rate limiting

---

# **⚙️ 3. Firewall'ın Çalışma Prensipleri**

Firewall trafiği şu açılardan analiz eder:

### 🔹 **A) Network Layer Analizi**

* Source IP
* Destination IP
* Port
* Protocol (TCP/UDP/ICMP)

### 🔹 **B) Transport Layer Analizi**

* TCP flags
* Connection state
* Session duration
* SYN flood tespiti

### 🔹 **C) Application Layer Analizi**

* HTTP header
* DNS query
* SMTP komutları
* TLS handshake
* JSON body tarama

---

# **📜 4. Firewall Kuralları (Ruleset) Yapısı**

Bir firewall kuralı genelde şu parametrelerden oluşur:

```
Action: ALLOW / DENY / DROP / REJECT
Protocol: TCP/UDP/ICMP
Source IP / Source Port
Destination IP / Destination Port
Direction: INBOUND / OUTBOUND
State: NEW / ESTABLISHED / RELATED
Time: Schedule (optional)
Logging: Enabled/Disabled
```

Örnek kural:

```
Allow TCP from 10.0.0.0/24 to 10.0.1.5 port 443 state NEW,ESTABLISHED
```

---

# **🧰 5. Firewall Teknik Türleri (Filter Methodologies)**

### **1. Stateless Filtering**

* Paket bağımsız değerlendirilir
* Sadece header bazlı
* Basit ve hızlı

### **2. Stateful Filtering**

* Connection tracking tablosu tutar
* Flood karşı dirençlidir

### **3. Proxy Filtering**

* Trafiği kendisi işleyip yönlendirir

### **4. Deep Packet Inspection**

* Paket payload’ını okur
* Malware, exploit, shellcode tespiti

### **5. Behavioral Filtering**

* Anomali tespiti
* Machine learning tabanlı firewalllarda kullanılır

---

# **🔐 6. NAT + Firewall İlişkisi**

Firewalllar sıklıkla NAT ile birlikte çalışır:

* **SNAT**: Outbound trafikte kaynak IP değiştirme
* **DNAT**: Port forwarding
* **Masquerade**: Dinamik SNAT
* **PAT**: Port Address Translation

Firewall NAT sonrası trafik üzerinde çalıştığı için doğru sırayla uygulanır.

---

# **🧨 7. Firewall Üzerinde Tespit Edilen Saldırılar**

### 🔸 Port scanning (Nmap, Masscan)

Firewall loglarında SYN flood olarak görünür.

### 🔸 Spoofing

Stateless firewalllar bu saldırıya yatkındır.

### 🔸 SYN Flood / DDoS

State table taşarsa → firewall çöker.

### 🔸 Brute force (SSH, RDP vs.)

IPS/NGFW ile engellenir.

### 🔸 Protocol tunneling

HTTP içinde SSH gibi protokol saklama teknikleri.
DPI gerekebilir.

---

# **🖥️ 8. Linux’ta Firewall Örnekleri (Teknik)**

### **iptables (legacy)**

```
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -j DROP
```

### **nftables (yeni nesil)**

```
nft add rule inet filter input tcp dport 22 accept
```

### **ufw (Ubuntu basit aracı)**

```
ufw allow 22/tcp
ufw enable
```

---

# **🌐 9. Enterprise Firewall Ürünleri**

* **Palo Alto NGFW**
* **Fortigate**
* **Cisco ASA / FirePower**
* **Check Point**
* **Sophos XG**
* **Juniper SRX**
* **SonicWall**

Bu cihazlar:

* DPI
* IPS/IDS
* SSL decrypt
* URL filtering
* Sandboxing

gibi çok gelişmiş özelliklerle gelir.

---

# **🧩 10. NGFW İçindeki Modüller**

| Modül                 | Açıklama                                      |
| --------------------- | --------------------------------------------- |
| **App-ID**            | Uygulama tespiti (Netflix, Discord, Telegram) |
| **User-ID**           | Active Directory entegrasyonu                 |
| **Content-ID**        | Payload analizi, malware tespiti              |
| **Threat Prevention** | IPS / IDS motoru                              |
| **Anti-Virus**        | Inline AV taraması                            |
| **SSL Decryption**    | TLS trafiğini çözümleme                       |

---

# **🛡️ 11. Firewall Hardening Teknikleri**

* Varsayılan inbound = **deny all**
* Sadece gereken portları aç
* Yönetim arayüzüne (GUI/SSH) IP whitelisting
* Radius/TACACS+ ile admin doğrulaması
* Loglar için SIEM entegrasyonu
* Geo-IP blocking
* Rate limiting
* Zaman bazlı erişim (time schedule rules)

---

# **📌 12. Firewall Mimarileri**

### **1. Single-layer firewall**

Tek cihaz → düşük güvenlik

### **2. Multi-layer firewall**

DMZ + iç network + dış network

### **3. Dual firewall architecture**

Birbiriyle farklı vendor’larda iki firewall kullanmak (Fortigate + Palo Alto gibi).
Amaç: Zero-day riskini azaltmak.

### **4. Segmentation & Micro-segmentation**

Network'ü küçük zone’lara bölmek.

---

# **🔎 13. Firewall Log Analizi (Örnek)**

Örnek bir Palo Alto log satırı:

```
threat id=10001 type=scan src=185.204.2.50 dst=10.0.0.5 proto=tcp dport=22 action=deny
```

Anlamı:

* Bir port taraması → firewall engellemiş
* Kaynak IP yurt dışı → block

---

# **📑 14. Özet**

Güvenlik duvarı teknik olarak:

* Network trafiğini katmanlı analiz eder
* Kurallara göre yönetir
* Oturum durumunu takip eder
* Protokol davranışlarını izler
* Saldırıları tespit eder
* IPS/WAF/Proxy gibi modüllerle genişletilebilir
* Modern mimarilerde NGFW veya Cloud Firewall kullanılır


# **Güvenlik Duvarları – Part 2: İleri Teknik README**

## 🔧 **1. NGFW – Next Generation Firewall İleri Teknikleri**

NGFW, klasik stateful firewall’ın üstüne şunları ekler:

| Özellik               | Açıklama                                                              |
| --------------------- | --------------------------------------------------------------------- |
| **App-ID**            | Trafiği port yerine uygulama bazında tespit eder (ör: Telegram, Zoom) |
| **User-ID**           | AD / LDAP entegrasyonu ile kullanıcı bazlı politika uygular           |
| **Content-ID**        | Payload tarama, malware / exploit tespiti                             |
| **IPS/IDS**           | Inline veya passive saldırı önleme / tespit                           |
| **TLS Decryption**    | Şifreli trafiği çözümleme ve inspeksiyon                              |
| **URL Filtering**     | Kategori bazlı erişim kontrolü                                        |
| **Threat Prevention** | Zero-day ve known exploit önleme                                      |

> NGFW, Layer 7 analiz yeteneği ile sadece port/protokol bazlı firewalllardan çok daha güçlüdür.

---

## 🧩 **2. Deep Packet Inspection (DPI)**

DPI, firewall trafiğinin payload seviyesinde incelenmesini sağlar.

* **Protokol doğrulama:** Trafik gerçekten HTTP mi, yoksa proxylenmiş mi?
* **Anomali tespiti:** HTTP header manipülasyonu, SQLi, XSS
* **Malware tarama:** Inline dosya incelemesi
* **TLS Inspection:** Şifreli trafiğin çözülmesi ve içerik analizi

**Teknik yaklaşım:**

1. Paketler capture edilir
2. TCP reassembly yapılır (paket parçaları birleştirilir)
3. Protokol ve içerik incelenir
4. Tehdit varsa kural uygular: drop / reset / alert

---

## 🔐 **3. TLS / SSL Inspection**

TLS inspection, firewallların şifreli trafiği görmesini sağlar:

1. Client → Firewall → Server
2. Firewall TLS terminates → içerik inspect → yeni TLS bağlantısı server’a forward
3. Public key ve sertifikalar firewall tarafından yönetilir

**Avantaj:** Malware ve C2 trafikleri tespit edilir
**Risk:** Privacy endişesi, sertifika yönetimi hataları

---

## ⚡ **4. Firewall Policy İleri Seviyesi**

### **A) Zone-Based Policy**

* Network zone’ları oluşturulur: LAN, DMZ, WAN
* Zone’lar arası erişim kuralları tanımlanır
* Örnek Palo Alto CLI:

```
set rulebase security rules "Allow-HTTPS" from LAN to WAN application web-browsing service application-default action allow
```

### **B) Layer 7 / App-ID Policies**

* Trafik uygulama bazlı engellenir / izin verilir
* Örnek:

```
Allow TCP 443 but block Zoom / Netflix
```

### **C) User-ID Policies**

* AD kullanıcı veya grup bazlı izin
* Örnek: IT_Admin → tüm portlar
* Marketing → sadece HTTP/HTTPS

### **D) Time-Based Policies**

* Kurallar belirli saatlerde aktif
* Örnek: Guest WiFi → sadece 08:00-18:00 arası

---

## 🧪 **5. iptables / nftables İleri Teknik**

### **Stateful ve Layer7 örneği (iptables + string match)**

```bash
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -p tcp --dport 80 -m string --algo bm --string "malicious" -j DROP
```

### **nftables Layer7 match**

```bash
nft add rule inet filter forward tcp dport 80 @payload(0,12) == "malware" drop
```

> Layer7 inspection Linux firewall’da sınırlıdır, NGFW daha etkili.

---

## 🔍 **6. Firewall ve IPS / IDS Kombinasyonu**

* **IPS (Intrusion Prevention System):** Inline olarak trafiği engeller
* **IDS (Intrusion Detection System):** Trafiği pasif izler, alert üretir

**DPI + IPS örneği:**

* HTTP paketinde SQL injection payload tespit → firewall drop ve log → SIEM alert

---

## 🌐 **7. Zero Trust Entegrasyonu**

Zero Trust mimarisi:

> “Hiçbir kullanıcı veya cihaz güvenilir değildir; her istek doğrulanır, yetkilendirilir ve izlenir.”

Firewall rolü:

* Mikro segmentasyon: Zone’lar arasında izin minimal
* User-ID ve Device-ID ile bağlam doğrulama
* Policy enforcement → least privilege access
* TLS inspect + authentication

**Örnek:**

```
HR Dept → sadece Payroll App erişebilir  
DevOps → sadece GitLab, Jenkins  
VPN bağlantısı → MFA + endpoint compliance check
```

---

## 🛡️ **8. Firewall Hardening İleri Teknik**

* CLI erişimi sadece yönetim subnet’inden
* SNMP / API erişimlerini şifrele (HTTPS / TLS 1.3)
* High availability (HA) cluster → failover ve state sync
* Logging → SIEM entegrasyonu
* Rate limiting → SYN flood ve brute force önleme
* Geo-IP blocking → riskli ülkelerden gelen bağlantı engelleme

---

## 🧵 **9. Advanced Threat Prevention Örnekleri**

| Threat           | Detection / Firewall Action             |
| ---------------- | --------------------------------------- |
| SQL Injection    | DPI Layer7 pattern match → drop & alert |
| XSS Attack       | Content-ID inspection → sanitize / drop |
| Malware download | Inline AV / sandboxing → block          |
| Botnet C2        | DNS/HTTP anomaly detection → drop       |
| DDoS             | Rate limit, SYN cookies, geo-blocking   |

---

## ⚡ **10. Firewall Log ve SIEM Entegrasyonu**

* NGFW logları: Threat log, Traffic log, URL log
* SIEM örnekleri: Splunk, ELK, QRadar
* Analiz:

  * Anomalous port activity
  * User-ID rule violations
  * IPS trigger events

**Alert pipeline:** Firewall → SIEM → SOC → Incident Response

---

## 🏁 **11. Özet – İleri Seviye Firewall Mantığı**

* NGFW = Stateful + DPI + App-ID + User-ID + Threat Prevention + SSL inspect
* Firewall policy: Zone + Layer7 + User-ID + Time + App bazlı
* DPI = Paket içeriği, anomali ve exploit tespiti
* TLS Inspection = şifreli trafik kontrolü
* Zero Trust = her bağlantı doğrulanır ve segmentlenir
* Logging + SIEM → sürekli güvenlik analizi
* Hardening = yönetim, HA, rate limiting, geo-blocking, MFA


---

## ▶️ Nasıl Çalıştırılır? (Kod Demosu)

Bu klasörde, firewall ve log analizi kavramlarını somutlaştıran bir Python demo dosyası vardır:

- `firewall_demo.py` → `multimedya-guvenligi-ai/src/firewall/firewall_log_demo.py` modülünü kullanarak **örnek firewall loglarını analiz eder** ve basit **kural önerileri** üretir.

Örnek kullanım (bu klasörden):

```bash
cd güvenlik_duvarları
python firewall_demo.py
```

> Not: Kodun çalışması için aynı repoda `multimedya-guvenligi-ai/` projesi
> bulunmalı ve oradaki `requirements.txt` dosyasındaki bağımlılıklar
> kurulmuş olmalıdır.




# **Yedekleme ve Felaket Kurtarma (Backup & Disaster Recovery) – README**

## 🎯 **1. Tanım ve Amaç**

**Yedekleme (Backup):**
Veri veya sistemlerin, veri kaybına karşı bir kopyasının oluşturulmasıdır.

**Felaket Kurtarma (Disaster Recovery – DR):**
Sistem, uygulama ve verilerin kritik bir felaket sonrası **hızlıca geri getirilmesi ve iş sürekliliğinin sağlanması** sürecidir.

Amaçlar:

* Veri kaybını önlemek
* İş sürekliliğini sağlamak
* Felaket sonrası hızlı geri dönüş
* Uyumluluk ve regülasyon gerekliliklerini karşılamak

---

## 🧱 **2. Yedekleme Türleri**

### 🔹 **A) Tam Yedekleme (Full Backup)**

* Tüm verinin kopyalanması
* Avantaj: Basit, hızlı geri dönüş
* Dezavantaj: Depolama maliyeti yüksek, zaman alıcı

### 🔹 **B) Artımlı Yedekleme (Incremental Backup)**

* Önceki tam yedek ve artımları kullanır
* Sadece değişen veriler yedeklenir
* Avantaj: Depolama tasarrufu, hızlı yedekleme
* Dezavantaj: Geri yükleme süresi uzun (tam + artımlı zincir gerekir)

### 🔹 **C) Fark Yedekleme (Differential Backup)**

* Son tam yedekten bu yana değişen tüm veriler yedeklenir
* Avantaj: Artımlıdan daha hızlı geri dönüş
* Dezavantaj: Tam yedek + fark yedek gerekli → depolama orta seviyede

---

## 🔍 **3. Yedekleme Medya ve Konumları**

* **Disk:** Hızlı, düşük maliyetli, snapshot destekli
* **Tape (Manyetik bant):** Uzun süreli arşivleme, düşük maliyetli, yavaş
* **Bulut:** AWS S3, Azure Blob, Google Cloud Storage
* **Offsite / Remote:** Felaket durumunda erişim için farklı lokasyon

> 3-2-1 kuralı:
>
> * 3 kopya
> * 2 farklı medya
> * 1 offsite / bulut

---

## ⚡ **4. Felaket Kurtarma Türleri**

### **A) Cold Site**

* Hazır sunucu yok, felaket anında kurulum yapılır
* Maliyet düşük, kurtarma süresi uzun

### **B) Warm Site**

* Kısmen hazır altyapı
* Kurtarma süresi orta
* Sunucular ve network hazır, veri kısmen güncel

### **C) Hot Site**

* Full hazır, veri sürekli replike edilir
* Maliyet yüksek
* Kurtarma süresi çok kısa

---

## 🛡️ **5. Yedekleme ve DR Planlama**

1. **Business Impact Analysis (BIA):**
   Hangi sistemlerin kritik olduğu belirlenir.

2. **Recovery Point Objective (RPO):**
   Verinin kaybedilebilecek maksimum zamanı.
   Örnek: RPO = 4 saat → en fazla 4 saatlik veri kaybı toleranslıdır.

3. **Recovery Time Objective (RTO):**
   Sistemin geri gelmesi gereken maksimum süre.
   Örnek: RTO = 2 saat → felaketten 2 saat içinde sistemi çalıştır.

4. **DR Plan:**

   * Yedekleme türleri
   * Kurtarma prosedürleri
   * Test ve validasyon
   * İletişim planı

---

## 🧩 **6. Yedekleme Stratejileri**

* **Full + Incremental:** Haftalık full, günlük incremental
* **Full + Differential:** Haftalık full, günlük differential
* **Continuous Data Protection (CDP):** Her değişiklik anında yedeklenir
* **Snapshot ve Replication:** Anlık görüntü, storage replication

---

## 🔧 **7. Teknik Yedekleme Örnekleri**

### Linux

* rsync ile incremental:

```bash
rsync -av --progress /data /backup/data
```

* Tar + gzip:

```bash
tar -czvf backup-$(date +%F).tar.gz /data
```

### Windows

* Windows Server Backup
* VSS snapshot ile yedekleme
* PowerShell ile otomasyon:

```powershell
wbadmin start backup -backupTarget:D: -include:C: -allCritical -quiet
```

### Bulut

* AWS S3 + Lifecycle Policy (versioning, Glacier)
* Azure Backup Vault
* Google Cloud Storage Nearline/Coldline

---

## 🧭 **8. Felaket Kurtarma Uygulamaları ve Araçlar**

* **Veeam Backup & Replication** → VM ve veri yedekleme
* **Zerto** → Continuous replication
* **Acronis** → Disk, sistem ve bulut yedekleme
* **Commvault** → Enterprise yedekleme ve DR

---

## 🔍 **9. Felaket Senaryoları**

1. **Veri kaybı:** Disk arızası → restore yedekten
2. **Sistem çökmesi:** Sunucu boot sorunları → hot/warm site devreye alınır
3. **DoS/DDoS:** Trafiği başka lokasyona yönlendir, offsite yedekle kurtar
4. **Ransomware saldırısı:** En son temiz yedeği restore et

---

## 🧵 **10. Felaket Kurtarma Testleri**

* **Plan Validation:** Planın belgelenmiş olması
* **Tabletop Exercises:** Senaryo üzerinden adım adım test
* **Full DR Test:** Hot site veya backup restore ile gerçek test
* **Continuous Improvement:** Test sonrası plan güncellenir

> Plan test edilmezse, DR sadece kağıt üzerinde kalır.

---

## ⚡ **11. Yedekleme ve DR Güvenlik Önlemleri**

* Yedekler şifrelenmeli (AES-256)
* Offsite ve bulut verileri SSL/TLS ile iletilmeli
* Erişim kontrolleri (RBAC) uygulanmalı
* Immutable / WORM depolama → ransomware karşı
* Logging ve izleme → SIEM ile entegre

---

## 🏁 **12. Özet**

* **Backup:** Veri kaybını önler
* **Disaster Recovery:** Felaket sonrası hızlı iş sürekliliği sağlar
* **3-2-1 kuralı:** 3 kopya, 2 farklı medya, 1 offsite
* **RPO ve RTO:** Kritik performans göstergeleri
* **Stratejiler:** Full / Incremental / Differential / Continuous / Snapshot
* **DR Testi:** Hayati, planın gerçekçi olduğundan emin olun
* **Güvenlik:** Şifreleme, erişim kontrol, immutable depolama


# **Yedekleme ve Felaket Kurtarma – Part 2: İleri Teknik Senaryolar README**

## 🔧 **1. Enterprise DR – Temel Kavramlar**

### **A) Replication**

* **Asenkron:** Veriler gecikmeli olarak hedefe gönderilir → düşük performans etkisi
* **Senkron:** Gerçek zamanlı veri kopyalama → minimal veri kaybı (RPO ≈ 0)
* Örnek: SAN replication, Zerto, Veeam replication

### **B) Snapshots**

* Anlık disk görüntüsü
* Hızlı yedekleme ve geri yükleme
* Storage vendor tarafından desteklenir (NetApp, DellEMC, AWS EBS)
* Örnek:

```bash
aws ec2 create-snapshot --volume-id vol-12345678 --description "pre-update snapshot"
```

---

## ⚡ **2. Cloud Disaster Recovery Senaryoları**

### **A) AWS DR Örneği**

* **Cross-Region Replication:** S3 → farklı bölgeye
* **EC2 AMI + EBS snapshot:** Sunucu ve veri hızlı restore
* **Route53 Failover:** Primary site down → traffic otomatik yönlendirilir

**Örnek AMI restore:**

```bash
aws ec2 run-instances --image-id ami-12345678 --count 1 --instance-type t3.medium --key-name MyKey
```

### **B) Azure DR Örneği**

* **Azure Site Recovery (ASR):** VM replikasyonu ve failover
* **Storage Account Replication:** LRS, GRS, RA-GRS
* **Failover testi:**

```powershell
Start-AzSiteRecoveryUnplannedFailover -ProtectionContainerName "PrimaryContainer" -RecoveryPlanName "DRPlan"
```

### **C) GCP DR Örneği**

* **Persistent Disk Snapshots + Regional Backup**
* **Cloud Load Balancer + Multi-region failover**

---

## 🛡️ **3. Ransomware Felaketi Senaryosu**

1. **Durum:** Prod sunucular şifrelenmiş
2. **Adım 1:** Felaket izole edilir → affected network disconnect
3. **Adım 2:** En son clean backup / snapshot restore edilir
4. **Adım 3:** Replikasyon / failover devreye alınır
5. **Adım 4:** Log ve SIEM incelemesi → root cause analysis
6. **Adım 5:** Güvenlik önlemleri artırılır: immutable backup, WORM storage, MFA, network segmentation

> Not: Incremental backup zincirinde bozulma varsa, tam restore için en son clean full + artımlı yedek kullanılır.

---

## 🧩 **4. Multi-Site DR ve Failover**

* **Active-Passive:** Bir site çalışıyor, diğer standby → failover anında aktif
* **Active-Active:** Her site çalışıyor, load balancing → felaket anında seamless traffic reroute

**Failover Senaryosu:**

1. Primary site down
2. DNS / Load balancer → secondary site
3. Replication log replay
4. Kullanıcı minimum kesinti ile devam eder

---

## 🔍 **5. Continuous Data Protection (CDP)**

* Değişiklik anında yedekleme
* Minimal RPO (neredeyse 0)
* Enterprise storage + software tabanlı
* Örnek: Zerto, Veeam CDP, Datrium

> CDP sayesinde kullanıcı dosya kaybı neredeyse sıfır olur.

---

## ⚡ **6. Snapshot + Replication Senaryosu**

### **AWS Örneği**

* RDS snapshot → cross-region restore
* EBS snapshot → yeni EC2 instance attach

```bash
aws rds create-db-snapshot --db-instance-identifier mydb --db-snapshot-identifier snapshot1
aws rds restore-db-instance-from-db-snapshot --db-instance-identifier mydb-restored --db-snapshot-identifier snapshot1
```

### **On-Prem Örneği**

* SAN snapshot → replication → DR site restore

> Snapshot + replication kombinasyonu → hem hızlı RTO hem güvenli RPO sağlar.

---

## 🔧 **7. Test Edilen DR Süreci**

1. **Failover Testi**

* Hot site devreye alınır, tüm servisler secondary site üzerinden çalıştırılır
* Veri tutarlılığı kontrol edilir

2. **Failback Testi**

* Primary site onarılır
* Replication ile veri sync edilir
* Servisler geri taşınır

3. **Backup Validation**

* Restore testi → verinin bütünlüğü SHA256 hash ile kontrol edilir

```bash
sha256sum restored_file
```

---

## 🧭 **8. İleri Teknik Güvenlik Önlemleri**

* **Immutable Backup:** Ransomware engelleme
* **WORM Storage:** Write Once, Read Many → yedek değiştirilemez
* **Encryption:** AES-256, TLS 1.3
* **Access Control:** RBAC, MFA
* **Logging & Monitoring:** SIEM entegrasyonu, alert sistemi
* **Multi-Region DR:** Bölgesel felaketlere karşı dayanıklılık

---

## 🧵 **9. Özet – İleri Teknik DR Mantığı**

* **Replication:** Senkron / Asenkron
* **Snapshots:** Hızlı restore için
* **Failover:** Active-Passive / Active-Active
* **Cloud DR:** AWS, Azure, GCP örnekleri
* **Ransomware Recovery:** Immutable + clean backups
* **Continuous Protection:** Minimal RPO
* **DR Testi:** Failover + failback + validation
* **Güvenlik:** Encryption, access control, monitoring

> Sonuç: İyi planlanmış ve test edilmiş DR, felaket sonrası kesintiyi minimize eder, veri kaybını neredeyse sıfıra indirir.

---

## ▶️ Nasıl Çalıştırılır? (Kod Demosu)

Bu klasörde, yedekleme ve felaket kurtarma kavramlarını somutlaştıran bir Python demo dosyası vardır:

- `backup_demo.py` → `multimedya-guvenligi-ai/src/backup/backup_dr_demo.py` modülünü kullanarak **3-2-1 yedekleme planı** ve **basit bir ransomware/DR senaryosu** simüle eder.

Örnek kullanım (bu klasörden):

```bash
cd yedekleme_felaket_kurtarma
python backup_demo.py
```

> Not: Kodun çalışması için aynı repoda `multimedya-guvenligi-ai/` projesi
> bulunmalı ve oradaki `requirements.txt` dosyasındaki bağımlılıklar
> kurulmuş olmalıdır.


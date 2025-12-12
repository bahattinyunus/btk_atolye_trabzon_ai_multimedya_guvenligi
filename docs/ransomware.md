

# 🛡️ Ransomware (Fidye Yazılımı) Nedir?

Ransomware, bir bilgisayar sistemine sızıp dosyaları **şifreleyen**, ardından bu dosyaların açılması için **fidye talep eden** kötü amaçlı yazılım türüdür. Saldırganın amacı, kurbanın verilerini rehin alarak para kazanmaktır.

---

## 🚨 Ransomware Nasıl Çalışır?

1. **Bulaşma**

   * Phishing e-mail (sahte e-posta ekleri)
   * Kötü amaçlı linkler
   * Crack programları, illegal yazılımlar
   * Güvenlik açığı olan sistem ve uygulamalar

2. **Şifreleme**

   * Saldırgan dosyalarına erişimi engeller, genellikle güçlü kriptografi kullanır.
   * Dosya uzantılarını değiştirir (.locked, .encrypted vb.)

3. **Fidye Notu**

   * Bir “readme” veya “how_to_recover_files” gibi bir not bırakılır.
   * Genellikle şu istenir:

     * Bitcoin/Ethereum ile ödeme
     * Belirli süre içinde ödemezsen dosyaları silmekle tehdit

4. **Ödeme → Çözme Anahtarı (Her zaman verilmeyebilir!)**

   * Ödeme yapılsa bile saldırgan çoğu zaman dosyaları geri vermez.

---

## 🧪 Ransomware Türleri

* **Crypto Ransomware:** Dosyaları şifreler (en yaygın).
* **Locker Ransomware:** Sistemi komple kilitler, masaüstüne bile giremezsin.
* **Scareware:** Korkutma amaçlı sahte virüs uyarıları verir.
* **Doxware (Leakware):** Verileri sızdırmakla tehdit eder.

---

## 🛡️ Nasıl Korunulur?

### ✔️ Teknik Korunma Önlemleri

* Güncel **antivirüs** ve **antimalware** kullanın.
* İşletim sistemini ve yazılımları güncel tutun.
* Güvensiz e-postaları açmayın, ekleri çalıştırmayın.
* Admin yetkilerini kısıtlayın.
* RDP portlarını (3389) kapatın veya VPN ile koruyun.

### ✔️ Yedekleme Stratejisi

* **3-2-1 Backup** kuralı:

  * 3 kopya
  * 2 farklı ortam
  * 1 offline/cloud yedek
* Offline yedekler ransomware’e karşı en etkili savunmadır.

---

## 🛠️ Ransomware Bulaşırsa Ne Yapılır?

1. **Paniğe girme. Cihazı kapatma.**
2. İnterneti kes (Wi-Fi / Ethernet).
3. Sistemi izole et.
4. Olayı uzman birine bildir (kurumsal ortamdaysan SOC’a).
5. Fidye ödeme!
6. Yedeklerden geri yükle.
7. “nomoreransom.org” gibi sitelerde çözüm araçlarına bak.

---

## 🧠 Ransomware Neden Bu Kadar Tehlikeli?

* Saldırganlar kripto para ile izlerini gizleyebiliyor.
* Kurbanların %60’ı işletmesi zarar gördüğü için ödeme yapıyor.
* Bazı varyantlar kendini ağ içinde otomatik yayıyor (ör: WannaCry).

    
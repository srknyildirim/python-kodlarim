## 📌 Temel Ağ Kavramları

### 🔹 **Bit ve Bayt**

- **Bit**, dijital verinin en küçük birimidir.
    
- **Bayt**, 8 bitten oluşur.
    
- Harf ve sayıların temsili için **ASCII kodları** kullanılır.
    
    - Örneğin:
        
        - `A = 01000001`
            
        - `9 = 00111001`
            
- Klavyeden girilen her karakterin bir ASCII karşılığı vardır.
    

---

### 🔹 **İstemci (Client) ve Sunucu (Server)**

- **İstemci (Client)**: Sunucudan bilgi talep eden ve görüntüleyen yazılımları barındırır.
    
- **Sunucu (Server)**: Ağdaki diğer cihazlara e-posta, web sayfası vb. bilgileri sağlayan yazılımları içerir.
    

---

## 📡 IP Yapılandırması

Ağ üzerinden cihazın bilgi gönderip alabilmesi için üç temel bilgi doğru şekilde tanımlanmalıdır:

1. **IP Adresi**: Cihazın yerel ağdaki kimliğidir.
    
2. **Subnet Mask**: Cihazın hangi ağ segmentine ait olduğunu gösterir.
    
3. **Default Gateway**: Dış dünyaya çıkış yapılan ağ geçidini belirtir.
    

- Çoğu cihaz, **DHCP (Dynamic Host Configuration Protocol)** ile otomatik IP alacak şekilde yapılandırılabilir.
    
    - DHCP sunucusu, cihazlara bir adres havuzundan otomatik IP atar.
        

---

## 🔌 Topolojiler

- **Physical Topology (Fiziksel Topoloji)**: Ağ aygıtlarının fiziksel olarak nasıl bağlandığını gösterir.
    
- **Logical Topology (Mantıksal Topoloji)**: Ağdaki veri akış yapısını ve adresleme mantığını tanımlar.
    

---

## 🌐 İnternet Üzerinden İletişim

- İnternete bağlı her cihazın **benzersiz (eşsiz) bir IP adresi** olmalıdır.
    
- **Ping Komutu**: İki cihaz arasındaki bağlantıyı test etmek için kullanılır.
    
    - Gidiş-dönüş süresi ve bağlantının başarılı olup olmadığı ölçülür.
        
- **Traceroute Komutu**: Ping işe yaramadığında kullanılır; verinin geçtiği ağ noktalarını gösterir.
    

---

## 🧩 Ağ İletişim Modelleri

### 🔄 Bir Web Sayfasına Erişimde Kullanılan Protokoller

1. **HTTP (HyperText Transfer Protocol)**
    
    - İstemci ve sunucu arasında web sayfası taleplerini ve yanıtlarını yönetir.
        
2. **TCP (Transmission Control Protocol)**
    
    - Bilginin güvenli ve sıralı bir şekilde iletilmesini garanti eder.
        
    - Akış kontrolü sağlar.
        
3. **IP (Internet Protocol)**
    
    - Verinin gönderen cihazdan alıcı cihaza nasıl ulaştırılacağını belirler.
        
    - Router cihazlar üzerinden yönlendirme yapar.
        
4. **Ethernet**
    
    - Aynı ağ içindeki cihazlar arasında veri iletimini sağlar.
        
    - Ağ kartları arasında çerçeve (frame) düzeyinde iletişim kurar.
        

📌 Bu yapı **katmanlı bir hiyerarşiye** sahiptir. Her üst düzey protokol, alt katmandaki protokollerin sunduğu hizmetlere bağlıdır.
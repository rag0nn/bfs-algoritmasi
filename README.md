### Bu repo Breadth First Search (BFS) 'un uygulanması ve  görselleştirmesi ile alakalı
### BFS Nedir?
BFS , graflar üzerinde işlem yaparken genişlik öncelikli arama yani queue kullanarak sıradaki komşuları tarayarak ilerleyen arama algoritması türüdür.
### Nasıl Çalışır?
BFS implemantasyonunda genellikle queue(sıra) kullanılır, bu projede de queue kullanılmıştır.
Graf bilgilerini tutan graf = {} python sözlüğü  bulunmakta, bu sözlük her düğümün komşu olduğu düğümleri içermektedir;örn:'A' : ['B','C'].Her bir kenar çift taraflı olarak düşünülmekte ve dolayısıyla x ve y düğümleri komşuysa bu komşuluk bilgisi hem x hem de y de yazılmaktadır.Algoritma arama yaparken düğümün grafta belirtilen komşularına bakarken 0. indeksten başlayarak ilerlemektedir.Amaç A düğümünden başlayarak istenilen hedef düğüme giden en kısa yolu bulmaktır.Bunun için queue'mıza A yi ekleyerek başlıyoruz ve aynı zamanda kullanılanlar adlı daha önce uğranmış düğümleri tutan dizimizede ekliyoruz.Bu dizi x düğümünden y düğümüne ulaştıktan sonra y düğümüne geldiğimizde tekrar x düğümüne ulaşmamak için kullanılıyor.Bu diziye ekleme yapmanın ardından sonuc = {} adlı sözlüğümüze düğümün A'ya olan uzaklığını ekleyerek devam ediyoruz ki A'nın A'ya olan uzaklığı "0" olarak eklenmekte.Sıra A'nın komşularından B'ye geliyor.B'yi queue ye eklidekten sonra A'yı queueden çıkartıyoruz ve aynı işlemleri B içinde gerçekleştiriyoruz ta ki hedef düğüme ulaşana kadar.

<img src="https://raw.githubusercontent.com/rag0nn/bfs-algoritmasi/main/gifs/k%C4%B1lavuz.gif" width="auto">
Bu işlemler olurken aynı zamanda yol = {} adlı bir sözlük tutuyoruz,bu sözlük hangi düğüme hangi düğümün hangi indeksinden ulaşıldıgını gösteriyor;örn: yol["C"] = ["B",2]
Yol adlı sözlüğü arama algoritması hedefe ulaştığında geriye yayılım yaparak en kısa yolu tespit edip kayıt altına almak ve işaretlemek için kullanıyoruz.
### İşte Bazı Örnekler
<img src="https://raw.githubusercontent.com/rag0nn/bfs-algoritmasi/main/gifs/ornek-1.gif" width="auto">
<img src="https://raw.githubusercontent.com/rag0nn/bfs-algoritmasi/main/gifs/ornek-2.gif" width="auto">
<img src="https://raw.githubusercontent.com/rag0nn/bfs-algoritmasi/main/gifs/ornek-3.gif" width="auto">

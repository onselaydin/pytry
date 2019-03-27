Seo araçlarını barındıran kullanışlı bir site önerisi https://dmoztools.net/
search engine ler 200 den fazla kurala göre tarama yaparlar.Bunlardan bazıları
    - Domain yaşı ve ileriye doğru olan yaşına bakarlar.
    - Diğer sitelerde olan linkler
    - Çok fazla gereksiz taglar açmamak iyi değil.
    - Sitenin açılma hızınada bakmaktalar.
    - Benzer sitelerle karşılaştırma yapar.
    - Sayfa başlıklarının büyük yazılmasını sevmezler.
       örnek title : En güzen ayakkabılar | Kargo bedava
    - Her sayfanın başlığı h1 i olmalı. h2 den önce h1 olmalı.
    - meta taglar önemli bir detay.
      <meta name="keyword" content="kelime1,kelime2 ...." /> gibi kullanılmalı diyor. Önem sırasına göre kelimeleri dizmeliyiz.
      <meta name="abstract" content="kısa bir açıklama yazın diyor" />
    - Site haritası oluşturmak önemli. kök dizinde olmalı. sitemap.xml şeklinde.
        SiteMap olan sitelerin sayfalarına erişim önceliği tanınmaktadır.
        ücretsiz sitemap oluşturma servisi https://www.xml-sitemap.com/
        örnek sitemap.xml 
            <?xml version="1.0" encoding="UTF-8"?>
            <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <url>
                <loc>http://www.example.com/</loc>
                <lastmod>2005-01-01</lastmod>
                <changefreq>monthly</changefreq>
                <priority>0.8</priority>
            </url>
            <!-- ... -->
            </urlset>

    - Sayfalarda çok fazla ve saçma linkler kullanmamak gerekli.
    - Kırık linklere dikkat etmek gerekli. Tespit etmek için https://www.brokenlinkcheck.com/
    - Sitenizi özgün yapmak önemli.
    - 404 sayfalarında geri buttonu ve sorun bildirme formu gibi araçlar önemli.
    - css sprites konusu öneli https://www.toptal.com/developers/css/sprite-generator
    - robot.txt dosyası ve içeriğini girmemiz gerekli.
    - .htaccess dosyası gerekli.
örnek .htaccess
siteye zarar verebilecek botlardan korumak için
<IfModule mod_rewriter.c>
RewriteEngine On
RewriteCond %{HTTP_USER_AGENT} ^BlackWidow [OR]
RewriteCond %{HTTP_USER_AGENT} ^Bot\ mailto:craftbot@yahoo.com [OR]
RewriteCond %{HTTP_USER_AGENT} ^ChinaClaw [OR]
RewriteCond %{HTTP_USER_AGENT} ^DISCo [OR]
RewriteCond %{HTTP_USER_AGENT} ^Download\ Demon [OR]
RewriteCond %{HTTP_USER_AGENT} ^eCatch [OR]
RewriteCond %{HTTP_USER_AGENT} ^EirGrabber [OR]
RewriteCond %{HTTP_USER_AGENT} ^EmailSiphon [OR]
RewriteCond %{HTTP_USER_AGENT} ^EmailWolf [OR]
RewriteCond %{HTTP_USER_AGENT} ^Express\ WebPictures [OR]
RewriteCond %{HTTP_USER_AGENT} ^ExtractorPro [OR]
RewriteCond %{HTTP_USER_AGENT} ^EyeNetIE [OR]
RewriteCond %{HTTP_USER_AGENT} ^GrabNet [OR]
RewriteCond %{HTTP_USER_AGENT} ^Grafula [OR]
RewriteCond %{HTTP_USER_AGENT} ^HMView [OR]
RewriteCond %{HTTP_USER_AGENT} ^HTTrack [NC, OR]
RewriteCond %{HTTP_USER_AGENT} ^Image\ Stripper [OR]
RewriteCond %{HTTP_USER_AGENT} ^Image\ Sucker [OR]
RewriteCond %{HTTP_USER_AGENT} ^InterGET [OR]
RewriteCond %{HTTP_USER_AGENT} ^LeechFTP [OR]
RewriteCond %{HTTP_USER_AGENT} ^Mass\ Downloader [OR]
RewriteCond %{HTTP_USER_AGENT} ^MIDown\ tool [OR]
RewriteCond %{HTTP_USER_AGENT} ^Mister\ PiX [OR]
RewriteCond %{HTTP_USER_AGENT} ^Navroad [OR]
RewriteCond %{HTTP_USER_AGENT} ^NearSite [OR]
RewriteCond %{HTTP_USER_AGENT} ^NetAnts [OR]
RewriteCond %{HTTP_USER_AGENT} ^NetSpider [OR]
RewriteCond %{HTTP_USER_AGENT} ^Net\ Vampire [OR]
RewriteCond %{HTTP_USER_AGENT} ^Offline\ Explorer [OR]
RewriteCond %{HTTP_USER_AGENT} ^Offline\ Navigator [OR]
RewriteCond %{HTTP_USER_AGENT} ^RealDownload [OR]
RewriteCond %{HTTP_USER_AGENT} ^ReGet [OR]
RewriteCond %{HTTP_USER_AGENT} ^SuperHTTP [OR]
RewriteCond %{HTTP_USER_AGENT} ^Web\ Sucker [OR]
RewriteCond %{HTTP_USER_AGENT} ^WebAuto [OR]
RewriteCond %{HTTP_USER_AGENT} ^WebCopier [OR]
RewriteCond %{HTTP_USER_AGENT} ^WebFetch [OR]
RewriteCond %{HTTP_USER_AGENT} ^WebReaper [OR]
RewriteCond %{HTTP_USER_AGENT} ^WebSauger [OR]
RewriteCond %{HTTP_USER_AGENT} ^Website\ eXtractor [OR]
RewriteCond %{HTTP_USER_AGENT} ^Website\ Quester [OR]
RewriteCond %{HTTP_USER_AGENT} ^WWWOFFLE [OR]
RewriteCond %{HTTP_USER_AGENT} ^Xaldon\ WebSpider [OR]
RewriteCond %{HTTP_USER_AGENT} ^Zeus [OR]
RewriteRule .* - [F,L]
</ifModule>
-Site görsellerini korumak için
RewriteEngine On
RewriteCond %{http_REFERER} !^$
RewriteCond %{http_REFERER} !^http://(www\.)?okipu.net/imgs.*$ [NC]
RewriteRule \.(gifjpgpng)$ - [F]
    
    - canonical link head tagları arasına girilmeli.
        örnek <link rel="canonical" href="http://www.sitemiz.com/" />
    - Dinamik olmayak ziyaretçilerle etkileşimde bulunmayan sitelerin işleri çok zordur.
    - Standartlık testi :   https://validator.w3.org/
    - iframeler siteye ciddi eksi puanlar veriyor.
    - Görsellerde alt metin eklemek.
    - css validator http://jigsaw.w3.org/css-validator/
    - js dosyaları sayfanın altına refere edilmeli.
    - domain otoritesi -   moz.com/researchtools/ose
    - rank aracı http://www.seomastering.com/trust-rank-checker.php
    - Uygunsuz kalitesiz sitelere link çıkmamak.
    - Siteyi güncel tutmak.
    - Sosyal ağlardan siteye düzenli hit sağlamak.
    - backlink   https://majestic.com
        https://www.ranksignals.com/
    - Backlink alıncak sitelerin kalitesi önemli.
    - site ilk açıldığında kesinlikle forum backlink alma.
    - sitemiz ile alakalı sitelerden backlink almak daha iyi.
    - XFN kullanımı yeni siteler için faydalıdır.
        örneğin: <a href="stemiz.com" rel="friend me">sitemiz </a>
        me kelimesi kendi sitemizden başka sitemize link verdiğimizi gösterir.
        acquaintance(Tanıdık), friend(Arkadaş), met (yüz yüze) co-worker(iş arkadaşı)
        http://gmpg.org/xfn/creator
    - pop-up ve splash reklam olan sitelere backlink verme.
    - sitemizde doğal bir görüntü çizmezsek google Bomb cezası alabilir.zarar
    - anchor text
        örnek : <a title="kadın ayakkabıları" href="sitemiz.com" rel="dofollow"> kadın ayakkabıları </a>
        kelimeleri düzgün seçmeli. kadın ayakkanı değilde kadın ayakkabıları daha doğru.
    - dmoz mottosu "Human do it beter" insan daha iysini yapar. Başvur: https://dmoztools.net/
    - google, yandex dizinlerine kaydol
    - yahoo dizinine siteyi eklemek paralı.
    - kayıt olunması gereken diğer dizinler
        - www.arama.com                 - goguides.org
        - www.arabul.com                - liveinternet.ru
        - adres.gen.tr                  - annusurf.net
        - tekbul.com                    - jasminedirectory.com
        - botw.org                      - chiff.com
        - ipl.org                       - highrankdirectory.com
        - vlib.org                      - dizila.com
        - avivadirectory.com            - hotvsnot
        - about.com                     - webservis.gen.tr
        - joeant.com                    - siteekle.com.tr
        - apahcinc.org                  - turkish-media.com
        - amray.com                     - gimpsy.com
        - linkopedia.com                
    
    - googleda dizin bulmak için inurl:add.php intitle:link
        - inurl:siteekle.php
        - inurl:siteekle.asp
    - e-ticaret siteleri için dizin hizmeti veren www.alisaverissitelerim.com
    - bulurum.com firma bulma dizini. yellowpages.com  minarehber.com ticiz.com adresara.com
    - google ın webmaster tooları etkin kullanılmalı.
    - google dilini anlamak seo çalışmalarında önemlidir. bot algoritmaları sürekli gelişiyor.
    - google siteleri puanlarken en önemli kriter "faydalı olma" kriteridir.
    - Tüm çalışmalarda maksimum doğallık.
    - nitelikli backlink
    - sayfanın hızı
    - anahtar kelime yoğunluğu
    - anahtar kelimeleri sayfalarda %1-3 arasında kullanılmalıdır.
    - anahtar kelime ölçümü (Anahtar kelime yoğunluğu = (anahtar kelime sayısı x Toplam kelime sayısı) / 100 )
    - anahtar kelime yoğunluğu ölçmek için site : http://tools.seobook.com/general/keyword-density
    - 



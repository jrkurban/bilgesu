import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları (Sekme adı ve ikon)
st.set_page_config(page_title="Beni Affet ❤️", layout="wide")

# Kenar boşluklarını kaldırmak ve tam ekran hissi vermek için CSS
st.markdown("""
<style>
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
    }
    iframe {
        width: 100% !important;
        height: 100vh !important;
    }
</style>
""", unsafe_allow_html=True)

# Senin HTML Kodun (Buraya yapıştırıldı)
html_code = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beni Affet ❤️</title>
    <style>
        /* GENEL GÖRÜNÜM AYARLARI */
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #fce4ec; /* Arka plan rengi (açık pembe) */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            overflow: hidden; /* Taşmaları engellemek için */
            text-align: center;
        }

        /* RESİM KUTUSU (İstersen buraya gif koyabilirsin) */
        .gif-container img {
            width: 200px;
            border-radius: 15px;
            margin-bottom: 20px;
        }

        /* SORU YAZISI */
        #soru {
            font-size: 2rem;
            color: #d81b60;
            margin-bottom: 20px;
            padding: 0 20px;
            transition: all 0.3s ease;
        }

        /* BUTONLARI TUTAN KUTU */
        .btn-container {
            display: flex;
            gap: 20px;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
        }

        /* BUTON GENEL AYARLARI */
        button {
            padding: 15px 30px;
            font-size: 1.2rem;
            cursor: pointer;
            border: none;
            border-radius: 50px;
            transition: all 0.3s ease; /* Büyüme efekti için animasyon */
            font-weight: bold;
        }

        /* EVET BUTONU STİLİ */
        #evetBtn {
            background-color: #4caf50; /* Yeşil */
            color: white;
            box-shadow: 0 4px 15px rgba(76, 175, 80, 0.4);
        }

        /* HAYIR BUTONU STİLİ */
        #hayirBtn {
            background-color: #f44336; /* Kırmızı */
            color: white;
            box-shadow: 0 4px 15px rgba(244, 67, 54, 0.4);
        }

        #hayirBtn:hover {
            background-color: #d32f2f;
        }

    </style>
</head>
<body>

    <div class="gif-container">
        <img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" id="gifGorsel" alt="Cute Gif">
    </div>

    <h1 id="soru">Yilbasina beraber girelim mi? 🥺</h1>

    <div class="btn-container">
        <button id="evetBtn" onclick="kabulEtti()">Evet ❤️</button>
        <button id="hayirBtn" onclick="redEtti()">Hayır 💔</button>
    </div>

    <script>
        // --- BURADAKİ YAZILARI KENDİNE GÖRE DÜZENLE --- //
        
        // 1. Red butonuna her bastığında sırasıyla çıkacak yazılar:
        const redMesajlari = [
            "Emin misin?",
            "Gerçekten mi?",
            "Lütfen bir daha düşün...",
            "Kalbimi kırıyorsun 😢",
            "Bence pişman olacaksın",
            "Çok üzülürüm bak...",
            "Yapma böyle...",
            "Son şansın!"
        ];

        // 2. En son kabul edince çıkacak yazı:
        const kabulMesaji = "Yeeeey! Seni çok seviyorum! ❤️🥰";

        // 3. Kabul edince değişecek GIF (Opsiyonel):
        const mutluGif = "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif"; 

        // --- AYARLAR BİTTİ, BURADAN AŞAĞISINA DOKUNMANA GEREK YOK --- //

        let turSayisi = 0;
        let evetBoyut = 1.2; // Başlangıç font boyutu (rem)
        let hayirBoyut = 1.2; // Başlangıç font boyutu (rem)

        function redEtti() {
            const soruElementi = document.getElementById('soru');
            const hayirButonu = document.getElementById('hayirBtn');
            const evetButonu = document.getElementById('evetBtn');

            // Eğer listedeki mesajlar bittiyse butonu gizle
            if (turSayisi < redMesajlari.length) {
                // Soruyu değiştir
                soruElementi.innerText = redMesajlari[turSayisi];
                
                // Evet butonunu büyüt
                evetBoyut += 0.5; // Her seferinde ne kadar büyüyeceği
                evetButonu.style.fontSize = evetBoyut + "rem";
                
                // Hayır butonunu küçült
                hayirBoyut -= 0.1; 
                // Çok küçülürse okunmaz hale gelmesin diye minimum sınır
                if(hayirBoyut < 0.5) hayirBoyut = 0.5; 
                
                hayirButonu.style.fontSize = hayirBoyut + "rem";
                hayirButonu.innerText = "Hayır"; // İçindeki yazıyı sabit tutar veya değiştirebilirsin

                turSayisi++;
            } else {
                // 8 tur bittiğinde Hayır butonu yok olur
                hayirButonu.style.display = "none";
                soruElementi.innerText = "Artık başka seçeneğin yok... Beni affet! ❤️";
                // Evet butonu ekranı kaplayacak kadar büyüsün
                evetButonu.style.fontSize = "4rem";
            }
        }

        function kabulEtti() {
            document.getElementById('soru').innerText = kabulMesaji;
            // Butonları gizle
            document.getElementById('evetBtn').style.display = 'none';
            document.getElementById('hayirBtn').style.display = 'none';
            
            // Mutlu GIF'i göster
            document.getElementById('gifGorsel').src = mutluGif;
            
            // Arka planı konfetili veya daha canlı yapalım
            document.body.style.backgroundColor = "#ffc1e3";
        }
    </script>
</body>
</html>
"""

# HTML'i Streamlit içinde göster (Tam ekran boyutu vererek)
components.html(html_code, height=800, scrolling=False)
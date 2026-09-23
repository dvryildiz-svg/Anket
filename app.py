import streamlit as st

st.set_page_config(
    page_title="Akademik ve Kariyer Simülasyonu",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 Akademik ve Kariyer Yönelimli Uyum Envanteri")
st.markdown(
    """
Lütfen aşağıdaki ifadeleri **1 (Hiç katılmıyorum) ile 5 (Tamamen katılıyorum)** arasında puanla. 
Tüm soruları yanıtladıktan sonra en alttaki butona tıkla.
"""
)

# Soruların Tanımlanması (4 Modül, Toplam 20 Soru)
questions = {
    "Modül 1: Duygusal Yük ve Tepkisel Bağlanma": [
        (
            "Geçmişte yaşanan haksızlıklar ve disiplin süreçleri zihnimde"
            " hâlâ büyük bir öfke veya adaletsizlik duygusu uyandırıyor."
        ),
        (
            "Bir ortama aidiyet hissederken, oranın bana adil davranıp"
            " davranmadığı benim için başarıdan daha önemlidir."
        ),
        (
            "Yaşadığım kriz ortamında kalıp mücadele etmek ('pes etmeme'"
            " dürtüsü), rasyonel olarak başka bir yere gitmemden daha baskın"
            " geliyor."
        ),
        (
            "Günlük zihinsel enerjimin büyük kısmını akademik projelerime"
            " değil, çevremdeki insanların bana bakışına ve sosyal gerginliğe"
            " harcıyorum."
        ),
        (
            "Karar alırken mantıksal kariyer hedeflerimden ziyade, gururumu"
            " veya kırgınlıklarımı tatmin etme isteğim kararlarımı etkiliyor."
        ),
    ],
    "Modül 2: STEM ve Alan Uyumu": [
        (
            "Yabancı dil/sosyal bilimler ekolü yerine, saf fen, matematik ve"
            " teknoloji odaklı bir eğitim modeli benim zihinsel yapılanmama"
            " daha uygundur."
        ),
        (
            "İTÜ’deki akademisyenle yürüttüğüm fizik çalışmaları ve STEM"
            " projeleri, kariyerimin asıl temel taşıdır."
        ),
        (
            "Kendi entelektüel seviyemde, teknoloji ve bilim odaklı projeler"
            " üreten akranlarla aynı sınıf ortamında bulunmak en büyük"
            " motivasyon kaynağımdır."
        ),
        (
            "İtalyan lisesi ekolünün sağladığı avantajlar ile Bahçeşehir FenTek"
            " gibi köklü bir fen lisesinin STEM altyapısı karşılaştırıldığında,"
            " fen lisesi hedeflerime daha hızlı hizmet eder."
        ),
        (
            "Bilimsel bir problem çözerken veya laboratuvar çalışması"
            " yaparken hissettiğim 'akış (flow)' ve tatmin duygusu, diğer tüm"
            " derslerden fazladır."
        ),
    ],
    "Modül 3: Küresel Vizyon ve Gelecek Projeksiyonu": [
        (
            "Önümüzdeki 5-10 yıllık kariyer planımda kendimi uluslararası"
            " düzeyde mühendislik, fizik veya teknoloji Ar-Ge merkezlerinde"
            " konumlandırıyorum."
        ),
        (
            "Amerika'daki köklü üniversite kabullerinde güçlü bir fen lisesi"
            " referansının ve proje altyapısının ne kadar kritik olduğunun"
            " bilincindeyim."
        ),
        (
            "Tarihi bir okulun sosyal statüsünden ziyade, bana kazandıracağı"
            " teknik yetkinlikler ve laboratuvar imkânları benim için daha"
            " değerlidir."
        ),
        (
            "Hayatımın direksiyonunu ele alıp, geçmişin olumsuzluklarını"
            " düzeltmeye çalışmak yerine, enerjimi doğrudan küresel hedeflerime"
            " yönlendirmek istiyorum."
        ),
        (
            "Mevcut düzenin değişmesi fikri ilk başta bir kayıp gibi gelse"
            " de, mantıksal olarak düşündüğümde bu durum kariyerim için bir"
            " 'üst lige çıkış' basamağıdır."
        ),
    ],
    "Modül 4: Rasyonel Problem Çözme ve Adaptasyon": [
        (
            "Yaşadığım zorlukların, beni yanlış bir kulvardan (sosyal/dil"
            " ağırlıklı) doğru kulvara (saf fen/mühendislik) yönlendiren bir"
            " katalizör olabileceğini kabul edebiliyorum."
        ),
        (
            "Yeni bir okula uyum sağlama süreci, eski okulda yaşayacağım"
            " potansiyel dışlanma ve stres yükünden çok daha düşük"
            " maliyetlidir."
        ),
        (
            "Geleceğimi planlarken duygusal kırgınlıklarımı bir kenara"
            " bırakıp tamamen uzun vadeli başarı parametrelerine odaklanmaya"
            " hazırım."
        ),
        (
            "Çevremdekilerin ne düşüneceğinden ziyade, kendi bilimsel ve"
            " akademik geleceğim için en doğru olan stratejik hamleyi yapmak"
            " istiyorum."
        ),
        (
            "Hedeflerime ulaşmak için esnek olabilmeyi ve gerektiğinde en"
            " verimli ortama geçiş yapabilme cesaretini gösterebilirim."
        ),
    ],
}

scores = {}
with st.form("simulation_form"):
    q_index = 1
    for module_name, q_list in questions.items():
        st.subheader(module_name)
        scores[module_name] = []
        for q in q_list:
            val = st.slider(f"Soru {q_index}: {q}", 1, 5, 3)
            scores[module_name].append(val)
            q_index += 1

    submitted = st.form_submit_button("Anketi Tamamla")

if submitted:
    # Ali Yiğit'e sadece nötr ve profesyonel bir teşekkür mesajı gösterilir, skorlar gizlenir.
    st.success(
        "Teşekkürler! Yanıtların başarıyla kaydedildi. Bu pencereyi"
        " kapatabilirsin."
    )

    # Oturumda verileri sakla
    st.session_state["scores"] = scores
    st.session_state["completed"] = True

# --- YÖNETİCİ (EBEVEYN) GİZLİ PANELİ ---
st.markdown("---")
with st.expander("🔒 Ebeveyn / Yönetici Girişi (Analiz Raporu İçin Tıkla)"):
    admin_password = st.text_input("Yönetici Şifresini Girin:", type="password")

    if admin_password == "1453":  # Buradaki şifreyi kendinize göre değiştirebilirsiniz
        if "completed" in st.session_state and st.session_state["completed"]:
            st.subheader("📊 Gizli Analiz ve Değerlendirme Raporu")

            sc = st.session_state["scores"]
            mod1_avg = sum(sc["Modül 1: Duygusal Yük ve Tepkisel Bağlanma"]) / 5
            mod2_avg = sum(sc["Modül 2: STEM ve Alan Uyumu"]) / 5
            mod3_avg = sum(sc["Modül 3: Küresel Vizyon ve Gelecek Projeksiyonu"]) / 5
            mod4_avg = (
                sum(sc["Modül 4: Rasyonel Problem Çözme ve Adaptasyon"]) / 5
            )

            col1, col2 = st.columns(2)
            col1.metric("Duygusal / Tepkisel Yük Skoru", f"{mod1_avg:.1f} / 5.0")
            col1.metric("STEM ve Alan Uyumu", f"{mod2_avg:.1f} / 5.0")
            col2.metric("Küresel Vizyon Skoru", f"{mod3_avg:.1f} / 5.0")
            col2.metric(
                "Rasyonel Adaptasyon Kapasitesi", f"{mod4_avg:.1f} / 5.0"
            )

            st.markdown("---")
            if mod1_avg > 3.5 and mod4_avg < 3.0:
                st.warning(
                    "**Yönetici Notu:** Ali Yiğit'in skorları, kararda mantıksal"
                    " hedeflerden ziyade haksızlığa uğramış olmanın yarattığı"
                    " gurur ve 'pes etmeme' dürtüsünün baskın olduğunu"
                    " gösteriyor. Yaklaşımınızda ona eski okulunun bir"
                    " 'ödül/aidiyet' değil, potansiyelini kısıtlayan bir"
                    " kısıır döngü olduğunu hissettirmeniz gerekebilir."
                )
            elif mod2_avg >= 4.0 and mod3_avg >= 4.0:
                st.info(
                    "**Yönetici Notu:** Zihinsel altyapısı ve STEM uyumu çok"
                    " yüksek. Aklı zaten FenTek ve küresel vizyonu onaylıyor."
                    " Duygusal direnci kırmak için İTÜ'deki projelerini ve"
                    " Amerika hedeflerini ön plana alarak rasyonel bir konuşma"
                    " yapabilirsiniz."
                )
            else:
                st.success(
                    "**Yönetici Notu:** Skorlar dengeli bir geçişe hazır"
                    " olduğunu gösteriyor. Doğru bir yönlendirmeyle FenTek"
                    " geçişini bir 'üst lige çıkış' olarak kabullenecektir."
                )
        else:
            st.info(
                "Henüz Ali Yiğit tarafından tamamlanmış bir anket verisi"
                " bulunmuyor."
            )
    elif admin_password != "":
        st.error("Hatalı şifre!")

import streamlit as st

# --- SAYFA AYARLARI VE KURUMSAL CSS ---
st.set_page_config(page_title="Yatırım Uygunluk Testi", layout="centered")

st.markdown("""
    <style>
    /* 1. ANA ARKA PLAN */
    .stApp { 
        background-color: #F4F7F6; 
        color: #333333; 
        font-family: 'Segoe UI', Arial, sans-serif; 
    }
    
    /* LOGO */
    .stApp::after {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: url("https://www.kuveytturk.com.tr/_assets/svg/logo.svg");
        background-repeat: no-repeat;
        background-position: center center;
        background-size: 650px;
        opacity: 0.10; 
        z-index: 9999; 
        pointer-events: none; 
    }
    
    /* BAŞLIKLAR VE METİNLER */
    h1, h2, h3, h4, h5, h6 { color: #006554 !important; font-weight: 800; letter-spacing: -0.5px; }
    p, span, div, label { color: #333333; } 
    .stSelectbox label { color: #006554 !important; font-size: 15px !important; font-weight: 700 !important; margin-bottom: 5px; }
    
    /* ANA FORM KARTI */
    div[data-testid="stForm"] { 
        background-color: #FFFFFF; 
        border-radius: 12px; 
        padding: 35px; 
        border-top: 6px solid #006554;
        box-shadow: 0px 10px 40px rgba(0, 101, 84, 0.08), 0px -2px 0px #D2A042 inset; 
        position: relative;
        z-index: 10;
    }
    
    /* İnput ve Select Alanları */
    div[data-baseweb="select"] > div { background-color: #FAFAFA !important; color: #333333 !important; border: 1px solid #E0E0E0 !important; border-radius: 8px !important; padding: 6px; transition: all 0.2s; }
    div[data-baseweb="select"] > div:hover { border-color: #D2A042 !important; box-shadow: 0px 0px 5px rgba(210, 160, 66, 0.2) !important; }
    div[data-baseweb="select"] * { color: #333333 !important; background-color: transparent !important; }
    
    /*  BUTONLAR */
    
    /* 1. FORM GÖNDERME BUTONLARI (İleri & Testi Tamamla) */
    button[kind="primaryFormSubmit"] {
        background: linear-gradient(135deg, #006554 0%, #004C3F 100%) !important;
        border: none !important;
        border-bottom: 4px solid #D2A042 !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        min-height: 50px !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
        box-shadow: 0px 4px 10px rgba(0, 101, 84, 0.15) !important;
    }
    button[kind="primaryFormSubmit"] p, 
    button[kind="primaryFormSubmit"] div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 17px !important;
    }
    button[kind="primaryFormSubmit"]:hover {
        transform: translateY(2px) !important;
        border-bottom-width: 2px !important;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.2) !important;
    }

    /* 2. NORMAL BUTONLAR (Geri Dön & Baştan Çöz) */
    button[kind="secondary"] {
        background: #FFFFFF !important;
        border: 2px solid #E0E0E0 !important;
        border-bottom: 4px solid #006554 !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        min-height: 50px !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }
    button[kind="secondary"] p, 
    button[kind="secondary"] div {
        color: #006554 !important;
        font-weight: 700 !important;
        font-size: 17px !important;
    }
    button[kind="secondary"]:hover {
        transform: translateY(2px) !important;
        border-bottom-width: 2px !important;
    }
    
    /* SEÇENEKLER VE KARTLAR */
    div[role="radiogroup"] > label { background-color: #FFFFFF !important; padding: 18px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #EAEAEA !important; border-left: 4px solid #EAEAEA !important; transition: all 0.2s ease-in-out; position: relative; z-index: 10;}
    div[role="radiogroup"] > label p { color: #444444 !important; font-weight: 500;}
    div[role="radiogroup"] > label:hover { border-color: #EAEAEA !important; border-left: 4px solid #D2A042 !important; background-color: #FDFBF7 !important; transform: translateX(3px); }
    
    /* Uyarı Mesajları */
    .stAlert { background-color: #FDFBF7 !important; border-left: 4px solid #D2A042 !important; border-radius: 6px; box-shadow: 0px 2px 10px rgba(0,0,0,0.03);}
    div[data-testid="stAlert"]:has(svg[aria-label="error icon"]) { background-color: #FFF3F3 !important; border-left: 4px solid #DC3545 !important; }
    
    /* Dashboard Metrik Kartları */
    div[data-testid="metric-container"] { background-color: #FFFFFF; border: 1px solid #EAEAEA; border-top: 3px solid #006554; border-radius: 8px; padding: 15px; text-align: center; box-shadow: 0px 4px 12px rgba(0,0,0,0.04); }
    div[data-testid="metric-container"] label { color: #777777 !important; font-weight: 600 !important; font-size: 14px !important; }
    div[data-testid="metric-container"] div { color: #D2A042 !important; font-weight: 800 !important; font-size: 28px !important; }
    
    /* Sonuç Tablosu */
    .sonuc-satir { display: flex; flex-direction: column; padding: 16px; border-bottom: 1px solid #F0F0F0; background-color: #FFFFFF; transition: background 0.2s; position: relative; z-index: 10;}
    .sonuc-satir:hover { background-color: #FDFBF7; }
    .sonuc-satir:first-child { border-top-left-radius: 8px; border-top-right-radius: 8px; border-top: 1px solid #EAEAEA; }
    .sonuc-satir:last-child { border-bottom: 1px solid #EAEAEA; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px; }
    .sonuc-baslik-satiri { display: flex; justify-content: space-between; align-items: center; width: 100%; }
    .grup-ismi { font-weight: 700; font-size: 15px; color: #222222; }
    .gerekce-text { font-size: 13px; color: #888888; margin-top: 6px; display: flex; align-items: center; gap: 5px; font-weight: 500;}
    
    .uygun { color: #006554; font-weight: bold; background-color: #E6F4F1; padding: 5px 14px; border-radius: 20px; font-size: 13px; border: 1px solid #BEE3DB; }
    .uygun-degil { color: #DC3545; font-weight: bold; background-color: #FCEAEA; padding: 5px 14px; border-radius: 20px; font-size: 13px; border: 1px solid #F5C6CB; }
    
    /* Öneri Kartı CSS */
    .oneri-karti { background: linear-gradient(to right, #FDFBF7, #FFFFFF); border: 1px solid #EAEAEA; border-left: 5px solid #D2A042; border-radius: 8px; padding: 22px; margin-top: 25px; margin-bottom: 25px; box-shadow: 0px 4px 12px rgba(0,0,0,0.03); position: relative; z-index: 10; }
    .oneri-baslik { color: #006554; font-weight: 800; font-size: 17px; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
    .oneri-alt-metin { color: #555555; font-size: 14px; margin-bottom: 15px; line-height: 1.5; }
    .oneri-liste { margin-top: 5px; padding-left: 20px; color: #333333; font-weight: 500; font-size: 14px; line-height: 1.8; }
    .oneri-liste li::marker { color: #D2A042; font-size: 18px; }
    
    hr { border-top: 2px dashed #D2A042; margin-top: 25px; margin-bottom: 30px; opacity: 0.5; position: relative; z-index: 10;}
    .urun-baslik { color: #006554; font-weight: 800; font-size: 17px; margin-top: 15px; margin-bottom: 4px; }
    .urun-alt-baslik { color: #D2A042; font-size: 14px; font-weight: 600; margin-bottom: 18px; }
    .ayirici-cizgi { border-top: 1px solid #EEEEEE; margin: 30px 0; }
    </style>
""", unsafe_allow_html=True)

# --- MESLEKLER LİSTESİ (A-Z) ---
meslekler_listesi = [
    "Seçiniz", "Akademisyen", "Aktüer", "Antrenör", "Araştırma Görevlisi", "Asker", "Aşçı", "Avukat", 
    "Bankacı", "Berber / Kuaför", "Bilgisayar Mühendisi", "Bilişim Uzmanı", "Borsacı", "Çiftçi", 
    "Danışman", "Denetçi", "Diş Hekimi", "Diyetisyen", "Doktor", "Eczacı", "Ekonomist", "Emlakçı", 
    "Emekli", "Endüstri Mühendisi", "Esnaf", "Ev Hanımı", "Finansal Analist", "Fizyoterapist", 
    "Gazeteci", "Gemi Kaptanı", "Gümrük Müşaviri", "Güvenlik Görevlisi", "Hakim / Savcı", "Hemşire", 
    "İktisatçı", "İnşaat Mühendisi", "İnsan Kaynakları Uzmanı", "İşçi", "İşletmeci", "İtfaiyeci", 
    "Kasiyer", "Kimyager", "Kurye / Dağıtım Elemanı", "Makine Mühendisi", "Mali Müşavir", 
    "Mimar", "Muhasebeci", "Mühendis (Diğer)", "Müfettiş", "Müteahhit", "Mütercim / Tercüman", 
    "Öğrenci", "Öğretmen", "Pazarlama Uzmanı", "Pilot", "Polis", "Proje Yöneticisi", "Psikolog", 
    "Reklamcı", "Satış Danışmanı", "Sekreter / Asistan", "Sigortacı", "Sporcu", "Şoför", "Tasarımcı", 
    "Teknisyen / Tekniker", "Terzi", "Turizmci / Rehber", "Veteriner", "Yazılımcı / Geliştirici", 
    "Yönetici / CEO", "Ziraat Mühendisi", "Diğer"
]

if 'step' not in st.session_state:
    st.session_state.step = 1

st.markdown("<h2 style='text-align: center; font-size: 32px; position: relative; z-index: 10;'>KUVEYT TÜRK</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D2A042 !important; margin-top: -10px; position: relative; z-index: 10;'>Yeni Nesil Katılım Uygunluk Testi</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='position: relative; z-index: 10;'>SPK tebliğine göre, yatırım kuruluşlarının katılım finans prensiplerine uygun ürün ve hizmetlerin müşteriye uygun olup olmadığını tespit etmek amacıyla uygulamaları gereken testtir.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ==========================================
# 1. ÖZLÜK BİLGİLER VE RİSK TERCİHİ
# ==========================================
if st.session_state.step == 1:
    with st.form("etap1_form"):
        st.subheader("Kişisel Bilgiler")
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Yaş", ["Seçiniz", "18-30 Yaş", "31-50 Yaş", "51-65 Yaş", "66 ve üzeri", "Kurumsal Müşteri"], key="yas")
            st.selectbox("Eğitim Durumu", ["Seçiniz", "İlköğretim/Ortaöğretim", "Lise", "Lisans ve Üstü", "Kurumsal Müşteri"], key="egitim")
        with col2:
            st.selectbox("Meslek", meslekler_listesi, key="meslek")
            st.selectbox("Yatırım Değerlendirme Süresi", ["Seçiniz", "Kısa Vadeli (0-1 Yıl)", "Orta Vadeli (1-3 Yıl)", "Uzun Vadeli (3 Yıl ve Üzeri)"], key="sure")
            
        st.selectbox("Yatırım Tecrübesi", ["Seçiniz", "1 yıldan az", "1-4 yıl", "5-10 yıl", "10 yıldan fazla"], key="tecrube")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Risk ve Getiri Tercihi Seçimi")
        st.info("Lütfen 100.000 TL'lik bir yatırım yaptığınızı varsayarak sizin için en uygun senaryoyu seçiniz:")
        
        st.radio(" ", [
            "1. 100.000 TL anaparamdan hiç kayıp yaşamak istemem. Getirim düşük kalsa bile Kira Sertifikası/Katılma Hesabı ile ilerlerim.",
            "2. 100.000 TL yatırımımda maksimum 5.000 TL'ye kadar (%5) geçici düşüşlere dayanabilirim. Temkinli fonları tercih ederim.",
            "3. 100.000 TL yatırımımda uzun vadede 15.000 TL - 20.000 TL (%15-%20) dalgalanmaları normal karşılar, orta riskli ürünlerde beklerim.",
            "4. Yüksek getiri uğruna 100.000 TL yatırımımın 30.000 TL - 40.000 TL (%30-%40) erimesini göğüsleyebilirim. Agresif hisse fonlarına yatırım yaparım.",
            "5. Çok yüksek getiri için 100.000 TL'nin tamamını kaybetme riskini alır, kompleks katılım ürünlerinde işlem yaparım."
        ], key="risk_tercihi", index=None, label_visibility="collapsed")
        
        st.markdown("<br>", unsafe_allow_html=True)
        ileri_btn = st.form_submit_button("İleri")
        
        if ileri_btn:
            if "Seçiniz" in [st.session_state.yas, st.session_state.egitim, st.session_state.meslek, st.session_state.sure, st.session_state.tecrube] or st.session_state.risk_tercihi is None:
                st.error("⚠️ Lütfen tüm alanları doldurunuz.")
            else:
                st.session_state.kalici_risk_tercihi = st.session_state.risk_tercihi
                st.session_state.step = 2
                st.rerun()

# ==========================================
# 2. ÜRÜN BİLGİSİ VE İŞLEM TECRÜBESİ
# ==========================================
elif st.session_state.step == 2:
    st.subheader("Ürün Bilgisi ve İşlem Tecrübesi")
    st.info("Aşağıdaki ürün gruplarında bilgi ve tecrübe seviyenizi belirtiniz.")
    
    with st.form("etap2_form"):
        st.markdown("<div class='urun-baslik'>1/5 - Çok Düşük Riskli Ürünler</div>", unsafe_allow_html=True)
        st.markdown("<div class='urun-alt-baslik'>Katılma Hesapları, Kısa Vadeli Kira Sertifikaları (Sukuk) vb.</div>", unsafe_allow_html=True)
        st.radio("Bilgi Seviyeniz:", [
            "Bilgim yok: Bu ürünlerin ne olduğunu ve nasıl çalıştığını bilmiyorum.",
            "Bilgim kısıtlı: İsimlerini duydum ama kâr payı dağıtım havuzları ve getiri hesaplamasını tam olarak yapamam.",
            "Yeterince bilgim var: Bu ürünlerin kâr payı mekanizmalarını hesaplar, aktif olarak nakdimi değerlendiririm."
        ], key="bilgi_1", index=None)
        c1, c2 = st.columns(2)
        with c1: st.selectbox("İşlem Sıklığı", ["Seçiniz", "Yılda birkaç kez", "Ayda birkaç kez", "Haftada birkaç kez"], key="siklik_1")
        with c2: st.selectbox("Hacim (TL)", ["Seçiniz", "1 TL - 50.000 TL", "50.001 TL - 500.000 TL", "500.001 TL ve üzeri"], key="hacim_1")
        st.markdown("<div class='ayirici-cizgi'></div>", unsafe_allow_html=True)

        st.markdown("<div class='urun-baslik'>2/5 - Düşük Riskli Ürünler</div>", unsafe_allow_html=True)
        st.markdown("<div class='urun-alt-baslik'>Kamu/Özel Sektör Kira Sertifikaları, Temkinli Katılım Fonları vb.</div>", unsafe_allow_html=True)
        st.radio("Bilgi Seviyeniz:", [
            "Bilgim yok: Bu ürünlerde daha önce hiç işlem yapmadım.",
            "Bilgim kısıtlı: Kira sertifikasının (Sukuk) ne olduğunu biliyorum ama ihraç süreçleri veya fon fiyatlamaları hakkında analiz yapamam.",
            "Yeterince bilgim var: Katılım fonu izahnamelerini okuyabilir, getiri oranlarını kıyaslayıp stratejik olarak fon alım-satımı yapabilirim."
        ], key="bilgi_2", index=None)
        c1, c2 = st.columns(2)
        with c1: st.selectbox("İşlem Sıklığı", ["Seçiniz", "Yılda birkaç kez", "Ayda birkaç kez", "Haftada birkaç kez"], key="siklik_2")
        with c2: st.selectbox("Hacim (TL)", ["Seçiniz", "1 TL - 50.000 TL", "50.001 TL - 500.000 TL", "500.001 TL ve üzeri"], key="hacim_2")
        st.markdown("<div class='ayirici-cizgi'></div>", unsafe_allow_html=True)

        st.markdown("<div class='urun-baslik'>3/5 - Orta Riskli Ürünler</div>", unsafe_allow_html=True)
        st.markdown("<div class='urun-alt-baslik'>Katılım Endeksi Hisse Senetleri, Katılım Hisse Fonları, Kıymetli Madenler vb.</div>", unsafe_allow_html=True)
        st.radio("Bilgi Seviyeniz:", [
            "Bilgim yok: Borsada veya hisse katılım fonlarında hiç işlem yapmadım.",
            "Bilgim kısıtlı: Hisse senedi alıp satabilirim ama şirket bilançosu okuyamam veya KAP bildirimlerini detaylı analiz edemem.",
            "Yeterince bilgim var: Şirketlerin temel analizini (F/K, PD/DD, FAVÖK) yapabilir, makroekonomik verilere göre hisse portföyümü aktif yönetebilirim."
        ], key="bilgi_3", index=None)
        c1, c2 = st.columns(2)
        with c1: st.selectbox("İşlem Sıklığı", ["Seçiniz", "Yılda birkaç kez", "Ayda birkaç kez", "Haftada birkaç kez"], key="siklik_3")
        with c2: st.selectbox("Hacim (TL)", ["Seçiniz", "1 TL - 50.000 TL", "50.001 TL - 500.000 TL", "500.001 TL ve üzeri"], key="hacim_3")
        st.markdown("<div class='ayirici-cizgi'></div>", unsafe_allow_html=True)

        st.markdown("<div class='urun-baslik'>4/5 - Yüksek Riskli Ürünler</div>", unsafe_allow_html=True)
        st.markdown("<div class='urun-alt-baslik'>Agresif Katılım Fonları, Uluslararası Katılım Fonları vb.</div>", unsafe_allow_html=True)
        st.radio("Bilgi Seviyeniz:", [
            "Bilgim yok: Yurtdışı piyasalarda veya agresif büyüme odaklı fonlarda hiç bulunmadım.",
            "Bilgim kısıtlı: Global teknoloji hisselerini/fonlarını duydum ancak uluslararası piyasa risklerini, kur dalgalanmalarını veya yüksek volatiliteyi yönetemem.",
            "Yeterince bilgim var: Uluslararası piyasalardaki pozisyon büyüklüğümü hesaplayabilir, küresel makroekonomik verilere göre strateji kurabilir ve yüksek volatiliteyi profesyonelce yönetebilirim."
        ], key="bilgi_4", index=None)
        c1, c2 = st.columns(2)
        with c1: st.selectbox("İşlem Sıklığı", ["Seçiniz", "Yılda birkaç kez", "Ayda birkaç kez", "Haftada birkaç kez"], key="siklik_4")
        with c2: st.selectbox("Hacim (TL)", ["Seçiniz", "1 TL - 50.000 TL", "50.001 TL - 500.000 TL", "500.001 TL ve üzeri"], key="hacim_4")
        st.markdown("<div class='ayirici-cizgi'></div>", unsafe_allow_html=True)
            
        st.markdown("<div class='urun-baslik'>5/5 - Çok Yüksek Riskli Ürünler</div>", unsafe_allow_html=True)
        st.markdown("<div class='urun-alt-baslik'>Serbest Katılım Fonları, Girişim Sermayesi Yatırım Fonları vb.</div>", unsafe_allow_html=True)
        st.radio("Bilgi Seviyeniz:", [
            "Bilgim yok: Serbest fonlarda veya yapılandırılmış özel fonlarda işlem yapmadım.",
            "Bilgim kısıtlı: Serbest katılım fonlarını duydum ancak bu kompleks varlıkların barındırdığı düşük likidite ve yüksek anapara kaybı risklerini yönetemem.",
            "Yeterince bilgim var: Nitelikli yatırımcılara özel serbest fonlarda strateji kurabilir, portföy çeşitlendirmesi ile karmaşık risk/getiri senaryolarını profesyonelce yönetebilirim."
        ], key="bilgi_5", index=None)
        c1, c2 = st.columns(2)
        with c1: st.selectbox("İşlem Sıklığı", ["Seçiniz", "Yılda birkaç kez", "Ayda birkaç kez", "Haftada birkaç kez"], key="siklik_5")
        with c2: st.selectbox("Hacim (TL)", ["Seçiniz", "1 TL - 50.000 TL", "50.001 TL - 500.000 TL", "500.001 TL ve üzeri"], key="hacim_5")

        st.markdown("<br>", unsafe_allow_html=True)
        tamamla_btn = st.form_submit_button("Testi Tamamla")
        
        if tamamla_btn:
            hata_var = False
            for i in range(1, 6):
                if st.session_state[f"bilgi_{i}"] is None or st.session_state[f"siklik_{i}"] == "Seçiniz" or st.session_state[f"hacim_{i}"] == "Seçiniz":
                    hata_var = True
            
            if hata_var:
                st.error("⚠️ Lütfen tüm ürün gruplarındaki bilgi, sıklık ve hacim alanlarını yanıtlayın.")
            else:
                for i in range(1, 6):
                    st.session_state[f"kalici_bilgi_{i}"] = st.session_state[f"bilgi_{i}"]
                    st.session_state[f"kalici_siklik_{i}"] = st.session_state[f"siklik_{i}"]
                    st.session_state[f"kalici_hacim_{i}"] = st.session_state[f"hacim_{i}"]
                st.session_state.step = 3
                st.rerun()
                
    if st.button("⬅️ Geri Dön"):
        st.session_state.step = 1
        st.rerun()

# ==========================================
# 3. SONUÇLAR VE ÖNERİLER
# ==========================================
elif st.session_state.step == 3:
    st.success("✅ Risk profilleme algoritması başarıyla tamamlandı.")
    
    risk_skoru = int(st.session_state.kalici_risk_tercihi[0])
    gruplar = ["Çok Düşük Riskli", "Düşük Riskli", "Orta Riskli", "Yüksek Riskli", "Çok Yüksek Riskli"]
    
    sonuclar = []
    onaylanan_sayisi = 0
    
    for i, grup in enumerate(gruplar, start=1):
        risk_yeterli = risk_skoru >= i
        bilgi_yeterli = True
        tecrube_yeterli = True
        gerekceler = []
        
        cevap_bilgi = st.session_state[f"kalici_bilgi_{i}"]
        cevap_siklik = st.session_state[f"kalici_siklik_{i}"]
        cevap_hacim = st.session_state[f"kalici_hacim_{i}"]
        
        if not risk_yeterli: gerekceler.append("Risk İştahı Uyumsuz")
            
        if "Bilgim yok" in cevap_bilgi:
            bilgi_yeterli = False; gerekceler.append("Teorik Bilgi Eksik")
        elif "Bilgim kısıtlı" in cevap_bilgi:
            if i > 2: bilgi_yeterli = False; gerekceler.append("Teorik Bilgi Yetersiz")
                
        if i >= 4:
            if cevap_siklik == "Yılda birkaç kez" or cevap_hacim == "1 TL - 50.000 TL":
                tecrube_yeterli = False; gerekceler.append("Pratik Tecrübe Yetersiz")
                
        is_uygun = risk_yeterli and bilgi_yeterli and tecrube_yeterli
        if is_uygun: onaylanan_sayisi += 1
        
        sonuclar.append({
            "grup": grup,
            "uygun": is_uygun,
            "gerekce_metni": "SPK Kriterleri Sağlandı" if is_uygun else " & ".join(gerekceler)
        })

    st.markdown("<div style='position: relative; z-index: 10;'>", unsafe_allow_html=True)
    st.markdown("### 📊 Yönetici Özeti & Sonuçlar")
    m1, m2, m3 = st.columns(3)
    with m1: st.metric(label="Risk Skorunuz", value=f"{risk_skoru} / 5")
    with m2: st.metric(label="Onaylanan Ürün Grubu", value=f"{onaylanan_sayisi}")
    with m3: st.metric(label="Kısıtlanan Ürün Grubu", value=f"{5 - onaylanan_sayisi}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 25px; position: relative; z-index: 10;'>", unsafe_allow_html=True)
    for sonuc in sonuclar:
        durum_class = "uygun" if sonuc["uygun"] else "uygun-degil"
        durum_text = "Uygun" if sonuc["uygun"] else "Uygun Değil"
        ikon = "✅" if sonuc["uygun"] else "🔒"
        
        st.markdown(f"""
        <div class='sonuc-satir'>
            <div class='sonuc-baslik-satiri'>
                <span class='grup-ismi'>{sonuc["grup"]}</span>
                <span class='{durum_class}'>{durum_text}</span>
            </div>
            <div class='gerekce-text'>{ikon} Sistem Gerekçesi: <strong>{sonuc["gerekce_metni"]}</strong></div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # --- VARLIK ÖNERİ MOTORU ---
    oneri_veritabani = {
        1: ["Klasik Katılma Hesapları (TL/Döviz/Altın)", "Kısa Vadeli Kamu Kira Sertifikaları (Sukuk)", "Fiziki Altın/Gümüş Cari Hesapları"],
        2: ["KT Portföy Kısa Vadeli Katılım Fonları", "Özel Sektör Kira Sertifikaları (Sukuk)", "Uzun Vadeli Katılma Hesapları"],
        3: ["KT Portföy Kıymetli Madenler Katılım Fonları", "Karma Katılım Fonları", "BIST Katılım 30 Endeksi Hisseleri"],
        4: ["KT Portföy Hisse Senedi Katılım Fonları", "Sürdürülebilirlik/Teknoloji Fonları", "BIST Tüm Katılım Endeksi Hisseleri"],
        5: ["KT Portföy Serbest Katılım Fonları", "Kuveyt Türk GSYF (Girişim Sermayesi)", "Özel Bankacılık Yapılandırılmış Ürünleri"]
    }
    
    liste_html = ""
    # SONUÇ VE ÖNERİLERİ LİSTELEME
    for i, sonuc in enumerate(sonuclar, start=1):
        if sonuc["uygun"]:
            urunler = ", ".join(oneri_veritabani[i])
            liste_html += f"<li><span style='color: #006554; font-weight: bold;'>Risk Seviyesi {i}:</span> {urunler}</li>"
            
    # Eğer müşteri hiçbir seviyeden geçemezse (Çok nadir ama Mümkün):
    if liste_html == "":
        liste_html = "<li>Mevcut bilgi ve tecrübe eksikliğiniz nedeniyle şu aşamada işlem yapabileceğiniz uygun bir varlık sınıfı bulunamamıştır. Yatırım temsilcinizden destek alabilirsiniz.</li>"
    
    st.markdown(f"""
        <div class="oneri-karti">
            <div class="oneri-baslik">🎯 Size Özel Kuveyt Türk Yatırım Sepeti</div>
            <div class="oneri-alt-metin">Uygunluk testi algoritmamız sonucunda, risk profilinize ve tecrübenize istinaden işlem yapmanızın <b>uygun bulunduğu</b> varlık grupları aşağıda listelenmiştir:</div>
            <ul class="oneri-liste">
                {liste_html}
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    profil_metinleri = {
        1: "Finansal kayba karşı yüksek hassasiyetiniz var. Enflasyon riskinden ziyade anapara koruması sizin için psikolojik olarak daha güven verici.",
        2: "Temkinli bir yatırımcısınız. Piyasayı takip ediyor ancak büyük dalgalanmalarda stres yaşamak istemediğiniz için kontrollü ilerliyorsunuz.",
        3: "Dengeli bir risk algınız var. Kâr/zarar ortaklığının doğasını kavramış, uzun vadeli trendlere odaklanan analitik bir yapıya sahipsiniz.",
        4: "Büyüme odaklısınız. Yüksek kazanç potansiyeli için anlık portföy erimelerini (drawdown) psikolojik olarak yönetebilecek finansal dayanıklılığa sahipsiniz.",
        5: "Agresif ve profesyonel bir risksever profilsiniz. Spekülatif dalgalanmalar sizi korkutmuyor; aksine kompleks yatırım araçlarında fırsat görüyorsunuz."
    }
    
    st.info(f"**💡 Davranışsal Finans Profiliniz:** {profil_metinleri[risk_skoru]}")
    st.warning("ℹ️ Verdiğim bilgilerin doğru olduğunu ve bunlar doğrultusunda yapılan değerlendirme sonuçlarının yatırımlarıma yön vereceğini kabul ediyorum.")
    
    if st.button("🔄 Testi Baştan Çöz"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.session_state.step = 1
        st.rerun()
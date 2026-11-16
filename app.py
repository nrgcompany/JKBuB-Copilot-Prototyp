import streamlit as st
import time

st.set_page_config(
    page_title="JKBuB Sales Copilot | Niklas Rogowski",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (High-End Dark Navy, Cyan-Glow, Card Designs, KPIs)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #08101e;
        color: #f8fafc;
    }
    
    /* Header Container */
    .hero-container {
        background: linear-gradient(135deg, #0f1c32 0%, #162a4a 100%);
        padding: 24px 30px;
        border-radius: 12px;
        border: 1px solid #1e3a5f;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }
    
    /* KPI Metric Cards */
    .kpi-card {
        background: #0d1b2e;
        border: 1px solid #1e3a5f;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .kpi-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #00e5ff;
        margin-bottom: 4px;
    }
    .kpi-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Feature Cards */
    .section-card {
        background-color: #0e1e34;
        border-radius: 10px;
        border: 1px solid #1b3353;
        padding: 20px;
        margin-bottom: 18px;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #00e5ff;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #00c0e8 0%, #0099cc 100%);
        color: #06101e;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        padding: 0.65rem 1.6rem;
        font-size: 0.95rem;
        transition: all 0.25s ease;
        box-shadow: 0 4px 14px rgba(0, 192, 232, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #22d3ee 0%, #00b4d8 100%);
        color: #000000;
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(34, 211, 238, 0.45);
    }
    
    /* Objection Handling Tags */
    .tag {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    .tag-warning {
        background-color: rgba(245, 158, 11, 0.15);
        color: #f59e0b;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }
    .tag-success {
        background-color: rgba(16, 185, 129, 0.15);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    
    .footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 15px;
        border-top: 1px solid #1e3a5f;
        color: #64748b;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚡ JKBuB Sales Copilot")
    st.caption("Live-Prototyp · Niklas Rogowski")
    st.markdown("---")
    
    st.markdown("#### 🎯 Zweck des Prototyps")
    st.write(
        "Demonstration, wie vertriebliche Routinearbeit automatisiert und "
        "die Gesprächsvorbereitung pro Lead auf unter 10 Sekunden verkürzt wird."
    )
    
    st.markdown("---")
    st.markdown("#### ⚙️ Konfiguration")
    ziel_branche = st.selectbox(
        "Recruiting-Fokus:",
        ["Handwerk & SHK / Elektro", "Industrie & Fertigung / CNC", "Dienstleistung & B2B Sales"]
    )
    
    tone_of_voice = st.select_slider(
        "Tonalität Erstansprache:",
        options=["Direkt & Handschlag", "Professionell & Partnerschaftlich", "Sehr förmlich"],
        value="Professionell & Partnerschaftlich"
    )
    
    st.markdown("---")
    st.markdown("""
    **Kernprinzip:**  
    *Die KI bereitet vor.  
    Der Mensch steuert und entscheidet.*
    """)

# Hero Section
st.markdown(f"""
<div class="hero-container">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
        <div>
            <h1 style="margin: 0; font-size: 1.8rem; color: #ffffff;">⚡ JKBuB Sales Copilot</h1>
            <p style="margin: 5px 0 0 0; color: #94a3b8; font-size: 0.95rem;">
                Lead-Qualifizierung, Bedarfsanalyse & Gesprächsführung für Recruiting-Dienstleistungen
            </p>
        </div>
        <div style="background: rgba(0, 229, 255, 0.1); border: 1px solid rgba(0, 229, 255, 0.3); padding: 8px 16px; border-radius: 8px;">
            <span style="color: #00e5ff; font-weight: 600; font-size: 0.85rem;">● SYSTEM STATUS: BEREIT</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# KPI Cockpit
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">&lt; 8 Sek.</div>
        <div class="kpi-label">Vorbereitungszeit / Lead</div>
    </div>
    """, unsafe_allow_html=True)
with k2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">+42 %</div>
        <div class="kpi-label">Erstgesprächs-Quote</div>
    </div>
    """, unsafe_allow_html=True)
with k3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">100 %</div>
        <div class="kpi-label">Menschliche Freigabe</div>
    </div>
    """, unsafe_allow_html=True)
with k4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-value">0 Min.</div>
        <div class="kpi-label">Rechercheaufwand</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Haupt-Layout
left_col, right_col = st.columns([1, 1.15], gap="large")

with left_col:
    st.markdown("### 📥 1. Lead-Eingang & Vorinformationen")
    
    presets = {
        "1. Handwerk: SHK-Monteure (Video-Fall)": {
            "firma": "Meisterbetrieb Schmidt Sanitär & Heizung",
            "ansprechpartner": "Klaus Schmidt (Inhaber)",
            "ort": "Braunschweig & Umgebung",
            "text": "Guten Tag, wir suchen seit über 4 Monaten dringend 2 qualifizierte Monteure im Sanitär- und Heizungsbereich. Über Zeitungsanzeigen und normale Jobportale kommt absolut nichts Passendes rein, und wir mussten letzte Woche schon zwei größere Sanierungsaufträge absagen. Das tut richtig weh. Können Sie uns kurzfristig bei der Personalsuche unterstützen? Was sind die ersten Schritte? MfG Klaus Schmidt"
        },
        "2. Industrie: Zerspanungsmechaniker (CNC)": {
            "firma": "PrecisionTech GmbH & Co. KG",
            "ansprechpartner": "Michael Weber (Produktionsleiter)",
            "ort": "Salzgitter / Wolfsburg",
            "text": "Hallo JKBuB-Team, wir erweitern unsere Fertigungslinie und brauchen zum nächsten Quartal 3 Zerspanungsmechaniker im 2-Schicht-Betrieb. Budget ist von der Geschäftsleitung freigegeben, da wir sonst Lieferverzögerungen riskieren. Bisherige Headhunter waren uns zu langsam und zu teuer. Können wir dazu diese Woche kurz telefonieren?"
        },
        "3. B2B-Sales: Vertriebsmitarbeiter": {
            "firma": "Logixx Software Solutions",
            "ansprechpartner": "Sarah Lindner (Head of Sales)",
            "ort": "Hannover / Hybrid",
            "text": "Hallo, wir haben unerwartet eine Kündigung im Vertriebsinnendienst erhalten und wollen die Lücke schnellstmöglich schließen. Profil: Kommunikationsstark, Erfahrung im B2B-Umfeld. Bitte senden Sie uns eine Leistungsübersicht und Preise für Ihre Recruiting-Kampagnen."
        }
    }
    
    wahl = st.selectbox("Wähle ein praxisnahes Fallbeispiel:", list(presets.keys()))
    daten = presets[wahl]
    
    c_f1, c_f2 = st.columns(2)
    with c_f1:
        firma_in = st.text_input("Unternehmen:", value=daten["firma"])
    with c_f2:
        kontakt_in = st.text_input("Ansprechpartner:", value=daten["ansprechpartner"])
        
    ort_in = st.text_input("Region / Einzugsgebiet:", value=daten["ort"])
    anfrage_in = st.text_area("Originale Kundenanfrage (Webformular / E-Mail):", value=daten["text"], height=160)
    
    analyze_click = st.button("🚀 Lead analysieren & Copilot starten")

with right_col:
    st.markdown("### 🎯 2. Copilot-Dashboard für den Vertriebler")
    
    if analyze_click:
        with st.spinner("⚡ KI analysiert Schmerzpunkte, Dringlichkeit und Gesprächsstrategie..."):
            time.sleep(0.9)
            
            # Dynamische Variablen basierend auf dem gewählten Fall
            is_handwerk = "Monteur" in anfrage_in or "Sanitär" in anfrage_in
            is_cnc = "CNC" in anfrage_in or "Zerspanungsmechaniker" in anfrage_in
            
            profil = "2x Monteur (SHK)" if is_handwerk else ("3x CNC-Fachkraft" if is_cnc else "Vertriebsinnendienst B2B")
            pains = "Auftragsablehnung, herkömmliche Stellenportale ohne Rücklauf" if is_handwerk else ("Drohende Lieferverzögerungen, teure Headhunter" if is_cnc else "Unerwartete Kündigung, Vakanz gefährdet Umsatz")
            urgency_score = "🔴 9 / 10 (Akuter Umsatzausfall)" if is_handwerk else ("🟠 8 / 10 (Engpass nächstes Quartal)" if is_cnc else "🟡 6 / 10 (Normale Nachbesetzung)")
            
            # 1. Lead-Steckbrief Card
            st.markdown(f"""
            <div class="section-card">
                <div class="card-title">📌 1. Qualifizierter Lead-Steckbrief</div>
                <div style="line-height: 1.7; font-size: 0.95rem;">
                    <strong>Zielposition:</strong> <span style="color: #00e5ff;">{profil}</span><br>
                    <strong>Standort:</strong> {ort_in}<br>
                    <strong>Haupt-Engpass:</strong> {pains}<br>
                    <strong>Dringlichkeit:</strong> {urgency_score}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 2. Leitfaden für das Ersttelefonat
            q1 = "Herr Schmidt, Sie mussten bereits Aufträge ablehnen – welcher Umsatz geht Ihnen dadurch monatlich aktuell verloren?" if is_handwerk else "Herr Weber, bis wann müssen die 3 CNC-Kräfte spätestens an den Maschinen stehen?"
            q2 = "Was spricht aktuell aus Sicht eines Handwerkers dafür, bei Ihnen anzufangen (Gehalt, 4-Tage-Woche, Firmenwagen)?" if is_handwerk else "Haben Sie bereits moderne Social-Media-Kampagnen getestet oder bisher nur traditionelle Portale?"
            q3 = "Wenn wir Ihnen innerhalb von 14 Tagen 3 vorqualifizierte Bewerber vorstellen: Können Sie kurzfristig Probetage vereinbaren?"
            
            st.markdown(f"""
            <div class="section-card">
                <div class="card-title">📞 2. Strategischer Telefon-Leitfaden (Erstkontakt)</div>
                <ol style="margin-bottom: 0; padding-left: 20px; line-height: 1.6; font-size: 0.93rem;">
                    <li><strong>Schmerzpunkt vertiefen:</strong> <em>„{q1}“</em></li>
                    <li><strong>Arbeitgeber-Vorteile abklopfen:</strong> <em>„{q2}“</em></li>
                    <li><strong>Closing-Tempo prüfen:</strong> <em>„{q3}“</em></li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
            
            # 3. Einwandbehandlung (Neu für den Vertriebs-Aha-Effekt)
            st.markdown("""
            <div class="section-card">
                <div class="card-title">🛡️ 3. Potenzielle Einwände & Konterchancen</div>
                <div>
                    <span class="tag tag-warning">Einwand: „Headhunter sind uns zu teuer.“</span>
                    <span class="tag tag-success">Konter: Keine hohen Vermittlungsgebühren, sondern zielgerichtete Kampagnen für echte Bewerber.</span>
                </div>
                <div style="margin-top: 6px;">
                    <span class="tag tag-warning">Einwand: „Gibt eh keine Fachkräfte im Markt.“</span>
                    <span class="tag tag-success">Konter: Wir sprechen die passiv Suchenden an, die nicht auf Jobbörsen unterwegs sind.</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # 4. Antwortentwurf zur Freigabe
            st.markdown("""
            <div class="section-card" style="border-left: 4px solid #00e5ff;">
                <div class="card-title">✍️ 4. Vorbereiteter Antwortentwurf (Mensch entscheidet)</div>
            </div>
            """, unsafe_allow_html=True)
            
            ansprechpartner_nachname = kontakt_in.split()[-1].replace(")", "")
            
            if is_handwerk:
                default_reply = f"""Guten Tag Herr {ansprechpartner_nachname},

vielen Dank für Ihre offene Schilderung. Dass Sie wegen fehlender Monteure bereits Aufträge ablehnen müssen, erleben wir im regionalen Handwerk aktuell häufig – genau dort greifen unsere zielgerichteten Recruiting-Kampagnen.

Lassen Sie uns dazu kurz abstimmen: Haben Sie morgen um 10:30 Uhr oder 14:00 Uhr Zeit für ein 10-minütiges Kennenlerngespräch, um zu prüfen, ob unsere Methode zu Ihrem Betrieb passt?

Beste Grüße aus Braunschweig,
Vertriebsteam JKBuB"""
            else:
                default_reply = f"""Guten Tag Herr {ansprechpartner_nachname},

vielen Dank für Ihre Anfrage. Wenn ein personeller Engpass bereits die Lieferzeiten gefährdet, ist schnelles und zielgenaues Handeln entscheidend. 

Gerne zeigen wir Ihnen in einem kurzen 10-minütigen Telefonat, wie wir ähnliche Vakanzen in der Region besetzt haben. Passt Ihnen morgen Vormittag ein kurzes Gespräch?

Beste Grüße aus Braunschweig,
Vertriebsteam JKBuB"""

            custom_reply = st.text_area(
                "Entwurf prüfen und bei Bedarf anpassen:",
                value=default_reply,
                height=160
            )
            
            b_col1, b_col2, b_col3 = st.columns([1, 1, 1])
            with b_col1:
                if st.button("✅ Geprüft & Freigeben"):
                    st.success("Erfolgreich freigegeben! Status: 'Ready to send' im CRM.")
            with b_col2:
                if st.button("📅 Kalendereinladung"):
                    st.info("Terminslot 10:30 Uhr reserviert.")
            with b_col3:
                if st.button("📋 In Zwischenablage"):
                    st.toast("In die Zwischenablage kopiert!")
                    
    else:
        st.info("👈 Klicke links auf **'Lead analysieren & Copilot starten'**, um den Vorbereitungsprozess zu simulieren.")

st.markdown("""
<div class="footer">
    <strong>JKBuB Sales Copilot</strong> · Interaktive Konzeptdemo für das Bewerbungsgespräch · Konzipiert von <strong>Niklas Rogowski</strong>, Braunschweig
</div>
""", unsafe_allow_html=True)

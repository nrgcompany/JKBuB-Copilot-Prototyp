import json
import time
import streamlit as st

st.set_page_config(
    page_title="JKBuB Sales Copilot | Niklas Rogowski",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling (Dark Navy & Cyan passend zum Video)
st.markdown(
    """
<style>
    .main {
        background-color: #0b1526;
        color: #f1f5f9;
    }
    .stButton>button {
        background-color: #00bcd4;
        color: #0b1526;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.5rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #26c6da;
        color: #000000;
        box-shadow: 0 4px 12px rgba(0, 188, 212, 0.4);
    }
    .card {
        background-color: #132238;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #00bcd4;
        margin-bottom: 20px;
    }
    .footer-note {
        font-size: 0.8rem;
        color: #64748b;
        text-align: center;
        margin-top: 30px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
  st.title("Sales Copilot")
  st.caption("Konzeptdemo von Niklas Rogowski")
  st.markdown("---")
  demo_mode = st.toggle("Demo-Modus (ohne API-Key)", value=True)
  api_key = ""
  if not demo_mode:
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Wird nur temporär für diesen Aufruf genutzt.",
    )
  st.markdown("---")
  st.info(
      "💡 **Grundprinzip:** Die KI bereitet vor – der Mensch prüft, steuert und"
      " entscheidet."
  )

# Header
st.title("💼 KI-Vertriebsassistent für JKBuB")
st.subheader(
    "Schnelle Qualifizierung & Gesprächsvorbereitung für eingehende Leads"
)
st.markdown("---")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
  st.markdown("### 📥 1. Eingehende Anfrage")
  beispiel_anfragen = {
      (
          "Handwerk: Monteure (Video-Beispiel)"
      ): (
          "Wir suchen seit über 4 Monaten dringend 2 qualifizierte Monteure"
          " im Sanitär- und Heizungsbereich für unsere Baustellen im Raum"
          " Braunschweig. Über Zeitungsanzeigen und normale Portale kommt"
          " absolut nichts Brauchbares rein. Wir müssen schon Aufträge"
          " ablehnen. Können Sie uns kurzfristig helfen? MfG, Meisterbetrieb"
          " Schmidt"
      ),
      (
          "Industrie: CNC-Fachkraft"
      ): (
          "Guten Tag, wir expandieren und benötigen zum nächsten Quartal 3"
          " erfahrene CNC-Fräser im 2-Schicht-Betrieb. Budget für"
          " Personalsuche ist freigegeben, da der Engpass unsere"
          " Lieferzeiten gefährdet. Bitte um Rückruf zwecks Erstberatung."
      ),
      (
          "Dienstleistung: Vertriebsinnendienst"
      ): (
          "Hallo, wir haben kurzfristig eine Kündigung im Vertriebsinnendienst"
          " erhalten. Brauchen jemanden mit CRM-Erfahrung und"
          " Verhandlungsgeschick. Was kostet ein Recruiting-Paket bei Ihnen?"
      ),
  }

  auswahl = st.selectbox(
      "Beispiel laden oder selbst schreiben:", list(beispiel_anfragen.keys())
  )
  user_input = st.text_area(
      "Kundenanfrage:", value=beispiel_anfragen[auswahl], height=180
  )
  anfrager_name = st.text_input(
      "Absender / Ansprechpartner:",
      value="Meisterbetrieb Schmidt (Herr Schmidt)",
  )
  analysieren = st.button("🚀 Anfrage analysieren & vorbereiten")

with col2:
  st.markdown("### 📊 2. Vorbereitungskarte für den Vertriebler")

  if analysieren:
    with st.spinner(
        "KI extrahiert Bedarfe und strukturiert den Erstkontakt..."
    ):
      time.sleep(1.2)  # Natürliches Ladegefühl

      bedarf = (
          "2 Monteure (Sanitär/Heizung)"
          if "Monteur" in user_input
          else "Fachkräfte gemäß Anfrage"
      )
      dringlichkeit = (
          "🔴 Hoch (Aufträge werden bereits abgelehnt)"
          if "ablehnen" in user_input or "dringend" in user_input
          else "🟡 Mittel"
      )

      st.markdown(
          f"""
            <div class="card">
                <h4 style="color: #00bcd4; margin-top: 0;">1. Lead-Steckbrief</h4>
                <p><strong>Zielprofil:</strong> {bedarf}<br>
                <strong>Hauptproblem:</strong> Herkömmliche Portale ohne Rücklauf, Auftragsstau<br>
                <strong>Dringlichkeit:</strong> {dringlichkeit}</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

      st.markdown(
          """
            <div class="card">
                <h4 style="color: #00bcd4; margin-top: 0;">2. Leitfaden für das Ersttelefonat</h4>
                <ul>
                    <li><strong>Anforderung:</strong> Welche konkreten Scheine/Erfahrungen sind für den Sofortstart zwingend erforderlich?</li>
                    <li><strong>Bisherige Kanäle:</strong> Wo wurde bisher inseriert und wie sieht die aktuelle Arbeitgeber-Attraktivität/Benefits aus?</li>
                    <li><strong>Entscheidungstempo:</strong> Wer führt neben Herrn Schmidt das Bewerbungsgespräch und wie schnell kann eingestellt werden?</li>
                </ul>
            </div>
            """,
          unsafe_allow_html=True,
      )

      st.markdown(
          """
            <div class="card">
                <h4 style="color: #00bcd4; margin-top: 0;">3. Personalisierter Antwortentwurf</h4>
            </div>
            """,
          unsafe_allow_html=True,
      )

      default_draft = f"""Guten Tag Herr Schmidt,

vielen Dank für Ihre Anfrage. Dass Sie bereits Aufträge ablehnen müssen, hören wir im Handwerk derzeit häufig – genau an dieser Engpass-Stelle setzen wir mit unseren zielgerichteten Recruiting-Kampagnen an.

Lassen Sie uns dazu kurz abstimmen: Haben Sie morgen um 10:30 Uhr oder 14:00 Uhr Zeit für ein 10-minütiges Telefonat, um die Rahmenbedingungen kurz abzustecken?

Beste Grüße aus Braunschweig,
Vertriebsteam JKBuB"""

      edited_draft = st.text_area(
          "Entwurf anpassen (Der Mensch entscheidet):",
          value=default_draft,
          height=180,
      )

      col_b1, col_b2 = st.columns(2)
      with col_b1:
        if st.button("✅ Geprüft & Freigeben"):
          st.success(
              "Erfolgreich freigegeben! Entwurf ist im System hinterlegt."
          )
      with col_b2:
        if st.button("📞 Termin vormerken"):
          st.info("Terminvorschlag in Kalender übernommen.")
  else:
    st.info(
        "Klicke links auf **'Anfrage analysieren & vorbereiten'**, um den"
        " Assistenten zu starten."
    )

st.markdown(
    """
<div class="footer-note">
    Konzeptdemo · fiktive Beispieldaten · Erstellt von Niklas Rogowski für JKBuB Vertrieb Braunschweig
</div>
""",
    unsafe_allow_html=True,
)
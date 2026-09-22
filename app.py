import datetime
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Borah Service - Kaziranga Safari Booking",
    page_icon="🐅",
    layout="centered",
)

# Custom Luxury Dark Theme CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #09090b;
        color: #f4f4f5;
        max-width: 450px;
        margin: 0 auto;
    }
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif;
        color: #ffffff !important;
    }
    .gold-text {
        color: #d4af37 !important;
    }
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #aa771c 100%) !important;
        color: #09090b !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
        width: 100%;
        padding: 0.6rem;
    }
    .glass-card {
        background: rgba(18, 18, 22, 0.85);
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session State Data
if "packages" not in st.session_state:
  st.session_state.packages = [
      {
          "title": "Kohora Central Range",
          "price": 3500,
          "desc": (
              "Famous for high density of One-horned Rhinos and lush green"
              " swamp forests."
          ),
          "img": (
              "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?q=80&w=800&auto=format&fit=crop"
          ),
      },
      {
          "title": "Bagori Western Range",
          "price": 3800,
          "desc": (
              "Known for close encounters with rhinos and breathtaking"
              " riverine landscapes."
          ),
          "img": (
              "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?q=80&w=800&auto=format&fit=crop"
          ),
      },
      {
          "title": "Agoratoli Eastern Range",
          "price": 4000,
          "desc": (
              "A haven for bird watchers and water buffaloes with pristine"
              " wetland ecosystems."
          ),
          "img": (
              "https://images.unsplash.com/photo-1549366021-9f761d450615?q=80&w=800&auto=format&fit=crop"
          ),
      },
  ]

if "guides" not in st.session_state:
  st.session_state.guides = [
      {
          "name": "Dipen Saikia",
          "role": "Senior Jeep Pilot • +91 98765 43210",
      },
      {
          "name": "Bhaben Hazarika",
          "role": "Wildlife Tracker • +91 91234 56789",
      },
  ]

if "admin_logged_in" not in st.session_state:
  st.session_state.admin_logged_in = False

# Header & Visitor Counter Badge
col1, col2 = st.columns([2, 2])
with col1:
  st.markdown(
      "<h2 style='margin:0; color:#d4af37;'>Borah Service</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='margin:0; font-size:10px; color:#a1a1aa;'>KAZIRANGA"
      " EXPEDITIONS</p>",
      unsafe_allow_html=True,
  )
with col2:
  st.markdown(
      '<div style="text-align: right; padding-top: 5px;"><img'
      ' src="https://visitor-badge.laobi.icu/badge?page_id=borah_service_kaziranga_app"'
      ' alt="Visitor Count"/></div>',
      unsafe_allow_html=True,
  )

# Bottom Navigation using Radio Buttons (Styled as Tabs)
selected_tab = st.radio(
    "Navigation",
    ["Home", "Booking", "Admin", "Owner"],
    horizontal=True,
    label_visibility="collapsed",
)

st.markdown("---")

# 1. HOME TAB
if selected_tab == "Home":
  st.markdown(
      """
        <div style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.8)), url('https://images.unsplash.com/photo-1534188753412-3e26d1d618d6?q=80&w=1000&auto=format&fit=crop'); background-size: cover; padding: 30px; border-radius: 15px; border: 1px solid rgba(212, 175, 55, 0.3); margin-bottom: 20px;">
            <span style="background: rgba(212,175,55,0.2); color: #d4af37; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold;">LUXURY WILDERNESS</span>
            <h3 style="color: white; margin-top: 10px;">Experience Kaziranga's Majesty</h3>
            <p style="font-size: 11px; color: #d4d4d8;">Exclusive Jeep & Elephant safaris curated by Somnath Borah.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown("### Featured Safaris")

  for i, pkg in enumerate(st.session_state.packages):
    with st.container():
      st.markdown(
          f"""
                <div class="glass-card">
                    <img src="{pkg['img']}" style="width:100%; height:140px; object-fit:cover; border-radius:8px; margin-bottom:10px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="margin:0; font-size:16px;">{pkg['title']}</h4>
                        <span style="color: #d4af37; font-weight:bold; font-size:14px;">₹{pkg['price']:,} / Jeep</span>
                    </div>
                    <p style="font-size:12px; color:#a1a1aa; margin-top:5px;">{pkg['desc']}</p>
                </div>
            """,
          unsafe_allow_html=True,
      )
      if st.button(f"Book {pkg['title']}", key=f"book_btn_{i}"):
        st.session_state.selected_package = pkg["title"]
        st.success(
            "Package selected! Go to the **Booking** tab to complete"
            " reservation."
        )

# 2. BOOKING TAB
elif selected_tab == "Booking":
  st.markdown("### Secure Reservation")
  st.markdown(
      "<p style='font-size:12px; color:#a1a1aa;'>Book instantly via"
      " WhatsApp</p>",
      unsafe_allow_html=True,
  )

  with st.form("booking_form"):
    full_name = st.text_input("Full Name", placeholder="Enter your full name")

    pkg_titles = [p["title"] for p in st.session_state.packages]
    default_idx = 0
    if (
        "selected_package" in st.session_state
        and st.session_state.selected_package in pkg_titles
    ):
      default_idx = pkg_titles.index(st.session_state.selected_package)

    safari_range = st.selectbox(
        "Select Safari / Range", pkg_titles, index=default_idx
    )
    pref_date = st.date_input(
        "Preferred Date", min_value=datetime.date.today()
    )
    guests = st.number_input("Number of Guests", min_value=1, max_value=6, value=2)

    submit_booking = st.form_submit_button("Book Instantly via WhatsApp")

    if submit_booking:
      if not full_name.strip():
        st.error("Kripya apna poora naam bharein.")
      else:
        owner_phone = "919101311494"
        msg = (
            f"*New Safari Booking Request - Borah Service*%0A%0A*Name:* {full_name}%0A*Safari"
            f" Range:* {safari_range}%0A*Date:* {pref_date}%0A*Guests:*"
            f" {guests}%0A%0APlease confirm availability."
        )
        whatsapp_url = f"https://wa.me/{owner_phone}?text={msg}"
        st.markdown(
            f'<meta http-equiv="refresh" content="0;url={whatsapp_url}">',
            unsafe_allow_html=True,
        )
        st.success(
            "Redirecting to WhatsApp... Agar redirect na ho toh [Yahan"
            f" Click Karein]({whatsapp_url})"
        )

# 3. ADMIN PANEL TAB
elif selected_tab == "Admin":
  st.markdown("### Admin Dashboard")

  if not st.session_state.admin_logged_in:
    with st.form("admin_login"):
      st.markdown(
          "<p style='font-size:12px; color:#a1a1aa;'>Enter Admin PIN</p>",
          unsafe_allow_html=True,
      )
      pin = st.text_input("Admin PIN", type="password")
      login_btn = st.form_submit_button("Unlock Panel")
      if login_btn:
        if pin == "Biswa11":
          st.session_state.admin_logged_in = True
          st.rerun()
        else:
          st.error("Galat PIN!")
  else:
    if st.button("Lock Panel"):
      st.session_state.admin_logged_in = False
      st.rerun()

    st.markdown("---")
    st.markdown("#### Add Custom Package")
    with st.form("add_pkg"):
      new_title = st.text_input("Package Title")
      new_price = st.number_input("Price (₹)", min_value=500, value=3500)
      new_desc = st.text_area("Description")
      new_img = st.text_input(
          "Image URL",
          placeholder="https://images.unsplash.com/...",
      )
      add_pkg_btn = st.form_submit_button("Publish Package")

      if add_pkg_btn:
        if new_title:
          img_url = (
              new_img
              if new_img
              else "https://images.unsplash.com/photo-1534188753412-3e26d1d618d6?q=80&w=800&auto=format&fit=crop"
          )
          st.session_state.packages.append({
              "title": new_title,
              "price": new_price,
              "desc": (
                  new_desc
                  if new_desc
                  else "Custom luxury safari package by Borah Service."
              ),
              "img": img_url,
          })
          st.success("Package successfully added!")
          st.rerun()
        else:
          st.error("Package title zaroori hai.")

    st.markdown("---")
    st.markdown("#### Add Guide / Employee")
    with st.form("add_guide"):
      g_name = st.text_input("Guide Name")
      g_role = st.text_input("Role & Phone (e.g. Senior Guide • +91...)")
      add_guide_btn = st.form_submit_button("Add Team Member")

      if add_guide_btn:
        if g_name and g_role:
          st.session_state.guides.append({"name": g_name, "role": g_role})
          st.success("Guide successfully added!")
          st.rerun()
        else:
          st.error("Sabhi fields bharein.")

# 4. OWNER PROFILE TAB
elif selected_tab == "Owner":
  st.markdown("### Founder Profile")
  owner_html = (
      '<div class="glass-card" style="text-align: center;">'
      '<img'
      ' src="https://raw.githubusercontent.com/biswakalyanborah-creator/borah-safari-app/main/Screenshot_20260921-171022.png"'
      ' style="width:100px; height:100px; border-radius:50%; object-fit:cover;'
      ' border:2px solid #d4af37; margin-bottom:10px;">'
      '<h4 style="margin:0; font-size:18px;">Somnath Borah</h4>'
      '<p style="color: #d4af37; font-size:11px; text-transform:uppercase;'
      ' letter-spacing:1px; margin-top:2px;">Senior Tourist Guide & Safari'
      " Expert</p>"
      '<p style="font-size:12px; color:#d4d4d8; margin-top:10px;">With over'
      " 15+ years of guiding through Kaziranga's untamed jungles, Somnath Borah"
      " ensures safe and luxurious wildlife expeditions.</p>"
      '<div style="background: rgba(0,0,0,0.3); padding: 10px; border-radius:'
      ' 8px; margin: 12px 0; text-align: left; font-size: 12px; color:'
      ' #d4d4d8;">'
      '<p style="margin:4px 0;">📞 <b>Phone:</b> +91 091013 11494</p>'
      '<p style="margin:4px 0;">✉️ <b>Email:</b> borahservices07@gmail.com</p>'
      '<p style="margin:4px 0;">📍 <b>Location:</b> Assam, India</p>'
      "</div>"
      '<div style="display: flex; gap: 8px; margin-top: 15px; flex-wrap:'
      ' wrap;">'
      '<a href="https://wa.me/919101311494" target="_blank" style="flex:1;'
      ' background:rgba(16,185,129,0.2); border:1px solid'
      " rgba(16,185,129,0.4); color:#34d399; padding:8px; border-radius:8px;"
      " text-decoration:none; font-size:11px; font-weight:bold;"
      ' text-align:center;">WhatsApp</a>'
      '<a href="https://www.facebook.com/share/19kLLT3wfS/" target="_blank"'
      ' style="flex:1; background:rgba(59,130,246,0.2); border:1px solid'
      " rgba(59,130,246,0.4); color:#60a5fa; padding:8px; border-radius:8px;"
      " text-decoration:none; font-size:11px; font-weight:bold;"
      ' text-align:center;">Facebook</a>'
      '<a'
      ' href="https://youtube.com/@somnathborah-riseagain?si=kv22Z5XJ94YAgRYv"'
      ' target="_blank" style="flex:1; background:rgba(239,68,68,0.2);'
      ' border:1px solid rgba(239,68,68,0.4); color:#f87171; padding:8px;'
      " border-radius:8px; text-decoration:none; font-size:11px;"
      ' font-weight:bold; text-align:center;">YouTube</a>'
      "</div>"
      "</div>"
  )
  st.markdown(owner_html, unsafe_allow_html=True)

  st.markdown("### Active Expert Guides")
  for guide in st.session_state.guides:
    st.markdown(
        f"""
            <div class="glass-card" style="display:flex; justify-content:space-between; align-items:center; padding:12px;">
                <div>
                    <h5 style="margin:0; font-size:14px; color:white;">{guide['name']}</h5>
                    <p style="margin:0; font-size:11px; color:#a1a1aa;">{guide['role']}</p>
                </div>
                <span style="width:8px; height:8px; background:#10b981; border-radius:50%; box-shadow: 0 0 8px #10b981;"></span>
            </div>
        """,
        unsafe_allow_html=True,
    )
    

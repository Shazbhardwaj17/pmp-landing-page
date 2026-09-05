import streamlit as st

st.set_page_config(page_title="PMP Elite Simulator", layout="wide")

# Hide Streamlit UI
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .hero {text-align: center; padding: 60px 0 40px 0;}
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.markdown("<h1 style='font-size: 3.5rem; color: #111827; margin-bottom: 20px;'>Master the PMP® Exam with Data-Driven Mock Sprints</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 20px; color: #4B5563; max-width: 700px; margin: 0 auto 30px auto; line-height: 1.6;'>Stop guessing. Identify your weak spots instantly with 6 full-length mocks, targeted domain sprints, and advanced performance analytics.</p>", unsafe_allow_html=True)

_, btn_col, _ = st.columns([1, 1, 1])
with btn_col:
    st.link_button("Start Free Sample Test", "https://app.pmpelite.com", type="primary", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr style='margin: 40px 0; border-top: 1px solid #E5E7EB;'>", unsafe_allow_html=True)

# --- FEATURES ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<h3 style='color: #2563EB;'>📊 Advanced Analytics</h3>", unsafe_allow_html=True)
    st.write("Track your exact performance and time-management across People, Process, and Business Environment domains.")
with c2:
    st.markdown("<h3 style='color: #2563EB;'>🎯 Domain Sprints</h3>", unsafe_allow_html=True)
    st.write("Short on time? Master specific PMI knowledge areas with intensely focused 60-question timed sprints.")
with c3:
    st.markdown("<h3 style='color: #2563EB;'>📝 Full-Length Mocks</h3>", unsafe_allow_html=True)
    st.write("Build your cognitive stamina with 180-question simulators timed exactly like the real certification exam.")

st.markdown("<hr style='margin: 40px 0; border-top: 1px solid #E5E7EB;'>", unsafe_allow_html=True)

# --- PRICING ---
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Simple, Transparent Pricing</h2>", unsafe_allow_html=True)
p1, p2, p3 = st.columns([1, 1.5, 1])
with p2:
    st.markdown("""
    <div style="border: 2px solid #2563EB; border-radius: 12px; padding: 40px; text-align: center; background: white; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
        <h3 style="margin-top: 0;">Elite Access</h3>
        <h1 style="color: #2563EB; font-size: 3rem; margin: 10px 0;">₹699</h1>
        <p style="color: #6B7280; font-size: 15px; margin-bottom: 25px;">Lifetime access to all 6 mocks, domain sprints, and detailed analytics.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.link_button("Unlock Premium Now", "https://app.pmpelite.com", type="primary", use_container_width=True)

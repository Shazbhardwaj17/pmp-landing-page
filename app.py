import streamlit as st

st.set_page_config(page_title="PMP Elite Simulator", layout="wide", initial_sidebar_state="collapsed")

# Session state for footer navigation
if "active_doc" not in st.session_state:
    st.session_state.active_doc = None

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Inter', sans-serif !important; 
        background-color: #F8FAFC !important; 
        scroll-behavior: smooth;
    }
    
    /* Hide Streamlit Defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 0rem !important; padding-bottom: 0rem !important; max-width: 100% !important; padding-left: 0 !important; padding-right: 0 !important;}
    
    /* Typography matching reference site */
    h1, h2, h3, .serif-text { font-family: 'Playfair Display', serif !important; letter-spacing: 0.5px; }
    
    /* Hero Banner */
    .hero-section {
        background: linear-gradient(135deg, #1E3A5F 0%, #0F172A 100%);
        padding: 110px 20px;
        text-align: center;
        color: white;
        border-bottom: 4px solid #EAB308;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 25px;
        line-height: 1.2;
        color: #F8FAFC;
    }
    .hero-subtitle {
        font-size: 1.15rem;
        font-weight: 300;
        max-width: 750px;
        margin: 0 auto 40px auto;
        color: #CBD5E1;
        line-height: 1.7;
    }
    
    /* Custom Buttons */
    .btn-primary {
        background-color: #EAB308;
        color: #0F172A !important;
        padding: 15px 32px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        display: inline-block;
        margin: 10px;
    }
    .btn-primary:hover { background-color: #CA8A04; transform: translateY(-2px); }
    
    .btn-secondary {
        background-color: transparent;
        color: #F8FAFC !important;
        padding: 15px 32px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 500;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        display: inline-block;
        margin: 10px;
        border: 1px solid #94A3B8;
    }
    .btn-secondary:hover { background-color: rgba(255,255,255,0.05); border-color: #F8FAFC; }
    
    /* Feature Cards */
    .white-section { padding: 90px 8%; background-color: #FFFFFF; }
    .gray-section { padding: 90px 8%; background-color: #F8FAFC; }
    
    .value-card { text-align: center; padding: 30px 20px; }
    .value-icon { font-size: 2.5rem; color: #EAB308; margin-bottom: 20px; }
    
    /* UI Mockup Cards */
    .ui-card {
        background: white;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        overflow: hidden;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .ui-header {
        background: #F1F5F9;
        padding: 12px 20px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #64748B;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-bottom: 1px solid #E2E8F0;
    }
    .ui-body { padding: 25px 20px; flex-grow: 1; }
    .ui-mock-element {
        background: #F8FAFC;
        border: 1px dashed #CBD5E1;
        border-radius: 6px;
        padding: 20px;
        margin-bottom: 20px;
    }
    
    /* Testimonials Grid */
    .testimonial-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        margin-top: 40px;
    }
    .review-card {
        background: white;
        padding: 30px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
    }
    .stars { color: #EAB308; font-size: 1.2rem; margin-bottom: 15px; }
    .reviewer-name { font-weight: 600; color: #0F172A; margin-top: 20px; font-size: 0.95rem; }
    
    /* Pricing Card */
    .pricing-card {
        border: 2px solid #EAB308;
        border-radius: 8px;
        padding: 50px 40px;
        background: white;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }
    .pricing-badge {
        position: absolute;
        top: 20px;
        right: -35px;
        background: #0F172A;
        color: #EAB308;
        padding: 8px 40px;
        font-weight: 700;
        font-size: 0.75rem;
        letter-spacing: 1px;
        transform: rotate(45deg);
    }
    
    /* Footer Styling */
    .footer-container {
        background-color: #0F172A;
        padding: 60px 8% 20px 8%;
        color: #94A3B8;
    }
    div[data-testid="stButton"] button[kind="tertiary"] {
        color: #94A3B8 !important;
        padding: 0 !important;
        justify-content: flex-start !important;
        font-weight: 400 !important;
    }
    div[data-testid="stButton"] button[kind="tertiary"]:hover {
        color: #EAB308 !important;
        background: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# --- NOTIFICATION BAR ---
st.markdown("""
<div style="background-color: #EAB308; text-align: center; padding: 12px; color: #0F172A; font-weight: 600; font-size: 0.9rem; letter-spacing: 0.5px;">
    LATEST ECO 2026 ALIGNMENT COMPLETED. <a href="https://pmp-simulator-2026.streamlit.app" style="color: #0F172A; text-decoration: underline;">BEGIN YOUR FREE ASSESSMENT</a>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title serif-text">Know If You're Ready for<br>the Updated PMP Exam</h1>
    <p class="hero-subtitle">Start with the free readiness assessment, then strengthen your judgment with scenario-based practice aligned to the 2026 PMP Examination Content Outline and the PMBOK Guide—Eighth Edition.</p>
    <div>
        <a href="https://pmp-simulator-2026.streamlit.app" class="btn-primary" target="_self">Start Free Assessment</a>
        <a href="https://pmp-simulator-2026.streamlit.app" class="btn-secondary" target="_self">View Plans</a>
    </div>
    <p style="font-size: 0.85rem; color: #94A3B8; margin-top: 20px; font-weight: 300;">Free 15-Question Diagnostic • Immediate readiness feedback</p>
</div>
""", unsafe_allow_html=True)

# --- VALUE PROPS ---
st.markdown('<div class="white-section">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="value-card">
        <div class="value-icon">📖</div>
        <h3 class="serif-text" style="color: #0F172A;">Built for the 2026 exam</h3>
        <p style="color: #64748B; font-size: 0.95rem; line-height: 1.6;">100% aligned to the PMBOK® Guide Eighth Edition and the latest PMP® Examination Content Outline.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="value-card">
        <div class="value-icon">🎯</div>
        <h3 class="serif-text" style="color: #0F172A;">2,000+ scenario questions</h3>
        <p style="color: #64748B; font-size: 0.95rem; line-height: 1.6;">Judgment-based items across People, Process, and Business Environment—never recall or definitions.</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="value-card">
        <div class="value-icon">⏱️</div>
        <h3 class="serif-text" style="color: #0F172A;">Real exam conditions</h3>
        <p style="color: #64748B; font-size: 0.95rem; line-height: 1.6;">Full 180-question, 230-minute simulations with the interactive question types on the new exam.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PRODUCT SHOWCASE ---
st.markdown('<div class="gray-section">', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="text-align: center; font-size: 2.5rem; color: #0F172A; margin-bottom: 10px;">See the Real Product, Not a Mockup</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #64748B; margin-bottom: 50px;">These are genuine workflows from the live simulator: the question experience, coaching insights, and your readiness result.</p>', unsafe_allow_html=True)

sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown("""
    <div class="ui-card">
        <div class="ui-header">STEP 1 — PRACTICE</div>
        <div class="ui-body">
            <div class="ui-mock-element" style="border-left: 3px solid #3B82F6;">
                <div style="height: 10px; width: 40%; background: #E2E8F0; margin-bottom: 10px; border-radius: 2px;"></div>
                <div style="height: 10px; width: 90%; background: #E2E8F0; margin-bottom: 10px; border-radius: 2px;"></div>
                <div style="height: 10px; width: 70%; background: #E2E8F0; border-radius: 2px;"></div>
            </div>
            <h4 style="color: #0F172A; margin-bottom: 10px;">Question Experience</h4>
            <p style="color: #64748B; font-size: 0.9rem; line-height: 1.5;">Practice every PMP question format used on the live exam: multiple response, matching, point & click, and graphic-based.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
with sc2:
    st.markdown("""
    <div class="ui-card">
        <div class="ui-header">STEP 2 — LEARN</div>
        <div class="ui-body">
            <div class="ui-mock-element" style="background: #ECFDF5; border: 1px solid #10B981;">
                <div style="color: #10B981; font-weight: 600; margin-bottom: 8px; font-size: 0.9rem;">✓ Correct Logic Applied</div>
                <div style="height: 8px; width: 100%; background: #D1FAE5; margin-bottom: 8px; border-radius: 2px;"></div>
                <div style="height: 8px; width: 60%; background: #D1FAE5; border-radius: 2px;"></div>
            </div>
            <h4 style="color: #0F172A; margin-bottom: 10px;">Coaching Insights</h4>
            <p style="color: #64748B; font-size: 0.9rem; line-height: 1.5;">Understand exactly why the best answer is correct and how PMI expects a project manager to think in the field.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
with sc3:
    st.markdown("""
    <div class="ui-card">
        <div class="ui-header">STEP 3 — IMPROVE</div>
        <div class="ui-body">
            <div class="ui-mock-element" style="text-align: center; border: none; background: transparent;">
                <div style="display: inline-block; width: 80px; height: 80px; border-radius: 50%; border: 6px solid #EAB308; line-height: 68px; font-size: 1.5rem; font-weight: 700; color: #0F172A;">76%</div>
            </div>
            <h4 style="color: #0F172A; margin-bottom: 10px;">Readiness Result</h4>
            <p style="color: #64748B; font-size: 0.9rem; line-height: 1.5;">A real-time benchmark and personalized data guidance across all three domains before exam day.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- AUTHOR / CREDENTIALS ---
st.markdown('<div class="white-section">', unsafe_allow_html=True)
st.markdown('<div style="max-width: 900px; margin: 0 auto; text-align: center;">', unsafe_allow_html=True)
st.markdown('<p style="color: #EAB308; font-size: 0.85rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;">Engineered for Professionals, By a Professional</p>', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="color: #0F172A; margin-top: 10px; font-size: 2.2rem;">Built by an Enterprise Risk & Data Expert</h2>', unsafe_allow_html=True)
st.markdown("""
<p style="color: #475569; line-height: 1.8; font-size: 1.1rem; text-align: left; margin-top: 30px;">
    Built by a certified <strong>PMP® and PgMP® professional</strong> bringing over 15 years of hard-earned experience orchestrating complex enterprise risk systems, product management life cycles, and advanced data analytics.
    <br><br>
    This is not a generic, mass-produced test prep factory. The Elite Simulator was engineered utilizing sophisticated Python data pipelines to perfectly mirror the real exam's rigor, ensuring your study time is driven by precise, analytical performance tracking.
</p>
<div style="border-left: 4px solid #EAB308; padding-left: 20px; margin-top: 30px; text-align: left;">
    <p style="font-style: italic; color: #111827; font-size: 1.1rem;">"A faithful, principle-aligned preparation tool that bridges the gap between studying framework theory and executing actual project judgment."</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# --- 9-GRID TESTIMONIALS ---
st.markdown('<div class="gray-section">', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="text-align: center; font-size: 2.5rem; color: #0F172A;">What Candidates Are Saying</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="testimonial-grid">
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"Solid prep. The domain breakdown showed me I was way weaker on Business Environment than I thought. Fixed that in a week."</p>
        <div class="reviewer-name">Rajesh K.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"The domain analytics helped me identify my weak areas. I focused my study time efficiently and passed on my first attempt."</p>
        <div class="reviewer-name">James R.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"The scenario questions felt almost identical in tone to the real exam. Walking in on test day, nothing surprised me."</p>
        <div class="reviewer-name">Priya M.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"I failed my first attempt using generic mocks. The Elite Simulator's situational questions made all the difference on my second try."</p>
        <div class="reviewer-name">Amit S.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"No fluff, just hard, realistic questions. If you can score 75% on these full-length mocks, you are ready for the real deal."</p>
        <div class="reviewer-name">Michael T.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"Worth every penny. The bonus question banks and the strict 230-minute timers built the serious mental stamina I needed."</p>
        <div class="reviewer-name">Neha D.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"The interface is slick, and the coaching insights completely shifted how I approach PMI's servant-leadership logic."</p>
        <div class="reviewer-name">Vikram R.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"The best investment in my PMP journey. The questions are remarkably close to what I saw on the real ECO test."</p>
        <div class="reviewer-name">Sarah J.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"I loved the immediate feedback. The lifetime access let me pace my domain sprints perfectly over 3 months of studying."</p>
        <div class="reviewer-name">Anjali T.</div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PRICING ---
st.markdown('<div id="pricing" class="white-section">', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="text-align: center; font-size: 2.5rem; color: #0F172A;">Simple, One-Time Pricing</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #64748B; margin-bottom: 60px;">Training that prevents failure pays for itself. Instant access. Secure checkout.</p>', unsafe_allow_html=True)

p_empty1, p_col, p_empty2 = st.columns([1, 1.3, 1])
with p_col:
    st.markdown("""
    <div class="pricing-card">
        <div class="pricing-badge">LIFETIME</div>
        <h3 class="serif-text" style="color: #0F172A; margin-top: 0; font-size: 1.8rem;">Elite Access</h3>
        <h1 style="color: #0F172A; font-size: 4rem; margin: 10px 0; font-weight: 700;">₹699</h1>
        <p style="color: #64748B; font-size: 0.95rem;">One-time secure payment</p>
        <hr style="border-top: 1px solid #E2E8F0; margin: 30px 0;">
        <ul style="list-style-type: none; padding-left: 0; color: #334155; line-height: 2.4; font-size: 1.05rem;">
            <li>✓ <strong>6 Full-Length Mocks</strong> (180 questions each)</li>
            <li>✓ <strong>Targeted Domain Sprints</strong> for rapid review</li>
            <li>✓ <strong>Bonus Question Banks</strong> included</li>
            <li>✓ Advanced analytical dashboard & trend tracking</li>
            <li>✓ Deep-dive rationales for every option</li>
            <li>✓ Lifetime platform access</li>
        </ul>
        <div style="text-align: center; margin-top: 40px;">
            <a href="https://pmp-simulator-2026.streamlit.app" class="btn-primary" style="display: block; margin: 0; padding: 18px;">Secure Premium Access</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- FAQ ---
st.markdown('<div class="gray-section" style="padding-top: 40px; padding-bottom: 40px;">', unsafe_allow_html=True)
st.markdown('<div style="max-width: 800px; margin: 0 auto;">', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="text-align: center; font-size: 2rem; color: #0F172A; margin-bottom: 30px;">Common Questions</h2>', unsafe_allow_html=True)

with st.expander("Is this simulator aligned with PMBOK 8 and ECO 2026?"):
    st.write("Yes, the entire question bank has been systematically audited and aligned with the latest Project Management Professional (PMP)® Examination Content Outline (ECO) for 2026. This includes comprehensive coverage of the three core domains: People (42%), Process (50%), and Business Environment (8%). The scenarios heavily integrate Agile, Predictive, and Hybrid project management methodologies exactly as they are tested on the current PMBOK® Guide - Eighth Edition.")
    
with st.expander("Can I try it before paying?"):
    st.write("Absolutely. We believe the quality of the simulator speaks for itself. You can take our Free Readiness Assessment immediately—no credit card or commitment required. This 15-question diagnostic uses genuine scenario-based items from our premium bank to give you a baseline understanding of your current readiness and let you experience our interactive platform firsthand.")

with st.expander("What if I fail the PMP exam after using this simulator?"):
    st.write("Our Elite Tier provides lifetime access to the platform. Unlike subscription-based services that cut off your access, your account remains active indefinitely. If you do not pass on your first attempt, you will retain full access to all mock exams, domain sprints, and advanced performance analytics. This allows you to continuously identify weak spots and recalibrate your study plan without ever paying a renewal fee.")

with st.expander("Do I need 80% to pass the real PMP exam?"):
    st.write("The Project Management Institute (PMI) does not publish a specific numerical passing score; exams are graded using psychometric analysis based on the difficulty of the specific questions you receive. However, industry consensus and our data show that consistently scoring between 75% and 80% on first attempts of our full-length mock exams indicates a very strong readiness level and a high probability of passing the actual exam.")
st.markdown('</div></div>', unsafe_allow_html=True)

# --- BOTTOM CTA ---
st.markdown("""
<div class="hero-section" style="padding: 80px 20px;">
    <h1 class="hero-title serif-text" style="font-size: 2.8rem;">The Exam Won't Wait. Neither Should You.</h1>
    <p class="hero-subtitle" style="margin-bottom: 35px; color: #CBD5E1;">Find out exactly where you stand in 15 minutes, then turn your result into full exam practice.</p>
    <a href="https://pmp-simulator-2026.streamlit.app" class="btn-primary" target="_self">Start Free Readiness Assessment →</a>
</div>
""", unsafe_allow_html=True)

# --- NATIVE STREAMLIT FOOTER & LEGAL MODALS ---
st.markdown('<div class="footer-container">', unsafe_allow_html=True)
fc1, fc2, fc3, fc4 = st.columns(4)
with fc1:
    st.markdown("<h4 style='color: #F8FAFC; margin-bottom:15px; font-weight:600;'>Simulator</h4>", unsafe_allow_html=True)
    st.markdown("<a href='https://pmp-simulator-2026.streamlit.app' style='color:#94A3B8; text-decoration:none; display:block; margin-bottom:10px;'>Start Free Assessment</a>", unsafe_allow_html=True)
    st.markdown("<a href='https://pmp-simulator-2026.streamlit.app' style='color:#94A3B8; text-decoration:none; display:block; margin-bottom:10px;'>Pricing & Plans</a>", unsafe_allow_html=True)
    st.markdown("<a href='https://pmp-simulator-2026.streamlit.app' style='color:#94A3B8; text-decoration:none; display:block; margin-bottom:10px;'>Features Overview</a>", unsafe_allow_html=True)
with fc2:
    st.markdown("<h4 style='color: #F8FAFC; margin-bottom:15px; font-weight:600;'>Resources</h4>", unsafe_allow_html=True)
    st.markdown("<a href='https://pmp-simulator-2026.streamlit.app' style='color:#94A3B8; text-decoration:none; display:block; margin-bottom:10px;'>Bonus Question Banks</a>", unsafe_allow_html=True)
    st.markdown("<a href='https://pmp-simulator-2026.streamlit.app' style='color:#94A3B8; text-decoration:none; display:block; margin-bottom:10px;'>Performance Analytics</a>", unsafe_allow_html=True)
with fc3:
    st.markdown("<h4 style='color: #F8FAFC; margin-bottom:15px; font-weight:600;'>Company</h4>", unsafe_allow_html=True)
    if st.button("About Us", key="btn_about", type="tertiary", use_container_width=True): st.session_state.active_doc = "about"
    if st.button("Contact Support", key="btn_contact", type="tertiary", use_container_width=True): st.session_state.active_doc = "contact"
with fc4:
    st.markdown("<h4 style='color: #F8FAFC; margin-bottom:15px; font-weight:600;'>Legal</h4>", unsafe_allow_html=True)
    if st.button("Terms of Service", key="btn_terms", type="tertiary", use_container_width=True): st.session_state.active_doc = "terms"
    if st.button("Privacy Policy", key="btn_privacy", type="tertiary", use_container_width=True): st.session_state.active_doc = "privacy"
    if st.button("Refund Policy", key="btn_refund", type="tertiary", use_container_width=True): st.session_state.active_doc = "refund"
st.markdown('</div>', unsafe_allow_html=True)

# DYNAMIC LEGAL CONTENT RENDERER
if st.session_state.active_doc:
    st.markdown("<div style='background-color:#F8FAFC; padding: 40px 10%; border-top: 4px solid #EAB308;'>", unsafe_allow_html=True)
    if st.session_state.active_doc == "about":
        st.markdown("<h3 class='serif-text'>About Us</h3>", unsafe_allow_html=True)
        st.write("We are an independent educational technology initiative founded by seasoned enterprise project managers. Our singular mission is to bridge the gap between theoretical frameworks and real-world execution through rigorous, data-driven exam simulations. We build professional tools for professionals.")
    elif st.session_state.active_doc == "contact":
        st.markdown("<h3 class='serif-text'>Contact Support</h3>", unsafe_allow_html=True)
        st.write("**Customer Support & Billing Queries:**\nPlease direct all inquiries, technical support requests, or payment issues to:\n\n**Email:** sagar@assuretrac.com\n\nWe aim to respond to all inquiries within 24-48 business hours.")
    elif st.session_state.active_doc == "terms":
        st.markdown("<h3 class='serif-text'>Terms and Conditions</h3>", unsafe_allow_html=True)
        st.write("**1. Acceptance of Terms:** By accessing and using this platform, you accept and agree to be bound by the terms and provisions of this agreement.\n\n**2. Intellectual Property:** All mock exams, rationales, platform design, and provided text are the proprietary intellectual property of the platform creators. Users may not scrape, copy, distribute, or resell any materials from this platform.\n\n**3. Account Security:** Users are responsible for maintaining the confidentiality of their login credentials.\n\n**4. Limitation of Liability:** The platform is provided 'as is'. While we strive for accuracy, we do not guarantee that the use of this simulator will result in a passing score on the official exam.\n\n**5. Governing Law:** These terms are governed by the laws of Maharashtra, India.")
    elif st.session_state.active_doc == "privacy":
        st.markdown("<h3 class='serif-text'>Privacy Policy</h3>", unsafe_allow_html=True)
        st.write("**1. Data Collection:** We collect basic profile information (such as Name and Email Address) solely for the purpose of account creation, authentication, and providing access to the simulator.\n\n**2. Performance Data:** Exam results and analytics are securely stored to populate your personal dashboard.\n\n**3. Data Protection:** We utilize enterprise-grade backend infrastructure to ensure your data is encrypted and secure.\n\n**4. Third-Party Sharing:** We do not sell, trade, or rent your personal identification information to any third parties. Payments are processed securely via our payment gateway, and we do not store your credit card information.")
    elif st.session_state.active_doc == "refund":
        st.markdown("<h3 class='serif-text'>Refund and Cancellation Policy</h3>", unsafe_allow_html=True)
        st.write("Due to the nature of our product—which provides immediate, unhindered access to proprietary digital content and question banks upon purchase—**all sales are final**.\n\nWe do not offer refunds, cancellations, or partial credits once a payment is successfully processed and Elite access is granted to your account. We strongly encourage all users to utilize the Free Readiness Assessment to evaluate the platform before committing to a purchase. If you experience technical difficulties accessing your account post-purchase, please contact support immediately at sagar@assuretrac.com.")
    
    if st.button("Close Document", key="close_doc"):
        st.session_state.active_doc = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# COPYRIGHT DISCLAIMER
st.markdown("""
<div style="background-color: #0F172A; text-align: center; padding: 20px 8% 40px 8%; color: #64748B; font-size: 0.75rem;">
    <div style="background-color: #1E293B; padding: 10px 20px; border-radius: 4px; display: inline-block; margin-bottom: 15px;">
        Independent preparation platform. PMP®, PMBOK®, and PMI® are registered marks of the Project Management Institute, Inc.<br>
        This platform is not affiliated with, approved by, or endorsed by PMI.
    </div>
    <div style="margin-top: 10px;">© 2026 Elite Simulator Systems. All rights reserved.</div>
</div>
""", unsafe_allow_html=True)

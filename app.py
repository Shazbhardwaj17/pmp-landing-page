import streamlit as st

st.set_page_config(page_title="PMP Elite Simulator", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Inter', sans-serif !important; 
        background-color: #FAFAFA !important; 
    }
    
    /* Hide Streamlit Defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 0rem !important; padding-bottom: 0rem !important; max-width: 100% !important; padding-left: 0 !important; padding-right: 0 !important;}
    
    /* Typography */
    h1, h2, .serif-text { font-family: 'Playfair Display', serif !important; }
    
    /* Hero Banner (Dark Blue) */
    .hero-section {
        background-color: #214065;
        padding: 100px 20px;
        text-align: center;
        color: white;
    }
    .hero-title {
        font-size: 3.8rem;
        font-weight: 700;
        margin-bottom: 20px;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        font-weight: 400;
        max-width: 800px;
        margin: 0 auto 40px auto;
        color: #E2E8F0;
        line-height: 1.6;
    }
    
    /* Custom Buttons */
    .btn-primary {
        background-color: #EAB308;
        color: #111827 !important;
        padding: 14px 28px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: background-color 0.2s;
        display: inline-block;
        margin: 10px;
        border: 1px solid #EAB308;
    }
    .btn-primary:hover { background-color: #CA8A04; }
    
    .btn-secondary {
        background-color: transparent;
        color: white !important;
        padding: 14px 28px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: background-color 0.2s;
        display: inline-block;
        margin: 10px;
        border: 1px solid white;
    }
    .btn-secondary:hover { background-color: rgba(255,255,255,0.1); }
    
    /* Grid Cards */
    .feature-card {
        background: white;
        padding: 30px;
        border-radius: 8px;
        border: 1px solid #E5E7EB;
        height: 100%;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .feature-icon {
        font-size: 2rem;
        color: #EAB308;
        margin-bottom: 15px;
    }
    
    /* Section Formatting */
    .content-section {
        padding: 80px 10%;
        background-color: #FAFAFA;
    }
    .white-section {
        padding: 80px 10%;
        background-color: #FFFFFF;
    }
    .section-title {
        text-align: center;
        font-size: 2.8rem;
        color: #111827;
        margin-bottom: 15px;
    }
    .section-subtitle {
        text-align: center;
        color: #6B7280;
        font-size: 1.1rem;
        margin-bottom: 50px;
    }
    
    /* Pricing Card */
    .pricing-card {
        border: 2px solid #EAB308;
        border-radius: 12px;
        padding: 40px;
        background: white;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        position: relative;
    }
    .pricing-badge {
        position: absolute;
        top: -12px;
        right: 20px;
        background: #EAB308;
        color: #111827;
        padding: 4px 12px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# --- TOP NOTIFICATION BAR ---
st.markdown("""
<div style="background-color: #10B981; text-align: center; padding: 10px; color: white; font-weight: 500; font-size: 0.9rem;">
    🎯 The updated PMP Elite Simulator is now live. <a href="https://app.pmpelite.com" style="color: white; text-decoration: underline;">Start Practicing</a>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title serif-text">Know If You're Ready for<br>the Updated PMP Exam</h1>
    <p class="hero-subtitle">Start with the free readiness assessment, then strengthen your judgment with scenario-based practice aligned to the latest PMP Examination Content Outline.</p>
    <div>
        <a href="https://app.pmpelite.com" class="btn-primary" target="_self">Start Free Assessment →</a>
        <a href="#pricing" class="btn-secondary" target="_self">View Plans</a>
    </div>
    <p style="font-size: 0.85rem; color: #9CA3AF; margin-top: 15px;">Free • 15 questions • Immediate readiness feedback</p>
</div>
""", unsafe_allow_html=True)

# --- VALUE PROPS (3 COLUMNS) ---
st.markdown('<div class="white-section">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div class="feature-icon">📖</div>
        <h3 class="serif-text" style="color: #111827;">Built for the modern exam</h3>
        <p style="color: #6B7280; font-size: 0.95rem;">100% aligned to the current Examination Content Outline and Agile methodologies.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div class="feature-icon">🎯</div>
        <h3 class="serif-text" style="color: #111827;">Scenario-based logic</h3>
        <p style="color: #6B7280; font-size: 0.95rem;">Judgment-based items across People, Process, and Business Environment—never rote recall.</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div class="feature-icon">⏱️</div>
        <h3 class="serif-text" style="color: #111827;">Real exam conditions</h3>
        <p style="color: #6B7280; font-size: 0.95rem;">Full 180-question, 230-minute simulations with interactive question types and pressure.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PRODUCT SHOWCASE ---
st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title serif-text">See the Real Product, <span style="color: #EAB308;">Not a Mockup</span></h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Genuine workflows from the live simulator: the question experience, coaching insights, and analytics.</p>', unsafe_allow_html=True)

sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown("""
    <div class="feature-card">
        <div style="text-align: left; font-size: 0.8rem; color: #9CA3AF; font-weight: 600; letter-spacing: 1px; margin-bottom: 10px;">STEP 1 — PRACTICE</div>
        <div style="background: #F3F4F6; border-radius: 6px; height: 180px; margin-bottom: 20px; display:flex; align-items:center; justify-content:center; border: 1px solid #E5E7EB;">
            <span style="color: #9CA3AF;">[ Clean Exam Interface ]</span>
        </div>
        <h4 style="color: #111827; margin-bottom: 10px; text-align: left;">Question Experience</h4>
        <p style="color: #6B7280; font-size: 0.9rem; text-align: left;">Practice every PMP question format used on the live exam: multiple response, situational, and graphic-based.</p>
    </div>
    """, unsafe_allow_html=True)
with sc2:
    st.markdown("""
    <div class="feature-card">
        <div style="text-align: left; font-size: 0.8rem; color: #9CA3AF; font-weight: 600; letter-spacing: 1px; margin-bottom: 10px;">STEP 2 — LEARN</div>
        <div style="background: #F3F4F6; border-radius: 6px; height: 180px; margin-bottom: 20px; display:flex; align-items:center; justify-content:center; border: 1px solid #E5E7EB;">
            <span style="color: #9CA3AF;">[ Detailed Rationales ]</span>
        </div>
        <h4 style="color: #111827; margin-bottom: 10px; text-align: left;">Coaching Insights</h4>
        <p style="color: #6B7280; font-size: 0.9rem; text-align: left;">Understand exactly why the best answer is correct and how PMI expects a project manager to think in the field.</p>
    </div>
    """, unsafe_allow_html=True)
with sc3:
    st.markdown("""
    <div class="feature-card">
        <div style="text-align: left; font-size: 0.8rem; color: #9CA3AF; font-weight: 600; letter-spacing: 1px; margin-bottom: 10px;">STEP 3 — IMPROVE</div>
        <div style="background: #FFFBEB; border-radius: 6px; height: 180px; margin-bottom: 20px; display:flex; align-items:center; justify-content:center; border: 1px solid #FDE68A;">
            <div style="text-align: center;">
                <h2 style="color: #D97706; margin:0;">76%</h2>
                <p style="color: #D97706; font-size: 0.8rem; margin:0;">Target Readiness</p>
            </div>
        </div>
        <h4 style="color: #111827; margin-bottom: 10px; text-align: left;">Readiness Result</h4>
        <p style="color: #6B7280; font-size: 0.9rem; text-align: left;">A real-time benchmark and personalized data guidance across all three domains before exam day.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- AUTHOR / SOCIAL PROOF ---
st.markdown('<div class="white-section">', unsafe_allow_html=True)
st.markdown('<div style="max-width: 800px; margin: 0 auto;">', unsafe_allow_html=True)
st.markdown('<p style="color: #EAB308; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;">Engineered for Professionals, By a Professional</p>', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="color: #111827; margin-top: 5px;">Built by an Enterprise Risk & Data Expert</h2>', unsafe_allow_html=True)
st.markdown("""
<p style="color: #4B5563; line-height: 1.7; font-size: 1.05rem;">
    Created by a certified CPCU and seasoned Project Manager bringing 14 years of experience orchestrating enterprise risk systems, product management, and advanced data analytics. 
    <br><br>
    This simulator was not generated by a generic test-prep factory. It was engineered utilizing sophisticated Python data pipelines to perfectly mirror the real exam's rigor, ensuring your study time is driven by precise, analytical performance tracking.
</p>
<div style="border-left: 4px solid #EAB308; padding-left: 20px; margin-top: 30px;">
    <p style="font-style: italic; color: #111827; font-size: 1.1rem;">"A faithful, principle-aligned preparation tool that bridges the gap between studying framework theory and executing actual project judgment."</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# --- PRICING ---
st.markdown('<div id="pricing" class="content-section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title serif-text">Simple, <span style="color: #EAB308;">One-Time Pricing</span></h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Training that prevents failure pays for itself. Instant access. Secure checkout.</p>', unsafe_allow_html=True)

p_empty1, p_col, p_empty2 = st.columns([1, 1.5, 1])
with p_col:
    st.markdown("""
    <div class="pricing-card">
        <div class="pricing-badge">ELITE TIER</div>
        <h3 class="serif-text" style="color: #111827; margin-top: 0; font-size: 1.8rem;">Lifetime Access</h3>
        <h1 style="color: #111827; font-size: 3.5rem; margin: 10px 0;">₹699</h1>
        <p style="color: #6B7280; font-size: 0.95rem;">One-time payment</p>
        <hr style="border-top: 1px solid #E5E7EB; margin: 25px 0;">
        <ul style="list-style-type: none; padding-left: 0; color: #4B5563; line-height: 2.2;">
            <li>✓ <strong>6 Full Exam</strong> simulations (180 Qs each)</li>
            <li>✓ Targeted <strong>Domain Sprints</strong></li>
            <li>✓ Advanced performance trend tracking</li>
            <li>✓ Full rationales for every correct & incorrect option</li>
            <li>✓ Lifetime dashboard access</li>
        </ul>
        <div style="text-align: center; margin-top: 30px;">
            <a href="https://app.pmpelite.com" class="btn-primary" style="display: block; margin: 0;">Unlock Elite Access Now</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- FAQ ---
st.markdown('<div class="white-section" style="max-width: 800px; margin: 0 auto;">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title serif-text">Common Questions</h2>', unsafe_allow_html=True)

with st.expander("Is this simulator aligned with the current exam?"):
    st.write("Yes. The question bank is meticulously aligned with the current PMP Examination Content Outline (ECO), incorporating heavily weighted Agile, Hybrid, and Predictive methodologies.")
    
with st.expander("Can I try it before paying?"):
    st.write("Absolutely. You can launch the Free Readiness Assessment immediately with no credit card required to experience the interface and question quality.")

with st.expander("How does the performance analytics work?"):
    st.write("Our proprietary backend tracks your success rate across the three core domains: People, Process, and Business Environment. You can review past attempts and target your exact weak points to study efficiently.")
st.markdown('</div>', unsafe_allow_html=True)

# --- BOTTOM CTA ---
st.markdown("""
<div class="hero-section" style="padding: 80px 20px;">
    <h1 class="hero-title serif-text" style="font-size: 3rem;">The Exam Won't Wait. Neither Should You.</h1>
    <p class="hero-subtitle" style="margin-bottom: 30px;">Find out exactly where you stand in 15 minutes, then turn your result into full exam practice.</p>
    <a href="https://app.pmpelite.com" class="btn-primary" target="_self">Start Free Readiness Assessment →</a>
</div>
""", unsafe_allow_html=True)

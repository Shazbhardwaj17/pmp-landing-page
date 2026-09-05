import streamlit as st

st.set_page_config(page_title="PMP Elite Simulator", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');
    
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
    
    /* Typography */
    h1, h2, .serif-text { font-family: 'Cinzel', serif !important; letter-spacing: 0.5px; }
    
    /* Hero Banner (Midnight Slate & Gold) */
    .hero-section {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 110px 20px;
        text-align: center;
        color: white;
        border-bottom: 4px solid #D4AF37;
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
        background-color: #D4AF37;
        color: #0F172A !important;
        padding: 15px 32px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        display: inline-block;
        margin: 10px;
        box-shadow: 0 4px 14px 0 rgba(212, 175, 55, 0.39);
    }
    .btn-primary:hover { background-color: #B7942E; transform: translateY(-2px); }
    
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
        border: 1px solid #64748B;
    }
    .btn-secondary:hover { background-color: rgba(255,255,255,0.05); border-color: #F8FAFC; }
    
    /* Feature Cards */
    .white-section { padding: 90px 8%; background-color: #FFFFFF; }
    .gray-section { padding: 90px 8%; background-color: #F8FAFC; }
    
    .value-card { text-align: center; padding: 30px 20px; }
    .value-icon { font-size: 2.5rem; color: #D4AF37; margin-bottom: 20px; }
    
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
    .stars { color: #D4AF37; font-size: 1.2rem; margin-bottom: 15px; }
    .reviewer-name { font-weight: 600; color: #0F172A; margin-top: 20px; font-size: 0.95rem; }
    
    /* Pricing Card */
    .pricing-card {
        border: 2px solid #D4AF37;
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
        color: #D4AF37;
        padding: 8px 40px;
        font-weight: 700;
        font-size: 0.75rem;
        letter-spacing: 1px;
        transform: rotate(45deg);
    }
    
    /* Custom Footer */
    .footer-section {
        background-color: #0F172A;
        color: #94A3B8;
        padding: 60px 8% 20px 8%;
        font-family: 'Inter', sans-serif;
    }
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 30px;
        border-bottom: 1px solid #1E293B;
        padding-bottom: 40px;
    }
    .footer-column h4 {
        color: #F8FAFC;
        font-size: 1.05rem;
        margin-bottom: 20px;
        font-weight: 600;
    }
    .footer-column ul { list-style: none; padding: 0; margin: 0; }
    .footer-column li { margin-bottom: 12px; }
    .footer-column a {
        color: #94A3B8;
        text-decoration: none;
        font-size: 0.85rem;
        transition: color 0.2s;
    }
    .footer-column a:hover { color: #D4AF37; }
    .footer-bottom {
        text-align: center;
        padding-top: 20px;
        font-size: 0.75rem;
    }
    .footer-disclaimer {
        background-color: #1E293B;
        padding: 10px 20px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 15px;
        font-size: 0.7rem;
        color: #64748B;
    }
</style>
""", unsafe_allow_html=True)

# --- NOTIFICATION BAR ---
st.markdown("""
<div style="background-color: #D4AF37; text-align: center; padding: 12px; color: #0F172A; font-weight: 600; font-size: 0.9rem; letter-spacing: 0.5px;">
    LATEST ECO 2026 ALIGNMENT COMPLETED. <a href="https://app.pmpelite.com" style="color: #0F172A; text-decoration: underline;">BEGIN YOUR FREE ASSESSMENT</a>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title serif-text">Command the PMP® Exam<br>With Elite Precision</h1>
    <p class="hero-subtitle">Bypass the fluff. Validate your readiness with deeply analytical scenario-based mocks, targeted domain sprints, and exclusive bonus question banks built for the modern project manager.</p>
    <div>
        <a href="https://app.pmpelite.com" class="btn-primary" target="_self">Start Free Assessment</a>
        <a href="#pricing" class="btn-secondary" target="_self">View Elite Tier</a>
    </div>
    <p style="font-size: 0.85rem; color: #94A3B8; margin-top: 20px; font-weight: 300;">Free 15-Question Diagnostic • Instant Data Feedback • No Credit Card Required</p>
</div>
""", unsafe_allow_html=True)

# --- VALUE PROPS ---
st.markdown('<div class="white-section">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="value-card">
        <div class="value-icon">🏛️</div>
        <h3 class="serif-text" style="color: #0F172A;">Architected for 2026</h3>
        <p style="color: #64748B; font-size: 0.95rem; line-height: 1.6;">Strict adherence to the current Examination Content Outline, emphasizing Agile, Hybrid, and Predictive enterprise environments.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="value-card">
        <div class="value-icon">⚖️</div>
        <h3 class="serif-text" style="color: #0F172A;">Situational Judgment</h3>
        <p style="color: #64748B; font-size: 0.95rem; line-height: 1.6;">Eradicate rote memorization. Our items test your execution of PMI logic across People, Process, and Business Environment.</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="value-card">
        <div class="value-icon">🛡️</div>
        <h3 class="serif-text" style="color: #0F172A;">Exam-Day Conditioning</h3>
        <p style="color: #64748B; font-size: 0.95rem; line-height: 1.6;">Full 180-question, 230-minute stress tests designed to build the cognitive stamina required to pass on your first attempt.</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- PRODUCT SHOWCASE ---
st.markdown('<div class="gray-section">', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="text-align: center; font-size: 2.5rem; color: #0F172A; margin-bottom: 10px;">The Platform Engine</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #64748B; margin-bottom: 50px;">A glimpse into the workflow: rigorous practice, intelligent insights, and definitive readiness tracking.</p>', unsafe_allow_html=True)

sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown("""
    <div class="ui-card">
        <div class="ui-header">Phase 1: Simulation</div>
        <div class="ui-body">
            <div class="ui-mock-element" style="border-left: 3px solid #3B82F6;">
                <div style="height: 10px; width: 40%; background: #E2E8F0; margin-bottom: 10px; border-radius: 2px;"></div>
                <div style="height: 10px; width: 90%; background: #E2E8F0; margin-bottom: 10px; border-radius: 2px;"></div>
                <div style="height: 10px; width: 70%; background: #E2E8F0; border-radius: 2px;"></div>
            </div>
            <h4 style="color: #0F172A; margin-bottom: 10px;">Immersive Question UI</h4>
            <p style="color: #64748B; font-size: 0.9rem; line-height: 1.5;">Navigate complex scenarios, drag-and-drop matches, and multiple-response items in an interface mirroring the real Pearson VUE environment.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
with sc2:
    st.markdown("""
    <div class="ui-card">
        <div class="ui-header">Phase 2: Recalibration</div>
        <div class="ui-body">
            <div class="ui-mock-element" style="background: #ECFDF5; border: 1px solid #10B981;">
                <div style="color: #10B981; font-weight: 600; margin-bottom: 8px; font-size: 0.9rem;">✓ Correct Logic Applied</div>
                <div style="height: 8px; width: 100%; background: #D1FAE5; margin-bottom: 8px; border-radius: 2px;"></div>
                <div style="height: 8px; width: 60%; background: #D1FAE5; border-radius: 2px;"></div>
            </div>
            <h4 style="color: #0F172A; margin-bottom: 10px;">Deep-Dive Rationales</h4>
            <p style="color: #64748B; font-size: 0.9rem; line-height: 1.5;">Instantly dissect why the best answer is correct, and exactly why the distractors fail PMI's strict ethical and procedural logic.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
with sc3:
    st.markdown("""
    <div class="ui-card">
        <div class="ui-header">Phase 3: Execution</div>
        <div class="ui-body">
            <div class="ui-mock-element" style="text-align: center; border: none; background: transparent;">
                <div style="display: inline-block; width: 80px; height: 80px; border-radius: 50%; border: 6px solid #D4AF37; line-height: 68px; font-size: 1.5rem; font-weight: 700; color: #0F172A;">78%</div>
            </div>
            <h4 style="color: #0F172A; margin-bottom: 10px;">Predictive Analytics</h4>
            <p style="color: #64748B; font-size: 0.9rem; line-height: 1.5;">Stop guessing your readiness. Track cumulative scoring across all domains to know the exact moment you are ready to pass.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- AUTHOR / CREDENTIALS ---
st.markdown('<div class="white-section">', unsafe_allow_html=True)
st.markdown('<div style="max-width: 900px; margin: 0 auto; text-align: center;">', unsafe_allow_html=True)
st.markdown('<p style="color: #D4AF37; font-size: 0.85rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;">Engineered by a Practitioner, For Practitioners</p>', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="color: #0F172A; margin-top: 10px; font-size: 2.2rem;">Architected by an Enterprise Project Leader</h2>', unsafe_allow_html=True)
st.markdown("""
<p style="color: #475569; line-height: 1.8; font-size: 1.1rem; text-align: left; margin-top: 30px;">
    Built by a certified <strong>PMP® and PgMP® professional</strong> bringing over 15 years of hard-earned experience orchestrating complex enterprise risk systems, product management life cycles, and advanced machine learning data pipelines.
    <br><br>
    This is not a generic, mass-produced test bank. The Elite Simulator was engineered using sophisticated Python data structures to perfectly mirror the psychological rigor of the real exam, ensuring your study time is driven by precise, analytical performance metrics rather than outdated theory.
</p>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# --- 9-GRID TESTIMONIALS ---
st.markdown('<div class="gray-section">', unsafe_allow_html=True)
st.markdown('<h2 class="serif-text" style="text-align: center; font-size: 2.5rem; color: #0F172A;">Elite Alumni Outcomes</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="testimonial-grid">
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"The domain sprints were exactly what I needed to lock in Business Environment concepts. Passed Above Target!"</p>
        <div class="reviewer-name">Rajesh K.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"This simulator perfectly mirrors the actual exam's ambiguity. The detailed rationales for incorrect options are a goldmine."</p>
        <div class="reviewer-name">Priya M.</div>
    </div>
    <div class="review-card">
        <div class="stars">★★★★★</div>
        <p style="color: #475569; font-style: italic; font-size: 0.95rem;">"The analytics dashboard showed me my blind spots in Agile methodologies instantly. Highly recommend for the final week of prep."</p>
        <div class="reviewer-name">Sarah J.</div>
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
        <div class="reviewer-name">David L.</div>
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
st.markdown('<h2 class="serif-text" style="text-align: center; font-size: 2.5rem; color: #0F172A;">Transparent, One-Time Pricing</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #64748B; margin-bottom: 60px;">A single investment to secure your certification. No recurring subscriptions.</p>', unsafe_allow_html=True)

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
            <li>✓ <strong>Exclusive Bonus Question Banks</strong></li>
            <li>✓ Advanced analytical dashboard & trend tracking</li>
            <li>✓ Deep-dive rationales for every option</li>
            <li>✓ Lifetime platform access</li>
        </ul>
        <div style="text-align: center; margin-top: 40px;">
            <a href="https://app.pmpelite.com" class="btn-primary" style="display: block; margin: 0; padding: 18px;">Secure Premium Access</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- LEGAL & POLICIES (RAZORPAY COMPLIANCE) ---
st.markdown('<div id="legal-policies" class="white-section" style="padding-top: 20px; padding-bottom: 20px;">', unsafe_allow_html=True)
st.markdown('<div style="max-width: 900px; margin: 0 auto;">', unsafe_allow_html=True)
st.markdown('<h3 class="serif-text" style="color: #0F172A; margin-bottom: 20px;">Company Support & Legal</h3>', unsafe_allow_html=True)

with st.expander("About Us"):
    st.write("""
    We are an independent educational technology initiative founded by seasoned enterprise project managers. 
    Our singular mission is to bridge the gap between theoretical frameworks and real-world execution through rigorous, 
    data-driven exam simulations. We build professional tools for professionals.
    """)
    
with st.expander("Contact Us"):
    st.write("""
    **Customer Support & Billing Queries:**
    Please direct all inquiries, technical support requests, or payment issues to:
    **Email:** sagar@assuretrac.com
    We aim to respond to all inquiries within 24-48 business hours.
    """)

with st.expander("Terms and Conditions"):
    st.write("""
    **1. Acceptance of Terms:** By accessing and using this platform, you accept and agree to be bound by the terms and provisions of this agreement.
    **2. Intellectual Property:** All mock exams, rationales, platform design, and provided text are the proprietary intellectual property of the platform creators. Users may not scrape, copy, distribute, or resell any materials from this platform.
    **3. Account Security:** Users are responsible for maintaining the confidentiality of their login credentials. 
    **4. Limitation of Liability:** The platform is provided "as is". While we strive for accuracy, we do not guarantee that the use of this simulator will result in a passing score on the official PMP exam.
    **5. Governing Law:** These terms are governed by the laws of Maharashtra, India.
    """)

with st.expander("Privacy Policy"):
    st.write("""
    **1. Data Collection:** We collect basic profile information (such as Name and Email Address) solely for the purpose of account creation, authentication, and providing access to the simulator.
    **2. Performance Data:** Exam results and analytics are securely stored to populate your personal dashboard.
    **3. Data Protection:** We utilize enterprise-grade backend infrastructure (Supabase/PostgreSQL) to ensure your data is encrypted and secure. 
    **4. Third-Party Sharing:** We do not sell, trade, or rent your personal identification information to any third parties. Payments are processed securely via Razorpay, and we do not store your credit card information.
    """)

with st.expander("Refund and Cancellation Policy"):
    st.write("""
    Due to the nature of our product—which provides immediate, unhindered access to proprietary digital content and question banks upon purchase—**all sales are final**. 
    
    We do not offer refunds, cancellations, or partial credits once a payment is successfully processed and Elite access is granted to your account. We strongly encourage all users to utilize the Free Readiness Assessment to evaluate the platform before committing to a purchase. If you experience technical difficulties accessing your account post-purchase, please contact support immediately at sagar@assuretrac.com.
    """)
st.markdown('</div></div>', unsafe_allow_html=True)

# --- BOTTOM CTA ---
st.markdown("""
<div class="hero-section" style="padding: 80px 20px;">
    <h1 class="hero-title serif-text" style="font-size: 2.8rem;">The Exam Won't Wait.</h1>
    <p class="hero-subtitle" style="margin-bottom: 35px; color: #CBD5E1;">Identify your precise knowledge gaps in 15 minutes, then convert your baseline into exam-day confidence.</p>
    <a href="https://app.pmpelite.com" class="btn-primary" target="_self">Start Free Assessment</a>
</div>
""", unsafe_allow_html=True)

# --- HTML FOOTER ---
st.markdown("""
<div class="footer-section">
    <div class="footer-grid">
        <div class="footer-column">
            <h4>Simulator</h4>
            <ul>
                <li><a href="https://app.pmpelite.com">Start Free Assessment</a></li>
                <li><a href="#pricing">Pricing & Plans</a></li>
                <li><a href="#pricing">Features Overview</a></li>
            </ul>
        </div>
        <div class="footer-column">
            <h4>Resources</h4>
            <ul>
                <li><a href="#pricing">Bonus Question Banks</a></li>
                <li><a href="https://app.pmpelite.com">Performance Analytics</a></li>
            </ul>
        </div>
        <div class="footer-column">
            <h4>Company</h4>
            <ul>
                <li><a href="#legal-policies">About Us</a></li>
                <li><a href="#legal-policies">Contact Support</a></li>
            </ul>
        </div>
        <div class="footer-column">
            <h4>Legal</h4>
            <ul>
                <li><a href="#legal-policies">Terms of Service</a></li>
                <li><a href="#legal-policies">Privacy Policy</a></li>
                <li><a href="#legal-policies">Refund Policy</a></li>
            </ul>
        </div>
    </div>
    
    <div class="footer-bottom">
        <div class="footer-disclaimer">
            Independent preparation platform. PMP®, PMBOK®, and PMI® are registered marks of the Project Management Institute, Inc.<br>
            This platform is not affiliated with, approved by, or endorsed by PMI.
        </div>
        <div style="color: #64748B; margin-top: 10px;">
            © 2026 Elite Simulator Systems. All rights reserved.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

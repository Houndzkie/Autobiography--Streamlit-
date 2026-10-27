# pyrefly: ignore[missing-import]
import streamlit as st
import pandas as pd
import numpy as np
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Helge Justine O. Dano | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0d0d1a 0%, #111827 50%, #0d1117 100%);
    color: #e2e8f0;
}

header[data-testid="stHeader"] { background: transparent; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1a1f2e 100%);
    border-right: 1px solid #2d3748;
}
[data-testid="stSidebar"] * { color: #e2e8f0 !important; }

.hero-banner {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 40%, #06b6d4 100%);
    padding: 3rem 2rem;
    border-radius: 1.5rem;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 25px 50px rgba(99,102,241,0.35);
    position: relative;
    overflow: hidden;
}
.hero-name {
    font-size: 3rem;
    font-weight: 800;
    color: white;
    text-shadow: 0 2px 20px rgba(0,0,0,0.3);
    margin: 0;
    letter-spacing: -1px;
}
.hero-sub {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.85);
    margin-top: 0.4rem;
    font-weight: 400;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    color: white;
    padding: 0.3rem 1rem;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-top: 1rem;
    border: 1px solid rgba(255,255,255,0.3);
    letter-spacing: 1px;
}

.section-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 1rem;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
}
.section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #a5b4fc;
    margin-bottom: 0.8rem;
}

.skill-bar-label { font-size: 0.9rem; color: #94a3b8; margin-bottom: 0.2rem; }
.skill-bar-bg {
    background: rgba(255,255,255,0.07);
    border-radius: 999px;
    height: 10px;
    overflow: hidden;
    margin-bottom: 0.8rem;
}
.skill-bar-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #6366f1, #06b6d4);
}

.project-card {
    background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(6,182,212,0.08));
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 1rem;
    padding: 1.3rem 1.5rem;
    height: 100%;
}
.project-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #a5b4fc;
    margin-bottom: 0.5rem;
}
.project-role { font-size: 0.82rem; color: #64748b; margin-bottom: 0.5rem; }
.project-tech {
    display: inline-block;
    background: rgba(99,102,241,0.2);
    color: #a5b4fc;
    padding: 0.2rem 0.7rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-family: 'Fira Code', monospace;
    margin: 0.15rem 0.15rem 0 0;
    border: 1px solid rgba(99,102,241,0.3);
}

.timeline-item {
    border-left: 3px solid #6366f1;
    padding: 0.5rem 0 0.5rem 1.2rem;
    margin-bottom: 1rem;
    position: relative;
}
.timeline-item::before {
    content: '';
    width: 12px;
    height: 12px;
    background: #6366f1;
    border-radius: 50%;
    position: absolute;
    left: -7px;
    top: 8px;
    box-shadow: 0 0 10px rgba(99,102,241,0.6);
}
.timeline-year { font-size: 0.78rem; color: #6366f1; font-weight: 600; letter-spacing: 1px; }
.timeline-text { font-size: 0.95rem; color: #cbd5e1; margin-top: 0.15rem; }

.info-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(99,102,241,0.15);
    border: 1px solid rgba(99,102,241,0.3);
    color: #c7d2fe;
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 500;
    margin: 0.2rem;
}

.metric-box {
    background: linear-gradient(135deg, rgba(99,102,241,0.15), rgba(6,182,212,0.1));
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 1rem;
    padding: 1.2rem;
    text-align: center;
}
.metric-value { font-size: 2.2rem; font-weight: 800; color: #a5b4fc; }
.metric-label { font-size: 0.8rem; color: #64748b; margin-top: 0.2rem; text-transform: uppercase; letter-spacing: 1px; }

.fancy-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #6366f1, #06b6d4, transparent);
    border: none;
    margin: 2rem 0;
    border-radius: 999px;
}

.stTextInput > label, .stTextArea > label, .stSelectbox > label { color: #94a3b8 !important; font-size: 0.9rem !important; }

.stButton > button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: white !important;
    border: none !important;
    border-radius: 0.6rem !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.8rem !important;
}

.stTabs [data-baseweb="tab-list"] { gap: 0.5rem; background: transparent; }
.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 0.5rem;
    color: #94a3b8;
    font-weight: 500;
    padding: 0.5rem 1.2rem;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    border-color: transparent !important;
    color: white !important;
}

/* ── Industry-Standard Resume Paper Styling ── */
.resume-paper {
    background: #ffffff;
    color: #111827;
    border-radius: 4px;
    padding: 3.5rem 4rem;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.5;
    margin: 1rem auto 2.5rem auto;
    max-width: 850px;
}
.resume-name {
    font-size: 2.2rem;
    font-weight: 800;
    color: #111827;
    letter-spacing: -0.5px;
    margin: 0;
    text-align: center;
    text-transform: uppercase;
}
.resume-subtitle {
    font-size: 1rem;
    font-weight: 600;
    color: #374151;
    margin-top: 0.2rem;
    margin-bottom: 0.4rem;
    text-align: center;
}
.resume-contact-bar {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.9rem;
    font-size: 0.86rem;
    color: #4b5563;
    padding-bottom: 0.9rem;
    border-bottom: 1.5px solid #111827;
    margin-bottom: 1.4rem;
}
.resume-contact-item {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
}
.resume-section-heading {
    font-size: 0.98rem;
    font-weight: 800;
    color: #111827;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid #9ca3af;
    padding-bottom: 0.25rem;
    margin-top: 1.3rem;
    margin-bottom: 0.8rem;
}
.resume-item-title {
    font-size: 0.96rem;
    font-weight: 700;
    color: #111827;
}
.resume-item-subtitle {
    font-size: 0.9rem;
    font-style: italic;
    color: #374151;
}
.resume-item-date {
    font-size: 0.85rem;
    color: #4b5563;
    font-weight: 600;
}
.resume-bullet-list {
    margin: 0.35rem 0 0.9rem 1.2rem;
    padding: 0;
    color: #1f2937;
    font-size: 0.9rem;
}
.resume-bullet-list li {
    margin-bottom: 0.3rem;
    line-height: 1.5;
}
.resume-skill-tag {
    display: inline-block;
    background: #f3f4f6;
    color: #1f2937;
    font-weight: 600;
    font-size: 0.8rem;
    padding: 0.2rem 0.55rem;
    border-radius: 4px;
    border: 1px solid #e5e7eb;
    margin: 0.15rem 0.2rem 0.15rem 0;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "visit_count" not in st.session_state:
    st.session_state.visit_count = 1
else:
    st.session_state.visit_count += 1

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0 0.5rem;'>
        <div style='font-size:2rem;'>💻</div>
        <div style='font-weight:700; font-size:1rem; color:#a5b4fc; margin-top:0.3rem;'>Helge Justine O. Dano</div>
        <div style='font-size:0.75rem; color:#64748b;'>BSCS · Section F1</div>
    </div>
    <hr style='border-color: rgba(99,102,241,0.2); margin: 0.8rem 0;'>
    """, unsafe_allow_html=True)

    st.markdown("**🧭 Quick Navigation**")
    st.markdown("""
    <a href='#about' style='display:block;color:#94a3b8;padding:0.5rem 0.8rem;border-radius:0.5rem;text-decoration:none;font-size:0.9rem;margin-bottom:0.2rem;'>👤 About Me</a>
    <a href='#autobiography' style='display:block;color:#94a3b8;padding:0.5rem 0.8rem;border-radius:0.5rem;text-decoration:none;font-size:0.9rem;margin-bottom:0.2rem;'>📖 Autobiography</a>
    <a href='#skills' style='display:block;color:#94a3b8;padding:0.5rem 0.8rem;border-radius:0.5rem;text-decoration:none;font-size:0.9rem;margin-bottom:0.2rem;'>⚡ Skills</a>
    <a href='#projects' style='display:block;color:#94a3b8;padding:0.5rem 0.8rem;border-radius:0.5rem;text-decoration:none;font-size:0.9rem;margin-bottom:0.2rem;'>🚀 Projects</a>
    <a href='#resume' style='display:block;color:#94a3b8;padding:0.5rem 0.8rem;border-radius:0.5rem;text-decoration:none;font-size:0.9rem;margin-bottom:0.2rem;'>📄 Resume</a>
    <a href='#contact' style='display:block;color:#94a3b8;padding:0.5rem 0.8rem;border-radius:0.5rem;text-decoration:none;font-size:0.9rem;margin-bottom:0.2rem;'>✉️ Contact</a>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color: rgba(99,102,241,0.2);'>", unsafe_allow_html=True)

    st.markdown("**🎛️ Preferences**")
    show_fun_facts = st.checkbox("Show Fun Facts", value=True)
    skill_detail = st.radio("Skill Display", ["Chart", "Table", "Both"], index=2)

    st.markdown("<hr style='border-color: rgba(99,102,241,0.2);'>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style='background:rgba(99,102,241,0.1); border:1px solid rgba(99,102,241,0.2); border-radius:0.8rem; padding:0.8rem; text-align:center;'>
        <div style='font-size:1.5rem; font-weight:800; color:#a5b4fc;'>{st.session_state.visit_count}</div>
        <div style='font-size:0.75rem; color:#64748b;'>PAGE INTERACTIONS</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── PDF Resume Generator ──────────────────────────────────────────────────
    @st.cache_data
    def generate_resume_pdf() -> bytes:
        import io
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors

        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=34, bottomMargin=34)
        story = []
        styles = getSampleStyleSheet()

        primary = colors.HexColor('#1E3A8A')
        text_dark = colors.HexColor('#111827')
        muted = colors.HexColor('#4B5563')
        subtle_line = colors.HexColor('#CBD5E1')

        name_style = ParagraphStyle('RName', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=21, leading=25, textColor=primary, alignment=1)
        contact_style = ParagraphStyle('RContact', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=muted, alignment=1)
        sec_head_style = ParagraphStyle('RSecHead', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=primary, spaceBefore=6, spaceAfter=2, textTransform='uppercase')
        job_left = ParagraphStyle('RJobL', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=text_dark)
        job_right = ParagraphStyle('RJobR', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=primary, alignment=2)
        job_sub_left = ParagraphStyle('RJobSubL', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8, leading=11, textColor=muted)
        job_sub_right = ParagraphStyle('RJobSubR', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=muted, alignment=2)
        bullet_style = ParagraphStyle('RBullet', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=text_dark, leftIndent=12, firstLineIndent=-8, spaceAfter=1.5)
        summary_style = ParagraphStyle('RSummary', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=text_dark)
        skill_lbl = ParagraphStyle('RSkillLbl', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, textColor=text_dark)
        skill_val = ParagraphStyle('RSkillVal', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=text_dark)

        # Header
        story.append(Paragraph('HELGE JUSTINE O. DANO', name_style))
        story.append(Spacer(1, 2))
        story.append(Paragraph('Cebu City, Philippines &nbsp;&bull;&nbsp; Section F1 &nbsp;&bull;&nbsp; BS Computer Science &nbsp;&bull;&nbsp; CIT-U &nbsp;&bull;&nbsp; github.com/Helge-Dano', contact_style))
        story.append(Spacer(1, 4))
        story.append(HRFlowable(width='100%', thickness=1.2, color=primary, spaceBefore=0, spaceAfter=4))

        # Professional Summary
        story.append(Paragraph('PROFESSIONAL SUMMARY', sec_head_style))
        story.append(HRFlowable(width='100%', thickness=0.5, color=subtle_line, spaceBefore=1, spaceAfter=3))
        story.append(Paragraph('Goal-oriented and analytical 3rd Year Computer Science student at Cebu Institute of Technology University (CIT-U) with strong foundations in discrete mathematics, algorithmic problem-solving, and system design. Proven project experience delivering native Android mobile applications with Kotlin, engineering robust relational database backends with MySQL and Java, and constructing responsive web frontends. Passionate about applying computational principles and emerging AI technologies to develop reliable, human-centric software.', summary_style))
        story.append(Spacer(1, 3))

        # Education
        story.append(Paragraph('EDUCATION', sec_head_style))
        story.append(HRFlowable(width='100%', thickness=0.5, color=subtle_line, spaceBefore=1, spaceAfter=3))
        edu_table = Table([
            [Paragraph('<b>Cebu Institute of Technology University (CIT-U)</b>', job_left), Paragraph('Cebu City, Philippines', job_right)],
            [Paragraph('Bachelor of Science in Computer Science (BSCS) &bull; Section F1', job_sub_left), Paragraph('Expected 2026 &bull; 3rd Year', job_sub_right)]
        ], colWidths=[380, 160])
        edu_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
        story.append(edu_table)
        story.append(Spacer(1, 1.5))
        story.append(Paragraph('<b>Relevant Coursework:</b> Data Structures &amp; Algorithms, Object-Oriented Programming, Database Management Systems, Discrete Mathematics, Software Engineering, Applied Artificial Intelligence (CSIT 349 Section F1).', bullet_style))
        story.append(Spacer(1, 3))

        # Technical Skills
        story.append(Paragraph('TECHNICAL &amp; CORE SKILLS', sec_head_style))
        story.append(HRFlowable(width='100%', thickness=0.5, color=subtle_line, spaceBefore=1, spaceAfter=3))
        skills_table = Table([
            [Paragraph('<b>Programming Languages:</b>', skill_lbl), Paragraph('Kotlin, Java, Python, JavaScript (ES6+), SQL, HTML5, CSS3', skill_val)],
            [Paragraph('<b>Tools &amp; Frameworks:</b>', skill_lbl), Paragraph('Android SDK, Streamlit, MySQL, Git, GitHub, VS Code', skill_val)],
            [Paragraph('<b>Core Competencies:</b>', skill_lbl), Paragraph('Logical Thinking, Algorithmic Problem Solving, Mathematical Modeling, Database Normalization (3NF), Full-Stack Collaboration', skill_val)],
        ], colWidths=[140, 400])
        skills_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1)]))
        story.append(skills_table)
        story.append(Spacer(1, 3))

        # Featured Projects
        story.append(Paragraph('FEATURED PROJECTS', sec_head_style))
        story.append(HRFlowable(width='100%', thickness=0.5, color=subtle_line, spaceBefore=1, spaceAfter=3))

        # CampusFix
        t_cf = Table([
            [Paragraph('<b>CampusFix &mdash; Campus Maintenance &amp; Incident Reporting Mobile App</b>', job_left), Paragraph('Solo Developer', job_right)],
            [Paragraph('<i>Stack: Kotlin, Android SDK, SQLite, Material Design</i>', job_sub_left), Paragraph('Mobile App', job_sub_right)]
        ], colWidths=[380, 160])
        t_cf.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
        story.append(t_cf)
        story.append(Paragraph('&bull; Conceptualized, designed, and developed an end-to-end native Android mobile app for students and faculty to submit campus maintenance tickets and repair requests.', bullet_style))
        story.append(Paragraph('&bull; Engineered incident image uploads, categorized issue reporting, and real-time status lifecycle tracking to accelerate administrative triage.', bullet_style))
        story.append(Paragraph('&bull; Enforced clean mobile architectural patterns guaranteeing fluid UI responsiveness across diverse screen sizes and Android OS versions.', bullet_style))
        story.append(Spacer(1, 2.5))

        # OnlyCodes
        t_oc = Table([
            [Paragraph('<b>OnlyCodes &mdash; Collaborative Developer Code Sharing Platform</b>', job_left), Paragraph('Database Developer', job_right)],
            [Paragraph('<i>Stack: Java, SQL, MySQL, Relational Database Modeling, JDBC</i>', job_sub_left), Paragraph('Team Project', job_sub_right)]
        ], colWidths=[380, 160])
        t_oc.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
        story.append(t_oc)
        story.append(Paragraph('&bull; Spearheaded relational database architecture and normalization (up to 3NF) for high-concurrency developer code sharing and snippet retrieval.', bullet_style))
        story.append(Paragraph('&bull; Authored optimized SQL queries, indexing routines, and transactional triggers adhering to strict ACID properties.', bullet_style))
        story.append(Paragraph('&bull; Seamlessly integrated data access services with Java controllers to facilitate low-latency database connection pooling.', bullet_style))
        story.append(Spacer(1, 2.5))

        # Project NOPE
        t_pn = Table([
            [Paragraph('<b>Project NOPE &mdash; Interactive Modern Web Application</b>', job_left), Paragraph('Frontend Developer', job_right)],
            [Paragraph('<i>Stack: HTML5, CSS3, JavaScript (ES6+), Responsive UI</i>', job_sub_left), Paragraph('Team Project', job_sub_right)]
        ], colWidths=[380, 160])
        t_pn.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)]))
        story.append(t_pn)
        story.append(Paragraph('&bull; Developed user-facing layout components and micro-interactions utilizing semantic HTML5, modern CSS flexbox/grid, and vanilla JavaScript.', bullet_style))
        story.append(Paragraph('&bull; Guaranteed cross-device responsiveness, fast page rendering, and seamless user interaction design across desktop and mobile screens.', bullet_style))
        story.append(Paragraph('&bull; Collaborated through Git feature branching and agile workflows to coordinate interface bindings with upstream API services.', bullet_style))
        story.append(Spacer(1, 3))

        # Achievements & Background
        story.append(Paragraph('ACHIEVEMENTS &amp; MILESTONES', sec_head_style))
        story.append(HRFlowable(width='100%', thickness=0.5, color=subtle_line, spaceBefore=1, spaceAfter=3))
        story.append(Paragraph('&bull; <b>Mathematical Logic to Engineering:</b> Discovered a strong early passion for mathematics and logical reasoning, successfully transferring those talents into software engineering and computational algorithms.', bullet_style))
        story.append(Paragraph('&bull; <b>Academic Development:</b> Active in collegiate programming tasks, group software engineering workflows, and applied artificial intelligence coursework at CIT-U.', bullet_style))

        doc.build(story)
        return buf.getvalue()

    pdf_resume_bytes = generate_resume_pdf()

    st.markdown("**📄 Official Resume**")
    st.download_button(
        label="📥 Download Resume (PDF)",
        data=pdf_resume_bytes,
        file_name="Helge_Justine_Dano_Resume.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

# ── Hero Banner ───────────────────────────────────────────────────────────────
st.markdown("""
<div class='hero-banner'>
    <p class='hero-name'>Helge Justine O. Dano</p>
    <p class='hero-sub'>Bachelor of Science in Computer Science · Cebu Institute of Technology University</p>
    <span class='hero-badge'>📍 Section F1 &nbsp;|&nbsp; CSIT 349 Applied AI</span>
</div>
""", unsafe_allow_html=True)

# ── Quick metrics ─────────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown("""<div class='metric-box'><div class='metric-value'>3+</div><div class='metric-label'>Projects Built</div></div>""", unsafe_allow_html=True)
with m2:
    st.markdown("""<div class='metric-box'><div class='metric-value'>4</div><div class='metric-label'>Core Skills</div></div>""", unsafe_allow_html=True)
with m3:
    st.markdown("""<div class='metric-box'><div class='metric-value'>3rd</div><div class='metric-label'>Year Level</div></div>""", unsafe_allow_html=True)
with m4:
    st.markdown("""<div class='metric-box'><div class='metric-value'>CBU</div><div class='metric-label'>Cebu City Born</div></div>""", unsafe_allow_html=True)

st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["👤 About", "📖 Autobiography", "⚡ Skills", "🚀 Projects", "📄 Resume", "✉️ Contact"])

# ════════════════════════════════════════════════════════════════
# TAB 1 — ABOUT
# ════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("<a name='about'></a>", unsafe_allow_html=True)
    col_pic, col_bio = st.columns([1, 2], gap="large")

    with col_pic:
        st.markdown("<div class='section-title'>📸 Profile</div>", unsafe_allow_html=True)
        st.image("mypic.jpg", use_container_width=True, caption="Helge Justine O. Dano")
        st.markdown("""
        <div style='text-align:center; margin-top:0.8rem;'>
            <span class='info-chip'>🎓 BSCS</span>
            <span class='info-chip'>📍 Cebu City</span>
            <span class='info-chip'>🏫 CIT-U</span>
            <span class='info-chip'>📋 Section F1</span>
        </div>
        """, unsafe_allow_html=True)

    with col_bio:
        st.markdown("<div class='section-title'>👋 Hello, I'm Helge!</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='section-card'>
            <p style='color:#cbd5e1; line-height:1.8; font-size:0.98rem;'>
                I'm a <strong style='color:#a5b4fc;'>3rd Year Computer Science student</strong> at 
                Cebu Institute of Technology University. Born and raised in the heart of
                <strong style='color:#a5b4fc;'>Cebu City</strong>, I'm a naturally happy person
                with a love for logical thinking, mathematics, and all things programming.
            </p>
            <p style='color:#cbd5e1; line-height:1.8; font-size:0.98rem;'>
                I started my journey with a passion for mathematics, and over time discovered
                how beautifully that mindset translates into the world of programming — where
                logic, creativity, and problem-solving collide.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-title' style='margin-top:1rem;'>📋 Personal Info</div>", unsafe_allow_html=True)
        info_df = pd.DataFrame({
            "Field": ["Full Name", "Program", "Institution", "Section", "Year Level", "Hometown"],
            "Details": [
                "Helge Justine O. Dano",
                "Bachelor of Science in Computer Science",
                "Cebu Institute of Technology University",
                "F1",
                "3rd Year",
                "Cebu City, Philippines"
            ]
        })
        st.dataframe(info_df, hide_index=True, use_container_width=True)

        if show_fun_facts:
            st.markdown("<div class='section-title' style='margin-top:1rem;'>😄 Fun Facts</div>", unsafe_allow_html=True)
            for f in [
                "😂 A little crazy and jokes a lot — but lovably so!",
                "🧮 Was a math lover before becoming a coder.",
                "🏠 Moved from Tisa to Bulacao when the family built their own house.",
                "💡 Logic is my love language.",
            ]:
                st.markdown(f"- {f}")

# ════════════════════════════════════════════════════════════════
# TAB 2 — AUTOBIOGRAPHY
# ════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("<a name='autobiography'></a>", unsafe_allow_html=True)
    st.markdown("<div class='section-title' style='font-size:1.8rem;'>📖 My Story</div>", unsafe_allow_html=True)

    bio_col, timeline_col = st.columns([3, 2], gap="large")

    with bio_col:
        st.markdown("""
        <div class='section-card'>
            <div class='section-title'>🏠 Roots &amp; Early Life</div>
            <p style='color:#cbd5e1; line-height:1.85; font-size:0.97rem;'>
                I was born and raised right here in <strong style='color:#a5b4fc;'>Cebu City</strong>,
                the Queen City of the South. Growing up, our family first lived in
                <strong style='color:#a5b4fc;'>Tisa, Cebu City</strong>, where we rented a house
                while building our foundations — not just the physical ones, but the ones that
                truly matter: values, dreams, and determination.
            </p>
            <p style='color:#cbd5e1; line-height:1.85; font-size:0.97rem;'>
                Later on, my family made the exciting move to
                <strong style='color:#a5b4fc;'>Bulacao, Cebu City</strong>,
                our very own home that we built from the ground up. That move was more than
                just a change of address — it was a symbol of hard work paying off.
            </p>
        </div>

        <div class='section-card'>
            <div class='section-title'>😄 Who I Am</div>
            <p style='color:#cbd5e1; line-height:1.85; font-size:0.97rem;'>
                I am <em>always</em> a happy person, and maybe a little bit crazy sometimes —
                I joke a lot and love keeping the energy positive wherever I go.
                Life is too short to be serious all the time!
            </p>
            <p style='color:#cbd5e1; line-height:1.85; font-size:0.97rem;'>
                But beneath the humor lives a deep passion for
                <strong style='color:#a5b4fc;'>logical thinking</strong>. I have always been drawn
                to mathematics — the way numbers and patterns work together with such elegant
                precision fascinated me from a young age.
            </p>
        </div>

        <div class='section-card'>
            <div class='section-title'>💻 The Tech Journey</div>
            <p style='color:#cbd5e1; line-height:1.85; font-size:0.97rem;'>
                It did not take long before those mathematical instincts and love for logical
                thinking naturally found their way into <strong style='color:#a5b4fc;'>programming</strong>.
                Writing code scratched the same itch — a puzzle to solve, a logic to untangle,
                a system to build.
            </p>
            <p style='color:#cbd5e1; line-height:1.85; font-size:0.97rem;'>
                With that passion leading the way, I chose to pursue
                <strong style='color:#a5b4fc;'>Bachelor of Science in Computer Science</strong> and
                selected <strong style='color:#a5b4fc;'>Cebu Institute of Technology University (CIT-U)</strong>
                as my academic home — a place to grow, learn, collaborate, and ultimately
                accomplish my goals as a software developer.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with timeline_col:
        st.markdown("<div class='section-title'>🗓️ Milestones</div>", unsafe_allow_html=True)
        for year, text in [
            ("Born", "Born in Cebu City — the beginning of everything."),
            ("Early Childhood", "Grew up in Tisa, Cebu City while renting a family home."),
            ("Big Move", "Family built their own house and moved to Bulacao, Cebu City."),
            ("Discovery", "Fell in love with mathematics and logical thinking in school."),
            ("Pivot", "Transferred those skills into programming — the spark ignites."),
            ("CIT-U", "Enrolled in BSCS at Cebu Institute of Technology University."),
            ("3rd Year", "Thriving in 3rd year — building projects and growing fast."),
        ]:
            st.markdown(f"""
            <div class='timeline-item'>
                <div class='timeline-year'>{year}</div>
                <div class='timeline-text'>{text}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🎯 Shared Interests?</div>", unsafe_allow_html=True)
        interests = ["Mathematics 🧮", "Programming 💻", "Logic Puzzles 🧩", "Problem Solving 🔍", "Mobile Apps 📱", "Web Dev 🌐"]
        selected_interests = st.multiselect("What do we have in common?", interests, default=interests[:3])
        if selected_interests:
            st.success(f"We share {len(selected_interests)} interests! 🤝")

# ════════════════════════════════════════════════════════════════
# TAB 3 — SKILLS
# ════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("<a name='skills'></a>", unsafe_allow_html=True)
    st.markdown("<div class='section-title' style='font-size:1.8rem;'>⚡ Skills &amp; Abilities</div>", unsafe_allow_html=True)

    skills_data = {
        "Skill": ["Logical Thinking", "Problem Solving", "Mathematics", "Programming"],
        "Proficiency (%)": [92, 88, 90, 85],
        "Category": ["Cognitive", "Cognitive", "Academic", "Technical"],
        "Years of Experience": [10, 8, 12, 4],
    }
    df_skills = pd.DataFrame(skills_data)

    st.markdown("**🎚️ Filter by minimum proficiency:**")
    min_skill = st.slider("Show skills above:", 0, 100, 50, step=5)
    df_filtered = df_skills[df_skills["Proficiency (%)"] >= min_skill]

    if skill_detail in ["Chart", "Both"]:
        st.markdown("<div class='section-title' style='margin-top:1rem;'>📊 Proficiency Chart</div>", unsafe_allow_html=True)
        st.bar_chart(df_filtered.set_index("Skill")["Proficiency (%)"], color="#6366f1")

        st.markdown("<div class='section-title' style='margin-top:1rem;'>📈 Growth Over the Years</div>", unsafe_allow_html=True)
        growth_df = pd.DataFrame({
            "Logical Thinking": [60, 70, 78, 85, 92],
            "Problem Solving":  [55, 65, 73, 82, 88],
            "Mathematics":      [65, 72, 80, 87, 90],
            "Programming":      [20, 45, 65, 78, 85],
        }, index=["HS Yr1", "HS Yr3", "Col Yr1", "Col Yr2", "Col Yr3"])
        st.line_chart(growth_df)

    if skill_detail in ["Table", "Both"]:
        st.markdown("<div class='section-title' style='margin-top:1rem;'>📋 Skills Table</div>", unsafe_allow_html=True)
        st.dataframe(df_filtered, hide_index=True, use_container_width=True)

    st.markdown("<div class='section-title' style='margin-top:1.5rem;'>🎯 Visual Skill Bars</div>", unsafe_allow_html=True)
    if df_filtered.empty:
        st.info("No skills match your filter. Try lowering the slider! 😊")
    else:
        for _, row in df_filtered.iterrows():
            pct = row["Proficiency (%)"]
            st.markdown(f"""
            <div class='skill-bar-label'>{row['Skill']}
                <span style='float:right;color:#6366f1;font-weight:600;'>{pct}%</span>
            </div>
            <div class='skill-bar-bg'>
                <div class='skill-bar-fill' style='width:{pct}%;'></div>
            </div>
            """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 4 — PROJECTS
# ════════════════════════════════════════════════════════════════
with tab4:
    st.markdown("<a name='projects'></a>", unsafe_allow_html=True)
    st.markdown("<div class='section-title' style='font-size:1.8rem;'>🚀 My Projects</div>", unsafe_allow_html=True)

    projects = [
        {
            "title": "CampusFix",
            "emoji": "🛠️",
            "role": "Solo Developer",
            "tech": ["Kotlin", "Android"],
            "desc": "A mobile app for campus maintenance reporting. Designed and developed entirely solo from concept to deployment using Kotlin for Android.",
            "outcome": "Full end-to-end Android app allowing students to report campus issues to admins.",
            "type": "Solo Project"
        },
        {
            "title": "OnlyCodes",
            "emoji": "🗄️",
            "role": "Database Developer",
            "tech": ["Java", "SQL", "MySQL"],
            "desc": "Collaborated on a full-stack project handling all things database — schema design, query optimization, and data integrity.",
            "outcome": "Robust, well-structured database backend powering the application's data layer.",
            "type": "Team Project"
        },
        {
            "title": "Project NOPE",
            "emoji": "🌐",
            "role": "Frontend Developer",
            "tech": ["HTML", "CSS", "JavaScript"],
            "desc": "Served as frontend developer, responsible for building the entire UI — layouts, interactions, and visual design using core web technologies.",
            "outcome": "A clean, responsive web interface delivering a smooth user experience.",
            "type": "Team Project"
        },
    ]

    p_cols = st.columns(3, gap="medium")
    for i, proj in enumerate(projects):
        with p_cols[i]:
            tech_badges = "".join([f"<span class='project-tech'>{t}</span>" for t in proj["tech"]])
            st.markdown(f"""
            <div class='project-card'>
                <div style='font-size:2rem; margin-bottom:0.5rem;'>{proj['emoji']}</div>
                <div class='project-title'>{proj['title']}</div>
                <div class='project-role'>🎭 Role: {proj['role']} &nbsp;·&nbsp; {proj['type']}</div>
                <p style='color:#94a3b8; font-size:0.88rem; line-height:1.7; margin:0.7rem 0;'>{proj['desc']}</p>
                <div style='margin-bottom:0.7rem;'>{tech_badges}</div>
                <div style='border-top:1px solid rgba(99,102,241,0.2); padding-top:0.7rem; font-size:0.85rem; color:#6366f1;'>
                    ✅ {proj['outcome']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>📊 Projects Overview Table</div>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame({
        "Project":    ["CampusFix", "OnlyCodes", "Project NOPE"],
        "Role":       ["Solo Developer", "Database Dev", "Frontend Dev"],
        "Tech Stack": ["Kotlin + Android", "Java + SQL", "HTML + CSS + JS"],
        "Type":       ["Solo", "Team", "Team"],
        "Status":     ["✅ Complete", "✅ Complete", "✅ Complete"]
    }), hide_index=True, use_container_width=True)

    st.markdown("<div class='section-title' style='margin-top:1rem;'>🧑‍💻 Tech Stack Exposure</div>", unsafe_allow_html=True)
    st.bar_chart(
        pd.DataFrame({
            "Hours (est.)": [120, 90, 80, 60, 60, 70]
        }, index=["Kotlin", "Java", "SQL", "HTML", "CSS", "JavaScript"]),
        color="#8b5cf6"
    )

# ════════════════════════════════════════════════════════════════
# TAB 5 — RESUME / CURRICULUM VITAE
# ════════════════════════════════════════════════════════════════
with tab5:
    st.markdown("<a name='resume'></a>", unsafe_allow_html=True)
    
    r_head_col, r_btn_col = st.columns([3, 2])
    with r_head_col:
        st.markdown("<div class='section-title' style='font-size:1.8rem;'>📄 Curriculum Vitae / Resume</div>", unsafe_allow_html=True)
        st.caption("Standard 1-page software engineer resume. Ready to view and download as PDF.")
    with r_btn_col:
        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Official Resume (PDF)",
            data=pdf_resume_bytes,
            file_name="Helge_Justine_Dano_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
            key="resume_tab_pdf_main"
        )

    resume_raw_html = """<div class='resume-paper'>
<!-- Header -->
<div class='resume-name'>Helge Justine O. Dano</div>
<div class='resume-subtitle'>Aspiring Software Engineer &bull; Computer Science Undergraduate</div>
<div class='resume-contact-bar'>
<span class='resume-contact-item'>📍 Cebu City, Philippines</span>
<span class='resume-contact-item'>🏫 Cebu Institute of Technology University</span>
<span class='resume-contact-item'>🏷️ Section F1 &bull; CSIT 349</span>
<span class='resume-contact-item'>✉️ contact@helgedano.dev</span>
<span class='resume-contact-item'>🔗 github.com/Helge-Dano</span>
</div>

<!-- Professional Summary -->
<div class='resume-section-heading'>Professional Summary</div>
<p style='color:#1f2937; font-size:0.91rem; margin:0; line-height:1.6;'>
Goal-oriented and analytical 3rd Year Computer Science student at Cebu Institute of Technology University with strong foundations in discrete mathematics, algorithmic problem-solving, and logical systems design. Proven project experience delivering native Android mobile applications with Kotlin, engineering robust relational database backends with MySQL and Java, and constructing responsive web frontends. Passionate about applying computational principles and emerging AI technologies to develop reliable, human-centric software.
</p>

<!-- Education -->
<div class='resume-section-heading'>Education</div>
<div style='display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap;'>
<div>
<span class='resume-item-title'>Cebu Institute of Technology University (CIT-U)</span><br>
<span class='resume-item-subtitle'>Bachelor of Science in Computer Science (BSCS) &bull; Section F1</span>
</div>
<div style='text-align:right;'>
<span class='resume-item-date'>Cebu City, Philippines</span><br>
<span class='resume-item-date' style='color:#1e3a8a;'>Expected Graduation: 2026</span>
</div>
</div>
<div style='font-size:0.87rem; color:#4b5563; margin-top:0.35rem;'>
<strong>Relevant Coursework:</strong> Data Structures &amp; Algorithms, Object-Oriented Programming, Database Management Systems, Discrete Mathematics, Software Engineering, Applied Artificial Intelligence (CSIT 349).
</div>

<!-- Technical Skills -->
<div class='resume-section-heading'>Technical Skills</div>
<div style='font-size:0.9rem; color:#1f2937;'>
<div style='margin-bottom:0.3rem;'>
<strong>Programming Languages:</strong> 
<span class='resume-skill-tag'>Kotlin</span>
<span class='resume-skill-tag'>Java</span>
<span class='resume-skill-tag'>Python</span>
<span class='resume-skill-tag'>JavaScript (ES6+)</span>
<span class='resume-skill-tag'>SQL</span>
<span class='resume-skill-tag'>HTML5</span>
<span class='resume-skill-tag'>CSS3</span>
</div>
<div style='margin-bottom:0.3rem;'>
<strong>Tools &amp; Frameworks:</strong> 
<span class='resume-skill-tag'>Android SDK</span>
<span class='resume-skill-tag'>Streamlit</span>
<span class='resume-skill-tag'>MySQL</span>
<span class='resume-skill-tag'>Git / GitHub</span>
<span class='resume-skill-tag'>VS Code</span>
</div>
<div>
<strong>Core Competencies:</strong> Logical Thinking, Algorithmic Problem Solving, Mathematical Modeling, Database Normalization (3NF), Full-Stack Collaboration
</div>
</div>

<!-- Featured Projects -->
<div class='resume-section-heading'>Featured Projects</div>

<!-- Project 1 -->
<div style='margin-bottom:1rem;'>
<div style='display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap;'>
<div>
<span class='resume-item-title'>CampusFix</span> &mdash; 
<span class='resume-item-subtitle'>Campus Maintenance &amp; Incident Reporting Mobile App</span>
</div>
<div class='resume-item-date'>Solo Developer &bull; Android</div>
</div>
<div style='font-size:0.82rem; color:#4b5563; font-style:italic; margin-top:0.1rem;'>Tech Stack: Kotlin, Android SDK, SQLite, Material Design</div>
<ul class='resume-bullet-list'>
<li>Conceptualized, designed, and developed an end-to-end native Android application for students and faculty to submit campus maintenance tickets and repair requests directly to administrative teams.</li>
<li>Engineered incident image uploads, categorized issue reporting, and real-time status lifecycle tracking to accelerate ticket triage and resolution.</li>
<li>Enforced clean mobile architectural patterns guaranteeing fluid UI responsiveness across diverse screen sizes and Android OS versions.</li>
</ul>
</div>

<!-- Project 2 -->
<div style='margin-bottom:1rem;'>
<div style='display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap;'>
<div>
<span class='resume-item-title'>OnlyCodes</span> &mdash; 
<span class='resume-item-subtitle'>Collaborative Developer Code Sharing Platform</span>
</div>
<div class='resume-item-date'>Database Developer &bull; Team</div>
</div>
<div style='font-size:0.82rem; color:#4b5563; font-style:italic; margin-top:0.1rem;'>Tech Stack: Java, SQL, MySQL, Relational Database Modeling, JDBC</div>
<ul class='resume-bullet-list'>
<li>Spearheaded relational database architecture and normalization (up to 3NF) for high-concurrency developer code sharing and snippet retrieval.</li>
<li>Authored optimized SQL queries, indexing routines, and transactional triggers adhering to strict ACID properties.</li>
<li>Seamlessly integrated data access services with Java controllers to facilitate low-latency database connection pooling.</li>
</ul>
</div>

<!-- Project 3 -->
<div style='margin-bottom:0.5rem;'>
<div style='display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap;'>
<div>
<span class='resume-item-title'>Project NOPE</span> &mdash; 
<span class='resume-item-subtitle'>Interactive Modern Web Application</span>
</div>
<div class='resume-item-date'>Frontend Developer &bull; Team</div>
</div>
<div style='font-size:0.82rem; color:#4b5563; font-style:italic; margin-top:0.1rem;'>Tech Stack: HTML5, CSS3, JavaScript (ES6+), Responsive Design</div>
<ul class='resume-bullet-list'>
<li>Developed user-facing layout components and micro-interactions utilizing semantic HTML5, modern CSS flexbox/grid, and vanilla JavaScript.</li>
<li>Guaranteed cross-device responsiveness, fast page rendering, and seamless user interaction design across desktop and mobile screens.</li>
<li>Collaborated through Git feature branching and agile workflows to coordinate interface bindings with upstream API services.</li>
</ul>
</div>

<!-- Achievements & Milestones -->
<div class='resume-section-heading'>Achievements &amp; Milestones</div>
<ul class='resume-bullet-list' style='margin-bottom:0;'>
<li><strong>Mathematical Logic to Engineering:</strong> Discovered a strong early passion for mathematics and logical reasoning, successfully transferring those talents into software engineering and computational algorithms.</li>
<li><strong>Academic Development:</strong> Active in collegiate programming tasks, group software engineering workflows, and applied artificial intelligence coursework at CIT-U.</li>
</ul>
</div>"""
    st.markdown(resume_raw_html, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TAB 6 — CONTACT
# ════════════════════════════════════════════════════════════════
with tab6:
    st.markdown("<a name='contact'></a>", unsafe_allow_html=True)
    st.markdown("<div class='section-title' style='font-size:1.8rem;'>✉️ Get In Touch</div>", unsafe_allow_html=True)

    form_col, info_col = st.columns([3, 2], gap="large")

    with form_col:
        st.markdown("**Send me a message or leave feedback!** 👇")
        with st.form("contact_form"):
            name_input    = st.text_input("Your Name",  placeholder="e.g. Juan Dela Cruz")
            email_input   = st.text_input("Your Email", placeholder="e.g. juan@email.com")
            subject_input = st.selectbox("Subject", [
                "General Inquiry",
                "Project Collaboration",
                "Feedback on Portfolio",
                "Academic Discussion",
                "Just Saying Hi! 👋"
            ])
            message_input = st.text_area("Message", placeholder="Write your message here...", height=130)
            agree         = st.checkbox("I agree this is a friendly message 😄")
            sent          = st.form_submit_button("🚀 Send Message")

        if sent:
            if not name_input or not message_input:
                st.error("⚠️ Please fill in your name and message!")
            elif not agree:
                st.warning("☝️ Please check the agreement box first!")
            else:
                st.session_state.submitted = True
                with st.spinner("Sending your message..."):
                    time.sleep(1.2)
                st.success(f"✅ Message sent! Thanks **{name_input}**, I'll get back to you soon! 🎉")
                st.balloons()

    with info_col:
        st.markdown("<div class='section-title'>📍 About Me</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='section-card'>
            <p style='color:#cbd5e1; font-size:0.93rem; line-height:1.9;'>
                <strong style='color:#a5b4fc;'>Helge Justine O. Dano</strong><br>
                🎓 3rd Year BSCS Student<br>
                🏫 Cebu Institute of Technology University<br>
                📋 Section F1<br>
                📍 Cebu City, Philippines
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-title' style='margin-top:1rem;'>💬 Messages Received</div>", unsafe_allow_html=True)
        st.metric(
            label="Total Messages",
            value="1" if st.session_state.submitted else "0",
            delta="+1 new" if st.session_state.submitted else None
        )

        st.markdown("<div class='section-title' style='margin-top:1rem;'>⭐ Rate This Portfolio</div>", unsafe_allow_html=True)
        rating = st.select_slider(
            "Your rating:",
            options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
            value="⭐⭐⭐⭐⭐"
        )
        st.info(f"You rated: **{rating}** — Thank you! 🙏")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; padding:1.5rem 0 2rem; color:#475569;'>
    <div style='font-size:0.9rem;'>
        Made with ❤️ by
        <strong style='color:#a5b4fc;'>Helge Justine O. Dano</strong>
        &nbsp;·&nbsp;
        <strong style='color:#6366f1;'>Section F1</strong>
        &nbsp;·&nbsp; CSIT 349 Applied AI
    </div>
    <div style='font-size:0.78rem; margin-top:0.4rem; color:#374151;'>
        Cebu Institute of Technology University · 2024–2025
    </div>
</div>
""", unsafe_allow_html=True)

import streamlit as st
from src.crawler import crawl_website
from src.validator import validate_data
from src.chunker import create_chunks
from src.rag_pipeline import build_store, answer_query
from src.university_db import (
    UNIVERSITIES, get_all_continents, get_countries_by_continent,
    filter_universities, get_university_info
)
import time

st.set_page_config(
    page_title="🎓 Global University RAG Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1.5rem 0;
        animation: gradient 3s ease infinite;
        background-size: 200% 200%;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .sub-header {
        text-align: center;
        color: #8e9aaf;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .uni-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .uni-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .uni-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.4);
    }
    
    .uni-logo {
        background: white;
        padding: 0.8rem;
        border-radius: 12px;
        max-width: 100px;
        max-height: 100px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        object-fit: contain;
    }
    
    .uni-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0.5rem 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        position: relative;
    }
    
    .uni-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        margin-bottom: 1rem;
        position: relative;
    }
    
    .uni-info-row {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin: 1rem 0;
        position: relative;
    }
    
    .uni-info-badge {
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        backdrop-filter: blur(10px);
    }
    
    .visit-btn {
        background: white;
        color: #667eea;
        padding: 0.7rem 1.5rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin-top: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        position: relative;
    }
    
    .visit-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        text-decoration: none;
    }
    
    .answer-box {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        border-left: 6px solid #667eea;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        margin: 2rem 0;
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .answer-content {
        color: #2d3748;
        font-size: 1.15rem;
        line-height: 1.8;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.9rem 2.5rem;
        border-radius: 30px;
        font-weight: 600;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.6);
        transform: translateY(-3px);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p {
        color: white !important;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f7fafc 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
        text-align: center;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-label {
        color: #64748b;
        font-size: 0.95rem;
        margin-top: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .analytics-box {
        background: linear-gradient(135deg, #f7fafc 0%, #ffffff 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
    }
    
    .analytics-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 1.5rem;
    }
    
    .uni-detail-box {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    
    .uni-detail-box:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.15);
    }
    
    .stat-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem;
    }
    
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 4rem;
        border-radius: 10px;
        color: #64748b;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    hr {
        margin: 3rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
    }
    
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 0.9rem;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .streamlit-expanderHeader {
        background: #f7fafc;
        border-radius: 12px;
        font-weight: 600;
        padding: 1rem;
    }
    
    .footer {
        text-align: center;
        color: #8e9aaf;
        padding: 3rem 0 2rem 0;
        border-top: 1px solid #e2e8f0;
        margin-top: 3rem;
    }
    
    .footer-highlight {
        color: #667eea;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🎓 Global University RAG Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">✨ AI-Powered University Information System • 50+ Top Universities Worldwide</p>', unsafe_allow_html=True)

if 'store' not in st.session_state:
    st.session_state.store = None
if 'selected_universities' not in st.session_state:
    st.session_state.selected_universities = []
if 'crawled_data' not in st.session_state:
    st.session_state.crawled_data = {}
if 'total_documents' not in st.session_state:
    st.session_state.total_documents = 0

# ============================================================
# SIDEBAR: ONLY SELECTION CONTROLS - NOTHING ELSE
# ============================================================
with st.sidebar:
    st.markdown("### 🌍 Select Universities")
    
    st.markdown("#### 📍 Continent")
    continents = ["All"] + get_all_continents()
    selected_continent = st.selectbox("Continent", continents, key="continent_select", label_visibility="collapsed")
    
    st.markdown("#### 🌏 Country")
    countries = ["All"] + get_countries_by_continent(selected_continent)
    selected_country = st.selectbox("Country", countries, key="country_select", label_visibility="collapsed")
    
    st.markdown("#### 🔍 Search")
    search_query = st.text_input("Search", placeholder="Type university name...", key="search_input", label_visibility="collapsed")
    
    filtered_unis = filter_universities(
        continent=selected_continent if selected_continent != "All" else None,
        country=selected_country if selected_country != "All" else None,
        search_query=search_query
    )
    
    st.caption(f"✨ Found **{len(filtered_unis)}** universities")
    
    selected_universities = st.multiselect("Choose Universities", options=filtered_unis, default=st.session_state.selected_universities, label_visibility="collapsed")
    st.session_state.selected_universities = selected_universities

# END OF SIDEBAR - NO OTHER SECTIONS!

tab1, tab2, tab3 = st.tabs(["🏠 Home", "💬 Ask Questions", "📊 Analytics"])

with tab1:
    st.markdown("## 🔨 Build Knowledge Base")
    
    if not selected_universities:
        st.info("👈 **Select universities from the sidebar to begin!**")
        
        st.markdown("### 🌟 Featured Universities")
        cols = st.columns(3)
        for idx, name in enumerate(["MIT", "IIT Bombay", "Oxford"]):
            if name in UNIVERSITIES:
                with cols[idx]:
                    info = UNIVERSITIES[name]
                    if info.get('image'):
                        try:
                            st.image(info['image'], width=100)
                        except:
                            pass
                    st.markdown(f"**{name}**")
                    st.caption(f"📍 {info['country']}")
    else:
        # ============================================================
        # THIS IS WHERE UNIVERSITY INFO CARDS APPEAR - ON HOMEPAGE!
        # ============================================================
        st.markdown("### ✅ Selected Universities")
        
        for i in range(0, len(selected_universities), 2):
            cols = st.columns(2)
            for j, uni in enumerate(selected_universities[i:i+2]):
                with cols[j]:
                    info = get_university_info(uni)
                    
                    html = '<div class="uni-card">'
                    if info.get('image'):
                        html += f'<img src="{info["image"]}" class="uni-logo" onerror="this.style.display=\'none\'" />'
                    
                    html += f'''
                        <div class="uni-title">{uni}</div>
                        <div class="uni-subtitle">{info['name']}</div>
                        <div class="uni-info-row">
                            <div class="uni-info-badge">🌍 {info['city']}, {info['state']}, {info['country']}</div>
                            <div class="uni-info-badge">🏛️ Founded {info.get('established', 'N/A')}</div>
                        </div>
                        <div class="uni-info-row">
                            <div class="uni-info-badge">🏆 {info['ranking']}</div>
                            <div class="uni-info-badge">🎓 {info['type']}</div>
                        </div>
                        <a href="{info['url']}" target="_blank" class="visit-btn">🔗 Visit Website</a>
                    </div>
                    '''
                    st.markdown(html, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if st.button("🚀 Build Knowledge Base", type="primary", use_container_width=True):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            all_data = []
            total = len(selected_universities)
            
            for idx, uni_name in enumerate(selected_universities):
                status_text.markdown(f"### 📡 Crawling **{uni_name}**... ({idx+1}/{total})")
                progress_bar.progress((idx) / (total * 4))
                
                uni_info = get_university_info(uni_name)
                try:
                    data = crawl_website(uni_info['url'], max_pages=20)
                    if uni_info.get('admissions_url'):
                        try:
                            data.extend(crawl_website(uni_info['admissions_url'], max_pages=5))
                        except:
                            pass
                    all_data.extend(data)
                    st.session_state.crawled_data[uni_name] = len(data)
                except Exception as e:
                    st.warning(f"⚠️ Error: {str(e)}")
            
            progress_bar.progress(0.25)
            status_text.markdown("### ✅ Validating...")
            valid_data = validate_data(all_data)
            
            progress_bar.progress(0.50)
            status_text.markdown("### ✂️ Chunking...")
            documents = create_chunks(valid_data)
            st.session_state.total_documents = len(documents)
            
            progress_bar.progress(0.75)
            status_text.markdown("### 🔮 Building store...")
            store = build_store(documents)
            st.session_state.store = store
            
            progress_bar.progress(1.0)
            status_text.empty()
            progress_bar.empty()
            
            st.success("✨ **Knowledge Base Built Successfully!**")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f'<div class="metric-card"><div class="metric-value">{len(selected_universities)}</div><div class="metric-label">Universities</div></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="metric-card"><div class="metric-value">{len(documents)}</div><div class="metric-label">Documents</div></div>', unsafe_allow_html=True)
            with col3:
                st.markdown(f'<div class="metric-card"><div class="metric-value">{len(valid_data)}</div><div class="metric-label">Valid Records</div></div>', unsafe_allow_html=True)
            
            time.sleep(0.5)
            st.balloons()

with tab2:
    if st.session_state.store:
        st.markdown("## 💬 Ask Your Questions")
        
        with st.expander("💡 **Sample Questions**", expanded=False):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Admissions:**\n- What are admission requirements?\n- When is the application deadline?\n\n**Programs:**\n- Tell me about CS programs")
            with c2:
                st.markdown("**Financial:**\n- What are the tuition fees?\n- What scholarships are available?\n\n**Research:**\n- Compare research opportunities")
        
        question = st.text_input("🎯 Your Question", placeholder="Ask about admissions, programs, fees, research...", key="question_input")
        
        c1, c2 = st.columns([3, 1])
        with c1:
            ask = st.button("🔍 Get Answer", type="primary", use_container_width=True)
        with c2:
            if st.button("🔄 Reset All", use_container_width=True):
                st.session_state.store = None
                st.session_state.selected_universities = []
                st.session_state.crawled_data = {}
                st.rerun()
        
        if ask and question:
            with st.spinner("🤔 Analyzing..."):
                answer, sources = answer_query(st.session_state.store, question, k=5)
            
            st.markdown("---")
            st.markdown(f'<div class="answer-box"><h3 style="color: #667eea; margin-bottom: 1rem;">🎯 Answer</h3><div class="answer-content">{answer}</div></div>', unsafe_allow_html=True)
            
            if sources:
                st.markdown("### 📚 Sources & References")
                for idx, src in enumerate(sources, 1):
                    with st.expander(f"📖 Source {idx}: {src['metadata']['section']}", expanded=(idx==1)):
                        st.markdown(f"**🏫 {src['metadata']['university']}**")
                        st.markdown(f"**📄 {src['metadata']['section']}**")
                        st.markdown(f"**🔗 [{src['metadata']['url']}]({src['metadata']['url']})")
                        st.info(src['text'][:600] + "...")
        elif ask:
            st.warning("⚠️ Please enter a question")
    else:
        st.info("📝 **Build the knowledge base first in the Home tab**")

with tab3:
    st.markdown("## 📊 Comprehensive Analytics Dashboard")
    
    if st.session_state.store and st.session_state.crawled_data:
        st.markdown("### 📈 Key Performance Indicators")
        
        total_pages = sum(st.session_state.crawled_data.values())
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{len(st.session_state.selected_universities)}</div><div class="metric-label">Universities</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.total_documents}</div><div class="metric-label">Documents</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{st.session_state.store.get_size()}</div><div class="metric-label">Embeddings</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{total_pages}</div><div class="metric-label">Pages</div></div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        ca, cb = st.columns(2)
        
        with ca:
            st.markdown('<div class="analytics-box"><div class="analytics-title">🎓 University Breakdown</div>', unsafe_allow_html=True)
            for uni in st.session_state.selected_universities:
                info = get_university_info(uni)
                pages = st.session_state.crawled_data.get(uni, 0)
                docs = st.session_state.total_documents // len(st.session_state.selected_universities) if st.session_state.selected_universities else 0
                st.markdown(f'''<div class="uni-detail-box">
                    <div style="font-weight: 700; font-size: 1.2rem; color: #2d3748; margin-bottom: 0.8rem;">🏛️ {uni}</div>
                    <div style="color: #64748b; font-size: 0.95rem; margin-bottom: 0.8rem;">📍 {info['city']}, {info['country']} • Founded {info.get('established', 'N/A')}</div>
                    <div><span class="stat-badge">📄 {pages} pages</span><span class="stat-badge">📚 ~{docs} docs</span><span class="stat-badge">🏆 {info['ranking']}</span></div>
                </div>''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with cb:
            st.markdown('<div class="analytics-box"><div class="analytics-title">🌍 Geographic Distribution</div>', unsafe_allow_html=True)
            st.markdown("<strong>📊 By Country:</strong><br><br>", unsafe_allow_html=True)
            
            country_counts = {}
            for uni in st.session_state.selected_universities:
                country = UNIVERSITIES[uni]['country']
                country_counts[country] = country_counts.get(country, 0) + 1
            
            for country, count in sorted(country_counts.items(), key=lambda x: x[1], reverse=True):
                pct = (count / len(st.session_state.selected_universities)) * 100
                st.markdown(f'''<div style="margin: 1.5rem 0;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <span style="font-weight: 700; color: #2d3748;">🌐 {country}</span>
                        <span style="color: #667eea; font-weight: 700;">{count} ({pct:.0f}%)</span>
                    </div>
                    <div style="background: #e2e8f0; height: 12px; border-radius: 6px; overflow: hidden;">
                        <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); height: 100%; width: {pct}%; border-radius: 6px;"></div>
                    </div>
                </div>''', unsafe_allow_html=True)
            
            st.markdown("<br><strong>🗺️ By Continent:</strong><br><br>", unsafe_allow_html=True)
            continent_counts = {}
            for uni in st.session_state.selected_universities:
                cont = UNIVERSITIES[uni]['continent']
                continent_counts[cont] = continent_counts.get(cont, 0) + 1
            
            for cont, count in sorted(continent_counts.items(), key=lambda x: x[1], reverse=True):
                pct = (count / len(st.session_state.selected_universities)) * 100
                st.markdown(f'''<div style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #667eea;">
                    <strong>{cont}</strong>: {count} universities ({pct:.0f}%)
                </div>''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown('<div class="analytics-box"><div class="analytics-title">📊 Data Quality Metrics</div>', unsafe_allow_html=True)
        
        cd1, cd2, cd3, cd4 = st.columns(4)
        avg_pages = total_pages / len(st.session_state.crawled_data) if st.session_state.crawled_data else 0
        avg_docs = st.session_state.total_documents / len(st.session_state.selected_universities) if st.session_state.selected_universities else 0
        coverage = (len(st.session_state.crawled_data) / len(st.session_state.selected_universities) * 100) if st.session_state.selected_universities else 0
        
        with cd1:
            st.metric("📄 Avg Pages", f"{avg_pages:.1f}")
        with cd2:
            st.metric("📚 Avg Docs", f"{avg_docs:.0f}")
        with cd3:
            st.metric("✅ Coverage", f"{coverage:.0f}%")
        with cd4:
            density = st.session_state.store.get_size() // len(st.session_state.selected_universities) if st.session_state.selected_universities else 0
            st.metric("🔮 Density", f"{density}/uni")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 🔍 Quality Assessment")
        
        ci1, ci2 = st.columns(2)
        with ci1:
            st.info(f"""**💡 Summary:**
- ✅ **{len(st.session_state.selected_universities)} universities** indexed
- 📄 **{total_pages} pages** collected
- 📚 **{st.session_state.total_documents}** documents generated
- 🔮 **{st.session_state.store.get_size()}** embeddings created
- 🌍 **{len(country_counts)} countries** across **{len(continent_counts)} continents**""")
        
        with ci2:
            quality = "🌟 Excellent" if avg_pages > 15 else ("✅ Good" if avg_pages > 10 else "⚠️ Moderate")
            rec = "Outstanding coverage! Ready for complex queries." if avg_pages > 15 else ("Good coverage for most queries." if avg_pages > 10 else "Consider crawling more pages for better results.")
            
            st.success(f"""**📈 Quality: {quality}**

**Metrics:**
- Average: {avg_pages:.1f} pages/university
- Coverage: {coverage:.0f}%
- Density: {density} embeddings/uni

**Status:**
✅ Advanced Q&A ready  
✅ Semantic search enabled  
✅ Multi-university comparison

**💡 Recommendation:** {rec}""")
        
    else:
        st.info("📊 **Build a knowledge base to see comprehensive analytics**")

st.markdown("---")
st.markdown('<div class="footer"><p>Built with <span class="footer-highlight">❤️</span> using <span class="footer-highlight">Streamlit • FAISS • Groq LLM</span></p><p style="font-size: 0.9rem; margin-top: 0.5rem;">🎓 <strong>Global University RAG v5.0</strong> • 50+ Universities</p></div>', unsafe_allow_html=True)
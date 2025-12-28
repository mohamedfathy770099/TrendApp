import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.request
import xml.etree.ElementTree as ET

# 1. إعدادات الهوية والتصميم السينمائي
st.set_page_config(page_title="تـرنـد | النبض الحي", page_icon="🔥", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; background-color: #050505; color: white; }
    .stApp { background-color: #050505; }
    
    /* تصميم كروت الأخبار الفخمة */
    .news-card {
        background: linear-gradient(145deg, #1a1a1a, #0f0f0f);
        border-right: 5px solid #ff4b4b;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid #333;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.1);
    }
    .tag { background: #ff4b4b; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }
    .pulse { color: #4CAF50; font-weight: bold; animation: blink 1.5s infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    
    /* إخفاء القوائم الافتراضية المزعجة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. نظام التحقق بالأكواد المتفق عليها
MASTER_CODE = "MASTER-ADMIN-2026"
FRIEND_CODES = ["FRIEND-01", "FRIEND-02", "FRIEND-03", "FRIEND-04", "FRIEND-05"]

if 'auth_status' not in st.session_state:
    st.session_state.auth_status = None

# بوابة الدخول
if st.session_state.auth_status is None:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b; margin-top: 50px;'>🔥 تـرنـد</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>اتصل بالرادار الحي الآن</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        code = st.text_input("", type="password", placeholder="أدخل كود العبور...")
        if st.button("تـسجيل الـدخول"):
            if code == MASTER_CODE:
                st.session_state.auth_status = "admin"
                st.rerun()
            elif code in FRIEND_CODES:
                st.session_state.auth_status = "user"
                st.rerun()
            else:
                st.error("الكود غير صحيح! تواصل مع القائد.")
else:
    # 3. محرك سحب الأخبار الحقيقي (الرادار)
    def fetch_saudi_news():
        try:
            url = "https://news.google.com/rss/search?q=Saudi+Arabia&hl=ar&gl=SA&ceid=SA:ar"
            with urllib.request.urlopen(url) as response:
                tree = ET.parse(response)
                root = tree.getroot()
                news_items = []
                for item in root.findall('.//item')[:10]: # جلب أفضل 10 أخبار
                    news_items.append({
                        "title": item.find('title').text,
                        "link": item.find('link').text,
                        "date": item.find('pubDate').text[:16]
                    })
                return news_items
        except:
            return []

    # 4. الواجهة الرئيسية الكاملة
    with st.sidebar:
        st.markdown(f"<h2 style='color: #ff4b4b;'>🕹️ غرفة القيادة</h2>", unsafe_allow_html=True)
        st.write(f"الرتبة: {'قائد (أدمن)' if st.session_state.auth_status == 'admin' else 'عضو تجريبي'}")
        st.markdown("---")
        section = st.radio("الأقسام:", ["🔥 نبض المملكة", "🌍 الأخبار العالمية", "⚽ الرياضة"])
        if st.button("تسجيل الخروج"):
            st.session_state.auth_status = None
            st.rerun()

    st.markdown(f"<h1>📺 {section}</h1>", unsafe_allow_html=True)
    
    with st.spinner('جاري مسح الرادار وسحب النبض...'):
        news_list = fetch_saudi_news()
    
    if news_list:
        for news in news_list:
            st.markdown(f"""
            <div class="news-card">
                <span class="tag">عاجل</span>
                <h3>{news['title']}</h3>
                <p style='color: #888;'>{news['date']}</p>
                <span class="pulse">● نبض حي الآن</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("الرادار يواجه ضباباً حالياً، جاري محاولة إعادة الاتصال...")

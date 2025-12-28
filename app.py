import streamlit as st
from datetime import datetime

# 1. إعدادات الهوية البصرية (التصميم الفخم المتفق عليه)
st.set_page_config(page_title="تـرنـد | النبض الحي", page_icon="🔥", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #050505;
    }
    
    .stApp { background-color: #050505; color: white; }
    
    /* تصميم كرت الخبر المتوهج */
    .news-card {
        background: linear-gradient(145deg, #1a1a1a, #0f0f0f);
        border-right: 4px solid #ff4b4b;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        border: 1px solid #333;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    .tag { background: #ff4b4b; color: white; padding: 2px 10px; border-radius: 5px; font-size: 12px; font-weight: bold; }
    .pulse-dot { color: #4CAF50; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    
    /* تنسيق الأزرار */
    div.stButton > button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. قاعدة بيانات الأكواد (الأمان)
MASTER_CODE = "MASTER-ADMIN-2026"
FRIEND_CODES = ["FRIEND-01", "FRIEND-02", "FRIEND-03", "FRIEND-04", "FRIEND-05"]

if 'user_role' not in st.session_state:
    st.session_state.user_role = None

# 3. بوابة الدخول
if st.session_state.user_role is None:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b; margin-top: 50px;'>🔥 تـرنـد</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>أدخل كود العبور للاتصال بالنبض الحي</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        input_code = st.text_input("", type="password", placeholder="أدخل الكود هنا...")
        if st.button("فـتـح البـوابـة"):
            if input_code == MASTER_CODE:
                st.session_state.user_role = "admin"
                st.rerun()
            elif input_code in FRIEND_CODES:
                st.session_state.user_role = "user"
                st.rerun()
            else:
                st.error("❌ الكود غير صحيح أو منتهي الصلاحية")
else:
    # 4. واجهة التطبيق الكاملة (V1.0)
    with st.sidebar:
        st.markdown(f"<h2 style='color: #ff4b4b;'>🕹️ غرفة القيادة</h2>", unsafe_allow_html=True)
        if st.session_state.user_role == "admin":
            st.success("أهلاً بك يا قائد")
        else:
            st.info("وضع المستخدم: تجربة الأصدقاء")
            
        st.markdown("---")
        menu = st.radio("الأقسام الحالية:", ["🔥 نبض اليوم", "🇸🇦 المملكة", "⚽ الرياضة", "💰 الاقتصاد"])
        
        if st.button("تسجيل الخروج"):
            st.session_state.user_role = None
            st.rerun()

    # محتوى الأقسام (الرادار)
    st.markdown(f"<h1 style='text-align: right;'>📺 {menu}</h1>", unsafe_allow_html=True)
    
    # محاكاة لبيانات الرادار المحدثة
    trends = [
        {"cat": "عاجل", "title": "تحديث نظام الرادار الفعلي", "body": "تم بنجاح دمج أكواد الأصدقاء الخمسة وكود القائد الماستر. التطبيق الآن جاهز للمرحلة التجريبية الأولى.", "status": "متوهج الآن 🔥"},
        {"cat": "المملكة", "title": "ترند السعودية اليوم", "body": "نقاشات واسعة حول التحول الرقمي الجديد في العاصمة الرياض وتأثيره على جودة الحياة.", "status": "نشط 🟢"}
    ]

    for item in trends:
        st.markdown(f"""
        <div class="news-card">
            <span class="tag">{item['cat']}</span>
            <h2 style='margin-top: 10px; color: #fff;'>{item['title']}</h2>
            <p style='color: #bbb; font-size: 18px;'>{item['body']}</p>
            <span class="pulse-dot">● {item['status']}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("نسخة التجربة الأولى الكاملة V1.0 - جميع الصلاحيات محفوظة")

import streamlit as st
import random

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="تـرنـد | الحكاية من أولها", page_icon="🔥", layout="centered")

# تنسيق الواجهة (Dark Theme)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    div.stButton > button:first-child { background-color: #ff4b4b; color: white; width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. تعريف الأكواد (أكواد الأصدقاء وقائد)
MASTER_CODE = "MASTER-ADMIN-2026"
USER_CODES = ["FRIEND-01", "FRIEND-02", "FRIEND-03", "FRIEND-04", "FRIEND-05"]

# 3. إدارة الجلسة (Session State)
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

# 4. بوابة الدخول
if st.session_state.user_role is None:
    st.markdown("<h1 style='text-align: center;'>🔑 بوابة تـرنـد</h1>", unsafe_allow_html=True)
    entered_code = st.text_input("أدخل كود العبور الخاص بك:", type="password")
    
    if st.button("فـتـح البـوابـة"):
        if entered_code == MASTER_CODE:
            st.session_state.user_role = "admin"
            st.rerun()
        elif entered_code in USER_CODES:
            st.session_state.user_role = "user"
            st.rerun()
        else:
            st.error("الكود غير صحيح! يرجى التواصل مع الإدارة.")

else:
    # 5. واجهة التطبيق
    role_title = "قـائـد" if st.session_state.user_role == "admin" else "مـستـخدم"
    st.markdown(f"<h1 style='text-align: center;'>🔥 نـبـض الـتـرنـد ({role_title})</h1>", unsafe_allow_html=True)
    
    # القائمة الجانبية (تختلف حسب الرتبة)
    with st.sidebar:
        st.title("🕹️ غرفة القيادة")
        if st.session_state.user_role == "admin":
            st.success("أهلاً بك يا قائد. صلاحياتك كاملة ✅")
            st.write("إحصائيات الرادار: نشط 📡")
        else:
            st.info("أهلاً بك يا ضيف تـرنـد. استمتع بالحكايات ✨")
        
        if st.button("تسجيل الخروج"):
            st.session_state.user_role = None
            st.rerun()

    # محتوى الأخبار (النبض)
    st.markdown("---")
    st.subheader("📡 آخر التحديثات الآن")
    
    # مثال لقصة تظهر للجميع
    with st.container():
        st.markdown("### 🇸🇦 أخبار المملكة | مشروع تقني واعد")
        with st.expander("الحكاية من أولها.."):
            st.write("بدأت كفكرة في مختبرات الرياض، واليوم نراها واقعاً يغير مجرى التقنية المحلية.")

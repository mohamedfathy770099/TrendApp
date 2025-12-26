import streamlit as st
import random

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(
    page_title="تـرنـد | الحكاية من أولها",
    page_icon="🔥",
    layout="centered"
)

# تنسيق مخصص لجعل الواجهة فخمة (Dark Theme)
st.markdown("""
    <style>
    .main {
        direction: rtl;
        text-align: right;
    }
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام التحقق والدخول
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center;'>🔑 بوابة تـرنـد</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>أدخل كود القائد للوصول إلى النبض الحي</p>", unsafe_allow_html=True)
    
    admin_code = st.text_input("", type="password", placeholder="أدخل الكود هنا...")
    
    if st.button("فـتـح البـوابـة"):
        if admin_code == "COMMANDER-01":
            st.session_state.authenticated = True
            st.success("تم التحقق بنجاح.. جاري الدخول")
            st.rerun()
        else:
            st.error("الكود غير صحيح! الوصول مرفوض.")

else:
    # 3. واجهة التطبيق الحقيقية (بعد الدخول)
    st.markdown("<h1 style='text-align: center;'>🔥 نـبـض الـتـرنـد</h1>", unsafe_allow_html=True)
    
    # قائمة جانبية للتحكم
    with st.sidebar:
        st.title("🕹️ غرفة القيادة")
        st.write("الحالة: متصل بالرادار ✅")
        st.write("المستخدمين الآن: 1 (أنت)")
        if st.button("تسجيل الخروج"):
            st.session_state.authenticated = False
            st.rerun()

    # محاكاة لبيانات الرادار (ستتحدث تلقائياً مستقبلاً)
    stories = [
        {
            "category": "🇸🇦 أخبار المملكة",
            "title": "إنجاز تقني جديد في الرياض",
            "heat": "🔥 متوهج",
            "hook": "الشرارة بدأت من..",
            "full_story": "إطلاق مبادرة وطنية ضخمة لدمج الذكاء الاصطناعي في التعليم العام، بدأت بورشة عمل سرية قبل 6 أشهر واليوم أصبحت واقعاً."
        },
        {
            "category": "💰 اقتصاد",
            "title": "قفزة في أسهم الطاقة",
            "heat": "🟠 دافئ",
            "hook": "الحكاية من أولها..",
            "full_story": "تسريبات عن عقود توريد عالمية جديدة جعلت المستثمرين يتسابقون منذ ساعات الصباح الأولى، مما رفع المؤشر بنسبة 3%."
        }
    ]

    # عرض القصص في الواجهة
    for s in stories:
        with st.expander(f"{s['category']} | {s['title']} ({s['heat']})"):
            st.markdown(f"**{s['hook']}**")
            st.write(s['full_story'])
            st.button(f"مشاركة نبض {s['title']}", key=s['title'])

    st.markdown("---")
    st.caption("التطبيق يعمل الآن بنسخة Alpha 1.0")

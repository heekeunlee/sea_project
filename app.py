import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import random

# Page configuration
st.set_page_config(
    page_title="Ocean Explorer",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for a beautiful look
st.markdown("""
<style>
    .main {
        background-color: #f0f8ff;
    }
    .stApp {
        background: linear-gradient(135deg, #e0f2fe, #fdfbfb);
    }
    h1 {
        color: #0077b6;
        font-family: 'Gothic', sans-serif;
        font-weight: 800;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #0077b6;
        color: white;
        border-radius: 12px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #00b4d8;
        transform: scale(1.05);
    }
    .sidebar-content {
        background-color: #0077b6;
        color: white;
    }
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Application Navigation
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1459213599465-03ad6a47b431?ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80", use_container_width=True)
    st.title("🌊 바다 탐험가 (Ocean Explorer)")
    menu = st.radio(
        "메뉴 선택",
        ["🏠 홈 (Home)", "📚 학습 (Learning)", "💡 퀴즈 (Quiz)", "📷 활동 기록 (Data Logger)", "🗺️ 바다 지도 (Ocean Map)"]
    )
    st.markdown("---")
    st.write("2026 바다꾸러기 키움사업")

# Home Section
if menu == "🏠 홈 (Home)":
    st.title("🌊 바다를 지키는 미래 리더, '바다 탐험가'")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 안녕하세요, 바다 탐험가 여러분! 👋
        
        해양 생태계는 우리 지구의 70%를 차지하며, 우리가 숨 쉬는 산소의 절반 이상을 만들어냅니다. 
        하지만 기후 변화와 플라스틱 오염으로 바다는 점점 아파하고 있어요.
        
        이 앱은 **바다꾸러기 키움사업**의 일환으로 제작되었습니다.
        함께 바다에 대해 배우고, 문제를 고민하며, 아름다운 바다를 지켜나가는 주인공이 되어볼까요?
        """)
        
        st.info("💡 왼쪽 메뉴에서 학습과 퀴즈를 시작해 보세요!")
        
    with col2:
        st.image("https://images.unsplash.com/photo-1544551763-47a184117db7?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", caption="우리가 지켜야 할 아름다운 바다")

# Learning Section
elif menu == "📚 학습 (Learning)":
    st.title("📚 바다에 대해 알아볼까요?")
    
    tab1, tab2, tab3 = st.tabs(["해양 생태계", "바다 오염의 진실", "기후 변화와 바다"])
    
    with tab1:
        st.markdown("### 🐠 바다 속 다양한 친구들")
        st.write("""
        바다에는 산호초, 심해, 연안 갯벌 등 다양한 생태계가 있어요. 
        특히 '바다의 열대우림'이라 불리는 **산호초**는 수많은 해양 생물의 안식처입니다.
        우리나라의 **갯벌** 또한 전 지구적으로 중요한 생태적 가치를 지니고 있습니다.
        """)
        st.image("https://images.unsplash.com/photo-1546026423-cc064306478c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80")
        
    with tab2:
        st.markdown("### ⚠️ 미세 플라스틱의 위험")
        st.write("""
        해마다 약 800만 톤 이상의 플라스틱이 바다로 흘러갑니다. 
        이 플라스틱은 햇빛과 파도에 쪼개져 **미세 플라스틱**이 되고, 
        물고기들이 이를 먹으면 결국 우리 인간의 건강까지 위협하게 됩니다.
        """)
        st.warning("분리수거를 철저히 하고, 일회용품 사용을 줄이는 것이 바다를 살리는 첫걸음입니다!")
        
    with tab3:
        st.markdown("### 🌡️ 뜨거워지는 바다")
        st.write("""
        이산화탄소가 증가하면서 지구 전체가 뜨거워지고 있습니다. 
        바다는 열을 흡수하지만, 온도가 너무 높아지면 산호가 하얗게 변하는 **백화 현상**이 일어납니다.
        """)

# Quiz Section
elif menu == "💡 퀴즈 (Quiz)":
    st.title("💡 바다 박사 도전! 퀴즈 타임")
    
    questions = {
        "우리나라에서 '바다의 열대우림'이라 불리며 많은 생물이 사는 곳은?": ["산호초", "심해", "남극", "갯벌"],
        "이산화탄소가 많아져 바다 온도가 올라가 산호가 하얗게 변하는 현상은?": ["백화 현상", "적조 현상", "녹조 현상", "해수면 상승"],
        "지구 산소의 절반 이상을 생산하는 곳은 어디일까요?": ["바다", "아마존 정글", "도시의 공원", "히말라야 산맥"]
    }
    
    correct_answers = ["산호초", "백화 현상", "바다"]
    
    score = 0
    for i, (q, options) in enumerate(questions.items()):
        st.subheader(f"Q{i+1}. {q}")
        ans = st.radio(f"정답을 선택하세요! ({i+1})", options, key=f"q{i}")
        if st.button(f"정답 확인 ({i+1})"):
            if ans == correct_answers[i]:
                st.success("🎉 정답입니다!")
                score += 1
            else:
                st.error(f"⚠️ 아쉬워요! 정답은 '{correct_answers[i]}'입니다.")
    
    if score == 3:
        st.balloons()
        st.markdown("### 🏅 당신은 완벽한 바다 탐험가입니다!")

# Data Logger Section
elif menu == "📷 활동 기록 (Data Logger)":
    st.title("📷 나만의 바다 관찰 기록")
    
    st.info("직접 관찰한 바다 생물이나 분리수거 등 바다 지키기 활동 사진을 업로드해 보세요!")
    
    with st.form("activity_form"):
        date = st.date_input("활동 날짜")
        activity_type = st.selectbox("활동 종류", ["바다 생물 관찰", "비치코밍(쓰레기 줍기)", "분리수거 실천", "기타"])
        content = st.text_area("활동 내용이나 느낀 점을 적어주세요.")
        uploaded_file = st.file_uploader("사진을 업로드하세요 (JPG, PNG)", type=["jpg", "png", "jpeg"])
        
        submit = st.form_submit_button("기록 저장하기")
        
        if submit:
            st.success(f"[{date}] {activity_type} 기록이 저장되었습니다!")
            if uploaded_file:
                st.image(uploaded_file, caption="업로드된 사진", width=300)
            st.balloons()

# Map Section
elif menu == "🗺️ 바다 지도 (Ocean Map)":
    st.title("🗺️ 주요 해양 보호구역 확인하기")
    
    st.write("우리나라와 세계의 아름다운 해양 보호구역을 지도로 확인해 보세요.")
    
    # Mock data for demonstration
    locations = pd.DataFrame({
        'name': ['제주 서귀포 문섬', '충남 태안군 신두리', '전남 보성·순천 갯벌', '그레이트 배리어 리프 (호주)', '갈라파고스 군도 (에콰도르)'],
        'lat': [33.2201, 36.8504, 34.8105, -18.2871, -0.9538],
        'lon': [126.5619, 126.1852, 127.4815, 147.6992, -90.9656],
        'type': ['산호초 보호구역', '해안사구 보호구역', '유네스코 갯벌', '세계 최대 산호초', '생태계의 보고']
    })
    
    fig = px.scatter_mapbox(locations, lat="lat", lon="lon", hover_name="name", hover_data=["type"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=500)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    > **해양 보호구역(MPA)**이란?  
    > 생물 다양성이 풍부하거나 생태적으로 보전 가치가 높은 해역을 지정하여 특별히 관리하는 곳입니다.
    """)

# Footer
st.markdown("---")
st.caption("Copyright © 2026 바다꾸러기 키움사업 Team. All rights reserved.")

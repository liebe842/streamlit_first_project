import streamlit as st
import pandas as pd

st.title('🎭 MBTI 성격 유형 분석기')
st.write('당신의 MBTI를 선택하면 어울리는 직업과 궁합이 맞는 유형을 알려드립니다!')

# MBTI 데이터
mbti_data = {
    'INTJ': {
        'jobs': ['데이터 사이언티스트 📊', '전략 기획자 📈', '시스템 설계자 💻', '연구원 🔬', '투자 분석가 💰'],
        'match': ['ENFP 🦋', 'ENTP 🎭', 'ENFJ 🌟'],
        'description': '완벽주의적이고 전략적인 "용의주도한 전략가" 유형입니다. 혼자만의 시간을 통해 아이디어를 발전시키는 것을 좋아합니다. 🎯'
    },
    'INTP': {
        'jobs': ['프로그래머 💻', '물리학자 ⚛️', '철학자 🤔', '게임 개발자 🎮', '건축가 🏛️'],
        'match': ['ENTJ 👑', 'ENFJ 🌟', 'ESTJ 📋'],
        'description': '논리적이고 창의적인 "논리적인 사색가" 유형입니다. 복잡한 문제 해결을 즐기며 새로운 이론을 탐구하는 것을 좋아합니다. 🧩'
    },
    'ENTJ': {
        'jobs': ['CEO 👔', '변호사 ⚖️', '경영 컨설턴트 💼', '정치인 🎤', '기업가 💫'],
        'match': ['INTP 🤔', 'ISTP 🔧', 'INFP 🎨'],
        'description': '카리스마 있고 효율적인 "대담한 통솔자" 유형입니다. 목표 달성을 위해 열정적으로 노력하며 리더십이 뛰어납니다. 👑'
    },
    'ENTP': {
        'jobs': ['발명가 💡', '기업가 🚀', '마케터 📢', '변호사 ⚖️', '컨설턴트 💼'],
        'match': ['INFJ 🎭', 'INTJ 🔮', 'INFP 🎨'],
        'description': '혁신적이고 독창적인 "논쟁을 즐기는 혁신가" 유형입니다. 새로운 아이디어를 만들어내는 것을 좋아합니다. 💫'
    },
    'INFJ': {
        'jobs': ['상담사 🤝', '작가 ✍️', '심리학자 🧠', '교사 📚', '예술 치료사 🎨'],
        'match': ['ENTP 🎭', 'ENFP 🦋', 'INFP 🎨'],
        'description': '이상적이고 통찰력 있는 "선의의 옹호자" 유형입니다. 다른 사람들을 돕고 세상을 더 나은 곳으로 만들고 싶어합니다. 🌟'
    },
    'INFP': {
        'jobs': ['작가 ✍️', '예술가 🎨', '음악가 🎵', '심리 상담사 💕', '번역가 📖'],
        'match': ['ENFJ 🌟', 'ENTJ 👑', 'INFJ 🎭'],
        'description': '이상적이고 창의적인 "열정적인 중재자" 유형입니다. 자신만의 가치관을 중요시하며 예술적 표현을 즐깁니다. 🌈'
    },
    'ENFJ': {
        'jobs': ['교사 📚', '인사 관리자 👥', 'NGO활동가 🌍', '카운슬러 💝', '마케팅 매니저 📢'],
        'match': ['INFP 🎨', 'ISFP 🎵', 'INTP 🤔'],
        'description': '카리스마 있고 영감을 주는 "정의로운 사회운동가" 유형입니다. 다른 사람의 성장을 돕는 것을 좋아합니다. 💖'
    },
    'ENFP': {
        'jobs': ['배우 🎭', '기자 📰', '광고 크리에이터 🎨', '이벤트 플래너 🎉', '강연자 🎤'],
        'match': ['INTJ 🔮', 'INFJ 🎭', 'ISTJ 📋'],
        'description': '열정적이고 창의적인 "재기발랄한 활동가" 유형입니다. 새로운 가능성을 발견하고 도전하는 것을 좋아합니다. 🌈'
    },
    'ISTJ': {
        'jobs': ['회계사 📊', '군인 🎖️', '판사 ⚖️', '행정가 📋', '엔지니어 🔧'],
        'match': ['ESFP 🎉', 'ESTP 🏃', 'ENFP 🦋'],
        'description': '신중하고 책임감 있는 "청렴결백한 논리주의자" 유형입니다. 규칙과 전통을 중요시하며 체계적으로 일합니다. 📋'
    },
    'ISFJ': {
        'jobs': ['간호사 ⚕️', '초등학교 교사 📚', '사서 📖', '행정 지원 📁', '영양사 🍎'],
        'match': ['ESFP 🎉', 'ESTP 🏃', 'ENTP 💡'],
        'description': '따뜻하고 헌신적인 "용감한 수호자" 유형입니다. 다른 사람을 돕고 보살피는 것을 좋아합니다. 💝'
    },
    'ESTJ': {
        'jobs': ['관리자 👔', '군인 🎖️', '판사 ⚖️', '금융인 💰', '프로젝트 매니저 📊'],
        'match': ['ISFP 🎵', 'ISTP 🔧', 'INTP 🤔'],
        'description': '실용적이고 체계적인 "엄격한 관리자" 유형입니다. 목표 달성을 위해 효율적으로 일하는 것을 좋아합니다. 📋'
    },
    'ESFJ': {
        'jobs': ['교사 📚', '영업직 💼', '호텔리어 🏨', '간호사 ⚕️', '이벤트 플래너 🎉'],
        'match': ['ISFP 🎵', 'ISTP 🔧', 'INTP 🤔'],
        'description': '사교적이고 배려심 많은 "사교적인 외교관" 유형입니다. 다른 사람들을 돕고 화합을 이루는 것을 좋아합니다. 💖'
    },
    'ISTP': {
        'jobs': ['엔지니어 🔧', '파일럿 ✈️', '운동선수 ⚽', '정비사 🔨', '건축가 🏗️'],
        'match': ['ESTJ 📋', 'ENTJ 👑', 'ESFJ 💝'],
        'description': '과감하고 실용적인 "만능 재주꾼" 유형입니다. 손으로 직접 만들고 문제를 해결하는 것을 좋아합니다. 🔧'
    },
    'ISFP': {
        'jobs': ['아티스트 🎨', '음악가 🎵', '패션 디자이너 👗', '사진작가 📸', '요리사 👨‍🍳'],
        'match': ['ENFJ 🌟', 'ESFJ 💝', 'ESTJ 📋'],
        'description': '예술적이고 자유로운 "호기심 많은 예술가" 유형입니다. 감각적인 경험과 자기표현을 즐깁니다. 🎨'
    },
    'ESTP': {
        'jobs': ['기업가 💼', '영업직 🤝', '운동선수 ⚽', '소방관 🚒', '경찰관 👮'],
        'match': ['ISFJ 💝', 'ISTJ 📋', 'INFJ 🎭'],
        'description': '모험적이고 현실적인 "대담한 사업가" 유형입니다. 즉흥적인 행동과 새로운 경험을 즐깁니다. 🎯'
    },
    'ESFP': {
        'jobs': ['연예인 🎭', '영업직 🤝', '이벤트 플래너 🎉', '헤어디자이너 💇', '여행 가이드 🌍'],
        'match': ['ISFJ 💝', 'ISTJ 📋', 'INTJ 🔮'],
        'description': '즐거움을 추구하는 "자유로운 영혼의 연예인" 유형입니다. 삶을 즐기고 다른 사람들을 행복하게 만드는 것을 좋아합니다. 🌟'
    }
}

# MBTI 선택
selected_mbti = st.selectbox(
    '당신의 MBTI를 선택하세요 ✨',
    list(mbti_data.keys())
)

if selected_mbti:
    st.header(f'🎯 {selected_mbti} 유형 분석')
    
    # 성격 설명
    st.subheader('💫 성격 특성')
    st.write(mbti_data[selected_mbti]['description'])
    
    # 추천 직업
    st.subheader('👔 추천 직업')
    jobs = mbti_data[selected_mbti]['jobs']
    for job in jobs:
        st.write(f'• {job}')
    
    # 궁합이 잘 맞는 MBTI
    st.subheader('❤️ 궁합이 잘 맞는 MBTI')
    matches = mbti_data[selected_mbti]['match']
    for match in matches:
        st.write(f'• {match}')

# 푸터
st.markdown('---')
st.markdown('Made with ❤️ by Your MBTI Analyzer')

# import streamlit as st

# # 화면에 표시할 초기 콘텐츠
# st.write("### 현재 페이지의 콘텐츠입니다.")
# st.write("여기에는 다양한 텍스트와 그래프, 버튼 등이 포함될 수 있습니다.")

# # 버튼 생성
# if st.button("화면 지우기"):
#     # 컨테이너를 생성하고 그 안에 콘텐츠를 넣기
#     st.write("xxx0")
#     placeholder = st.empty()
#     st.write("xxx1")
#     # 클릭 시 화면을 지움
#     placeholder.empty()
#     st.write("xxx2")
# else:
#     # 지우기 버튼이 눌리지 않은 경우에만 콘텐츠 유지
#     st.write("화면을 지우려면 위의 버튼을 클릭하세요.")



# st.write("yyy")


import streamlit as st

# 컨테이너 생성
placeholder = st.empty()

# 초기 화면 콘텐츠
with placeholder.container():
    st.write("### 현재 페이지의 콘텐츠입니다.")
    st.write("화면을 지우려면 아래 버튼을 클릭하세요.")

# 버튼 클릭 시 화면을 비우고 새로운 콘텐츠를 표시
if st.button("화면 지우기 및 새 콘텐츠 표시"):
    placeholder.empty()  # 기존 콘텐츠 지우기
    placeholder.write("### 새로운 콘텐츠입니다.")
    placeholder.write("이 화면은 버튼을 클릭하여 업데이트된 내용입니다.")
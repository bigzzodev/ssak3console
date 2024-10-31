    # 프로퍼타 아래에서 확인
    # https://echarts.apache.org/en/api.html#events
    #     [
    # 0:"click"         type
    
    # 1:"Sun"           name                    <<---
    # 2:410             value                   <<---
    # 3:"series"        componentType
    
    # 4:"bar"           seriesType
    # 5:3               seriesIndex
    # 6:"Video Ad"      seriesName              <<---

    # 7:6               dataIndex
    # 8:NULL            dataType
    # 9:410             data
    
    # 10:"#ee6666"      color
    # 11:NULL           info
    # ]


    # 프로퍼타 아래에서 확인
    # https://echarts.apache.org/en/api.html#events
    #     [
    # 0:"click"         type
    
    # 1:"Sun"           name                    <<---
    # 2:410             value                   <<---
    # 3:"series"        componentType
    
    # 4:"bar"           seriesType
    # 5:3               seriesIndex
    # 6:"Video Ad"      seriesName              <<---

    # 7:6               dataIndex
    # 8:NULL            dataType
    # 9:410             data
    
    # 10:"#ee6666"      color
    # 11:NULL           info
    # ] 
    # dblclick



    # st.divider()
    # st.success('MUSIC', icon="✅")
    # st.info('MUSIC', icon="ℹ️")
    # st.info('MUSIC')
    # st.info('**MUSIC**')
    # st.warning('This is a warning', icon="⚠️")
    # st.error('This is an error', icon="🚨")

#     # 초기 데이터 구조 설정
#     days_in_month = [f"{str(day).zfill(2)}일" for day in range(1, 32)]
#     class_data = {class_name: [0] * 31 for class_name in class_keys}  # 모든 클래스별로 0 초기화된 배열 생성


    # #---------------
    # # md = st.text_area('Type in your markdown string (without outer quotes)',
    # #                 "Happy Streamlit-ing! :balloon:")
    # md1 = '- 안녕하세요.'
    # md2 = '- 하이루.'
    # # st.code(f"""
    # # import streamlit as st

    # # st.markdown('''{md}''')
    # # """)

    # st.code(f"""
    # {md1}
    # {md2}
    # """)

    # st.markdown(md)

    # st.header("_Streamlit_ is :blue[cool] :sunglasses:")
    # st.header("This is a header with a divider", divider="gray")
    # st.header("These headers have :red[rotating] dividers", divider=True)
    # st.header("One", divider=True)
    # st.header("Two", divider=True)
    # st.header("Three", divider=True)
    # st.header("Four", divider=True)




    # st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
    # st.subheader("This is a subheader with a divider", divider="gray")
    # st.subheader("These subheaders have :red[rotating] dividers", divider=True)
    # st.subheader(":gray[One]", divider='blue')
    # st.subheader("Two", divider='red')
    # st.subheader("Three", divider=True)
    # st.subheader("해시태그", divider=True)

    #####################################################################
    # data = [
    #     {"name": name, "value": value}
    #     for name, value in [
    #         ("서태지", "999"),
    #         ("노랴", "8828"),
    #         ("컨2소트", "888"),
    #         ("수상이력", "888"),
    #         ("서3태지", "999"),
    #         ("노3랴", "888"),
    #         ("컨3소트", "888"),
    #         ("수4상이력", "888"),
    #         ("서5태지", "999"),
    #         ("노6랴", "888"),
    #         ("컨7소트", "8288"),
    #         ("수상8이력", "8828"),
    #     ]
    # ]
    # wordcloud_option = {"series": [{"type": "wordCloud", "data": data}]}
    # st_echarts(wordcloud_option)


    # https://github.com/tvst/st-annotated-text
    # from annotated_text import annotated_text, annotation, parameters
    # parameters.SHOW_LABEL_SEPARATOR = False
    # parameters.BORDER_RADIUS = 30
    # parameters.PADDING = "3 3rem"



    # data_list = [
    #     [100, 302, 301, 334, 390, 330, 320, 301, 334, 390, 88, 399],
    #     [555, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 99],
    #     [100, 182, 191, 234, 290, 330, 310, 191, 234, 290, 330, 310],
    #     [150, 212, 201, 154, 190, 330, 410, 201, 154, 190, 330, 410],
    #     [820, 832, 901, 934, 1290, 1330, 1320, 901, 934, 1290, 1330, 1320],
    #     [820, 832, 901, 934, 1290, 1330, 1320, 901, 934, 1290, 1330, 1320],
    #     [120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 99],
    #     [120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 99],
    #     [120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 199]
    # ]


#     data_list = [
#               12월   11월  10월  09월 08월   07월 06월   05월 04월  03월  02월  01월
#     MENTION  [100,  302,  301, 334, 390,  330, 320,  301, 334, 390, 88,  399],
#     BAD      [555,  132,  101, 134, 901,  230, 210,  101, 134, 190, 230,  99],
#     GOOD     [100,  182,  191, 234, 290,  330, 310,  191, 234, 290, 330, 310],
#     MUSIC    [150,  212,  201, 154, 190,  330, 410,  201, 154, 190, 330, 410],
#     ENT      [820,  832,  901, 934, 129,  130, 120,  901, 934, 190, 130, 120],
#     CONTRACT [820,  832,  901, 934, 129,  130, 120,  901, 934, 190, 130, 120],
#     AD       [120,  132,  101, 134, 910,  230, 210,  101, 134,  90, 230,  99],
#     RIP      [120,  132,  101, 134, 910,  230, 210,  101, 134,  90, 230,  99],
#     NO       [120,  132,  101, 134, 910,  230, 210,  101, 134,  90, 230, 199]
#     ]




    data_list = [
        [555, 302, 301, 334, 390, 330, 320, 301, 334, 390, 88, 99, 555, 302, 301, 334, 390, 330, 320, 301, 334, 390, 88, 99, 390, 330, 320, 301, 334, 390, 508],
        [120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 99, 120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 99, 390, 330, 320, 301, 334, 390, 507],
        [220, 182, 191, 234, 290, 330, 310, 191, 234, 290, 330, 310, 220, 182, 191, 234, 290, 330, 310, 191, 234, 290, 330, 310, 390, 330, 320, 301, 334, 390, 506],
        [150, 212, 201, 154, 190, 330, 410, 201, 154, 190, 330, 410, 150, 212, 201, 154, 190, 330, 410, 201, 154, 190, 330, 410, 390, 330, 320, 301, 334, 390, 505],
        [820, 832, 901, 934, 1290, 1330, 1320, 901, 934, 1290, 1330, 1320, 820, 832, 901, 934, 1290, 1330, 1320, 901, 934, 1290, 1330, 1320, 390, 330, 320, 301, 334, 390, 504],
        [820, 832, 901, 934, 1290, 1330, 1320, 901, 934, 1290, 1330, 1320, 390, 330, 320, 301, 334, 390, 200, 390, 330, 320, 301, 334, 390, 503],
        [120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 99, 390, 330, 320, 301, 334, 390, 200, 390, 330, 320, 301, 334, 390, 200, 301, 334, 390, 200, 502],
        [120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 99, 390, 330, 320, 301, 334, 390, 200, 390, 330, 320, 301, 334, 390, 200, 301, 334, 390, 200, 501],
        [120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 99, 390, 330, 320, 301, 334, 390, 200, 390, 330, 320, 301, 334, 390, 200, 301, 334, 390, 200, 500],
    ]


    # annotated_text(
    #     "This ",
    #     ("# is", "", "#3aa"),
    #     " some ",
    #     ("# 임창정 사기", "(2)", "#3aa"),
    #     ("text", "noun"),
    #     " for those of ",
    #     ("# 잠실 콘서트", "(31)", "#3a3"),
    #     " who ",
    #     ("like", "verb"),
    #     " this sort of ",
    #     ("thing", "noun"),
    #     "."
    # )
    # annotated_text(
    #     "이건뭐지? ",
    #     annotation("임창정!", "(31)", font_family="Comic Sans MS", border="2px dashed red"),
    # )
    # annotated_text(
    #     annotation("임창정!", "(31)", font_family="Comic Sans MS", border="2px red"), "  ",
    #     annotation("임창정!", "(31)", font_family="Comic Sans MS", border="2px red"), " ,  ",
    #     annotation("임창정!", "(31)", font_family="Comic Sans MS", border="2px red"), "  ",
    # )
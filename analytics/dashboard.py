import json
import streamlit as st
from streamlit_echarts import st_echarts
from .chart_options import year_option, year_series, month_option, month_series, all_option, all_series
from annotated_text import annotated_text, annotation, parameters
from collections import defaultdict
# class_MENTION, class_BAD, class_GOOD, class_MUSIC, class_ENT, class_CONTRACT, class_AD, , class_RIP, class_NO
SX_CLASS_NAME = ["MENTION", "BAD", "GOOD", "MUSIC", "ENT", "CONTRACT", "AD", "RIP", "NO"]


# ------------------------------------------------------------------------------------------------------------------------
def generate_data_list(json_data):
    # 클래스 이름 정의
    class_names = ["class_MENTION", "class_BAD", "class_GOOD", "class_MUSIC", 
                   "class_ENT", "class_CONTRACT", "class_AD", "class_RIP", "class_NO"]
    
    # 각 클래스별 연도별 값 리스트 생성 (연도 제외)
    data_list = []
    for class_name in class_names:
        # 각 연도별 해당 클래스의 값을 수집
        year_values = []
        for year_data in json_data:
            year_key = list(year_data.keys())[0]
            class_counts = year_data[year_key].get("class_counts", {})
            year_values.append(class_counts.get(class_name, 0))  # 클래스 값이 없으면 0 추가
        data_list.append(year_values)
    
    return data_list
# ------------------------------------------------------------------------------------------------------------------------
def _extract_year_data(_year, _data):
    class_keys = ["class_MENTION", "class_BAD", "class_GOOD", "class_MUSIC", "class_ENT", "class_CONTRACT", "class_AD", "class_RIP", "class_NO"]
    # months = ["01월", "02월", "03월", "04월", "05월", "06월", "07월", "08월", "09월", "10월", "11월", "12월"]
    year_data = {class_name: [0] * 12 for class_name in class_keys}
    for entry in _data:
        for month, info in entry.items():
            entry_year, entry_month = month.split("-")
            if entry_year == _year:
                month_index = int(entry_month) - 1
                for class_name in class_keys:
                    year_data[class_name][month_index] = info["class_counts"].get(class_name, 0)
    # 각 클래스의 데이터를 역순으로 저장
    data_list = [year_data[class_name][::-1] for class_name in class_keys]
    return data_list

# ------------------------------------------------------------------------------------------------------------------------
def _get_total_articles(json_data, target_month):
    for month_data in json_data:
        if target_month in month_data:
            return month_data[target_month].get("total_articles", 0)  # 값이 없으면 0 반환
    return 0  # 대상 월이 없으면 0 반환

# ------------------------------------------------------------------------------------------------------------------------
def _get_all_articles(json_data, target_year):
    # JSON 데이터 탐색
    for year_data in json_data:
        if target_year in year_data:
            return year_data[target_year].get("total_articles", 0)  # 값이 없으면 0 반환
    return 0  # 대상 연도가 없으면 0 반환

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# def all_dashboard(_singer, _selected_year):
def all_dashboard(_singer):
    # head = f'{_selected_year}년'
    # st.subheader(f'{head} - {_singer}')
    st.subheader(f'{_singer}')

    fmname = f'./jsondata/year_{_singer}.json'
    with open(fmname, "r", encoding="utf-8") as file:
        year_data = json.load(file)

    data_list = generate_data_list(year_data)

    #
    names = SX_CLASS_NAME
    series = all_series(names, data_list)
    options = all_option(series)
    events = {
        "click": "function(params) { return [params.type, params.name, params.value, params.componentType, params.seriesType, params.seriesIndex, params.seriesName, params.dataIndex, params.dataType, params.data, params.color, params.info ]}",
    }

    if st.button("off", key="key_all_button1"):
        options['legend'] = options.get('legend', {})
        options['legend']['selected'] = {name: False for name in names}  # 모든 항목을 False로 설정

    s = st_echarts(options=options, events=events, height="500px", key="key_all_dashboard")
    st.divider()
    if s is not None:
        xx = s[1].replace("년", "").strip()
        susu = _get_all_articles(year_data, xx)
        # ['click', '2023년', 584, 'series', 'bar', 0, 'MENTION', 3, None, 584, '#5470c6', None]
        year_dashboard(_singer, xx, susu)

# ------------------------------------------------------------------------------------------------------------------------
def year_dashboard(_singer, _selected_year, susu):
    head = f'{_selected_year}년'
    # st.subheader(f'{head} - {_singer}')
    st.subheader(f'{head} - ({susu})')
    names = SX_CLASS_NAME
    fmname = f'./jsondata/month_{_singer}.json'
    with open(fmname, "r", encoding="utf-8") as file:
        month_data = json.load(file)

    data_list = _extract_year_data(_selected_year, month_data)
    #
    series = year_series(names, data_list)
    options = year_option(series)
    events = {
        "click": "function(params) { return [params.type, params.name, params.value, params.componentType, params.seriesType, params.seriesIndex, params.seriesName, params.dataIndex, params.dataType, params.data, params.color, params.info ]}",
    }

    if st.button("off", key="key_year_button1"):
        options['legend'] = options.get('legend', {})
        options['legend']['selected'] = {name: False for name in names}  # 모든 항목을 False로 설정

    s = st_echarts(options=options, events=events, height="500px", key="key_year_dashboard")
    st.divider()
    if s is not None:
        xx = s[1].replace("월", "").strip()
        susu = _get_total_articles(month_data, f'{_selected_year}-{xx}')
        month_dashboard(_singer, susu, head, s[1])

# ------------------------------------------------------------------------------------------------------------------------
def _extract_monthly_data(_year_month, _json_data):
    class_keys = ["class_MENTION", "class_BAD", "class_GOOD", "class_MUSIC", "class_ENT", 
                  "class_CONTRACT", "class_AD", "class_RIP", "class_NO"]
    class_data = {class_name: [0] * 31 for class_name in class_keys}
    # JSON 데이터에서 해당 월에 해당하는 날짜 필터링 및 데이터 추출
    for month_data in _json_data:
        for date, day_data in month_data.items():
            if date.startswith(_year_month):  # "년-월"에 해당하는 날짜만 추출
                day = int(date.split("-")[2]) - 1  # 일별 인덱스 (0부터 시작)
                for class_type, count in day_data["class_counts"].items():
                    if class_type in class_keys:  # 클래스 키에 해당하는 데이터만 업데이트
                        class_data[class_type][day] = count  # 해당 일에 카운트 데이터 추가

    # data_list 생성 (클래스명과 날짜 레이블 없이 일별 카운트만 포함)
    data_list = [class_data[class_type] for class_type in class_keys]  # 클래스명 없이 일별 카운트 배열만 추가
    return data_list

# ------------------------------------------------------------------------------------------------------------------------
def month_dashboard(_singer, susu, _year, _month):
    head = f'{_year} {_month}'
    st.subheader(f'{head} - ({susu})')
    names = SX_CLASS_NAME
    fdname = f'./jsondata/day_{_singer}.json'
    with open(fdname, "r", encoding="utf-8") as file:
        day_data = json.load(file)
    ynname = head.replace("년 ", "-").replace("월", "").strip()
    data_list = _extract_monthly_data(ynname, day_data)
    series = month_series(names, data_list)
    options = month_option(series)
    eventsx = {
        "click": "function(params) { return [params.type, params.name, params.value, params.componentType, params.seriesType, params.seriesIndex, params.seriesName, params.dataIndex, params.dataType, params.data, params.color, params.info ]}",
    }

    if st.button("off", key="key_month_button1"):
        options['legend'] = options.get('legend', {})
        options['legend']['selected'] = {name: False for name in names}

    s = st_echarts(options=options, events=eventsx, height="500px", key="key_month_dashboard")
    st.divider()
    if s is not None:
        head = f'{head} {s[1]}'
        st.subheader(head)
        main_dashboard(_singer, day_data, head)

# ------------------------------------------------------------------------------------------------------------------------
def _get_total(json_data, target_date):
    for month_data in json_data:
        if target_date in month_data:
            total = month_data[target_date].get("total_articles", 0) 
            return total
    return 0
# ------------------------------------------------------------------------------------------------------------------------
def _get_news_agencies(json_data, target_date):
    for month_data in json_data:
        if target_date in month_data:
            news_agencies = month_data[target_date].get("news_agencies", {})
            sorted_news_agencies = dict(sorted(news_agencies.items(), key=lambda x: x[1], reverse=True))
            return sorted_news_agencies
    return {}

# ------------------------------------------------------------------------------------------------------------------------
def _get_bullets(json_data, target_date, class_type):
    for month_data in json_data:
        if target_date in month_data:
            summaries = month_data[target_date].get("summary_per_class", {})
            if class_type in summaries:
                return summaries[class_type][0].get("bullet", [])
    return []

# ------------------------------------------------------------------------------------------------------------------------
def _get_urls(json_data, target_date, class_type):
    for month_data in json_data:
        if target_date in month_data:
            urls = month_data[target_date].get("url_per_class", {})
            if class_type in urls:
                return urls[class_type]
    return []

# ------------------------------------------------------------------------------------------------------------------------
def _get_hashtags(json_data, target_date, class_type):
    if class_type == 'class_MENTION':
        return []
    for month_data in json_data:
        if target_date in month_data:
            entities = month_data[target_date].get("entities_per_class", {})
            if class_type in entities:
                sorted_entities = dict(sorted(entities[class_type].items(), key=lambda x: x[1], reverse=True))
                return sorted_entities
    return []

# ------------------------------------------------------------------------------------------------------------------------
def _is_skip_date(_json_data, _target):
    for month_data in _json_data:
        if _target in month_data:
            return True
    return False

# ------------------------------------------------------------------------------------------------------------------------
def _is_skip_class(_json_data, _target, _class):
    for month_data in _json_data:
        if _target in month_data:
            urls = month_data[_target].get("class_counts", {})
            # return _class in urls
            if _class in urls:
                return True, urls[_class]  # True와 클래스 값 반환
    return False, None

# ------------------------------------------------------------------------------------------------------------------------
def main_dashboard(_singer, day_data, _head):
    dname = _head.replace("년 ", "-").replace("월 ", "-").replace("일", "").strip()
    if not _is_skip_date(day_data, dname):
        return

    except_mention = [name for name in SX_CLASS_NAME if name != "MENTION"]

    class_counts = []

    for _cidx in except_mention:
        is_skip, class_count = _is_skip_class(day_data, dname, f'class_{_cidx}')
        if is_skip:  # 클래스가 스킵되지 않으면 수집
            class_counts.append((_cidx, class_count))

    sorted_classes = sorted(class_counts, key=lambda x: x[1], reverse=True)


    for _cidx, class_count in sorted_classes:
        day_dashboard(_singer, day_data, dname, _cidx)


    day_dashboard(_singer, day_data, dname, "MENTION")



    st.warning('NEWS AGENCIES')
    agency_list = _get_news_agencies(day_data, dname)
    with st.expander("언론사 리스트:"):
        for key, value in agency_list.items():
            st.write(f'{key} ({value})')






# # ------------------------------------------------------------------------------------------------------------------------
# def main_dashboard(_singer, day_data, _head):
#     dname = _head.replace("년 ", "-").replace("월 ", "-").replace("일", "").strip()
#     if not _is_skip_date(day_data, dname):
#         return

#     except_mention = [name for name in SX_CLASS_NAME if name != "MENTION"]

#     class_counts = []

#     for _cidx in except_mention:
#         day_dashboard(_singer, day_data, dname, _cidx)



#     day_dashboard(_singer, day_data, dname, "MENTION")



#     st.warning('NEWS AGENCIES')
#     agency_list = _get_news_agencies(day_data, dname)
#     with st.expander("언론사 리스트:"):
#         for key, value in agency_list.items():
#             st.write(f'{key} ({value})')








# ------------------------------------------------------------------------------------------------------------------------
def day_dashboard(_singer, day_data, _dname, _class):
    is_skip, class_count = _is_skip_class(day_data, _dname, f'class_{_class}')
    if not is_skip:
        return
    


    total = _get_total(day_data, _dname)
    st.info(f'**{_class} ( {class_count} / {total} )**')

    #####################################################################
    hashtags = _get_hashtags(day_data, _dname, f'class_{_class}')
    if hashtags:
        def generate_annotated_text(_data):
            annotations = []
            for key, value in _data.items():
                annotations.append(annotation(key, f"({value})", font_family="Comic Sans MS", border="2px red"))
                annotations.append("  ")
            if annotations:
                annotations.pop()
            annotated_text(*annotations)
        generate_annotated_text(hashtags)

    #####################################################################
    summary_list = _get_bullets(day_data, _dname, f'class_{_class}')
    with st.expander("SUMMARY:"):
        for _idx in summary_list:
            st.code(_idx)

    #####################################################################
    url_list = _get_urls(day_data, _dname, f'class_{_class}')
    with st.expander("URLS:"):
        for _idx in url_list:
            st.write(_idx)

    st.divider()

# eof


# # ------------------------------------------------------------------------------------------------------------------------
# def main_dashboard(_singer, day_data, _head):
#     dname = _head.replace("년 ", "-").replace("월 ", "-").replace("일", "").strip()
#     if not _is_skip_date(day_data, dname):
#         return

#     except_mention = ["MENTION", "BAD", "GOOD", "MUSIC", "ENT", "CONTRACT", "AD", "RIP", "NO"]
#     for _cidx in except_mention:
#         day_dashboard(_singer, day_data, dname, _cidx)



#     day_dashboard(_singer, day_data, dname, "MENTION")



#     st.warning('NEWS AGENCIES')
#     agency_list = _get_news_agencies(day_data, dname)
#     with st.expander("언론사 리스트:"):
#         for key, value in agency_list.items():
#             st.write(f'{key} ({value})')

# # ------------------------------------------------------------------------------------------------------------------------
# def day_dashboard(_singer, day_data, _dname, _class):
#     is_skip, class_count = _is_skip_class(day_data, _dname, f'class_{_class}')
#     if not is_skip:
#         return
    

    
#     total = _get_total(day_data, _dname)
#     st.info(f'**{_class} ( {class_count} / {total} )**')


# 위 코드는 except_mention 에 기록된 순서대로 day_dashboard 를 호출하고 있어.
# 나는 우선 day_dashboard 를 호출하면 class_count 을 얻을수 있거든. 그래서 class_count 를 모두 얻은뒤
# class_count 의 수가 큰 순서대로 day_dashboard 를 호출하고 싶어. 코드를 수정해줘
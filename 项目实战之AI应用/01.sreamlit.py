import streamlit as st

st.title("新型电力系统预警平台")
st.header("合肥工业大学")
st.subheader("电气学院")

#页面设置
st.set_page_config(
    page_title="新型电力系统预警平台",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# 这是由本团队制作的新型电力系统预警平台，旨在为如今的新型电力系统安全运行提供帮助"
    }
)
#文字
st.write('你好，这是我们团队做的新型电力系统预警平台')

#图片
st.image('./resources/全年供需量图.jpg')

#音频
#st.audio('')

#视频
st.video('resources/视频1.mp4')


#logo
st.logo('resources/图片1.png')


#表格
#st.table('')

#输入框











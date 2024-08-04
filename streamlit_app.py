"""
构建你的第一个应用

"""
import streamlit as st

st.title('我的第一个streamlit应用')
st.write('欢迎来到streamlit的世界')

#在终端中运行以下命令

#streamlit run app.py



'''
交互性

创建输入
'''

#使用文本输入和滑块来获取用户输入

name=st.text_input('请输入你的名字')
age=st.slider('请选择你的年龄',0,100,25)

#显示输入结果
st.write(f'你好，{name}！你的年龄是{age}岁。')


#展示数据
#streamlit可以轻松地展示数据

import pandas as pd

#创建数据表

data={'姓名':['amy','focous','fivewang'],
      'age':[28,34,22]
}
df=pd.DataFrame(data)
st.write(df)



"""
高级组件和api介绍
"""

#在侧边栏添加一个文本输入框
sidebar_slider=st.sidebar.text_input('在这里输入内容')

#在侧边栏添加一个滑动条
sidebar_slider=st.sidebar.slider('请选择一个数值',0,100)




'''
缓存（caching）
streamlit提供了一个缓存机制，通过st.cache装饰器可以使数据加载或复杂计算的结果被缓存，这对处理大量数据或进行复杂计算的应用特别有用。
'''

@st.cache_data
def load_data():
      data=pd.read_csv('large_data.csv') #虚拟数据集
      return data




'''
文件传输器
file uploader
'''
uploaded_file=st.file_uploader('选择一个文件')
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)


'''
绘图库集成
支持多种绘图库

'''

# matplotlib示例

import matplotlib.pyplot as plt

fig,ax=plt.subplots()
ax.scatter([1,2,3],[1,2,3])
st.pyplot(fig)

# Plotly
import plotly.express as px

df=pd.DataFrame({
    'x':[1,2,3,4],
    'y':[10,20,30,40]}
)
fig=px.line(df,x='x',y='y')
st.plotly_chart(fig)

'''
进度条和状态信息
在处理长时间运行的任务时，显示进度条和状态信息对于提升用户体验重要


'''
import time
#添加一个进度条
progress_bar=st.progress(0)
for i in range(100):
    #更新进度条
    progress_bar.progress(i+1)
    time.sleep(0.1)

#显示成功消息
st.success('任务完成！！')

'''
布局控制
除了列布局和展开器，streamlit还提供了其他布局控制工具，如container和tabs，增强了布局的灵活性

'''

#使用tab
tab1,tab2=st.tabs(['第一标签','第二标签'])
with tab1:
    st.header('这是第一个标签内容')
with tab2:
    st.header('这是第二个标签')



'''
自定义样式
通过HTML和CSS，你可以自定义Streamlit应用的样式。使用st.markdown函数可以嵌入HTML和CSS代码。
'''

st.markdown(
     '''
     <style>
     .big-font{
         font-size:50px !important;
     }
     </style>
     ''',
     unsafe_allow_html=True
 )
st.markdown('<p class="big-font">这是大号字体</p>', unsafe_allow_html=True)

'''
测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容
测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容测试内容

'''

'''
在streamlit中实现多页面应用
'''

#创建主应用框架

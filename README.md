# Baidu_HumanFeature_and_gesture_recognition
此仓库用来盛放用调用百度AI接口做人体特征识别与手势识别的项目（opl校赛）

******原理/步骤详见下述：   
***参考文档：
   百度ai官方文档：
   https://cloud.baidu.com/doc/BODY/s/Rk3cpyo93 
   https://cloud.baidu.com/doc/BODY/s/6k3cpymz1
   https://cloud.baidu.com/doc/BODY/s/Yk3cpymjy
   CSDN：
   https://blog.csdn.net/c80486/article/details/130460278?spm=1001.2014.3001.5506 仅仅参考了一下怎么注册调用百度api，其
   封装并未使用


***1.conda环境配置：
配置了一个叫baidu_recognition的虚拟环境，Python版本为3.8
pip install baidu-aip     安装Python SDK（官方文件要求）  

conda install chardet   还得安一个这个，不然会报错，而且pip还不行，得conda
降低requests和urllib3版本,不然也会报错
pip uninstall requests urllib3
conda install requests==2.27  urllib3==1.25.8

安装完记得把解释器改成刚刚建立的conda环境

***接下来的内容可以转移到HumanFeatures_recognition.py或者Gesture_recognition.py中查看,均有详细注释


***2.建立官方推荐的客户端
“AipBodyAnalysis是人体分析的Python SDK客户端，为使用人体分析的开发人员提供了一系列的交互方法。参考如下代码新建一个AipBodyAnalysis:”

from aip import AipBodyAnalysis
""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

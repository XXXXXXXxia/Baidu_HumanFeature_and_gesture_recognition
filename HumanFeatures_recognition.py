########建立官方推荐的客户端

from aip import AipBodyAnalysis
""" 你的 APPID AK SK """
APP_ID = '57724331'         #这三个参数均可在百度智能云的应用列表中找到，作用貌似是验证用户之类的东西
API_KEY = 'OftKARn92r1gLDz5LlOB22jY'
SECRET_KEY = 'IIb2xpll0XduqCzlHzf51mKZPbInXQ46'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)  #定义类，名为client，接下来的工作均靠他

########配置完后，接下来开始进行操作
####读取照片（定义读取照片的函数）
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

##读照片
image = get_file_content('D:/Baidu_HumanFeature_and_gesture_recognition/image/chiken.jpg')   #照片带上路径，都放在单引号里

""" 如果有可选参数 """
options = {

}

# 带参数调用人体检测与属性识别，并将结果返回给字典options
options = client.bodyAttr(image, options)
print(options.values())

'''
    '"gender": None,
    "age": None,
    "upper_wear": None,
    "lower_wear": None,
    "upper_color": None,
    "lower_color": None,
    "orientation": None,
    "carrying_item": None,
    "is_human": None
    '''

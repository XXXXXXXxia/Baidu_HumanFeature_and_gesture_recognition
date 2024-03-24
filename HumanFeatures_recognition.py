from aip import AipBodyAnalysis
import time
import cv2
from threading import Thread

########建立官方推荐的客户端
""" 你的 APPID AK SK """
APP_ID = '57724331'         #这三个参数均可在百度智能云的应用列表中找到，作用貌似是验证用户之类的东西
API_KEY = 'OftKARn92r1gLDz5LlOB22jY'
SECRET_KEY = 'IIb2xpll0XduqCzlHzf51mKZPbInXQ46'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)  #定义类，名为client，接下来的工作均靠他

########配置完后，接下来开始进行操作,分为静止照片识别与摄像头实时识别，根据需要注释掉不需要的功能即可

####读取照片（定义读取照片的函数）
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

##读照片
image = get_file_content('D:/Baidu_HumanFeature_and_gesture_recognition/image/chiken.jpg')   #照片带上路径，都放在单引号里

""" 如果有可选参数 """
options = {

}

'''
    'gender': None,
    'age': None,
    'upper_wear': None,
    'lower_wear': None,
    'upper_color': None,
    'lower_color': None,
    'is_human': None
    '''

# 带参数调用人体检测与属性识别，并将结果返回给字典options
options = client.bodyAttr(image, options)
print(options)



######opencv调用摄像头进行手势识别      原理与手势识别极其类似，代码备注/解释详见Gesture_recognition.py


Features_client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
capture = cv2.VideoCapture(0)  #通过cv2.VideoCapture()方法初始化摄像头，0表示使用默认摄像头。
exit_flag = False              #用于控制程序退出的标志位，初始值为False。

def camera():
    global exit_flag
    while True:
        ret, frame = capture.read()  # 调用OpenCV拍照
        cv2.imshow('frame', frame)  # OpenCV显示图片
        if cv2.waitKey(1) == ord('q'):
            exit_flag = True
            break
'''
      定义摄像头线程函数camera()：
这个函数在一个独立的线程中运行，负责不断读取摄像头的图像并显示在屏幕上。
循环内部不断调用capture.read()读取摄像头捕获的图像，然后使用cv2.imshow()方法显示在名为'frame'的窗口中。
如果按下键盘上的'q'键，则将退出标志位exit_flag设置为True，并退出循环，结束线程。
'''

Thread(target=camera).start()   #使用Thread模块创建一个新的线程，并以camera函数作为目标函数启动线程。
'''   创建线程
创建一个新的线程对象：Thread(target=camera)。这个线程对象的目标函数是 camera 函数，即在新线程中执行 camera 函数的代码。
调用 start() 方法：start() 方法启动线程，使其开始执行目标函数。一旦调用了 start() 方法，线程就会在新的执行流中独立运行，与主线程并发执行。

这样做的原理是利用了 Python 中的多线程编程机制。通过创建一个新的线程来执行 camera 函数，程序可以同时执行主线程中的其他任务，例如图像处理和手势识别，而不会因为摄像头图像
的读取和显示而被阻塞。这样就能实现在一个线程中读取摄像头图像并显示，同时在另一个线程中进行手势识别，实现并发处理，提高了程序的效率和响应速度。
'''

while not exit_flag:    #exit_flag标志位为0时才执行，在camerah（）函数中，当按下q键的时候，该标志位会被置一，进而退出循环
    try:
        ret, frame = capture.read()
        image = cv2.imencode('.jpg', frame)[1]

        Features = Features_client.bodyAttr(image)  # 调用百度手势识别

        print(Features)

    except:
        print('什么都没有识别到')
    time.sleep(1)





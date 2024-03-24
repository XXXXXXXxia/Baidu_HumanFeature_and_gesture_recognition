from aip import AipBodyAnalysis  #百度AI的人体分析SDK，用于手势识别。
import time
import cv2
from threading import Thread

########建立官方推荐的客户端
""" 你的 APPID AK SK """
APP_ID = '57724331'         #这三个参数均可在百度智能云的应用列表中找到，作用貌似是验证用户之类的东西
API_KEY = 'OftKARn92r1gLDz5LlOB22jY'
SECRET_KEY = 'IIb2xpll0XduqCzlHzf51mKZPbInXQ46'

gesture_client0 = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)  #定义类，名为client，接下来的工作均靠他

########配置完后，接下来开始进行操作，分为静止照片识别与摄像头实时识别，根据需要注释掉不需要的功能即可

########静止照片识别
####读取照片（定义读取照片的函数）
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

##读照片
image = get_file_content('D:/Baidu_HumanFeature_and_gesture_recognition/image/chiken.jpg')  # 照片带上路径，都放在单引号里

options = {

}
options = gesture_client0.gesture(image);
print(options.values())


######opencv调用摄像头进行手势识别

hand = {'Fist': '石头','Two': '剪刀','Five': '布'}       #定义要识别的类型

'''      手势识别可以填这么多参数，但是这里只用到识别剪刀石头布的话，只用上面三个即可，且数字2表示剪刀，数字五表示布
        'One': '数字1', 'Five': '数字5', 'Fist': '拳头', 'Ok': 'OK',
        'Prayer': '祈祷', 'Congratulation': '作揖', 'Honour': '作别',
        'Heart_single': '比心心', 'Thumb_up': '点赞', 'Thumb_down': 'Diss',
        'ILY': '我爱你', 'Palm_up': '掌心向上', 'Heart_1': '双手比心1',
        'Heart_2': '双手比心2', 'Heart_3': '双手比心3', 'Two': '数字2',
        'Three': '数字3', 'Four': '数字4', 'Six': '数字6', 'Seven': '数字7',
        'Eight': '数字8', 'Nine': '数字9', 'Rock': 'Rock', 'Insult': '竖中指', 'Face': '脸'
'''

gesture_client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
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

        gesture = gesture_client.gesture(image)  # 调用百度手势识别
        words = gesture['result'][0]['classname']

        print(hand[words])

    except:
        print('什么都没有识别到')
    time.sleep(1)

'''  代码注释/讲解
主循环：

在主循环中，不断读取摄像头的图像，并通过百度AI的手势识别功能识别图像中的手势。
调用capture.read()读取摄像头捕获的图像，然后使用cv2.imencode()方法将图像编码为JPEG格式，以便传递给百度AI的手势识别接口。
调用gesture_client.gesture()方法，传入图像数据，进行手势识别。识别结果存储在gesture变量中。
从识别结果中提取手势类别的名称，存储在words变量中。
将手势类别的名称映射为对应的含义，并打印输出。


ret, frame = capture.read() 这句代码是使用 OpenCV 中的 VideoCapture 对象的 read() 方法来读取摄像头捕获的一帧图像，并将返回的结果赋值给 ret 和 frame 两个变量。
具体来说，这句代码完成了以下几个操作：
capture.read()：调用 VideoCapture 对象 capture 的 read() 方法，该方法返回两个值：
ret：一个布尔值，表示是否成功读取到了图像帧。如果成功读取到图像帧，则 ret 为 True，否则为 False。
frame：表示读取到的图像帧的内容。它是一个 numpy 数组，包含了图像的像素数据。
ret, frame = ...：将 read() 方法返回的两个值分别赋给 ret 和 frame 两个变量。这样，ret 变量将存储读取图像的结果（成功或失败），而 frame 变量将存储读取到的图像帧的内容。
通过这句代码，程序就能够获取到摄像头捕获的图像帧，并将其存储在 frame 变量中，以便后续的图像处理和手势识别操作。

frame变量是实时更新的吗？
frame 变量在每次调用 capture.read() 方法时更新为当前摄像头捕获的图像帧内容。因此，如果你在循环中多次调用 capture.read()，那么 frame 变量就
会在每次循环迭代中更新为新的图像帧内容。

在Python中，frame变量是一个存储图像帧内容的变量，它是一个指向图像数据的引用。当你调用capture.read()方法时，它返回的图像数据会被存储在内存中，而frame变量实际上是
指向这些图像数据的引用，而不是图像数据本身。
因此，虽然图像数据是保存在内存中的，但实际上是被frame变量引用的。当你更新frame变量时，它指向的图像数据也会随之更新。如果你不再需要这些图像数据，可以将frame变量
设置为None来释放它所引用的内存空间，或者让它超出作用域，Python的垃圾回收机制会自动释放相关的内存空间。


cv2.imencode('.jpg', frame) 这句代码是使用 OpenCV 的 imencode() 函数将图像帧 frame 编码为 JPEG 格式的图像数据。
具体来说，imencode() 函数的作用是将图像数据编码为指定格式的图像，返回一个包含编码结果的元组。元组的第一个元素是一个布尔值，表示编码是否成功，而第二个元素
是一个包含编码后的图像数据的字节对象。
因此，image = cv2.imencode('.jpg', frame)[1] 这句代码是将 imencode() 函数返回的元组的第二个元素（即编码后的图像数据）赋值给 image 变量，以便后续使用。


words = gesture['result'][0]['classname']
这两句代码的作用是从百度AI手势识别的结果中提取出手势类别的名称，并存储在 words 变量中。
具体来说，gesture['result'][0]['classname'] 这部分代码访问了百度AI手势识别结果中的数据结构，gesture 是调用手势识别接口返回的结果，它是一个字典对象。
在这个字典中，'result' 键对应的值是一个列表，其中包含了识别出的手势信息，而 [0] 表示取列表中的第一个元素，即第一个识别出的手势。在这个手势信息中，'classname' 键对应的
值就是手势的类别名称，即表示识别出的手势类型。

print(hand[words])
这句代码将 words 变量中存储的手势类别名称作为键，从事先定义好的 hand 字典中获取对应的含义，并将其打印输出。

例如，如果 words 的值是 'One'，那么 hand['One'] 就会返回 '数字1'，然后这个含义会被打印输出。这样就实现了将手势类别名称转换为对应的含义输出的功能。


'''




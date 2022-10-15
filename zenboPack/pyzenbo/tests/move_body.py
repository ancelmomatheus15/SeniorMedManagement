import os
import threading
import time

import pyzenbo
import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules import wheel_lights
from pyzenbo.modules.dialog_system import RobotFace

zenbo = pyzenbo.connect('')
record_video_file = None
record_picture_file = None


def on_result_callback(**kwargs):
    ac = kwargs.get('result').get('AC_PLUGGED')
    if ac is not None and not ac:
        def job():
            zenbo.media.stop_media()
            time.sleep(int(1))
            time.sleep(int(5))

        t = threading.Thread(target=job)
        t.start()
    ac = kwargs.get('result').get('AC_PLUGGED', None)
    if ac is not None and ac:
        def job():
            zenbo.media.stop_media()
            time.sleep(int(1))
            time.sleep(int(5))

        t = threading.Thread(target=job)
        t.start()
    if kwargs.get('cmd') == commands.MEDIA_RECORD_VIDEO or (
            kwargs.get('cmd') == commands.MEDIA_STOP_MEDIA and '.mp4' in kwargs.get('result').get('file')):
        global record_video_file
        record_video_file = kwargs.get('result').get('file')
    if kwargs.get('cmd') == commands.MEDIA_TAKE_PICTURE:
        global record_picture_file
        record_picture_file = kwargs.get('result').get('file')


zenbo.on_result_callback = on_result_callback
zenbo.system.register_ac_plug_status()
time.sleep(int(1))
zenbo.robot.set_expression(RobotFace.DEFAULT)

zenbo.robot.set_expression(RobotFace.SHY)
zenbo.wheelLights.set_color(wheel_lights.Lights.SYNC_BOTH, 0xff, 0x00ff0000)
zenbo.wheelLights.start_strobing(wheel_lights.Lights.SYNC_BOTH, wheel_lights.Speed.SPEED_DEFAULT)
time.sleep(int(2))
zenbo.wheelLights.turn_off(wheel_lights.Lights.ASYNC_LEFT)
zenbo.media.record_video(duration=15, sync=False)
time.sleep(int(20))
time.sleep(int(1))
if record_video_file is not None:
    filePath, fileName = os.path.split(record_video_file)
    zenbo.media.play_media(filePath, fileName, sync=True)
    time.sleep(int(1))
zenbo.media.take_picture()
time.sleep(int(1))
if record_picture_file is not None:
    filePath, fileName = os.path.split(record_picture_file)
    zenbo.media.play_media(filePath, fileName, sync=False)
    time.sleep(int(1))
time.sleep(int(2))
zenbo.media.stop_media()
time.sleep(int(1))
zenbo.media.play_media('', '變數.PNG', sync=False)  # 您需要將檔案放在裝置中指定的路徑 /sdcard/Zenbo實驗室/
time.sleep(int(1))
time.sleep(int(2))
zenbo.media.stop_media()
time.sleep(int(1))
time.sleep(int(20))
zenbo.system.unregister_ac_plug_status()
zenbo.media.stop_media()
zenbo.release()

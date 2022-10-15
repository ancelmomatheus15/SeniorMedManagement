import sys
sys.path.append('/var/www/ElderMedManagement/zenboPack/pyzenbo/')

import pyzenbo
from pyzenbo.modules.dialog_system import RobotFace

#definir conexao
host = '192.168.7.18'
zenbo = pyzenbo.connect(host)

#configurar volume e tom de voz da fala
zenbo_speakSpeed = 100
zenbo_speakPitch = 100
zenbo_speakLanguage = 100

zenbo.robot.set_expression(RobotFace.DEFAULT, "Hello there, how you doing? I am Zenbo and I'm here to help!", {'speed':zenbo_speakSpeed, 'pitch':zenbo_speakPitch, 'languageId':zenbo_speakLanguage} , sync = True)

zenbo.robot.set_expression(RobotFace.HIDEFACE)

zenbo.release()

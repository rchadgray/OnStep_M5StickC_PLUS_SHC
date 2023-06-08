from m5stack import *
from m5ui import *
from uiflow import *
import socket
import time
import wifiCfg
import hat

SSID = 'OnStep_Mount'
PASS = 'password'
TCP_IP = '192.168.0.1'
TCP_PORT = 9999

setScreenColor(0x111111)

hat_mini_joyc_0 = hat.get(hat.MINI_JOYC)

i = None
m = None
mw = None
me = None
ms = None
mn = None

label2 = M5TextBox(22, 19, "OnStep", lcd.FONT_DejaVu24, 0xf70000, rotate=0)
label3 = M5TextBox(20, 57, "Remote", lcd.FONT_DejaVu24, 0xfc0000, rotate=0)
line0 = M5Line(M5Line.PLINE, 0, 100, 140, 100, 0xff0000)
label5 = M5TextBox(29, 141, "     ", lcd.FONT_DejaVu24, 0xff0000, rotate=0)
label4 = M5TextBox(29, 193, "     ", lcd.FONT_DejaVu24, 0xff0000, rotate=0)


def buttonB_wasPressed():
  global i, m, mw, me, ms, mn
  if i == 0:
    i = 1
    label4.setText('FAST')
  else:
    i = 0
    label4.setText('SLOW')
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasPressed():
  global i, m, mw, me, ms, mn
  label5.setText('STOP')
  tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  tcpsocket.connect((TCP_IP, TCP_PORT))
  tcpsocket.send(':Q#')
  wait_ms(200)
  tcpsocket.close()
  wait(2)
  label5.setText('     ')
  pass
btnA.wasPressed(buttonA_wasPressed)


M5Led.on()
wifiCfg.doConnect(SSID, PASS)
M5Led.off()
m = 0
mw = 0
me = 0
ms = 0
mn = 0
i = 0
label4.setText('SLOW')
while True:
  if (hat_mini_joyc_0.get_10bit_calibrate_value(0)) <= -300:
    label5.setText('X-')
    m = 1  
    if (mw == 0) :
      mw = 1
      me = 0
      ms = 0
      mn = 0
      tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      tcpsocket.connect((TCP_IP, TCP_PORT))
      tcpsocket.send('#:Te#')
      wait_ms(200)
      tcpsocket.send(':RS#') if i == 0 else tcpsocket.send(':R9#')
      wait_ms(200)    
      tcpsocket.send(':Mw#')
      wait_ms(200)
      tcpsocket.close()
  else:
    if (hat_mini_joyc_0.get_10bit_calibrate_value(0)) > 300:
      label5.setText('X+')
      m = 1
      if (me == 0) :
        mw = 0
        me = 1
        ms = 0
        mn = 0
        tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsocket.connect((TCP_IP, TCP_PORT))
        tcpsocket.send('#:Te#')
        wait_ms(200)
        tcpsocket.send(':RS#') if i == 0 else tcpsocket.send(':R9#')
        wait_ms(200)       
        tcpsocket.send(':Me#')
        wait_ms(200)       
        tcpsocket.close()
    else:
      if (hat_mini_joyc_0.get_10bit_calibrate_value(1)) <= -300:
        label5.setText('Y-')
        m = 1
        if (ms == 0) :
          mw = 0
          me = 0
          ms = 1
          mn = 0
          tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          tcpsocket.connect((TCP_IP, TCP_PORT))
          tcpsocket.send('#:Te#')
          wait_ms(200)
          tcpsocket.send(':RS#') if i == 0 else tcpsocket.send(':R9#')
          wait_ms(200)       
          tcpsocket.send(':Ms#')
          wait_ms(200)                   
          tcpsocket.close()
      else:
        if (hat_mini_joyc_0.get_10bit_calibrate_value(1)) > 300:
          label5.setText('Y+')
          m = 1
          if (mn == 0) :
            mw = 0
            me = 0
            ms = 0
            mn = 1
            tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpsocket.connect((TCP_IP, TCP_PORT))
            tcpsocket.send('#:Te#')
            wait_ms(200)
            tcpsocket.send(':RS#') if i == 0 else tcpsocket.send(':R9#')
            wait_ms(200)       
            tcpsocket.send(':Mn#')
            wait_ms(200)          
            tcpsocket.close()
        else:
          if (hat_mini_joyc_0.get_button_status()) == 0:
            wait(2)
            if (hat_mini_joyc_0.get_button_status()) == 0:
              m = 0
              mw = 0
              me = 0
              ms = 0
              mn = 0
              label5.setText('Home')
              tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              tcpsocket.connect((TCP_IP, TCP_PORT))    
              tcpsocket.send('#:Te#')
              wait_ms(200)
              tcpsocket.send(':hC#')
              wait_ms(200)
              tcpsocket.close()
          else:
            if m == 1:
              m = 0
              mw = 0
              me = 0
              ms = 0
              mn = 0
              label5.setText('     ')
              tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              tcpsocket.connect((TCP_IP, TCP_PORT))
              tcpsocket.send(':Q#')
              wait_ms(200)
              tcpsocket.close()
  wait_ms(500)
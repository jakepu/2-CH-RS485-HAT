import RPi.GPIO as GPIO
import time
import os
import sys

from . import config
from . import SC16IS752

class RS485(object):
    def __init__(self):
        self.config= config.config()
        
    def RS485_CH1_begin(self, Baud):
        self.SC16IS752_CH1 = SC16IS752.SC16IS752(1)#CH1
        self.SC16IS752_CH1.Set_Baudrate(Baud)
        GPIO.output(self.config.TXDEN_1, GPIO.HIGH)  
        print ('SC16IS752_CH1')
    
    def RS485_CH1_begin(self, Baud, num_stop_config, word_len_config, 
                        break_ctrl=0, set_parity=0, parity_type=0, parity_en=0):
        self.SC16IS752_CH1 = SC16IS752.SC16IS752(1)#CH1
        self.SC16IS752_CH1.set_line_control_register(Baud=Baud, num_stop_config=num_stop_config,
                                                     word_len_config=word_len_config, 
                                                     break_ctrl=break_ctrl, set_parity=set_parity,
                                                     parity_type=parity_type, parity_en=parity_en)
        GPIO.output(self.config.TXDEN_1, GPIO.HIGH)  
        print ('SC16IS752_CH1')
        
    def RS485_CH2_begin(self, Baud):
        self.SC16IS752_CH2 = SC16IS752.SC16IS752(2)#CH2
        self.SC16IS752_CH2.Set_Baudrate(Baud)
        GPIO.output(self.config.TXDEN_2, GPIO.HIGH)  

    def RS485_CH2_begin(self, Baud, num_stop_config, word_len_config, 
                        break_ctrl=0, set_parity=0, parity_type=0, parity_en=0):
        self.SC16IS752_CH2 = SC16IS752.SC16IS752(2)#CH2
        self.SC16IS752_CH2.set_line_control_register(Baud=Baud, num_stop_config=num_stop_config,
                                                     word_len_config=word_len_config, 
                                                     break_ctrl=break_ctrl, set_parity=set_parity,
                                                     parity_type=parity_type, parity_en=parity_en)
        GPIO.output(self.config.TXDEN_2, GPIO.HIGH)  

    def RS485_CH1_ReadByte(self):
        GPIO.output(self.config.TXDEN_1, GPIO.HIGH)   
        return self.SC16IS752_CH1.UART_ReadByte()
        
    def RS485_CH2_ReadByte(self):
        GPIO.output(self.config.TXDEN_2, GPIO.HIGH)   
        return self.SC16IS752_CH2.UART_ReadByte()
        
    def RS485_CH1_Write(self, pData):
        GPIO.output(self.config.TXDEN_1, GPIO.LOW)  
        self.SC16IS752_CH1.UART_Write(pData)
        time.sleep(0.005)#Waiting to send
        GPIO.output(self.config.TXDEN_1, GPIO.HIGH) 
        
    def RS485_CH2_Write(self, pData):
        GPIO.output(self.config.TXDEN_2, GPIO.LOW)  
        self.SC16IS752_CH2.UART_Write(pData)
        time.sleep(0.005)#Waiting to send
        GPIO.output(self.config.TXDEN_2, GPIO.HIGH) 
    
    def RS485_CH1_Read(self, Len):
        GPIO.output(self.config.TXDEN_1, GPIO.HIGH)   
        return self.SC16IS752_CH1.UART_Read(Len)
        
    def RS485_CH2_Read(self, Len):
        GPIO.output(self.config.TXDEN_2, GPIO.HIGH)   
        return self.SC16IS752_CH2.UART_Read(Len)
    

    def RS485_CH1_EnableSleep(self):
        self.SC16IS752_CH1.EnableSleep()
        
    def RS485_CH2_EnableSleep(self):
        self.SC16IS752_CH2.EnableSleep()
    
    def RS485_CH1_DisableSleep(self):
        self.SC16IS752_CH1.DisableSleep()
        
    def RS485_CH1_DisableSleep(self):
        self.SC16IS752_CH2.DisableSleep()
        
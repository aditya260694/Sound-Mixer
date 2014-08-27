#!/usr/bin/python
# -*- coding: utf-8 -*-

# newclass.py

import wx
import mixer
import record
import math

class Example(wx.Frame):

    def __init__(self, parent, title):    
        super(Example, self).__init__(parent, title=title, 
            size=(800, 500))

        self.InitUI()
        self.Centre()
        self.Show()     

    def InitUI(self):
        
        pnl = wx.Panel(self)
	title = wx.StaticBox(pnl, label="Wave Mixer")
        outer_vbox = wx.StaticBoxSizer(title,wx.VERTICAL)
    	
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
	sb1 = wx.StaticBox(pnl, label="Player1")
	vbox1 = wx.StaticBoxSizer(sb1,wx.VERTICAL)
	btn1 = wx.Button(pnl, label='Browse', pos=(20, 30))
	btn1.Bind(wx.EVT_BUTTON, self.Browse1)	
	vbox1.Add(btn1)
	st1 = wx.StaticText(pnl, label='Amplitude')
	vbox1.Add(st1)
	self.sld1 = wx.Slider(pnl, value=1, minValue=0, maxValue=5, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox1.Add(self.sld1)

	st2 = wx.StaticText(pnl, label='Time Shift(/100)secs')
	vbox1.Add(st2)
	self.sld2 = wx.Slider(pnl, value=0, minValue=-100, maxValue=100, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox1.Add(self.sld2)

	st3 = wx.StaticText(pnl, label='Time Scaling')
	vbox1.Add(st3)
	self.sld3 = wx.Slider(pnl, value=0, minValue=-3, maxValue=3, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox1.Add(self.sld3)

	self.cb1 = wx.CheckBox(pnl, label='Time Reversal', pos=(20, 20))
	vbox1.Add(self.cb1)	
	self.cb2 = wx.CheckBox(pnl, label='Select for Modulation', pos=(20, 20))
	vbox1.Add(self.cb2)	
	self.cb3 = wx.CheckBox(pnl, label='Select for Mixing', pos=(20, 20))
	vbox1.Add(self.cb3)	
		
	self.gauge = wx.Gauge(pnl, range=100, size=(250, 25), pos=(100,100))
	vbox1.Add(self.gauge)	
        play_1 = wx.Button(pnl, label='Play', pos=(20, 30))	
	play_1.Bind(wx.EVT_BUTTON, self.Play1)			
	vbox1.Add(play_1)
	hbox.Add(vbox1, flag=wx.LEFT | wx.TOP, border=10)


	sb2 = wx.StaticBox(pnl, label="Player2")
	vbox2 = wx.StaticBoxSizer(sb2,wx.VERTICAL)
	
	btn1_2 = wx.Button(pnl, label='Browse', pos=(20, 30))	
	btn1_2.Bind(wx.EVT_BUTTON, self.Browse2)	
	vbox2.Add(btn1_2)
	st1_2 = wx.StaticText(pnl, label='Amplitude')
	vbox2.Add(st1_2)
	self.sld1_2 = wx.Slider(pnl, value=1, minValue=0, maxValue=5, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox2.Add(self.sld1_2)

	st2_2 = wx.StaticText(pnl, label='Time Shift(/100)secs')
	vbox2.Add(st2_2)
	self.sld2_2 = wx.Slider(pnl, value=0, minValue=-100, maxValue=100, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox2.Add(self.sld2_2)

	st3_2 = wx.StaticText(pnl, label='Time Scaling')
	vbox2.Add(st3_2)
	self.sld3_2 = wx.Slider(pnl, value=0, minValue=-3, maxValue=3, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox2.Add(self.sld3_2)

	self.cb1_2 = wx.CheckBox(pnl, label='Time Reversal', pos=(20, 20))
	vbox2.Add(self.cb1_2)	
	self.cb2_2 = wx.CheckBox(pnl, label='Select for Modulation', pos=(20, 20))
	vbox2.Add(self.cb2_2)	
	self.cb3_2 = wx.CheckBox(pnl, label='Select for Mixing', pos=(20, 20))
	vbox2.Add(self.cb3_2)	
		
	self.gauge2 = wx.Gauge(pnl, range=100, size=(250, 25), pos=(100,100))
	vbox2.Add(self.gauge2)	
        play_2 = wx.Button(pnl, label='Play', pos=(20, 30))
	play_2.Bind(wx.EVT_BUTTON, self.Play2)		
	vbox2.Add(play_2)
	hbox.Add(vbox2, flag=wx.LEFT | wx.TOP, border=10)
	
	
	sb3 = wx.StaticBox(pnl, label="Player3")
	vbox3 = wx.StaticBoxSizer(sb3,wx.VERTICAL)
	
	btn1_3 = wx.Button(pnl, label='Browse', pos=(20, 30))	
	btn1_3.Bind(wx.EVT_BUTTON, self.Browse3)	
	vbox3.Add(btn1_3)
	st1_3 = wx.StaticText(pnl, label='Amplitude')
	vbox3.Add(st1_3)
	self.sld1_3 = wx.Slider(pnl, value=1, minValue=0, maxValue=5, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox3.Add(self.sld1_3)

	st2_3 = wx.StaticText(pnl, label='Time Shift(/100)secs')
	vbox3.Add(st2_3)
	self.sld2_3 = wx.Slider(pnl, value=0, minValue=-100, maxValue=100, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox3.Add(self.sld2_3)

	st3_3 = wx.StaticText(pnl, label='Time Scaling')
	vbox3.Add(st3_3)
	self.sld3_3 = wx.Slider(pnl, value=0, minValue=-3, maxValue=3, pos=(20, 20), 
            size=(250, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS | wx.SL_LABELS)
	vbox3.Add(self.sld3_3)




	self.cb1_3 = wx.CheckBox(pnl, label='Time Reversal', pos=(20, 20))
	vbox3.Add(self.cb1_3)	
	self.cb2_3 = wx.CheckBox(pnl, label='Select for Modulation', pos=(20, 20))
	vbox3.Add(self.cb2_3)	
	self.cb3_3 = wx.CheckBox(pnl, label='Select for Mixing', pos=(20, 20))
	vbox3.Add(self.cb3_3)	
		
	self.gauge3 = wx.Gauge(pnl, range=100, size=(250, 25), pos=(100,100))
	vbox3.Add(self.gauge3)	
	
	play_3 = wx.Button(pnl, label='Play', pos=(20, 30))	
	vbox3.Add(play_3)
	
	play_3.Bind(wx.EVT_BUTTON, self.Play3)		
	
	hbox.Add(vbox3, flag=wx.RIGHT | wx.TOP, border=10)

	outer_vbox.Add(hbox,flag=wx.RIGHT|wx.TOP,border=10)	





	hbox2 = wx.BoxSizer(wx.HORIZONTAL)
       
	sb4 = wx.StaticBox(pnl, label="Modulate and Play")
	vbox4 = wx.StaticBoxSizer(sb4,wx.VERTICAL)
	self.gaugeModulate = wx.Gauge(pnl, range=100, size=(250, 25), pos=(100,100))
	vbox4.Add(self.gaugeModulate)
	btn_mod = wx.Button(pnl, label='Play', pos=(20, 30))	
	btn_mod.Bind(wx.EVT_BUTTON, self.Mod)
	vbox4.Add(btn_mod)
	hbox2.Add(vbox4)
        sb5 = wx.StaticBox(pnl, label="Mix and Play")
	vbox5 = wx.StaticBoxSizer(sb5,wx.VERTICAL)
	self.gaugeMix = wx.Gauge(pnl, range=100, size=(250, 25), pos=(100,100))
	vbox5.Add(self.gaugeMix)
	btn_mix = wx.Button(pnl, label='Play', pos=(20, 30))
	btn_mix.Bind(wx.EVT_BUTTON, self.Mix)	
	vbox5.Add(btn_mix)
	hbox2.Add(vbox5)
	
	vbox6 = wx.BoxSizer(wx.VERTICAL)
	btn_rec = wx.Button(pnl, label='Record a new wav file', pos=(20, 30))
	btn_rec.Bind(wx.EVT_BUTTON, self.new_recording)	
	vbox6.Add(btn_rec)
	
	btn_stop = wx.Button(pnl, label='Stop Recording', pos=(20, 30))
	btn_stop.Bind(wx.EVT_BUTTON, self.stop)	
	vbox6.Add(btn_stop)
	hbox2.Add(vbox6)

	outer_vbox.Add(hbox2,flag=wx.RIGHT|wx.TOP,border=10)	

        pnl.SetSizer(outer_vbox)
 
    def new_recording(self,event):
		record.new_recording(0)


    def stop(self,event):
		record.new_recording(1)
		
    def Browse1(self,event):
	self.openFileDialog1 = wx.FileDialog(self, "Open", "", "", 
                                       "All files (*.wav)|*.wav", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
	
	if self.openFileDialog1.ShowModal() == wx.ID_OK:	
		print self.openFileDialog1.GetFilename()
		print self.openFileDialog1.GetDirectory()
    def Browse2(self,event):
	self.openFileDialog2 = wx.FileDialog(self, "Open", "", "", 
                                       "All files (*.wav)|*.wav", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if self.openFileDialog2.ShowModal() == wx.ID_OK:	
		print self.openFileDialog2.GetFilename()
		print self.openFileDialog2.GetDirectory()

    def Browse3(self,event):
	self.openFileDialog3 = wx.FileDialog(self, "Open", "", "", 
                                       "All files (*.wav)|*.wav", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if self.openFileDialog3.ShowModal() == wx.ID_OK:	
		print self.openFileDialog3.GetFilename()
		print self.openFileDialog3.GetDirectory()

    def Pack1(self):
	x,params=mixer.pcm_channels(self.openFileDialog1.GetDirectory() + '/' + self.openFileDialog1.GetFilename())
	if self.sld1.GetValue() >= 0:	
		x=mixer.scale(x,self.sld1.GetValue())
	else:
		x=mixer.scale(x,2^float(self.sld1.GetValue()))
	x,params=mixer.shift(x,self.sld2.GetValue()/100,params)
	x,params=mixer.tim_scale(x,params,math.pow(2,self.sld3.GetValue()))
	if self.cb1.GetValue() == True:
		x=mixer.reverse(x)
	return x,params	


    def Pack2(self):
	x,params=mixer.pcm_channels(self.openFileDialog2.GetDirectory() + '/' + self.openFileDialog2.GetFilename())
	if self.sld1_2.GetValue() >= 0:	
		x=mixer.scale(x,self.sld1_2.GetValue())
	else:
		x=mixer.scale(x,1/float(self.sld1_2.GetValue())*-1)
		
	x,params=mixer.shift(x,self.sld2_2.GetValue()/100,params)
	print self.sld3_2.GetValue()	
	x,params=mixer.tim_scale(x,params,math.pow(2,self.sld3_2.GetValue()))
	if self.cb1_2.GetValue() == True:
		x=mixer.reverse(x)
	return x,params	

    def Pack3(self):
	x,params=mixer.pcm_channels(self.openFileDialog3.GetDirectory() + '/' + self.openFileDialog3.GetFilename())
	if self.sld1_2.GetValue() >= 0:	
		x=mixer.scale(x,self.sld1_3.GetValue())
	else:
		x=mixer.scale(x,1/float(self.sld1_3.GetValue())*-1)

	x,params=mixer.shift(x,self.sld2_3.GetValue()/100,params)
	print self.sld3_3.GetValue()	
	x,params=mixer.tim_scale(x,params,math.pow(2,self.sld3_3.GetValue()))
	x=mixer.reverse(x)
	return x,params	

    def Play1(self,event):
	x,params=self.Pack1()		
	string_data,params=mixer.pack(x,params)
	mixer.output(string_data,params)
	mixer.play("output.wav")	

    def Play2(self,event):
	x,params=self.Pack2()		
	string_data,params=mixer.pack(x,params)
	mixer.output(string_data,params)
	mixer.play("output.wav")	

    def Play3(self,event):
	x,params=self.Pack3()		
	string_data,params=mixer.pack(x,params)
	mixer.output(string_data,params)
	mixer.play("output.wav")	

    def Mix(self,event):    
	if self.cb3.GetValue() and self.cb3_2.GetValue() and self.cb3_3.GetValue():
		x,params1=self.Pack1()
		y,params2=self.Pack2()
		z,params3=self.Pack3()		
		x,params=mixer.mix(x,y,params1,params2)
		x,params=mixer.mix(x,z,params,params3)
	elif self.cb3.GetValue() and self.cb3_2.GetValue():	
		x,params1=self.Pack1()
		y,params2=self.Pack2()
		x,params=mixer.mix(x,y,params1,params2)
	elif self.cb3_2.GetValue() and self.cb3_3.GetValue():	
		x,params1=self.Pack2()
		y,params2=self.Pack3()
		x,params=mixer.mix(x,y,params1,params2)
	elif self.cb3.GetValue() and self.cb3_3.GetValue():	
		x,params1=self.Pack1()
		y,params2=self.Pack3()
		x,params=mixer.mix(x,y,params1,params2)
	else:
		return
	string_data,params=mixer.pack(x,params)
	mixer.output(string_data,params)
	mixer.play("output.wav")	


    def Mod(self,event):    
	if self.cb2.GetValue() and self.cb2_2.GetValue() and self.cb2_3.GetValue():
		x,params1=self.Pack1()
		y,params2=self.Pack2()
		z,params3=self.Pack3()		
		x,params=mixer.modulate(x,y,params1,params2)
		x,params=mixer.modulate(x,z,params,params3)
	elif self.cb2.GetValue() and self.cb2_2.GetValue():	
		x,params1=self.Pack1()
		y,params2=self.Pack2()
		x,params=mixer.modulate(x,y,params1,params2)
	elif self.cb2_2.GetValue() and self.cb2_3.GetValue():	
		x,params1=self.Pack2()
		y,params2=self.Pack3()
		x,params=mixer.modulate(x,y,params1,params2)
	elif self.cb2.GetValue() and self.cb2_3.GetValue():	
		x,params1=self.Pack1()
		y,params2=self.Pack3()
		x,params=mixer.modulate(x,y,params1,params2)
	string_data,params=mixer.pack(x,params)
	mixer.output(string_data,params)
	mixer.play("output.wav")		
if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title="Create Java Class")
    app.MainLoop()

import pyaudio  
import wave  
import numpy as np
import sys
import struct
import wx



def scale(ints,a):
	op=[]
	for i in range(len(ints)):
		val=ints[i]*a
		if val>32767:
			val=32767
		if val<-32768:
			val=-32768

		op.append(val)

	return tuple(op)
		

def reverse(ints):
	op=[]
	for i in range(len(ints)):
		val=ints[len(ints)-i-1]
		op.append(val)
	return tuple(op)


def shift(ints,a,params):
    op=[]
    new_params=[]
	
    if a >= 0:
    	shift=int(a*params[2]*params[0])
	for i in range(shift):
		op.append(0)

	for i in range(len(ints)):
		val=ints[i]
		if val>32767:
			val=32767
		if val<-32768:
			val=-32768
		op.append(val)

	for i in params:
		new_params.append(i)
    	new_params[3]+=params[2]*a
    
    else :
	for i in range(len(ints)):
		val=ints[i]
		if i >= -1*a*params[2]*params[0]:
			op.append(val)
	for i in params:
		new_params.append(i)
    	new_params[3]+=params[2]*a
    return tuple(op),tuple(new_params)


def tim_scale(temp,params,a):
	op=[]
	for i in range(int(len(temp)*a)):
		op.append(0)
	
	for i in range(len(temp)):
	    if float(i*a) == int(i*a):	
		op[int(i*a)]=temp[i]

	new_params=[]

	for i in params:
		new_params.append(i)
	new_params[3]=len(op)/params[0]
	return tuple(op),tuple(new_params)

def mix(ints1,ints2,param1,param2):
	l1=len(ints1)
	l2=len(ints2)
	op=[]

	for i in range(min(l1,l2)):
		val=ints1[i]+ints2[i]
		if val > 32767:
			val=32767
		if val < -32768:
			val= -32768
		op.append(val)

	if l1 >l2:
	  for i in range(l1-l2):
		op.append(ints1[i+l2])
	  return tuple(op),param1
	else:
	  for i in range(l2-l1):
		op.append(ints2[i+l1])
	  return tuple(op),param2

def modulate(ints1,ints2,param1,param2):
	l1=len(ints1)
	l2=len(ints2)
	op=[]

	for i in range(min(l1,l2)):
		val=ints1[i]*ints2[i]
		if val > 32767:
			val=32767
		if val < -32768:
			val= -32768
		op.append(val)

	if l1 >l2:
	  for i in range(l1-l2):
		op.append(0)
	  return tuple(op),param1
	else:
	  for i in range(l2-l1):
		op.append(0)
	  return tuple(op),param2

def pcm_channels(wave_file):
	    stream = wave.open(wave_file,"rb")
	    num_channels = stream.getnchannels()
	    sample_rate = stream.getframerate()
	    sample_width = stream.getsampwidth()
	    num_frames = stream.getnframes()
	    params=stream.getparams()

	    raw_data = stream.readframes( num_frames ) # Returns byte data

	    total_samples = num_frames * num_channels

	    if sample_width == 1: 
	        fmt = "%iB" % total_samples # read unsigned chars
	    elif sample_width == 2:
	        fmt = "%ih" % total_samples # read signed 2 byte shorts
	    else:
	        raise ValueError("Only supports 8 and 16 bit audio formats.")

	    integer_data = struct.unpack(fmt, raw_data)
	    temp=integer_data
	    del raw_data # Keep memory tidy (who knows how big it might be)

	    channels = [ [] for time in range(num_channels) ]

            for index, value in enumerate(integer_data):
	        bucket = index % num_channels
	        channels[bucket].append(value)

#            params=tim_scale(params,2)
	    return integer_data,params


def pack(temp,params):
	    total_samples = params[3] * params[0]
	    if params[1] == 1: 
	        fmt = "%iB" % total_samples # read unsigned chars
	    elif params[1] == 2:
	        fmt = "%ih" % total_samples # read signed 2 byte shorts
	    else:
	        raise ValueError("Only supports 8 and 16 bit audio formats.")
	    string_data = struct.pack(fmt, *temp)
            
	    return string_data,params







def output(string_data,params):
	op=wave.open('output.wav','wb')
	op.setparams(params)
	op.writeframes(string_data)
	op.close

def play(wave_file):
	chunk=1024
	f = wave.open(wave_file,"rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
		        channels = f.getnchannels(),  
		        rate = f.getframerate(),  
		        output = True)  
	#read data  
	data = f.readframes(chunk)  

	#paly stream  
	while data != '':  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  





def process(n):
   ip=1
   while ip != 10:
	print "enter a number"
	ip=input()

	if ip==1:
	    f1=raw_input()	
	    x,params=pcm_channels(f1)
	    a=input()	
	    x=scale(x,a)
	
	if ip==2:
	    	f1=raw_input()	
	    	x,params=pcm_channels(f1)
	    	a=input()
	    	x,params=shift(x,a,params)

	if ip==3:
	   	f1=raw_input()	
           	x,params=pcm_channels(f1)
	   	x=reverse(x)

	if ip==4:
	   	f1=raw_input()	
	   	x,params=pcm_channels(f1)
	   	a=input()
	   	x,params=tim_scale(x,params,a)

	if ip==5:
	    	f1=raw_input()	
	    	f2=raw_input()	
	    	z,params1=pcm_channels(f1)
	    	y,params2=pcm_channels(f2)
     	    	x,params=mix(z,y,params1,params2)
	if ip==6:
	    	f1=raw_input()	
	    	f2=raw_input()	
		z,params1=pcm_channels(f1)
		y,params2=pcm_channels(f2)
		x,params=modulate(z,y,params1,params2)
		
	if ip==10:
		break
	string_data,params=pack(x,params)
	output(string_data,params)
	play("output.wav")	












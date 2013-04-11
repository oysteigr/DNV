import wx
import time
import os
import wxmpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
import datetime
from random import randrange



MAINCOLOR = '#72CBD2'
BACKCOLOR = '#0E1A26'
SCNDCOLOR = '#1B454B'
CONTCOLOR = '#FBB034'

def updateGraph(vector, value):
	vector.append(value)
	del vector[0]

	return vector

def initGraph():
	vector = []

	for i in xrange(60):
		vector.append(0)

	return vector


class MyButton(wx.Button):
	def __init__(self, *a, **k):
		wx.Button.__init__(self, *a, **k)
		self.SetBackgroundColour(SCNDCOLOR)
		self.SetForegroundColour(MAINCOLOR)
		font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		self.SetFont(font)
				
class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "MainFrame",size=(1024,768))
				
		self.panel_top = TopPanel(self, wx.ID_ANY, size=(1024,168), pos=(0,0))
		self.panel_main = MainPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_drive = DrivePanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_race = RacePanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_energy = EnergyPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_phone = PhonePanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_gps = GpsPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_music = MusicPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.SetCursor( wx.StockCursor(wx.CURSOR_BLANK) )
		cursor = wx.StockCursor(wx.CURSOR_BLANK)
		self.SetCursor(cursor)	
			

		
		button1 = MyButton(self.panel_main, id=wx.ID_ANY, label="DRIVING",pos=(0,0),size=(512,200))
		button2 = MyButton(self.panel_main, id=wx.ID_ANY, label="RACING",pos=(512,0),size=(512,200))
		button3 = MyButton(self.panel_main, id=wx.ID_ANY, label="ENERGY",pos=(0,200),size=(512,200))
		button4 = MyButton(self.panel_main, id=wx.ID_ANY, label="NAVIGATE",pos=(512,200),size=(512,200))
		button5 = MyButton(self.panel_main, id=wx.ID_ANY, label="PHONE",pos=(0,400),size=(512,200))
		button6 = MyButton(self.panel_main, id=wx.ID_ANY, label="MEDIA",pos=(512,400),size=(512,200))
		
		button1_home = MyButton(self.panel_drive, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		button2_home = MyButton(self.panel_race, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		button3_home = MyButton(self.panel_energy, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		button4_home = MyButton(self.panel_gps, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		button5_home = MyButton(self.panel_phone, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		button6_home = MyButton(self.panel_music, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))

		
		button1.Bind(wx.EVT_BUTTON, self.onButton1)
		button2.Bind(wx.EVT_BUTTON, self.onButton2)
		button3.Bind(wx.EVT_BUTTON, self.onButton3)
		button4.Bind(wx.EVT_BUTTON, self.onButton4)
		button5.Bind(wx.EVT_BUTTON, self.onButton5)
		button6.Bind(wx.EVT_BUTTON, self.onButton6)
		
		button1_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		button2_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		button3_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		button4_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		button5_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		button6_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
	
		self.Refresh()

#----------------------------------------------------------------------
	def onButton1(self, event):
		self.panel_main.Hide()
		self.panel_drive.Show()


	def onButton2(self, event):
		self.panel_main.Hide()
		self.panel_race.Show()

	def onButton3(self, event):
		self.panel_main.Hide()
		self.panel_energy.Show()

	def onButton4(self, event):
		self.panel_main.Hide()
		self.panel_phone.Show()

	def onButton5(self, event):
		self.panel_main.Hide()
		self.panel_gps.Show()

	def onButton6(self, event):
		self.panel_main.Hide()
		self.panel_music.Show()

	def onButtonHome(self, event):
		
		self.panel_drive.Hide()
		self.panel_race.Hide()
		self.panel_energy.Hide()
		self.panel_phone.Hide()
		self.panel_gps.Hide()
		self.panel_music.Hide()
		self.panel_main.Show()
	
		
class TopPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(TopPanel, self).__init__(*args, **kw) 
		self.SetForegroundColour(BACKCOLOR)
		self.SetBackgroundColour(MAINCOLOR)
		
		self.timer = wx.Timer(self)
		self.timer.Start(1000)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)
		
		self.text1 = wx.StaticText(self, -1, time.strftime('%H:%M:%S'), pos=(380,50))
		self.text1.SetFont(wx.Font(40,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
	def update(self, event):

		self.text1.SetLabel(time.strftime('%H:%M:%S'))
		
	
	
class MainPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(MainPanel, self).__init__(*args, **kw) 
		
		self.SetBackgroundColour(BACKCOLOR)


class DrivePanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(DrivePanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "SPEED", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()



		
class RacePanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(RacePanel, self).__init__(*args, **kw)
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()

		self.panel_race_start = RacePanelStart(self, wx.ID_ANY, size=(1024,600), pos=(0,0))

		button_start = MyButton(self, id=wx.ID_ANY, label="START",pos=(256,100),size=(512,200))
		button_stop = MyButton(self.panel_race_start, id=wx.ID_ANY, label="STOP",pos=(256,500),size=(512,100))

		button_start.Bind(wx.EVT_BUTTON, self.start)
		button_stop.Bind(wx.EVT_BUTTON, self.stop)

	def start(self, event):
		self.panel_race_start.Show()
		self.panel_race_start.on_start()

	def stop(self, event):
		self.panel_race_start.Hide()


class RacePanelStart(wx.Panel):
	def __init__(self, *args, **kw):
		super(RacePanelStart, self).__init__(*args, **kw)
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()

		self.timer = wx.Timer(self)
		self.timer.Start(100)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)
		self.time_start = datetime.datetime.now()
		
		self.init()

		#self.vbox.Hide()
		
		#box_race.Add(self.text1, 1, wx.ALL, 20)
	def on_start(self):
		self.time_start = datetime.datetime.now()


	def update(self, event):

		self.time_elaps = datetime.datetime.now() - self.time_start

		self.lap_count_v.SetLabel(time.strftime('%S'))
		self.stopwatch_v.SetLabel(str(self.time_elaps.seconds/3600) + ':' + str("%02d" % ((self.time_elaps.seconds%3600)/60)) + ':' + str("%02d" % (self.time_elaps.seconds%3600)))
		self.speed_v.SetLabel(time.strftime('%H%M%S'))
		self.effect_v.SetLabel(time.strftime('%M%S'))
		self.energy_v.SetLabel(time.strftime('%M%S'))
		self.laptrip_v.SetLabel(time.strftime('%M%S'))

	def init(self):
		self.vbox = wx.BoxSizer(wx.HORIZONTAL)
		self.hbox_1 = wx.BoxSizer(wx.VERTICAL)
		self.hbox_2 = wx.BoxSizer(wx.VERTICAL)
		self.hbox_3 = wx.BoxSizer(wx.VERTICAL)
		

		self.lap_count_l = wx.StaticText(self, -1, 'Counter: ')
		self.lap_count_v = wx.StaticText(self, -1, time.strftime('%S') )
		self.lap_count_s = wx.StaticText(self, -1, ' laps')
		self.stopwatch_l = wx.StaticText(self, -1, 'Timer: ')
		self.stopwatch_v = wx.StaticText(self, -1, '1:00:00')
		self.stopwatch_s = wx.StaticText(self, -1, ' h:m:s')
		self.speed_l = wx.StaticText(self, -1, 'Speed: ')
		self.speed_v = wx.StaticText(self, -1, time.strftime('%H%M%S'))
		self.speed_s = wx.StaticText(self, -1, ' km/h')
		self.effect_l = wx.StaticText(self, -1, 'Effect: ')
		self.effect_v = wx.StaticText(self, -1, time.strftime('%M%S'))
		self.effect_s = wx.StaticText(self, -1, ' W')
		self.energy_l = wx.StaticText(self, -1, 'Energy: ')
		self.energy_v = wx.StaticText(self, -1, time.strftime('%M%S'))
		self.energy_s = wx.StaticText(self, -1, ' kW/h')
		self.laptrip_l = wx.StaticText(self, -1, 'Lap: ')
		self.laptrip_v = wx.StaticText(self, -1, time.strftime('%M%S'))
		self.laptrip_s = wx.StaticText(self, -1, ' m')


		self.lap_count_l.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.lap_count_v.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.lap_count_s.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.stopwatch_l.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.stopwatch_v.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.stopwatch_s.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.speed_l.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.speed_v.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.speed_s.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.effect_l.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.effect_v.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.effect_s.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.energy_l.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.energy_v.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.energy_s.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.laptrip_l.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.laptrip_v.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.laptrip_s.SetFont(wx.Font(27,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

		self.hbox_1.Add(self.lap_count_l, 0, wx.ALIGN_LEFT)
		self.hbox_2.Add(self.lap_count_v, 0, wx.ALIGN_RIGHT)
		self.hbox_3.Add(self.lap_count_s, 0, wx.ALIGN_LEFT)
		self.hbox_1.Add(self.stopwatch_l, 0, wx.ALIGN_LEFT)
		self.hbox_2.Add(self.stopwatch_v, 0, wx.ALIGN_RIGHT)
		self.hbox_3.Add(self.stopwatch_s, 0, wx.ALIGN_LEFT)
		self.hbox_1.Add(self.speed_l, 0, wx.ALIGN_LEFT)
		self.hbox_2.Add(self.speed_v, 0, wx.ALIGN_RIGHT)
		self.hbox_3.Add(self.speed_s, 0, wx.ALIGN_LEFT)
		self.hbox_1.Add(self.energy_l, 0, wx.ALIGN_LEFT)
		self.hbox_2.Add(self.energy_v, 0, wx.ALIGN_RIGHT)
		self.hbox_3.Add(self.energy_s, 0, wx.ALIGN_LEFT)
		self.hbox_1.Add(self.effect_l, 0, wx.ALIGN_LEFT)
		self.hbox_2.Add(self.effect_v, 0, wx.ALIGN_RIGHT)
		self.hbox_3.Add(self.effect_s, 0, wx.ALIGN_LEFT)
		self.hbox_1.Add(self.laptrip_l, 0, wx.ALIGN_LEFT)
		self.hbox_2.Add(self.laptrip_v, 0, wx.ALIGN_RIGHT)
		self.hbox_3.Add(self.laptrip_s, 0, wx.ALIGN_LEFT)

		self.vbox.Add(self.hbox_1, flag=wx.LEFT | wx.TOP)
		self.vbox.Add(self.hbox_2, flag=wx.LEFT | wx.TOP)
		self.vbox.Add(self.hbox_3, flag=wx.LEFT | wx.TOP)
		
		self.SetSizer(self.vbox)

		
		
class EnergyPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(EnergyPanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "ENERGY", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()
	
		
class PhonePanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(PhonePanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "SOLAR", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		box = wx.BoxSizer(wx.HORIZONTAL)



		self.data = initGraph()

		self.x = np.arange(-60, 0, 1)
		self.y = self.data

		
		### Plot it ###
		self.panel_plot = wxmpl.PlotPanel(self, wx.ID_ANY,size=(6.0, 8.0), dpi=48, cursor=False, location=False, crosshairs=False)
	
		self.fig = self.panel_plot.get_figure()
		

		self.fig.patch.set_facecolor(BACKCOLOR)

	
		self.axes = self.fig.gca()
		# Plot the function
		self.line, = self.axes.plot(self.x, self.data, color=CONTCOLOR)
		
		#self.fig.ylim((0,60))
		self.axes.autoscale(False)
		#self.axes.ylim((0, 60)) 
		self.axes.axis([0, -60, 0, 60])
		self.axes.patch.set_facecolor(BACKCOLOR)
		self.axes.patch.set_edgecolor(MAINCOLOR)
  		self.axes.spines['bottom'].set_color(MAINCOLOR)
  		self.axes.spines['top'].set_color(BACKCOLOR)
  		self.axes.spines['left'].set_color(MAINCOLOR)
  		self.axes.spines['right'].set_color(BACKCOLOR)
		self.axes.tick_params(axis='x', colors=MAINCOLOR)
		self.axes.tick_params(axis='y', colors=MAINCOLOR, size=20)
		

		#font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		#panel.SetFont(font)
		box.Add(self.panel_plot, 1, wx.ALL, 20)
		self.SetSizer(box);

		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()

		self.timer = wx.Timer(self)
		self.timer.Start(1000)
		self.Bind(wx.EVT_TIMER, self.update_graph, self.timer)

	def update_graph(self, event):
		self.data = updateGraph(self.data, randrange(40)+10)

		self.line.set_ydata(self.data)
		#self.axes.clear()
	#	self.axes.plot(self.x, self.data, color=MAINCOLOR)
		self.fig.canvas.draw()
		
		
class GpsPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(GpsPanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "GPS", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()
	
		
class MusicPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(MusicPanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "MUSIC", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()
		
# Run the program
if __name__ == "__main__":
	#os.system('clear')
	#os.system('setterm -cursor off')
	app = wx.App(False)
	frame = MainFrame()
	
#	frame.Show()
	
	frame.ShowFullScreen(True)
	cursor = wx.StockCursor(wx.CURSOR_BLANK)
	frame.SetCursor(cursor)	
	app.MainLoop()
	

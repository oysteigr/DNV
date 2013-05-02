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
			

		
		drive_button = MyButton(self.panel_main, id=wx.ID_ANY, label="DRIVING",pos=(0,0),size=(512,200))
		race_button = MyButton(self.panel_main, id=wx.ID_ANY, label="RACING",pos=(512,0),size=(512,200))
		energy_button = MyButton(self.panel_main, id=wx.ID_ANY, label="ENERGY",pos=(0,200),size=(512,200))
		navigate_button = MyButton(self.panel_main, id=wx.ID_ANY, label="NAVIGATE",pos=(512,200),size=(512,200))
		phone_button = MyButton(self.panel_main, id=wx.ID_ANY, label="PHONE",pos=(0,400),size=(512,200))
		media_button = MyButton(self.panel_main, id=wx.ID_ANY, label="MEDIA",pos=(512,400),size=(512,200))
		
		drive_button_home = MyButton(self.panel_drive, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		race_button_home = MyButton(self.panel_race, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		energy_button_home = MyButton(self.panel_energy, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		navigate_button_home = MyButton(self.panel_gps, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		phone_button_home = MyButton(self.panel_phone, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))
		media_button_home = MyButton(self.panel_music, id=wx.ID_ANY, label="HOME",pos=(256,500),size=(512,100))

		
		drive_button.Bind(wx.EVT_BUTTON, self.ondrive_button)
		race_button.Bind(wx.EVT_BUTTON, self.onrace_button)
		energy_button.Bind(wx.EVT_BUTTON, self.onenergy_button)
		navigate_button.Bind(wx.EVT_BUTTON, self.onnavigate_button)
		phone_button.Bind(wx.EVT_BUTTON, self.onphone_button)
		media_button.Bind(wx.EVT_BUTTON, self.onmedia_button)
		
		drive_button_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		race_button_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		energy_button_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		navigate_button_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		phone_button_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
		media_button_home.Bind(wx.EVT_BUTTON, self.onButtonHome)
	
		self.Refresh()

#----------------------------------------------------------------------
	def ondrive_button(self, event):
		self.panel_main.Hide()
		self.panel_drive.Show()


	def onrace_button(self, event):
		self.panel_main.Hide()
		self.panel_race.Show()

	def onenergy_button(self, event):
		self.panel_main.Hide()
		self.panel_energy.Show()

	def onnavigate_button(self, event):
		self.panel_main.Hide()
		self.panel_gps.Show()

	def onphone_button(self, event):
		self.panel_main.Hide()
		self.panel_phone.Show()

	def onmedia_button(self, event):
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

		png = wx.Image('logo_s.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture = wx.StaticBitmap(self,size=(1024,168),pos=(0,0))
		self.picture.SetBitmap(png)

		png = wx.Image('bluetooth.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture_bluetooth = wx.StaticBitmap(self,size=(1024,168),pos=(950,10))
		self.picture_bluetooth.SetBitmap(png)

		png = wx.Image('powerdump.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture_powerdump = wx.StaticBitmap(self,size=(1024,168),pos=(850,90))
		self.picture_powerdump.SetBitmap(png)

		png = wx.Image('gps.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture_gps = wx.StaticBitmap(self,size=(1024,168),pos=(850,10))
		self.picture_gps.SetBitmap(png)

		png = wx.Image('solcelle.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture_solcelle = wx.StaticBitmap(self,size=(1024,168),pos=(950,90))
		self.picture_solcelle.SetBitmap(png)

		png = wx.Image('lys.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture_lys = wx.StaticBitmap(self,size=(1024,168),pos=(750,10))
		self.picture_lys.SetBitmap(png)

		png = wx.Image('stoppeklokke.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture_stoppeklokke = wx.StaticBitmap(self,size=(1024,168),pos=(750,90))
		self.picture_stoppeklokke.SetBitmap(png)
		
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
		self.SetForegroundColour(MAINCOLOR)


class DrivePanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(DrivePanel, self).__init__(*args, **kw)
		
		self.SetBackgroundColour(BACKCOLOR)
		self.SetForegroundColour(MAINCOLOR)

		text1 = wx.StaticText(self, -1, "SPEED", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		

		self.Hide()



		
class RacePanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(RacePanel, self).__init__(*args, **kw)
		
		self.SetBackgroundColour(BACKCOLOR)
		self.SetForegroundColour(MAINCOLOR)
		self.Hide()

		self.panel_race_start = RacePanelStart(self, wx.ID_ANY, size=(1024,600), pos=(0,0))

		button_start = MyButton(self, id=wx.ID_ANY, label="START/RESET",pos=(256,50),size=(512,150))
		button_resume = MyButton(self, id=wx.ID_ANY, label="RESUME",pos=(256,230),size=(512,150))
		button_back = MyButton(self.panel_race_start, id=wx.ID_ANY, label="BACK",pos=(256,500),size=(512,100))

		button_start.Bind(wx.EVT_BUTTON, self.start)
		button_resume.Bind(wx.EVT_BUTTON, self.resume)
		button_back.Bind(wx.EVT_BUTTON, self.back)

	def start(self, event):
		self.panel_race_start.Show()
		self.panel_race_start.on_start()

	def resume(self, evnet):
		self.panel_race_start.Show()

	def back(self, event):
		self.panel_race_start.Hide()


class RacePanelStart(wx.Panel):
	def __init__(self, *args, **kw):
		super(RacePanelStart, self).__init__(*args, **kw)
		
		self.SetBackgroundColour(BACKCOLOR)
		self.SetForegroundColour(MAINCOLOR)
		self.Hide()

		self.timer = wx.Timer(self)
		self.timer.Start(100)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)
		self.time_start = datetime.datetime.now()
		
		self.init()

		png_track = wx.Image('track.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture_track = wx.StaticBitmap(self,size=(450,300),pos=(550,50))
		self.picture_track.SetBitmap(png_track)
		
		png_icon = wx.Image('logo_mini.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.x_pos = self.get_x_pos()
		self.y_pos = self.get_y_pos()
		self.picture_icon = wx.StaticBitmap(self,size=(450,300),pos=(880,294))
		self.picture_icon.SetBitmap(png_icon)

		png_outofrange = wx.Image('outofrange.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.picture_range = wx.StaticBitmap(self,size=(450,300),pos=(550,50))
		self.picture_range.SetBitmap(png_outofrange)

		#self.vbox.Hide()
		
		#box_race.Add(self.text1, 1, wx.ALL, 20)
	def get_x_cords(self):
		return 4851.0

	def get_y_cords(self):
		return 88200.0

	def get_x_pos(self):
		x_cord_start = 4831.0
		x_cord_end = 4916.0
		x_cord_current = self.get_x_cords()
		x_px_start = 9.0
		x_px_end = 432.0
		x_icon_center = 12.0
		if(x_cord_current<(x_cord_start-30) or x_cord_current>(x_cord_end+30)):
			return -1
		x_pos = 550 + x_px_start - x_icon_center + (x_cord_current - x_cord_start)*((x_px_end-x_px_start)/(x_cord_end-x_cord_start))
		return x_pos

	def get_y_pos(self):
		y_cord_start = 88121.0
		y_cord_end = 88448.0
		y_cord_current = self.get_y_cords()
		y_px_start = 18.0
		y_px_end = 277.0
		y_icon_center = 17.0
		if(y_cord_current<(y_cord_start-30) or y_cord_current>(y_cord_end+30)):
			return -1
		y_pos = 300 -((y_px_start - y_icon_center + (y_cord_current - y_cord_start)*((y_px_end-y_px_start)/(y_cord_end-y_cord_start))))
		return y_pos

	def update_laps(self):
		self.laps_timedif = datetime.datetime.now() - self.time_laps_update
		self.finish_x_pos = 4894.0
		self.finish_y_pos = 88368.0
		if self.laps_timedif.seconds > 1:
			if ( math.fabs(self.get_y_cords() - self.finish_y_pos) < 20.0 and math.fabs(self.get_x_cords() - self.finish_x_pos) < 4.0):	
				self.laps = self.laps + 1
				self.time_laps_update = datetime.datetime.now()



	def update_pos(self):
		if(self.get_y_pos() == -1 or self.get_x_pos() == -1):
			self.picture_icon.Hide()
			self.picture_range.Show()
			return
		self.picture_range.Hide()
		self.picture_icon.Show()
		self.picture_icon.SetPosition((self.get_x_pos(),self.get_y_pos()))

	def on_start(self):
		self.time_start = datetime.datetime.now()
		self.time_laps_update = datetime.datetime.now()
		self.laps = 0


	def update(self, event):

		self.time_elaps = datetime.datetime.now() - self.time_start

		self.lap_count_v.SetLabel(time.strftime(str("%02d" % self.laps)))
		self.stopwatch_v.SetLabel(str(self.time_elaps.seconds/3600) + ':' + str("%02d" % ((self.time_elaps.seconds%3600)/60)) + ':' + str("%02d" % (self.time_elaps.seconds%60)))
		self.speed_v.SetLabel(time.strftime("%02d" % self.speed))
		self.effect_v.SetLabel(time.strftime("%02d" % self.effect))
		self.energy_v.SetLabel(time.strftime("%04d" % self.energy))
		self.laptrip_v.SetLabel(time.strftime("%02d" % self.laptrip))
		self.update_pos()
		self.update_laps()

	def init(self):
		self.vbox = wx.BoxSizer(wx.HORIZONTAL)
		self.hbox_1 = wx.BoxSizer(wx.VERTICAL)
		self.hbox_2 = wx.BoxSizer(wx.VERTICAL)
		self.hbox_3 = wx.BoxSizer(wx.VERTICAL)

		self.laps = 0
		self.time_laps_update = datetime.datetime.now()

		self.effect = 45;
		self.energy = 1343;
		self.laptrip = 1300;
		self.speed = 23;

		self.lap_count_l = wx.StaticText(self, -1, 'Counter: ')
		self.lap_count_v = wx.StaticText(self, -1, str("%02d" % self.laps))
		self.lap_count_s = wx.StaticText(self, -1, ' laps')
		self.stopwatch_l = wx.StaticText(self, -1, 'Timer: ')
		self.stopwatch_v = wx.StaticText(self, -1, '1:00:00')
		self.stopwatch_s = wx.StaticText(self, -1, ' h:m:s')
		self.speed_l = wx.StaticText(self, -1, 'Speed: ')
		self.speed_v = wx.StaticText(self, -1, time.strftime("%02d" % self.speed))
		self.speed_s = wx.StaticText(self, -1, ' km/h')
		self.effect_l = wx.StaticText(self, -1, 'Effect: ')
		self.effect_v = wx.StaticText(self, -1, time.strftime("%02d" % self.effect))
		self.effect_s = wx.StaticText(self, -1, ' W')
		self.energy_l = wx.StaticText(self, -1, 'Energy: ')
		self.energy_v = wx.StaticText(self, -1, time.strftime("%04d" % self.energy))
		self.energy_s = wx.StaticText(self, -1, ' kW/h')
		self.laptrip_l = wx.StaticText(self, -1, 'Lap: ')
		self.laptrip_v = wx.StaticText(self, -1, time.strftime("%02d" % self.laptrip))
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

		self.box_left = wx.BoxSizer(wx.HORIZONTAL)
		self.box_top = wx.BoxSizer(wx.HORIZONTAL)

		self.box_left.Add(self.vbox, flag=wx.LEFT, border=40)
		self.box_top.Add(self.box_left, flag=wx.TOP, border=80)
		
		self.SetSizer(self.box_top)
		#self.vbox.SetPosition(0,0)

		
		
class EnergyPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(EnergyPanel, self).__init__(*args, **kw)
	
		self.SetBackgroundColour(BACKCOLOR)
		self.SetForegroundColour(MAINCOLOR)

		text1 = wx.StaticText(self, -1, "ENERGY", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		

		self.Hide()
	
		
class PhonePanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(PhonePanel, self).__init__(*args, **kw)

		self.SetBackgroundColour(BACKCOLOR)
		self.SetForegroundColour(MAINCOLOR)
		
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
		
		self.SetBackgroundColour(BACKCOLOR)
		self.SetForegroundColour(MAINCOLOR)

		text1 = wx.StaticText(self, -1, "GPS", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		

		self.Hide()
	
		
class MusicPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(MusicPanel, self).__init__(*args, **kw)
		
		self.SetBackgroundColour(BACKCOLOR)
		self.SetForegroundColour(MAINCOLOR)

		text1 = wx.StaticText(self, -1, "MUSIC", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		

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
	

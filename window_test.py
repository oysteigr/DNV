import wx
import time
import os
import wxmpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math



MAINCOLOR = '#ff8c02'
BACKCOLOR = '#000000'

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

fig = plt.figure()
ax = fig.add_subplot(111)

# the histogram of the data
n, bins, patches = ax.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# hist uses np.histogram under the hood to create 'n' and 'bins'.
# np.histogram returns the bin edges, so there will be 50 probability
# density values in n, 51 bin edges in bins and 50 patches.  To get
# everything lined up, we'll compute the bin centers
bincenters = 0.5*(bins[1:]+bins[:-1])
# add a 'best fit' line for the normal PDF
y = mlab.normpdf( bincenters, mu, sigma)
l = ax.plot(bincenters, y, 'r--', linewidth=1)

ax.set_xlabel('Smarts')
ax.set_ylabel('Probability')
#ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
ax.set_xlim(40, 160)
ax.set_ylim(0, 0.03)
ax.grid(True)

class MyButton(wx.Button):
	def __init__(self, *a, **k):
		wx.Button.__init__(self, size=(512,200), *a, **k)
		self.SetBackgroundColour(BACKCOLOR)
		self.SetForegroundColour(MAINCOLOR)
		font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		self.SetFont(font)
				
class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "MainFrame",size=(1024,768))
				
		self.panel_top = TopPanel(self, wx.ID_ANY, size=(1024,168), pos=(0,0))
		self.panel_main = MainPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_speed = SpeedPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_distance = DistancePanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_energy = EnergyPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_solar = SolarPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_gps = GpsPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.panel_music = MusicPanel(self, wx.ID_ANY, size=(1024,600), pos=(0,168))
		self.SetCursor( wx.StockCursor(wx.CURSOR_BLANK) )
		cursor = wx.StockCursor(wx.CURSOR_BLANK)
		self.SetCursor(cursor)	
			

		
		button1 = MyButton(self.panel_main, id=wx.ID_ANY, label="SPEED",pos=(0,0))
		button2 = MyButton(self.panel_main, id=wx.ID_ANY, label="DISTANCE",pos=(512,0))
		button3 = MyButton(self.panel_main, id=wx.ID_ANY, label="ENERGY",pos=(0,200))
		button4 = MyButton(self.panel_main, id=wx.ID_ANY, label="SOLAR PANEL",pos=(512,200))
		button5 = MyButton(self.panel_main, id=wx.ID_ANY, label="GPS",pos=(0,400))
		button6 = MyButton(self.panel_main, id=wx.ID_ANY, label="MUSIC",pos=(512,400))
		
		button1_home = MyButton(self.panel_speed, id=wx.ID_ANY, label="HOME",pos=(256,400))
		button2_home = MyButton(self.panel_distance, id=wx.ID_ANY, label="HOME",pos=(256,400))
		button3_home = MyButton(self.panel_energy, id=wx.ID_ANY, label="HOME",pos=(256,400))
		button4_home = MyButton(self.panel_solar, id=wx.ID_ANY, label="HOME",pos=(256,400))
		button5_home = MyButton(self.panel_gps, id=wx.ID_ANY, label="HOME",pos=(256,400))
		button6_home = MyButton(self.panel_music, id=wx.ID_ANY, label="HOME",pos=(256,400))

		
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
		self.panel_speed.Show()


	def onButton2(self, event):
		self.panel_main.Hide()
		self.panel_distance.Show()

	def onButton3(self, event):
		self.panel_main.Hide()
		self.panel_energy.Show()

	def onButton4(self, event):
		self.panel_main.Hide()
		self.panel_solar.Show()

	def onButton5(self, event):
		self.panel_main.Hide()
		self.panel_gps.Show()

	def onButton6(self, event):
		self.panel_main.Hide()
		self.panel_music.Show()

	def onButtonHome(self, event):
		
		self.panel_speed.Hide()
		self.panel_distance.Hide()
		self.panel_energy.Hide()
		self.panel_solar.Hide()
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
		
		self.SetBackgroundColour(MAINCOLOR)


class SpeedPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(SpeedPanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "SPEED", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()

		
class DistancePanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(DistancePanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "DISTANCE", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()
	
		
class EnergyPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(EnergyPanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "ENERGY", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()
	
		
class SolarPanel(wx.Panel):
	def __init__(self, *args, **kw):
		super(SolarPanel, self).__init__(*args, **kw)
		
		text1 = wx.StaticText(self, -1, "SOLAR", pos=(0,200), style=wx.ALIGN_CENTRE)
		text1.Centre(wx.HORIZONTAL)
		text1.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		
		vbox = wx.BoxSizer(wx.VERTICAL);

		x = np.arange(0.0, 2, 0.01)
		y = np.sinc(math.pi*x)

		
		### Plot it ###
		self.panel_plot = wxmpl.PlotPanel(self, wx.ID_ANY,size=(4.0, 3.7), dpi=96, cursor=False, location=False, crosshairs=False)
		#self.panel_plot.SetBackgroundColour(wx.BLACK)
		#self.panel_plot.figure.set_edgecolor('black')
       	#self.panel_plot.figure.set_facecolor(wx.BLACK)
		# All of WxMpl's plotting classes have a get_figure(),
		# which returns the associated matplotlib Figure.
		fig = self.panel_plot.get_figure()
		
	#	fig.set_edgecolor(MAINCOLOR)
	#	fig.patch.set_facecolor(MAINCOLOR)
	##	fig.set_alpha(0.2)
		fig.patch.set_facecolor(BACKCOLOR)

		# Create an Axes on the Figure to plot in.
		axes = fig.gca()
		# Plot the function
		axes.plot(x, y, color=MAINCOLOR)
		axes.patch.set_facecolor(BACKCOLOR)
		axes.patch.set_edgecolor(MAINCOLOR)
  		axes.spines['bottom'].set_color(MAINCOLOR)
  		axes.spines['top'].set_color(MAINCOLOR)
  		axes.spines['left'].set_color(MAINCOLOR)
  		axes.spines['right'].set_color(MAINCOLOR)
		axes.tick_params(axis='x', colors=MAINCOLOR)
		axes.tick_params(axis='y', colors=MAINCOLOR)
		#font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		#panel.SetFont(font)
		vbox.Add(self.panel_plot, 1, wx.EXPAND | wx.ALL, 20)
		self.SetSizer(vbox);

		self.SetBackgroundColour(BACKCOLOR)
		self.Hide()
	
		
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
	

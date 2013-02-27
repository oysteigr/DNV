import wx
#General comment

class MyButton(wx.Button):
	def __init__(self, *a, **k):
		wx.Button.__init__(self, size=(512,200), *a, **k)
		self.SetBackgroundColour('#000000')
		self.SetForegroundColour('#ff8c02')
		font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		self.SetFont(font)
		
class SpeedFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "SpeedFrame",size=(1024,768))
		panel1 = wx.Panel(self, wx.ID_ANY, size=(1024,168))
		panel2 = wx.Panel(self, wx.ID_ANY, size=(1024,600))
		
		panel1.SetBackgroundColour('#ff8c02')
		panel2.SetBackgroundColour('#000000')
		#font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		#panel.SetFont(font)
		box = wx.BoxSizer(wx.VERTICAL)
		box.Add(panel1, 168, flag=wx.ALIGN_TOP|wx.LEFT)
		box.Add(panel2, 600, flag=wx.ALIGN_BOTTOM|wx.LEFT)
		
		self.SetSizer(box)

		
class MainFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "MainFrame",size=(1024,768))
		panel_top = wx.Panel(self, wx.ID_ANY, size=(1024,168))
		panel_main = wx.Panel(self, wx.ID_ANY, size=(1024,600))
		panel_speed = wx.Panel(self, wx.ID_ANY, size=(1024,600))
		
		panel_speed.Hide()
		
		panel_top.SetBackgroundColour('#ff8c02')
		panel_main.SetBackgroundColour('#000000')
		#font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		#panel.SetFont(font)
		box = wx.BoxSizer(wx.VERTICAL)
		box.Add(panel_top, 168, flag=wx.ALIGN_TOP|wx.LEFT)
		box.Add(panel_main, 600, flag=wx.ALIGN_BOTTOM|wx.LEFT)
		box.Add(panel_speed, 600, flag=wx.ALIGN_BOTTOM|wx.LEFT)
		
		self.SetSizer(box)
		
		button1 = MyButton(panel_main, id=wx.ID_ANY, label="SPEED",pos=(0,0))
		button2 = MyButton(panel_main, id=wx.ID_ANY, label="DISTANCE",pos=(512,0))
		button3 = MyButton(panel_main, id=wx.ID_ANY, label="ENERGY",pos=(0,200))
		button4 = MyButton(panel_main, id=wx.ID_ANY, label="SOLAR PANEL",pos=(512,200))
		button5 = MyButton(panel_main, id=wx.ID_ANY, label="GPS",pos=(0,400))
		button6 = MyButton(panel_main, id=wx.ID_ANY, label="MUSIC",pos=(512,400))
		
		
		button1.Bind(wx.EVT_BUTTON, self.onButton1, panel_main, panel_speed)
		button2.Bind(wx.EVT_BUTTON, self.onButton2)
		button3.Bind(wx.EVT_BUTTON, self.onButton3)
		button4.Bind(wx.EVT_BUTTON, self.onButton4)
		button5.Bind(wx.EVT_BUTTON, self.onButton5)
		button6.Bind(wx.EVT_BUTTON, self.onButton6)
	
		self.Refresh()

#----------------------------------------------------------------------
	def onButton1(self, event, panel1, panel2):
		"""
		This method is fired when its corresponding button is pressed
		"""
		print "Button1 pressed!"
	def onButton2(self, event):
		"""
		This method is fired when its corresponding button is pressed
		"""
		print "Button2 pressed!"
	def onButton3(self, event):
		"""
		This method is fired when its corresponding button is pressed
		"""
		print "Button3 pressed!"
	def onButton4(self, event):
		"""
		This method is fired when its corresponding button is pressed
		"""
		print "Button4 pressed!"
	def onButton5(self, event):
		"""
		This method is fired when its corresponding button is pressed
		"""
		print "Button5 pressed!"
	def onButton6(self, event):
		"""
		This method is fired when its corresponding button is pressed
		"""
		print "Button6 pressed!"    
# Run the program
if __name__ == "__main__":
	app = wx.App(False)
	frame = MainFrame()
	frame.Show()
	frame.ShowFullScreen(True)
	app.MainLoop()

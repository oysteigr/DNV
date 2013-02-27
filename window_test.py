import wx
#General comment

class MyButton(wx.Button):
	def __init__(self, *a, **k):
		wx.Button.__init__(self, size=(512,200), *a, **k)
		self.SetBackgroundColour('#000000')
		self.SetForegroundColour('#ff8c02')
		font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		self.SetFont(font)
		
class MyForm(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "Button Tutorial",size=(1024,768))
		panel = wx.Panel(self, wx.ID_ANY)
		panel.SetBackgroundColour('#ff8c02')
		#font = wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		#panel.SetFont(font)
		
		button1 = MyButton(panel, id=wx.ID_ANY, label="SPEED",pos=(0,168))
		button2 = MyButton(panel, id=wx.ID_ANY, label="DISTANCE",pos=(512,168))
		button3 = MyButton(panel, id=wx.ID_ANY, label="ENERGY",pos=(0,368))
		button4 = MyButton(panel, id=wx.ID_ANY, label="SOLAR PANEL",pos=(512,368))
		button5 = MyButton(panel, id=wx.ID_ANY, label="GPS",pos=(0,568))
		button6 = MyButton(panel, id=wx.ID_ANY, label="MUSIC",pos=(512,568))
		
		
		button1.Bind(wx.EVT_BUTTON, self.onButton1)
		button2.Bind(wx.EVT_BUTTON, self.onButton2)
		button3.Bind(wx.EVT_BUTTON, self.onButton3)
		button4.Bind(wx.EVT_BUTTON, self.onButton4)
		button5.Bind(wx.EVT_BUTTON, self.onButton5)
		button6.Bind(wx.EVT_BUTTON, self.onButton6)

		
		self.Refresh()

    #----------------------------------------------------------------------
	def onButton1(self, event):
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
	frame = MyForm()
	frame.Show()
	app.MainLoop()

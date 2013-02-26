import wx

class MyButton(wx.Button):
	def __init__(self, *a, **k):
		wx.Button.__init__(self, size=(512,135), *a, **k)
		self.SetBackgroundColour('#ff8c02')
 
class MyForm(wx.Frame):
 
	def __init__(self):
	        wx.Frame.__init__(self, None, wx.ID_ANY, "Button Tutorial",size=(1024,600))
	        panel = wx.Panel(self, wx.ID_ANY)
		panel.SetBackgroundColour('Black')
 
	        button1 = MyButton(panel, id=wx.ID_ANY, label="SPEED",pos=(0,60))
	        button2 = MyButton(panel, id=wx.ID_ANY, label="DISTANCE",pos=(512,60))
	        button3 = MyButton(panel, id=wx.ID_ANY, label="ENERGY",pos=(0,195))
	        button4 = MyButton(panel, id=wx.ID_ANY, label="SOLAR PANEL",pos=(512,195))
	        button5 = MyButton(panel, id=wx.ID_ANY, label="GPS",pos=(0,330))
	        button6 = MyButton(panel, id=wx.ID_ANY, label="MUSIC",pos=(512,330))
	        button7 = MyButton(panel, id=wx.ID_ANY, label="STATUS",pos=(0,465))
	        button8 = MyButton(panel, id=wx.ID_ANY, label="ABOUT",pos=(512,465))


	        button1.Bind(wx.EVT_BUTTON, self.onButton1)
	        button2.Bind(wx.EVT_BUTTON, self.onButton2)
	        button3.Bind(wx.EVT_BUTTON, self.onButton3)
	        button4.Bind(wx.EVT_BUTTON, self.onButton4)
	        button5.Bind(wx.EVT_BUTTON, self.onButton5)
	        button6.Bind(wx.EVT_BUTTON, self.onButton6)
	        button7.Bind(wx.EVT_BUTTON, self.onButton7)
	        button8.Bind(wx.EVT_BUTTON, self.onButton8)
		
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
	def onButton7(self, event):
	        """
	        This method is fired when its corresponding button is pressed
	        """
	        print "Button7 pressed!"
	def onButton8(self, event):
	        """
	        This method is fired when its corresponding button is pressed
	        """
	        print "Button8 pressed!"
    
# Run the program
if __name__ == "__main__":
	app = wx.App(False)
	frame = MyForm()
	frame.Show()
	app.MainLoop()

import wx

class Example(wx.Frame):
  
    def __init__(self, parent, id):
	wx.Frame.__init__(self, parent, id, title='main', pos=(0,0), size=(1024,600))
	

app = wx.App()
frame = Example(None, id=1)
frame.ShowFullScreen(True)
wx.CallLater(3000, frame.ShowFullScreen, False)

app.MainLoop()

__author__ = 'aram'

#!/usr/bin/python

import wx

class Login(wx.Frame):

    def __init__(self, parent, title):
        super(Login, self).__init__(parent, title=title,
            size=(390, 350))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        stName = wx.StaticText(panel, label='Name:')
        stName.SetFont(font)
        hbox1.Add(stName, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)

        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        stPass = wx.StaticText(panel, label='Password:')
        stPass.SetFont(font)
        hbox2.Add(stPass, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox2.Add(tc, proportion=1)

        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))


        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1, flag=wx.RIGHT, border=5)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_CENTER|wx.RIGHT, border=10)

        panel.SetSizer(vbox)


if __name__ == '__main__':

    app = wx.App()
    Login(None, title='Login')
    app.MainLoop()
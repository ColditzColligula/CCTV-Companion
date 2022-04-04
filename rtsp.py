#!/usr/bin/env python
import PySimpleGUI as sg
import cv2
import webbrowser
import pyperclip

# Simple example of TabGroup element and the options available to it

sg.theme('Dark Amber')     # Please always add color to your window

#try:
#    splashscreen = ("splashscreen.png")
#    DISPLAY_TIME_MILLISECONDS = 1000
#
#    sg.Window('Window Title', [[sg.Image(splashscreen)]], transparent_color=sg.theme_background_color(), no_titlebar=True, keep_on_top=True).read(timeout=DISPLAY_TIME_MILLISECONDS, close=True)
#except:
#    pass

def opencamerastream():
    global ADDRESS, USERNAME, PASSWORD, CHANNELSELECT
    capture = cv2.VideoCapture("rtsp://"+USERNAME+":"+PASSWORD+"@"+ADDRESS+'/cam/realmonitor?channel=1&subtype='+CHANNELSELECT)
    #capture = cv2.VideoCapture("rtsp://admin:123456789a@192.168.178.222/cam/realmonitor?channel=1&subtype=1")

    while(capture.isOpened()):
        ret, frame = capture.read()
        #   Allowing to resize the window
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('Q'):
            break
        #   Checks if the Window is being closed by pressing the "X" button, if the window becomes invisible it'll break
        if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) <1:
            break
    capture.release()
    cv2.destroyAllWindows()


# The tab 1, 2, 3 layouts - what goes inside the tab



tab1_layout = [[sg.Text('RTSP Stream')],      
        [sg.Text('IP Address & Port'), sg.Input(key='-ADDRESS-')],
        [sg.Text('Username'), sg.Input(key='-USERNAME-')],
        [sg.Text('Password'), sg.Input(password_char = "•", key='-PASSWORD-')],
        [sg.Radio('Main Stream', 'CHANNEL', default=True, key='-CHANNEL0-'), sg.Radio('Sub Stream', 'CHANNEL', key='-CHANNEL1-')],
        [sg.Button('Open'), sg.Button('Copy RTSP Link'), sg.Button('Web Interface'), sg.Button('Exit', key='-EXIT-'), sg.Button('Help')]]
        

#tab2_videosize = [sg.Text('Under Construction')]
#tab2_recordtime = [sg.Text('Under Construction')]
#tab2_diskarray = [sg.Text('Under Construction')]
#tab2grouplayout = [sg.Tab('Video Size', tab2_videosize, key='-VIDEOSIZE-'), 
                #sg.Tab('Record Time', tab2_recordtime, key='-RECORDTIME-'),
                #sg.Tab('Disk Array', tab2_diskarray, key='-DISKARRAY-')]
tab2_layout = [[sg.Text('Capacity Calculation')],
                [sg.Text('Bandwith Calculation - WORK IN PROGRESS')],
                [sg.Text('Resolution'), sg.Text('# of Cameras'), sg.Text('Codec')],
                [sg.Text('1 Megapixel'), sg.Input('', key='-#1MP-', size=(4, 1)), sg.Radio('H.265', 'CODECSEL', default=True, key='#1MPh265'), sg.Radio('H.264', 'CODECSEL', key='#1MPh264'), sg.Radio('MJPEG', 'CODECSEL', key='#1MPMJPEG')],
                [sg.Text('2 Megapixel'), sg.Input('', key='-#2MP-', size=(4, 1)), sg.Radio('H.265', 'CODECSEL', default=True, key='#2MPh265'), sg.Radio('H.264', 'CODECSEL', key='#2MPh264'), sg.Radio('MJPEG', 'CODECSEL', key='#2MPMJPEG')],
                [sg.Text('4 Megapixel'), sg.Input('', key='-#4MP-', size=(4, 1)), sg.Radio('H.265', 'CODECSEL', default=True, key='#4MPh265'), sg.Radio('H.264', 'CODECSEL', key='#4MPh264'), sg.Radio('MJPEG', 'CODECSEL', key='#4MPMJPEG')],
                [sg.Text('5 Megapixel'), sg.Input('', key='-#5MP-', size=(4, 1)), sg.Radio('H.265', 'CODECSEL', default=True, key='#5MPh265'), sg.Radio('H.264', 'CODECSEL', key='#5MPh264'), sg.Radio('MJPEG', 'CODECSEL', key='#5MPMJPEG')],
                [sg.Text('6 Megapixel'), sg.Input('', key='-#6MP-', size=(4, 1)), sg.Radio('H.265', 'CODECSEL', default=True, key='#6MPh265'), sg.Radio('H.264', 'CODECSEL', key='#6MPh264'), sg.Radio('MJPEG', 'CODECSEL', key='#6MPMJPEG')],
                [sg.Text('8 Megapixel'), sg.Input('', key='-#8MP-', size=(4, 1)), sg.Radio('H.265', 'CODECSEL', default=True, key='#8MPh265'), sg.Radio('H.264', 'CODECSEL', key='#8MPh264'), sg.Radio('MJPEG', 'CODECSEL', key='#8MPMJPEG')],
                [sg.Text('12 Megapixel'), sg.Input('', key='-#12MP-', size=(4, 1)), sg.Radio('H.265', 'CODECSEL', default=True, key='#12MPh265'), sg.Radio('H.264', 'CODECSEL', key='#12MPh264'), sg.Radio('MJPEG', 'CODECSEL', key='#12MPMJPEG')]]



tab3_layout = [[sg.Text('IP Calculation')]]
tab4_layout = [[sg.Text('Lens Calculation')]]
tab5_layout = [[sg.Text('Controlex')],
                [sg.Button('Website', key='-CONTROLEXWEBSITE-'), sg.Button('Online Shop', key='-CONTROLEXWEBSHOP-'), sg.Button('Support Portal', key='-CONTROLEXSUPPORTPORTAL-'), sg.Button('Exit', key='-EXIT5-'), sg.Button('Help', key='-CONTROLEXHELP-')]]



tab6_layout = [[sg.Text('Controlex CCTV Companion\n\n'
                        'Version 0.1\n')]]


# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [[sg.Tab('RTSP Stream', tab1_layout, key='-TAB1-'),
                     sg.Tab('Capacity Calculation', tab2_layout, key='-TAB2-'),
                     sg.Tab('IP Calculation', tab3_layout, key='-TAB3-'),
                     sg.Tab('Lens Calculation', tab4_layout, key='-TAB4-'),
                     sg.Tab('Controlex', tab5_layout, key='-TAB5-'),
                     sg.Tab('About', tab6_layout, key='-TAB6-'),
                     ]]

# The window layout - defines the entire window
layout = [[sg.TabGroup(tab_group_layout,
                       enable_events=True,
                       key='-TABGROUP-')]]
#          [sg.Text('Make tab number'), sg.Input(key='-IN-', size=(30,30)), sg.Button('Invisible'), sg.Button('Visible'), sg.Button('Select')]]

window = sg.Window('CCTV Companion', layout, no_titlebar=False)

tab_keys = ('-TAB1-','-TAB2-','-TAB3-', '-TAB4-','-TAB5-','-TAB6-',)         # map from an input value to a key

while True:
    event, values = window.read()
    #print(event, values)
    if event == 'Open':
        ADDRESS = values['-ADDRESS-']
        USERNAME = values['-USERNAME-']
        PASSWORD = values['-PASSWORD-']
        if values["-CHANNEL0-"] == True:
            CHANNELSELECT = '0'
        elif values["-CHANNEL1-"] == True:
            CHANNELSELECT = '1'
        ###ADDRESS = values['-ADDRESS-']
        opencamerastream()
    if event == 'Copy RTSP Link':
        ADDRESS = values['-ADDRESS-']
        USERNAME = values['-USERNAME-']
        PASSWORD = values['-PASSWORD-']
        if values["-CHANNEL0-"] == True:
            CHANNELSELECT = '0'
        elif values["-CHANNEL1-"] == True:
            CHANNELSELECT = '1'
        pyperclip.copy("rtsp://"+USERNAME+":"+PASSWORD+"@"+ADDRESS+'/cam/realmonitor?channel=1&subtype='+CHANNELSELECT)
        sg.popup_no_wait('Link copied')
    if event == 'Web Interface':
        ADDRESS = values['-ADDRESS-']
        webbrowser.open(ADDRESS)
    if event == 'Help':
        sg.popup(
            'RTSP Stream\n\n'
            'This Window can be used to open the RTSP Stream of an IP-Camera.\n\n'
            "Enter the IP-Address of your desired Camera (If you're using the Default RTSP-Port 554 then you don't need to enter the Port)\n\n"
            "Clicking 'Copy RTSP Link' will take the Input of the above fields, merge them together and copy a usable RTSP Link to your clipboard\n\n"
            "If you click on the Button 'Web Interface' it'll open your default Webbrowser and navigate you to the entered IP-Address\n\n"
            "You can select which Stream you want to see by clicking either 'Main Stream' or 'Sub Stream'\n")

    if event == '-CONTROLEXWEBSITE-':
        webbrowser.open('https://controlex.eu')

    if event == '-CONTROLEXWEBSHOP-':
        webbrowser.open('https://controlex-shop.com')

    if event == '-CONTROLEXSUPPORTPORTAL-':
        webbrowser.open('https://controlex-shop.freshdesk.com/support/login')

    if event == '-CONTROLEXHELP-':
        [sg.Popup('Controlex\n\n'
                    'Use the links on this Site to quickly navigate to our Website, Online-Shop or Helpdesk\n')]

    if event == sg.WIN_CLOSED or event == '-EXIT-' or event == '-EXIT5-':
        break
    # handle button clicks
    #if event == 'Invisible':
    #    window[tab_keys[int(values['-IN-'])-1]].update(visible=False)
    #if event == 'Visible':
    #    window[tab_keys[int(values['-IN-'])-1]].update(visible=True)
    #if event == 'Select':
    #    window[tab_keys[int(values['-IN-'])-1]].select()

window.close()
from tkinter import *
from tkVideoPlayer import TkinterVideo
import time


class GUI:
    MIN_VOL = 0
    MAX_VOL = 10
    MIN_CH = 0
    MAX_CH = 3

    VID_ONE = 'assets/news.mp4'
    VID_TWO = 'assets/sports.mp4'
    VID_THREE = 'assets/spongebob.mp4'
    VID_FOUR = 'assets/tv_show.mp4'

    def __init__(self, window: Tk) -> None:
        self.__status = False
        self.__mute = False
        self.__vol = GUI.MIN_VOL
        self.__ch = GUI.MIN_CH

        self.window = window
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        self.window.columnconfigure(4, weight=1)
        self.window.columnconfigure(5, weight=1)
        self.window.columnconfigure(6, weight=1)

        # Power
        self.button_pw = Button(self.window, text='Power', command=self.power)
        self.button_pw.grid(row=0, column=1, pady=2)

        # Video
        self.vid_player = TkinterVideo(master=window, scaled=True)
        self.vid_player.load(GUI.VID_ONE)
        self.vid_player.grid(row=0, column=3, pady=2)

        # Volume
        self.button_vol_up = Button(self.window, text=' + ', command=self.vol_up)
        self.button_vol_up.grid(row=1, column=1, sticky=E, pady=2)
        self.button_vol_down = Button(self.window, text=' - ', command=self.vol_down)
        self.button_vol_down.grid(row=3, column=1, sticky=E, pady=2)
        self.label_vol = Label(self.window, text='VOL = 0')
        self.label_vol.grid(row=2, column=1, sticky=E, pady=2)

        self.vol_view = Scale(self.window, from_=GUI.MIN_VOL, to=GUI.MAX_VOL, orient=HORIZONTAL, showvalue=False)
        self.vol_view.grid(row=2, column=3, pady=2)

        # Mute
        self.button_mute = Button(self.window, text='Mute', command=self.mute)
        self.button_mute.grid(row=3, column=3, pady=2)

        # Channel
        self.button_ch_up = Button(self.window, text=' /\ ', command=self.ch_up)
        self.button_ch_up.grid(row=1, column=5, sticky=W, pady=2)
        self.button_ch_down = Button(self.window, text=' \/ ', command=self.ch_down)
        self.button_ch_down.grid(row=3, column=5, sticky=W, pady=2)
        self.label_ch = Label(self.window, text='CH = 0')
        self.label_ch.grid(row=2, column=5, sticky=W, pady=2)

    def power(self) -> None:
        '''
        Function that allows the tv to turn on off, handles showing videos and removing them.
        :return: None
        '''
        if not self.__status:
            self.__status = True
            self.play()
        else:
            self.__status = False
            self.vid_player.grid_forget()
            self.vid_player.stop()
        # Videos
        '''
        Function to play and remove videos and sets up in GUI grid.
        :return: None
        '''

    def play(self) -> None:
        if self.__status:
            self.vid_player.grid(row=0, column=3, pady=2)
            self.vid_player.play()

    def stop(self) -> None:
        self.vid_player.grid_forget()
        self.vid_player.stop()
        time.sleep(.1)
        self.play()

    # Volume Changes and MUTE
    def change_vol(self, value: int) -> None:
        '''
        Function for changing volume, changes slider GUI and produces text showing volume.
        :return: None:
        '''

        if self.__status:
            self.__vol = int(value)
            self.label_vol['text'] = f'VOL = {self.__vol}'
        else:
            self.vol_view.set(GUI.MIN_VOL)

    def vol_up(self) -> None:
        '''
        Function adjusts TV volume, checks if on and if muted, changes volume, and adjusts GUI labels and slider.
        :return: None:
        '''

        if self.__status:
            if not self.__mute:
                if self.__vol == GUI.MAX_VOL:
                    pass
                else:
                    self.__vol += 1
                    self.label_vol['text'] = f'VOL: {self.__vol}'
                    self.vol_view.set(self.__vol)
        else:
            pass

    def vol_down(self) -> None:
        if self.__status:
            if not self.__mute:
                if self.__vol == GUI.MIN_VOL:
                    pass
                else:
                    self.__vol -= 1
                    self.label_vol['text'] = f'VOL: {self.__vol}'
                    self.vol_view.set(self.__vol)
        else:
            pass

    def mute(self) -> None:
        '''
        Function mutes the tv and unmutes it. Adjusts slider aswell, and changes GUI labels to account for mute.
        :return: None
        '''

        if self.__status:
            if not self.__mute:
                self.__mute = True
                self.label_vol['text'] = f'VOL = MUTE'
            else:
                self.__mute = False
                self.label_vol['text'] = f'VOL = {self.__vol}'
                self.vol_view.set(self.__vol)

    # Channel Up and Down
    def ch_up(self) -> None:
        '''
        Function adjusts channel of TV, checks if on, changes channel, adjusts GUI labels and slider, and loads
        videos and stopping video in order to change them.
        :return: None:
        '''

        if self.__ch >= GUI.MAX_CH and self.__status:
            self.__ch = GUI.MIN_CH
            self.label_ch['text'] = f'CH: {self.__ch}'

            if self.__ch == 0:
                self.vid_player.load(GUI.VID_ONE)
            elif self.__ch == 1:
                self.vid_player.load(GUI.VID_TWO)
            elif self.__ch == 2:
                self.vid_player.load(GUI.VID_THREE)
            elif self.__ch == 3:
                self.vid_player.load(GUI.VID_FOUR)

        elif self.__status:
            self.__ch += 1
            self.label_ch['text'] = f'CH: {self.__ch}'

            if self.__ch == 0:
                self.vid_player.load(GUI.VID_ONE)
            elif self.__ch == 1:
                self.vid_player.load(GUI.VID_TWO)
            elif self.__ch == 2:
                self.vid_player.load(GUI.VID_THREE)
            elif self.__ch == 3:
                self.vid_player.load(GUI.VID_FOUR)

        self.stop()

    def ch_down(self) -> None:
        if self.__ch <= GUI.MIN_CH and self.__status:
            self.__ch = GUI.MAX_CH
            self.label_ch['text'] = f'CH: {self.__ch}'

            if self.__ch == 0:
                self.vid_player.load(GUI.VID_ONE)
            elif self.__ch == 1:
                self.vid_player.load(GUI.VID_TWO)
            elif self.__ch == 2:
                self.vid_player.load(GUI.VID_THREE)
            elif self.__ch == 3:
                self.vid_player.load(GUI.VID_FOUR)
        elif self.__status:
            self.__ch -= 1
            self.label_ch['text'] = f'CH: {self.__ch}'

            if self.__ch == 0:
                self.vid_player.load(GUI.VID_ONE)
            elif self.__ch == 1:
                self.vid_player.load(GUI.VID_TWO)
            elif self.__ch == 2:
                self.vid_player.load(GUI.VID_THREE)
            elif self.__ch == 3:
                self.vid_player.load(GUI.VID_FOUR)

        self.stop()


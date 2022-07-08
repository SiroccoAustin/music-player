import time
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
import os
from kivy.clock import Clock
Window.size = (300, 600)

kv = '''
MDRelativeLayout:
    md_bg_color: 0.1, 0.1, 0.1, 1
    MDIconButton:
        id: play_button
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        icon: "play"
        on_press: app.playbutton()

    # MDIconButton:
    #     id: stop_button
    #     pos_hint: {'center_x': 0.2, 'center_y': 0.09}
    #     icon: "stop"
    #     disabled: True
    #     on_press: app.stopbutton()
        
    MDIconButton:
        id: next
        icon: 'skip-forward'
        pos_hint: {'center_x': 0.67, 'center_y': 0.09}
        on_press: app.nextsong()
        
    MDIconButton:
        id: prev
        icon: 'skip-backward'
        pos_hint: {'center_x': 0.3, 'center_y': 0.09}
        on_press: app.previous_song()
         
    Image:
        id: my_image
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: 0.7, 0.6
    MDProgressBar:
        id: my_duration
        pos_hint: {'center_x': 0.47, 'center_y': 0.14}
        max: 100
        value: 0
        size_hint: 0.85, 0.02
    MDLabel:
        id: my_song
        pos_hint: {'center_x': 0.5, 'center_y': 0.86}
        text: ''
        font_size: 18
        halign: 'center'
        color: 1, 0, 0, 1
    MDLabel:
        id: current_time
        pos_hint: {'center_x': 0.54, 'center_y': 0.17}
        text: '00:00'
        color: 1, 0, 0, 1
    MDLabel:
        id: total_time
        pos_hint: {'center_x': 1.23, 'center_y': 0.17}
        text: '00:00'
        color: 1, 0, 0, 1
'''

class MyMusicApp(MDApp):
    def build(self):
        self.icon = 'artwork_front_small.jpg'
        self.music_dir = os.listdir("C:/Users/sirocco/PycharmProjects/pythonProject")
        self.my_music = [x for x in self.music_dir if x.endswith('mp3')]
        self.song_length = len(self.my_music)
        self.count = 0
        self.my_label = Builder.load_string(kv)
        return self.my_label

    def playbutton(self):
        # self.root.ids.stop_button.disabled = False

        self.song_title = self.my_music[0]
        self.sound = SoundLoader.load(self.song_title)
        self.root.ids.my_image.source = 'artwork_front.jpg'
        self.root.ids.my_song.text = 'Playing ' + self.song_title[2:-4]
        # self.root.ids.volume.bind(value=self.volume)
        if self.sound:
            self.sound.play()
            self.root.ids.play_button.disabled = True
        self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.sound.length / 60.0)
        self.timeEvent = Clock.schedule_interval(self.settime, 5.0 / 60.0)

    def stopbutton(self):
        # self.root.ids.stop_button.disabled = True
        self.root.ids.play_button.disabled = False
        self.progressEvent.cancel()
        self.timeEvent.cancel()
        self.root.ids.my_duration.value = 0
        self.root.ids.current_time.text = '00:00'
        self.root.ids.total_time.text = '00:00'
        self.sound.stop()

    def update_progressbar(self, value):
        if self.root.ids.my_duration.value < 300:
            self.root.ids.my_duration.value += 1
    def settime(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.sound.length))

    def setduration1(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song1.length))

    def setduration2(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song2.length))

    def setduration3(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song3.length))

    def setduration4(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song4.length))

    def setduration5(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song5.length))

    def setduration6(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song6.length))

    def setduration7(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song7.length))
    def setduration8(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song8.length))

    def setduration9(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song9.length))

    def setduration10(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song10.length))

    def setduration11(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song11.length))

    def setduration12(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song12.length))

    def setduration13(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song13.length))

    def setduration14(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song14.length))

    def setduration15(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song15.length))

    def setduration16(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song16.length))

    def setduration17(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song17.length))

    def setduration18(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song18.length))

    def setduration19(self, dt):
        self.root.ids.current_time.text = time.strftime('%M:%S', time.gmtime(self.root.ids.my_duration.value))
        self.root.ids.total_time.text = time.strftime('%M:%S', time.gmtime(self.my_song19.length))

    def nextsong(self):
        self.stopbutton()
        self.count += 1
        if self.count == 1:
            self.music1 = self.my_music[self.count]
            self.my_song1 = SoundLoader.load(self.music1)
            self.root.ids.my_song.text = 'Playing ' + self.music1[2:-4]
            if self.my_song1:
                self.my_song1.play()
                self.root.ids.play_button.disabled = True
                self.root.ids.prev.disabled = False
                self.progressEvent1 = Clock.schedule_interval(self.update_progressbar, self.my_song1.length / 60.0)
                self.timeEvent1 = Clock.schedule_interval(self.setduration1, 5.0 / 60.0)

        if self.count == 2:
            self.my_song1.stop()
            self.music2 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music2[2:-4]
            self.my_song2 = SoundLoader.load(self.music2)
            if self.my_song2:
                self.my_song2.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent2 = Clock.schedule_interval(self.update_progressbar, self.my_song2.length / 60.0)
                self.timeEvent2 = Clock.schedule_interval(self.setduration2, 5.0 / 60.0)

        if self.count == 3:
            self.my_song2.stop()
            self.music3 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music3[2:-4]
            self.my_song3 = SoundLoader.load(self.music3)
            if self.my_song3:
                self.my_song3.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song3.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration3, 5.0 / 60.0)

        if self.count == 4:
            self.my_song3.stop()
            self.music4 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music4[2:-4]
            self.my_song4 = SoundLoader.load(self.music4)
            if self.my_song4:
                self.my_song4.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song4.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration4, 5.0 / 60.0)

        if self.count == 5:
            self.my_song4.stop()
            self.music5 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music5[2:-4]
            self.my_song5 = SoundLoader.load(self.music5)
            if self.my_song5:
                self.my_song5.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song5.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration5, 5.0 / 60.0)

        if self.count == 6:
            self.my_song5.stop()
            self.music6 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music6[2:-4]
            self.my_song6 = SoundLoader.load(self.music6)
            if self.my_song6:
                self.my_song6.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song5.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration6, 5.0 / 60.0)

        if self.count == 7:
            self.my_song6.stop()
            self.music7 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music7[2:-4]
            self.my_song7 = SoundLoader.load(self.music7)
            if self.my_song7:
                self.my_song7.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song7.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration7, 5.0 / 60.0)

        if self.count == 8:
            self.my_song7.stop()
            self.music8 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music8[2:-4]
            self.my_song8 = SoundLoader.load(self.music8)
            if self.my_song8:
                self.my_song8.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song8.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration8, 5.0 / 60.0)

        if self.count == 9:
            self.my_song8.stop()
            self.music9 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music9[2:-4]
            self.my_song9 = SoundLoader.load(self.music9)
            if self.my_song9:
                self.my_song9.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song9.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration9, 5.0 / 60.0)

        if self.count == 10:
            self.my_song9.stop()
            self.music10 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music10[2:-4]
            self.my_song10 = SoundLoader.load(self.music10)
            if self.my_song10:
                self.my_song10.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song10.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration10, 5.0 / 60.0)

        if self.count == 11:
            self.my_song10.stop()
            self.music11 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music11[2:-4]
            self.my_song11 = SoundLoader.load(self.music11)
            if self.my_song11:
                self.my_song11.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song11.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration11, 5.0 / 60.0)

        if self.count == 12:
            self.my_song11.stop()
            self.music12 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music12[2:-4]
            self.my_song12 = SoundLoader.load(self.music12)
            if self.my_song12:
                self.my_song12.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song12.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration12, 5.0 / 60.0)

        if self.count == 13:
            self.my_song12.stop()
            self.music13 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music13[2:-4]
            self.my_song13 = SoundLoader.load(self.music13)
            if self.my_song13:
                self.my_song13.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song13.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration13, 5.0 / 60.0)

        if self.count == 14:
            self.my_song13.stop()
            self.music14 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music14[2:-4]
            self.my_song14 = SoundLoader.load(self.music14)
            if self.my_song14:
                self.my_song14.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.my_song14.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration14, 5.0 / 60.0)

        if self.count == 15:
            self.my_song14.stop()
            self.music15 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music15[2:-4]
            self.my_song15 = SoundLoader.load(self.music15)
            if self.my_song15:
                self.my_song15.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.sound.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration15, 5.0 / 60.0)

        if self.count == 16:
            self.my_song15.stop()
            self.music16 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music16[2:-4]
            self.my_song16 = SoundLoader.load(self.music16)
            if self.my_song16:
                self.my_song16.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.sound.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration16, 5.0 / 60.0)

        if self.count == 17:
            self.my_song16.stop()
            self.music17 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music17[2:-4]
            self.my_song17 = SoundLoader.load(self.music17)
            if self.my_song17:
                self.my_song17.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.sound.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration17, 5.0 / 60.0)

        if self.count == 18:
            self.my_song17.stop()
            self.music18 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music18[2:-4]
            self.my_song18 = SoundLoader.load(self.music18)
            if self.my_song18:
                self.my_song18.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.sound.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration18, 5.0 / 60.0)

        if self.count == 19:
            self.my_song18.stop()
            self.music19 = self.my_music[self.count]
            self.root.ids.my_song.text = 'Playing ' + self.music19[2:-4]
            self.my_song19 = SoundLoader.load(self.music19)
            if self.my_song19:
                self.my_song19.play()
                self.root.ids.play_button.disabled = True
                self.progressEvent = Clock.schedule_interval(self.update_progressbar, self.sound.length / 60.0)
                self.timeEvent = Clock.schedule_interval(self.setduration19, 5.0 / 60.0)
            if self.count == 19:
                self.root.ids.next.disabled = True
            else:
                self.root.ids.next.disabled = False

    def previous_song(self):
        self.count -= 1
        if self.count == 0:
            self.my_song1.stop()
            # self.prev0 = self.my_music[self.count]
            # self.my_prev0 = SoundLoader.load(self.prev0)
            # if self.my_prev0:
            #     self.my_prev0.play()
            self.playbutton()
            self.root.ids.prev.disabled = True

        if self.count == 1:
            self.my_song2.stop()
            # self.prev1 = self.my_music[self.count]
            # self.my_prev1 = SoundLoader.load(self.prev1)
            # if self.my_prev1:
            #     self.my_prev1.play()
            self.root.ids.my_song.text = 'Playing ' + self.music1[2:-4]
            self.my_song1.play()
            self.progressEvent1 = Clock.schedule_interval(self.update_progressbar, self.my_song1.length / 60.0)
            self.timeEvent1 = Clock.schedule_interval(self.setduration1, 5.0 / 60.0)
            self.root.ids.prev.disabled = False

        if self.count == 2:
            self.my_song3.stop()
            # self.prev2 = self.my_music[self.count]
            # self.myprev2 = SoundLoader.load(self.prev2)
            # if self.myprev2:
            #     self.myprev2.play()
            self.root.ids.my_song.text = 'Playing ' + self.music2[2:-4]
            self.my_song2.play()
            self.progressEvent2 = Clock.schedule_interval(self.update_progressbar, self.my_song2.length / 60.0)
            self.timeEvent2 = Clock.schedule_interval(self.setduration2, 5.0 / 60.0)

        if self.count == 3:
            self.my_song4.stop()
            # self.prev3 = self.my_music[self.count]
            # self.myprev3 = SoundLoader.load(self.prev3)
            # if self.myprev3:
            #     self.myprev3.play()
            self.root.ids.my_song.text = 'Playing ' + self.music3[2:-4]
            self.my_song3.play()
            self.progressEvent3 = Clock.schedule_interval(self.update_progressbar, self.my_song3.length / 60.0)
            self.timeEvent3 = Clock.schedule_interval(self.setduration3, 5.0 / 60.0)

        if self.count == 4:
            self.my_song5.stop()
            # self.prev4 = self.my_music[self.count]
            # self.myprev4 = SoundLoader.load(self.prev4)
            # if self.myprev4:
            #     self.myprev4.play()
            self.root.ids.my_song.text = 'Playing ' + self.music4[2:-4]
            self.my_song4.play()
            self.progressEvent4 = Clock.schedule_interval(self.update_progressbar, self.my_song4.length / 60.0)
            self.timeEvent4 = Clock.schedule_interval(self.setduration4, 5.0 / 60.0)

        if self.count == 5:
            self.my_song6.stop()
            # self.prev5 = self.my_music[self.count]
            # self.myprev5 = SoundLoader.load(self.prev5)
            # if self.myprev5:
            #     self.myprev5.play()
            self.root.ids.my_song.text = 'Playing ' + self.music5[2:-4]
            self.my_song5.play()
            self.progressEvent5 = Clock.schedule_interval(self.update_progressbar, self.my_song5.length / 60.0)
            self.timeEvent5 = Clock.schedule_interval(self.setduration5, 5.0 / 60.0)

        if self.count == 6:
            self.my_song7.stop()
            # self.prev6 = self.my_music[self.count]
            # self.myprev6 = SoundLoader.load(self.prev6)
            # if self.myprev6:
            #     self.myprev6.play()
            self.root.ids.my_song.text = 'Playing ' + self.music6[2:-4]
            self.my_song6.play()
            self.progressEvent6 = Clock.schedule_interval(self.update_progressbar, self.my_song6.length / 60.0)
            self.timeEvent6 = Clock.schedule_interval(self.setduration6, 5.0 / 60.0)

        if self.count == 7:
            self.my_song8.stop()
            # self.prev7 = self.my_music[self.count]
            # self.myprev7 = SoundLoader.load(self.prev7)
            # if self.myprev7:
            #     self.myprev7.play()
            self.root.ids.my_song.text = 'Playing ' + self.music7[2:-4]
            self.my_song7.play()
            self.progressEvent7 = Clock.schedule_interval(self.update_progressbar, self.my_song7.length / 60.0)
            self.timeEvent7 = Clock.schedule_interval(self.setduration7, 5.0 / 60.0)

        if self.count == 8:
            self.my_song9.stop()
            # self.prev8 = self.my_music[self.count]
            # self.myprev8 = SoundLoader.load(self.prev8)
            # if self.myprev8:
            #     self.myprev8.play()
            self.root.ids.my_song.text = 'Playing ' + self.music8[2:-4]
            self.my_song8.play()
            self.progressEvent8 = Clock.schedule_interval(self.update_progressbar, self.my_song8.length / 60.0)
            self.timeEvent8 = Clock.schedule_interval(self.setduration8, 5.0 / 60.0)

        if self.count == 9:
            self.my_song10.stop()
            # self.prev9 = self.my_music[self.count]
            # self.myprev9 = SoundLoader.load(self.prev9)
            # if self.myprev9:
            #     self.myprev9.play()
            self.root.ids.my_song.text = 'Playing ' + self.music9[2:-4]
            self.my_song9.play()
            self.progressEvent9 = Clock.schedule_interval(self.update_progressbar, self.my_song9.length / 60.0)
            self.timeEvent9 = Clock.schedule_interval(self.setduration9, 5.0 / 60.0)

        if self.count == 10:
            self.my_song11.stop()
            # self.prev10 = self.my_music[self.count]
            # self.myprev10 = SoundLoader.load(self.prev10)
            # if self.myprev10:
            #     self.myprev10.play()
            self.root.ids.my_song.text = 'Playing ' + self.music10[2:-4]
            self.my_song10.play()
            self.progressEvent10 = Clock.schedule_interval(self.update_progressbar, self.my_song10.length / 60.0)
            self.timeEvent10 = Clock.schedule_interval(self.setduration10, 5.0 / 60.0)

        if self.count == 11:
            self.my_song12.stop()
            # self.prev11 = self.my_music[self.count]
            # self.myprev11 = SoundLoader.load(self.prev11)
            # if self.myprev11:
            #     self.myprev11.play()
            self.root.ids.my_song.text = 'Playing ' + self.music11[2:-4]
            self.my_song11.play()
            self.progressEvent11 = Clock.schedule_interval(self.update_progressbar, self.my_song11.length / 60.0)
            self.timeEvent11 = Clock.schedule_interval(self.setduration11, 5.0 / 60.0)

        if self.count == 12:
            self.my_song13.stop()
            # self.prev12 = self.my_music[self.count]
            # self.myprev12 = SoundLoader.load(self.prev12)
            # if self.myprev12:
            #     self.myprev12.play()
            self.root.ids.my_song.text = 'Playing ' + self.music12[2:-4]
            self.my_song12.play()
            self.progressEvent12 = Clock.schedule_interval(self.update_progressbar, self.my_song12.length / 60.0)
            self.timeEvent12 = Clock.schedule_interval(self.setduration12, 5.0 / 60.0)

        if self.count == 13:
            self.my_song14.stop()
            # self.prev13 = self.my_music[self.count]
            # self.myprev13 = SoundLoader.load(self.prev13)
            # if self.myprev13:
            #     self.myprev13.play()
            self.root.ids.my_song.text = 'Playing ' + self.music13[2:-4]
            self.my_song13.play()
            self.progressEvent13 = Clock.schedule_interval(self.update_progressbar, self.my_song13.length / 60.0)
            self.timeEvent13 = Clock.schedule_interval(self.setduration13, 5.0 / 60.0)

        if self.count == 14:
            self.my_song15.stop()
            # self.prev14 = self.my_music[self.count]
            # self.myprev14 = SoundLoader.load(self.prev14)
            # if self.myprev14:
            #     self.myprev14.play()
            self.root.ids.my_song.text = 'Playing ' + self.music14[2:-4]
            self.my_song14.play()
            self.progressEvent14 = Clock.schedule_interval(self.update_progressbar, self.my_song14.length / 60.0)
            self.timeEvent14 = Clock.schedule_interval(self.setduration14, 5.0 / 60.0)

        if self.count == 15:
            self.my_song16.stop()
            # self.prev15 = self.my_music[self.count]
            # self.myprev15 = SoundLoader.load(self.prev15)
            # if self.myprev15:
            #     self.myprev15.play()
            self.root.ids.my_song.text = 'Playing ' + self.music15[2:-4]
            self.my_song15.play()
            self.progressEvent15 = Clock.schedule_interval(self.update_progressbar, self.my_song15.length / 60.0)
            self.timeEvent15 = Clock.schedule_interval(self.setduration15, 5.0 / 60.0)

        if self.count == 16:
            self.my_song17.stop()
            # self.prev16 = self.my_music[self.count]
            # self.myprev16 = SoundLoader.load(self.prev16)
            # if self.myprev16:
            #     self.myprev16.play()
            self.root.ids.my_song.text = 'Playing ' + self.music16[2:-4]
            self.my_song16.play()
            self.progressEvent16 = Clock.schedule_interval(self.update_progressbar, self.my_song16.length / 60.0)
            self.timeEvent16 = Clock.schedule_interval(self.setduration16, 5.0 / 60.0)

        if self.count == 17:
            self.my_song18.stop()
            # self.prev17 = self.my_music[self.count]
            # self.myprev17 = SoundLoader.load(self.prev17)
            # if self.myprev17:
            #     self.myprev17.play()
            self.root.ids.my_song.text = 'Playing ' + self.music17[2:-4]
            self.my_song17.play()
            self.progressEvent17 = Clock.schedule_interval(self.update_progressbar, self.my_song17.length / 60.0)
            self.timeEvent17 = Clock.schedule_interval(self.setduration17, 5.0 / 60.0)

        if self.count == 18:
            self.my_song19.stop()
            # self.prev18 = self.my_music[self.count]
            # self.myprev18 = SoundLoader.load(self.prev18)
            # if self.myprev18:
            #     self.myprev18.play()
            self.root.ids.my_song.text = 'Playing ' + self.music18[2:-4]
            self.my_song18.play()
            self.progressEvent18 = Clock.schedule_interval(self.update_progressbar, self.my_song18.length / 60.0)
            self.timeEvent18 = Clock.schedule_interval(self.setduration18, 5.0 / 60.0)

        # if self.count == 19:
            # self.my_song19.stop()
            # self.prev19 = self.my_music[self.count]
            # self.myprev19 = SoundLoader.load(self.prev19)
            # if self.myprev19:
            #     self.myprev19.play()


        # print(self.count)
if __name__ == '__main__':
    MyMusicApp().run()
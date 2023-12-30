# coding: utf-8

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from about import About
from gui_presenter import GuiPresenter
from downloader import Downloader
from gui_launcher import GuiLauncher

class TkinterView():
    def __init__(self):
        self.presenter = None

    def show(self):
        root = Tk()

        for c in range(2): root.columnconfigure(index=c, weight=1)
        for r in range(5): root.rowconfigure(index=r, weight=1)
        
        title = About.about_message
        root.title(title)

        margin_x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 480 / 4
        margin_y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 480 / 4
        root.wm_geometry("480x480+%d+%d" % (margin_x, margin_y))
        
        font = ('Comic Sans MS', 16)
        bg = '#4c70d8'
        fg = '#e4cf10'

        root.config(bg='#4c70d8')
        root.resizable(width=False, height=False)

        label_frame = LabelFrame(root,
            font=font,
            text='Ссылка',
            bg=bg,
            fg=fg
        )
        for c in range(1): label_frame.columnconfigure(index=c, weight=1)
        for r in range(1): label_frame.rowconfigure(index=r, weight=1)

        self.link_text = Text(label_frame,
            font=font,
            height=3
        )

        self.progressbar = ttk.Progressbar(orient="horizontal", 
            mode="indeterminate"
        )

        self.download_button = Button(root,
            font=font,
            text = 'Загрузить',
            command=self._start_downloading
        )

        self.status_label = Label(root,
            font=font,
            text='Статус:',
            bg=bg,
            fg=fg
        )

        self.download_result_status_label_text_variable = StringVar()
        self.download_result_status_label = Label(root,
            font=font,
            textvariable = self.download_result_status_label_text_variable,
            bg=bg,
            fg=fg
        )

        self.time_label = Label(root,
            font=font,
            text='Время (сек):',
            bg=bg,
            fg=fg
        )

        self.download_result_time_label_text_variable = StringVar()
        self.download_result_time_label = Label(root,
            font=font,
            textvariable=self.download_result_time_label_text_variable,
            bg=bg,
            fg=fg
        )

        self.empty_label = Label(root,
            font=font,
            bg=bg
        )

        label_frame.grid(row=0, column=0, sticky=W+E, columnspan=2, pady=10, padx=10)
        self.link_text.grid(row=0, column=0, sticky=W+E, pady=10, padx=10)
        self.download_button.grid(row=1, column=0, columnspan=2, sticky=W+E, pady=10, padx=10)
        self.status_label.grid(row=2, column=0, sticky=W+E, pady=10, padx=10)
        self.download_result_status_label.grid(row=2, column=1, sticky=W+E, pady=10, padx=10)
        self.time_label.grid(row=3, column=0, sticky=W+E, pady=10, padx=10)
        self.download_result_time_label.grid(row=3, column=1, sticky=W+E, pady=10, padx=10)
        self.empty_label.grid(row=4, column=0, columnspan=2, sticky=W+E, pady=10, padx=10)

        root.bind_all("<Key>", self._on_key_release, "+")
        root.mainloop()

    def _start_downloading(self):
        link = self.link_text.get('1.0', 'end-1c')
        self.presenter.start_downloading(link)

    def set_download_button_enabled(self, enabled):
        state = NORMAL if enabled else DISABLED
        self.download_button.config(state=state)

    def set_link_text_state_enabled(self, enabled):
        state = NORMAL if enabled else DISABLED
        self.link_text.config(state=state)

    def start_progressbar(self):
        self.empty_label.grid_forget()
        self.progressbar.grid(row=4, column=0, columnspan=2, sticky=W+E, pady=10, padx=10)
        self.progressbar.start()

    def stop_progressbar(self):
        self.progressbar.stop()
        self.progressbar.grid_forget()
        self.empty_label.grid(row=4, column=0, columnspan=2, sticky=W+E, pady=10, padx=10)

    def hide_download_result_status(self):
        self.download_result_status_label.text = ''

    def set_download_result_status(self, status):
        self.download_result_status_label_text_variable.set(status)

    def hide_download_result_time(self):
        self.download_result_time_label = ''

    def set_download_result_time(self, time):
        self.download_result_time_label_text_variable.set(time)

    def _on_key_release(self, event):
        ctrl = (event.state & 0x4) != 0

        keycode = event.keycode
        keysym = event.keysym.lower()
        event_generate = lambda name : event.widget.event_generate(name)

        if keycode==88 and ctrl and keysym != "x": 
            event_generate("<<Cut>>")

        if keycode==86 and ctrl and keysym != "v": 
            event_generate("<<Paste>>")

        if keycode==67 and ctrl and keysym != "c":
            event_generate("<<Copy>>")

        if keycode==65 and ctrl and keysym != "a":
            event_generate("<<SelectAll>>")

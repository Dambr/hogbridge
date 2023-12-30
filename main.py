# coding: utf-8

from tkinter_view import TkinterView
from gui_presenter import GuiPresenter
from gui_launcher import GuiLauncher
from downloader import Downloader

def main():

    downloader = Downloader()
    view = TkinterView()
    presenter = GuiPresenter()
    launcher = GuiLauncher(downloader)
    view.presenter = presenter
    presenter.view = view
    launcher.presenter = presenter
    presenter.gui_launcher = launcher

    launcher.launch()

if __name__ == "__main__":
    main()

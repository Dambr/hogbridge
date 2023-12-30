# coding: utf-8

import argparse

from run_mode import RunMode
from console_launcher import ConsoleLauncher
from tkinter_view import TkinterView
from gui_presenter import GuiPresenter
from gui_launcher import GuiLauncher
from about import About
from downloader import Downloader

def main():
    program_name = About.program_name
    description = "The program is designed to download videos from YouTube hosting"
    version_message = About.about_message

    parser = argparse.ArgumentParser(prog=program_name, description=description)
    parser.add_argument("-v", "--version", help="show program version and exit", action="version", version=version_message)

    console_group_title = "console"
    console_group_description = "A group of parameters required to launch and operate the program in console mode"
    console_group = parser.add_argument_group(title=console_group_title, description=console_group_description)
    console_group.add_argument("--link", help="link to video on YouTube hosting", dest="link")

    args = parser.parse_args()

    downloader = Downloader()

    launcher = None
    run_mode = determine_run_mod(args)
    if run_mode == RunMode.GUI:
        view = TkinterView()
        presenter = GuiPresenter()
        launcher = GuiLauncher(downloader)
        view.presenter = presenter
        presenter.view = view
        launcher.presenter = presenter
        presenter.gui_launcher = launcher
        
    elif run_mode == RunMode.CONSOLE:
        link = args.link
        link = "https://www.youtube.com/watch?v=DfndlgFDEYA&ab_channel=%D0%9F%D0%B8%D0%B3%D0%BC%D0%B5%D0%B8-Topic"
        launcher = ConsoleLauncher(link, downloader)

    launcher.launch()

def determine_run_mod(args):
    link = args.link
    return RunMode.GUI if link == None else RunMode.CONSOLE

if __name__ == "__main__":
    main()

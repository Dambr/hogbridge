# coding: utf-8

class GuiPresenter:
	def __init__(self):
		self.gui_launcher = None
		self.view = None

	def show_gui(self):
		self.view.show()

	def start_downloading(self, link):
		self.view.hide_download_result_status()
		self.view.hide_download_result_time()
		self.view.set_link_text_state_enabled(False)
		self.view.set_download_button_enabled(False)
		self.view.start_progressbar()
		
		end_downloading_callback = lambda download_result : self._end_downloading(download_result)
		self.gui_launcher.start_downloading(link, end_downloading_callback)

	def _end_downloading(self, download_result):
		print(1)
		self.view.set_link_text_state_enabled(True)
		self.view.set_download_button_enabled(True)
		self.view.stop_progressbar()

		status = download_result.status.name
		time = download_result.time_duration

		print(status)
		print(time)

		self.view.set_download_result_status(status)
		self.view.set_download_result_time(time)
import sublime
import sublime_plugin
import subprocess
import os

class InputHelperCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sel = self.view.sel()
        text_output = None
        args = []

        if sublime.platform() == 'linux':

            location = os.path.join(sublime.packages_path(), 'InputHelper', 'lib', 'linux_text_input_gui.py')
            args = [location]

            proc = subprocess.Popen(args, stdout=subprocess.PIPE)
            text_returned = proc.communicate()[0].strip()
            text_output = text_returned.decode('utf-8')

        if text_output:
            for region in sel:
                self.view.erase(edit, region)
                self.view.insert(edit, region.begin(), text_output)

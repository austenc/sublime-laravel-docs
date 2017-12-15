import sublime_plugin
import webbrowser


class LaravelDocsCommand(sublime_plugin.WindowCommand):
    def run(self, page=''):
        # open a new page
        url = 'https://laravel.com/docs/'
        if(page != ''):
            url = url + page
            webbrowser.open_new_tab(url)

import webbrowser

# webbrowser.open("https://www.python.org")
#
# help(webbrowser)

chrome = webbrowser.get(using='windows-default')
chrome.open_new_tab("https://www.python.org")
# chrome.open("https://www.python.org")
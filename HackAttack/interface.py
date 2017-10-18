import webbrowser
url = 'http://localhost/HackAttack/speechToText.html';
cp = "open -a /Applications/Google\ Chrome.app %s"

webbrowser.get(cp).open(url);
exec("summarizeAndWordCloud.py")
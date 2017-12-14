import re
import json
import urllib.request

# Create a request with a valid User-Agent
req = urllib.request.Request(
    'https://laravel.com/docs/',
    data = None,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

# Pull the html from the main docs page and find all /docs links
docs = urllib.request.urlopen(req)
links = re.findall('"(/docs/.*?)"', docs.read().decode('utf-8'))

# Format each link as a sublime command, regenerate the command file
with open('Default.sublime-commands', 'w+') as f:
    f.write('[\n')
    first = True
    for url in set(links):
        if not first:
            f.write(', \n    ')
        else:
            f.write('    ')
            first = False

        topic = url.split('/')[3].title().replace('-', ' ')
        slug = url.split('/')[3].split('#')[0]

        j = {"caption": "Laravel Docs: {}".format(topic),
             "command": "laravel_docs",
             "args": {"page" : "{}".format(slug)}}
        json.dump(j,f)

    f.write('\n]\n')

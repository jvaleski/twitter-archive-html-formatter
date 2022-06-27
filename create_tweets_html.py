#!/usr/bin/env python3

import json

# you have to modify the tweets.js to make it compliant json. slight tweaks to the beginning and end of the file will do this. I also updated the file extension to .json
tweet_file = open('tweets.json')
data = json.load(tweet_file)
tweet_file.close()

html_file = open('tweets.html', 'w')
html_file.write('<html>\n')
html_file.write('<table>\n')
html_file.write('  <tr><th>Created</th><th>Tweet</th><th>Image (if any)</th><th>ID</th></tr>\n')

base_media_url = 'https://someserver.com/data/tweet_media/'

for tweet in data['tweets']:
  id_str = tweet['tweet']['id_str']
  html_file.write('  <tr>\n')
  html_file.write('    <td>' + tweet['tweet']['created_at'] + '</td>\n')
  html_file.write('    <td>' + tweet['tweet']['full_text'] + '</td>\n')
  html_file.write('    <td style="width:250px">')
  
  # if there's a photo/image, inject a URL to it
  if 'media' in tweet['tweet']['entities']:
    html_file.write('<img src="')

    #get the media filename and concatenate the id_str into it, and prepend it all with the base URL where the images are hosted.
    html_file.write(base_media_url + id_str + '-' + tweet['tweet']['entities']['media'][0]['media_url'].rpartition('/')[-1])
    html_file.write('" style="max-width:100%">')

  html_file.write('</td>\n')

  html_file.write('    <td>' + id_str + '</td>\n')
  html_file.write('  </tr>\n')

html_file.write('</table>')
html_file.write('</html>')
html_file.close()
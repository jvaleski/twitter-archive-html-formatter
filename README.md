# twitter-archive-html-formatter
takes a twitter archive and creates a simple html file out of it so you can host it yourself.
1. request a full twitter archive from twitter
2. pull it down and extract it somewhere
3. upload/copy the data/tweet_media folder to a web server somewhere
4. point the base_media_url varible in the py script to the http addr of the location in step 3
5. format the tweet.js file that came in the archive so it's properly formatted JSON (just delete the top variable bit and turn the outermost square brackets to curly braces); you don't have to mess with any other structure.
6. run the py script
7. upload/copy the resulting tweets.html file to a web server somewhere 

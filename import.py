import json
from datetime import datetime

from bs4 import BeautifulSoup
import html2text
import codecs

# open the posts file
with open('./input/posts.json') as posts_file:
    
    # convert post index json to python dictionary
    posts_data = json.load(posts_file)
    
    # loop through all posts
    for post in posts_data['posts']:
        selected_post = post['post']
        
        # DEBUG: limit to one post for image testing
        #if selected_post['slug'] == 'scaled-image-test':

        # translate to Hugo metadata
        # preposterous post properties:
        # * date
        # * url
        # * title
        # * slug
        # * author

        output = '---\n'
        # TODO: If the title contains a ', it breaks the Markdown parser: fix this.
        output = output + 'title: \'' + selected_post['title'] + '\'\n'
        date_string = selected_post['date'].split('-')[0][:-1]
        date = datetime.strptime(date_string,'%a, %d %b %Y %H:%M:%S') 
        output = output + 'date: \'' + date.isoformat() + '\'\n'
        output = output + 'author: ' + selected_post['author'] + '\n'
        output = output + 'draft: false\n'
        output = output + 'tags:\n'
        output = output + '  - preposterous\n'
        output = output + '---\n'

        # load refereneced HTML file
        post_html_filename = './input/' + selected_post['url'].split('/')[-1]

        # parse HTML into python object
        with open(post_html_filename) as post_html_data:

            print(f"processing {post_html_filename}")

            post_html = BeautifulSoup(post_html_data,"lxml")

            # identify and copy images 
            image_tags = post_html.findAll('img')
            for image_tag in image_tags:
                #image_tag['src'] = '/preposterous/' + image_tag['src']
                image_tag['src'] = '/' + image_tag['src']


            # TODO: handle other assets (video, audio, etc.)

            # reformat as markdown
            html = post_html.find('article').prettify()

            markdown = html2text.html2text(html)

            output = output + markdown

            print('---output-----------------------------------------')
            print(output)
            print('--------------------------------------------------')

            # write the result to a properly-named file
            file = codecs.open('./output/' + selected_post['slug'] + '.md', 'w', encoding='utf8')
            file.write(output)
            file.close()

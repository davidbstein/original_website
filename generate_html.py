"""
This is a simple file that takes in an image as an argument, and maps
regions to links. For use in generating david stein's website

Copyright (C) 2011 by David Stein

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

@author: stein
"""
from get_polygon import *
import sys

#regions are (title, image, alt, maplinks). all images are 900x700
generic_html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html
xmlns="http://www.w3.org/1999/xhtml"> 

<!-- know what's pretty cool? this is just a folder in my
dropbox. took like 20 minutes to set up, and now I can update and
manage my site anywhere! even the apache configuration is there! 

This website was autogenerated using generate_html.py and some drawing made in microsoft paint. Source is available if you want it.-->

<head>
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
 <title>%s</title> 
</head>

<body>  

<div align="center">

<img src="%s" alt="this website requires images. text only interface
under construction." width="900" height="700" align="middle" usemap =
#indexmap border = 0/> 

<map name=indexmap> 
%s 
</map> </div> </body>

</html>
'''
#regions are (comma seporated indecies, target foler)
area_map = '<area shape="poly" coords = "%s" href="%s" />'

root = '/home/stein/Dropbox/www/'
http_root = 'http://stein.mit.edu/'

def generate_area(coords, folder):
    return area_map%(str(coords)[1:-1], folder), '\n'

def generate_html(name):
    r = root
    hr = http_root
    if name != 'index':
        r += name + '/'
        hr += name + '/'
    #regions are (title, image, maplinks). all images are 900x700
    title = "David Stein's Webpage:) - %s "%name
    image = hr + 'image.png'
    local_image = r + 'image.png'
    maplinks = ''
    print '\n\n\n====================\nCurrent file: %s\n'%(hr)
    while 'y' == raw_input('do you have any links to add?(y/N)'):
        target = raw_input('please put the folder name, or put "index" or "file": ')
        link = http_root
        if target == 'index':
            pass
        elif target == 'file':
            link = raw_input('please enter the file name or external link: ')
        else:
            link += target
        coords = get_polygon(local_image)
        maplinks += generate_area(coords, link)
    outfile = str(r + 'index.html')
    with file(outfile, 'w') as f:
        print title
        print image
        print maplinks
        print 'writing to : %s'%outfile
        f.write(generic_html%(title,image,maplinks))

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        generate_html(arg)
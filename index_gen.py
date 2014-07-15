#!/usr/bin/env python

#
# index_gen.py
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
#
# Project's home page: 
# https://pythonadventures.wordpress.com/2011/03/26/static-html-filelist-generator/
#
# Version: 0.1 
# Date:    2011-03-26 (yyyy-mm-dd)
#
# This free software is copyleft licensed under the same terms as Python, or,
# at your option, under version 2 of the GPL license.
#

import os
import os.path
import sys

class SimpleHtmlFilelistGenerator:
    # start from this directory
    base_dir = None
    
    def __init__(self, dir):
        self.base_dir = dir
        
    def print_html_header(self):
        print """<html>
<body>
<code>
""",
    
    def print_html_footer(self):
        #home = 'https://pythonadventures.wordpress.com/2011/03/26/static-html-filelist-generator/'
        #name = 'Static HTML Filelist Generator'
        print '</code>'
        #href = "<a href=\"%s\">%s</a>" % (home, name)
        #print "<p><i><sub>This page was generated with Jabba Laci's %s.</sub></p>" % href
        print """</body>
</html>
""",

    def processDirectory ( self, args, dirname, filenames ):
        print '<strong>', dirname + '/', '</strong>', '<br>'
        for filename in sorted(filenames):
            rel_path = os.path.join(dirname, filename)
            if rel_path in [sys.argv[0], './index.html']:
                continue   # exclude this generator script and the generated index.html
            if os.path.isfile(rel_path):
                href = "<a href=\"%s\">%s</a>" % (rel_path, filename)
                print '&nbsp;' * 4, href, '<br>'

    def start(self):
        self.print_html_header()
        os.path.walk( self.base_dir, self.processDirectory, None )
        self.print_html_footer()
            
# class SimpleHtmlFilelistGenerator

if __name__ == "__main__":
    base_dir = '.'
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    gen = SimpleHtmlFilelistGenerator(base_dir)
    gen.start()

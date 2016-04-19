from os.path import join
from glob import glob
HTML_DIR = join('html-conversions', 'multi-page', 'when-nerds-and-words-collide')

for htmlname in glob(join(HTML_DIR, '*.html')):
    print(htmlname)

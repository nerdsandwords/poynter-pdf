from glob import glob
from os.path import join, basename
from os import makedirs
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString
CLEANED_DIR = join('cleaned', 'multi-page', 'html')
HTML_DIR = join('html-conversions', 'multi-page', 'when-nerds-and-words-collide')



def wrap_element(old_el, new_el):
    new_el.append(old_el)
    return new_el


def convert_span_tag(stag, soup):
# span tags are always single-child text NavigableStrings
    styles = stag.attrs.get('style')
    ctag = next(stag.children)
    if styles:
        for style in styles.split(';'):
            if 'italic' in style:
                ctag = wrap_element(ctag, soup.new_tag('em'))
            elif 'bold' in style:
                ctag = wrap_element(ctag, soup.new_tag('strong'))
    stag.replace_with(ctag)




if __name__ == '__main__':
    makedirs(CLEANED_DIR, exist_ok=True)
    filenames = glob(join(HTML_DIR, '*.html'))

    for fn in filenames:
        with open(fn, encoding='UTF-8-SIG') as rf:
            soup = BeautifulSoup(rf.read(), 'lxml')
            body = soup.find('body')
        # clean paragraph text
        for ptag in body.find_all('p'):
            for spantag in ptag.find_all('span'):
                convert_span_tag(spantag, soup)

        # clean headlines
        for hed in body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            for spantag in hed.find_all('span'):
                spantag.unwrap()
            a = hed.find('a')
            if a and a.attrs.get('name'):
                hed.attrs['id'] = a['name']
                a.unwrap()

        # remove brs
        for br in body.find_all('br'):
            br.unwrap()

        # remove divs
        for div in body.find_all('div'):
            if len(list(div.children)) < 1:
                div.unwrap()


        cname = join(CLEANED_DIR, basename(fn))
        with open(cname, 'w') as wf:
            wf.write(body.prettify())

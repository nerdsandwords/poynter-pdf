>  If newspapers are going to maintain their "watchdog-of-the-government role", they are going to eventually have to have access to electronic data as well as paper data.
>  
>  That day has come.

- Larry Sanders, computer-assisted reporting editor at _USA Today_, in 1991.



# Freeing "When Nerds and Words Collide" from its PDF prison

_**When Nerds and Words Collide**: Reflections on the Development of Computer Assisted Reporting_ (1999) was published by [The Poynter Institute](http://www.poynter.org) more than 15 years ago. But the 59-page manual contains timeless wisdom about the work of investigative and computational journalism. 

So what better tribute to give this manual than to set it free from its paper tomb and elevate it to a new, heavenly body among the cloud servers with  integrated, multi-platform-functionality!

<a href="https://www.documentcloud.org/documents/757701"><img src="doccloud-page-previews.png" alt="As previewed on DocumentCloud"></a>


[Investigative Reporters & Editors](http://ire.org/) has since made *When Nerds and Words Collide* [free to download as a scanned PDF on its website](http://store.ire.org/products/when-nerds-and-words-collide-reflections-on-the-development-of-computer-assisted-reporting). This repo is just an attempt to translate it into more shareable HTML.

From [the introduction](https://www.documentcloud.org/documents/757701#document/p8):

> In this collection you will find their definitions of CAR, reminiscences of their discovery of CAR, recollections of favorite “How I got ’em” CAR stories, and hard-earned advice to beginners and seasoned journalists venturing into the use of these ways of reporting...
> 
> We hope these essays will give you a sense of where CAR has been, how it got to where it is, and what it needs to keep it going. We’d like you to join us in this effort to better understand and promote the techniques of computer assisted reporting into daily and project journalism.



If you're interested in just reading the manual, [DocumentCloud](https://www.documentcloud.org/documents/757701) has a hosted, easy-to-read copy:

https://www.documentcloud.org/documents/757701

# Status

This repo currently contains:

- [pdfs/when-nerds-and-words-collide--tesseract-ocr.pdf](pdfs/when-nerds-and-words-collide--tesseract-ocr.pdf) -- the scanned PDF with OCRed text via Tesseract, as processed and downloaded from [DocumentCloud](https://www.documentcloud.org/documents/757701).
- [pdfs/when-nerds-and-words-collide--abbyy-ocr.pdf](pdfs/when-nerds-and-words-collide--abbyy-ocr.pdf) -- the scanned PDF as processed and OCRed via ABBYY FineReader Pro for Mac.
- [html-conversions/single-page/when-nerds-and-words-collide/](html-conversions/single-page/when-nerds-and-words-collide/) - The result of using FineReader Pro to convert the PDF to a __single-page__ HTML file, including a separate folder for all of the external media assets.
- [html-conversions/multi-page/when-nerds-and-words-collide/](html-conversions/multi-page/when-nerds-and-words-collide/) - The result of using FineReader Pro to convert the PDF to HTML, but with _each page_ converted into its own HTML file and assets folder.


I think the best approach is to do a quick HTML text extraction on the __multi-page__ conversion, creating a separate text file for each page. People can then make quick fixes to the main body text. And then everything can be glued together, albeit manually (it's only 59 pages).

Feel free to fork/clone this repo. Or suggest [something in the issues](https://github.com/nerdsandwords/poynter-pdf/issues).

## Tentative draft steps

- [ ] Extract plaintext from the body paragraph elements from every article page in the [multi-page HTML directory](html-conversions/multi-page/when-nerds-and-words-collide/)
- [ ] Goad people into doing the manual translation work.
- [ ] ???
- [ ] Prophet

# Special thanks

Send thanks to the [Poynter Institute](http://www.poynter.org/) and [IRE](http://ire.org/) for publishing this manual and making it free to download for future generations of journalists.

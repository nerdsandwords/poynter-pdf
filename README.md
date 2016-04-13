
# Digitizing the CAR manual, "When Nerds and Words Collide"

_**When Nerds and Words Collide**: Reflections on the Development of Computer Assisted Reporting_ (1999) was published by [The Poynter Institute](http://www.poynter.org) more than 15 years ago. But the 59-page manual contains timeless wisdom about the work of investigative and computational journalism.

[Investigative Reporters & Editors](http://ire.org/) has since made *When Nerds and Words Collide* [free to download as a scanned PDF on its website](http://store.ire.org/products/when-nerds-and-words-collide-reflections-on-the-development-of-computer-assisted-reporting). This repo is just an attempt to translate it into more shareable HTML.




# Status

This repo currently contains:

- [pdfs/when-nerds-and-words-collide--tesseract-ocr.pdf] -- the scanned PDF with OCRed text via Tesseract, as processed and downloaded from [DocumentCloud](https://www.documentcloud.org/documents/757701).
- [pdfs/when-nerds-and-words-collide--abbyy-ocr.pdf] -- the scanned PDF as processed and OCRed via ABBYY FineReader Pro for Mac.
- [html-conversions/single-page/when-nerds-and-words-collide/] - The result of using FineReader Pro to convert the PDF to a __single-page__ HTML file, including a separate folder for all of the external media assets.
- [html-conversions/multi-page/when-nerds-and-words-collide/] - The result of using FineReader Pro to convert the PDF to HTML, but with _each page_ converted into its own HTML file and assets folder.


I think the best approach is to do a quick HTML text extraction on the __multi-page__ conversion, creating a separate text file for each page. People can then make quick fixes to the main body text. And then everything can be glued together, albeit manually (it's only 59 pages).

Feel free to fork/clone this repo. Or suggest [something in the issues](https://github.com/nerdsandwords/poynter-pdf/issues).

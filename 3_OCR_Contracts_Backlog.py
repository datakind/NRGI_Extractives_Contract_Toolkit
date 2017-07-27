# # Omidyar Extractives Project 1
# ## OCR Contracts Backlog (Notebook 3 of 8)
# ### From directory of PDFs, performs OCR and outputs txt files to same directory

import io, os
import json
import unicodedata
from PIL import Image as PI
import pyocr
import pyocr.builders
from wand.image import Image
from tqdm import tqdm

# Where you want to save the PDFspip 
destination_folder = 'contract_data/Contracts_Backlog/'
tempdir = "/private/var/tmp/"

pdfs = [unicodedata.normalize('NFKC',f.decode('utf8')) for f in os.listdir(destination_folder) if f.lower().endswith('.pdf')]
txt_files = [unicodedata.normalize('NFKC',f.decode('utf8')) for f in os.listdir(destination_folder) if f.lower().endswith('.txt')]


# ### Perform OCR on PDFs
def ocr_pdf_to_text(filename):
    tool = pyocr.get_available_tools()[0]
    lang = 'spa'
    req_image = []
    final_text = []
    image_pdf = Image(filename=filename, resolution=300)
    image_jpeg = image_pdf.convert('jpeg')
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))

    for img in req_image: 
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)
    return final_text



for filename in tqdm(pdfs):

    txt_file = filename[:-3] +'txt'
    txt_filename = destination_folder + txt_file
    if not txt_file in txt_files: 

        print 'Converting ' + filename 

        try:

            ocr_txt = ocr_pdf_to_text(destination_folder + filename)
            with open(txt_filename,'w') as f:
                for i in range(len(ocr_txt)):
                    f.write(json.dumps({i:ocr_txt[i].encode('utf8')}))
                    f.write('\n')
            f.close()

        except:
            print "Could not OCR " + filename

        files = os.listdir(tempdir)
        for file in files:
            if "magick" in file:
                os.remove(os.path.join(tempdir,file))
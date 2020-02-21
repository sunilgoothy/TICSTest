# Reference: https://thejoeblankenship.com/blogs/concept_code/concept_code_p1.html

# import library
import pdfx

# import MongoClient from the PyMongo library, datetime, and pprint
from pymongo import MongoClient
import datetime
import pprint


# if you have already created a database or need to create a new database
client = MongoClient()
db = client.pdf_database

def store_pdf():

    # create a pdf object for a single file
    pdf = pdfx.PDFx("STC.pdf")

    # extract the metadata from the pdf object
    metadata = pdf.get_metadata()
    # print("METADATA==> ", metadata)

    # extract the references from the pdf
    # create a python dictionary of the references

    reference_dict = pdf.get_references_as_dict()
    # print("references==> ", reference_dict)

    # later if you wanted to crawl from this PDF via its references
    # it can download PDFs from reference hyperlinks

    # pdf.download_pdfs("temp_down_folder/")

    # extract the text from the PDF
    # replace the return characters with nothing creating one long string
    # split the string at the form feed characters
    text = pdf.get_text()
    text_to_mongo = text.replace('\n', '').split("\x0c")
    # print("PDFTEXT==> ", text_to_mongo)

    # insert documents (stored as dictionaries in BSON (JSON) format (UTF-8))
    # notice we can create the schema we want ad-hoc for our document
    post = {
        "metadata": metadata,
        "text": text_to_mongo,
        "references": reference_dict,
        "import_date": datetime.datetime.utcnow(),
        "tags": "pdf"
    }

    # create an object for your PDF data, then insert it into the database
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id

    # now check the output for your new MongoDB document
    pprint.pprint(posts.find_one())  # search with dict keys or "_id" for Mongo UID


def find_all_pdf():
    # create an object for your PDF data, then insert it into the database
    posts = db.posts

    # get all posts
    rs_posts = posts.find()
    for post in rs_posts:
        pprint.pprint(post.get('metadata', None))

def find_pdf():
    # create an object for your PDF data, then insert it into the database
    posts = db.posts

    rs = posts.find_one({'tags': 'pdf'})   # search with dict keys or "_id" for Mongo UID
    pprint.pprint(rs['metadata'])  

if __name__ == '__main__':
    # store_pdf()
    # find_all_pdf()
    find_pdf()
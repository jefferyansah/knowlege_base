from abbreviations import schwartz_hearst
import PyPDF2
import textract
import pandas as pd



#open the pdf object
pdf_obj = open('trial.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_obj)

accro_dict = {}
for (page_number)in range(pdf_reader.numPages):
    page_obj = pdf_reader.getPage(page_number)
    text = page_obj.extractText()
    pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text= text, most_common_definition=True)
    accro_dict.update(pairs)
    print(accro_dict)

df =pd.DataFrame()
df['ACRONYM'] = accro_dict.keys()
df['MEANING'] = accro_dict.values() 
df.to_csv('example.csv', index =False)   #break


# By default, the most recently encountered definition for each term is returned
#pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text= text)


# pairs = schwartz_hearst.extract_abbreviation_definition_pairs(file_path='<path_to_file>')

# # If multiple definitions are encountered for each term, you might want to return the most common for each
# pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text='...', most_common_definition=True)

# # ... or you might want to return the first encountered definition for each
# pairs = schwartz_hearst.extract_abbreviation_definition_pairs(doc_text='...', first_definition=True)
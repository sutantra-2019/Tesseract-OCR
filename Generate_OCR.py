import os

non_ocr_file = input("\nEnter file name that you want to Convert to Searchable Format    : ")
non_ocr_key = "non_ocr_documents/" + non_ocr_file

getObj = 'aws s3 cp s3://ocrmydocuments/' + non_ocr_key + ' ./' + non_ocr_file
os.system(getObj)

searchableFile = non_ocr_file.split(".")[0] + "_Searchable.pdf"
ocrCmd = 'ocrmypdf ' + non_ocr_file + ' ' + searchableFile
os.system(ocrCmd)

putObj = 'aws s3 cp ' + searchableFile + ' ' + 's3://ocrmydocuments/ocr_documents/' + searchableFile
os.system(putObj)

rmCmd = 'rm -fR ' +  non_ocr_file + ' ' + searchableFile
os.system(rmCmd)
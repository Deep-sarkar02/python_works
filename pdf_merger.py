# This can take more then 2 pdf files to merge
# import following library
import PyPDF2
pdf_1 = input("Enter the name of  1st pdf:-")
pdf_2 = input("Enter the name of  2nd pdf:-")
# take the pdf file in form of list
pdffiles = [pdf_1,pdf_2]
# keep the function form of variable
merger = PyPDF2.PdfMerger()
# iterate each pdf file and open them in rb mode
for filename in pdffiles:
  pdfFile = open(filename,"rb")
  pdfReader = PyPDF2.PdfReader(pdfFile)# read the pdf file
  merger.append(pdfReader)# after reading the pdf files append the files in form of list in the merger
pdfFile.close()
merger.write("merged.pdf")
print("Thank you for using pdf merger the resultant file will be stored in the parent location")



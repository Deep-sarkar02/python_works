# pdf to text convertor and pdf reader:-
import win32com.client
import PyPDF2
# configure the speaker:-
speaker = win32com.client.Dispatch("SAPI.spVoice")
print("...............welcome to pdf to txt convertor and speaker.................")
print("please dont upload any kind of photo-pdfs")
pdf = input("Enter the name of pdf:-")
# read the pdf
reader=PyPDF2.PdfReader(pdf)
print("\ndisplaying data.......................")
# read the length of the pdf file and then iterate over the length
for page in range(len(reader.pages)):
    p = reader.pages[page]
    text=p.extract_text()# extract the text from the pdf
    print("\n")
    print(f"..............Pg.no:-{page+1}...............")
    print("\n")
    print(text)
    speaker.Speak(text)
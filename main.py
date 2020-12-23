import pyttsx3
import PyPDF2

# for opening pdf
book = open('Class 11 - India Physical Environment.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages

# setting up engine to speak
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

# engine reading pdf
for num in range(9, pages):
 page = pdf_reader.getPage(num)
 text = page.extractText()
 speaker.say(text)
# this will  wait after saying text
 speaker.runAndWait()


import textract
text = textract.process('GradeCard.pdf', method='pdfminer')
print(text)

# copy paste the output to a.txt file
# then run cgpa.py file
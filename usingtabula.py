from tabula import read_pdf
df= read_pdf("/home/mayank/tensorFlowFiles/PythonTesseract/pythonOcrImageToText/A004258.pdf" ,output_format="json")
df
print(df)

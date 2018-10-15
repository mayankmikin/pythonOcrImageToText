with open("/home/mayank/tensorFlowFiles/PythonTesseract/pythonOcrImageToText/testfile.txt") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)
        else:
            print()
            

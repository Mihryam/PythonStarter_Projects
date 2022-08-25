#importing EANI3 a standard barcode type from barcode
import barcode
from barcode import EAN13

#ImageWriter is used to generate our barcode in any format
#Barcode is an image, if we dont import image writer, our barcode will be in savg format
from barcode.writer import ImageWriter

#Requesting user input on no of barcodes to be generated
UserPrompt = int(input("Hey There!!\nHow Many Barcodes do you wish to generate:\n"))

#defining a number variable for looping through the range of no of requested amount of barcodes
Number = range(UserPrompt)

#Calling the for loop
for i in Number:
    #requesting for barcode id
    CodeId = input("Kindly enter 12 DIGIT barcode id:\n")
    BarCode = EAN13(CodeId, writer =ImageWriter)
    CodeName = input("Please give a name to save your code:\n")
    BarCode.save(CodeName)
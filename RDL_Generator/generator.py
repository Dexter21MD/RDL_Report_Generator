
from lxml import etree
#C:\Users\Dexter\Desktop\pythonerinho\RDL Report Generator\templates\test.txt
#"C:\\Users\\Dexter\\Desktop\\pythonerinho\\RDL Report Generator\\templates\\Template.rdl"

#Load the .rdl file
file_binary = open("C:\\Users\\Dexter\\Desktop\\pythonerinho\\RDL Report Generator\\templates\\Template.rdl", "rb")
#new_parser = etree.XMLParser(remove_blank_text=True) 
root = etree.parse(file_binary)


elements = root.xpath("//*")
for element in elements:
        if element.tag == "DataSources":
            print(element.tag)




file_binary.close()





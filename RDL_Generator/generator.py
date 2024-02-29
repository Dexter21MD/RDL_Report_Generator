
from lxml import etree
from rdl_tree_manipulation import Rdl_Tree_Manipulation


# C:\Users\Dexter\Desktop\pythonerinho\RDL Report Generator\templates\test.txt
# "C:\\Users\\Dexter\\Desktop\\pythonerinho\\RDL Report Generator\\templates\\Template.rdl"

# open the .rdl file

namespaces = {
    'default': 'http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition',
    'rd': 'http://schemas.microsoft.com/SQLServer/reporting/reportdesigner',
    'df': 'http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition/defaultfontfamily'
}

file_binary = open(
    "C:\\Users\\Dexter\\Desktop\\pythonerinho\\RDL Report Generator\\templates\\Template.rdl", "rb")

tree = etree.parse(file_binary)


x = Rdl_Tree_Manipulation(tree)

without_namespaces_tree = x.get_rid_of_namespaces()

# prints element's path to the console
for element in without_namespaces_tree.iter():
    print(tree.getpath(element))


file_binary.close()

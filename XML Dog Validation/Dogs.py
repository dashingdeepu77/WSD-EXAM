from lxml import etree

xml_file="./Dogs.xml"
xsd_file="./Dogs.xsd"
xsl_file="./Dogs.xsl"

xml_tree=etree.parse(xml_file)
xsd_tree=etree.parse(xsd_file)
xsl_transform=etree.XSLT(etree.parse(xsl_file))

html_transform=xsl_transform(xml_tree)

with open("output.html","wb") as output_file:
    output_file.write(etree.tostring(html_transform,pretty_print=True))

schema=etree.XMLSchema(xsd_tree)
is_valid=schema.validate(xml_tree)

if is_valid:
    print("VALID")
else:
    print("no")
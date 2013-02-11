from xml.dom import minidom

doc = minidom.Document()
root = doc.createElement('root')
doc.appendChild(root)
main = doc.createElement('Text')
root.appendChild(main)

text = doc.createTextNode('Some text here')
main.appendChild(text)
f = open('test.xml', 'a')
root.writexml(f)
f.close()
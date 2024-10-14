import json
from docxtpl import DocxTemplate

# Open and read the JSON file
with open('./output/Muzammil-bloodgroup.json', 'r') as file:
    data = json.load(file)
    file.close()

doc = DocxTemplate("./doc-templates/bloodgroup-template.docx") # template
print(doc)
doc.render(data) # Render the data into the document
doc.save(f"./output/{data['person_name']}-bloodgroup.docx") # Save document
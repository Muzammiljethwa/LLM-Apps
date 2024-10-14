from langchain_core.prompts import ChatPromptTemplate

from config.congif_ai import llm
from src.doc_parsers import CV, BloodInfoCard, UniCard
from pprint import pprint

import json 
from docxtpl import DocxTemplate

DOC_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", """
                    You are provided the baseModel for Structure Output.
                    Read the provided input information carefully and structure the output according to the given structure.
                    If the provided information does not have any data required in structure output, keep that feild empty.
                    Remember to keep data as it is, don't add custom lines into it
                    """),
        ("human", "{input}")
    ]
)

doc_chain = DOC_TEMPLATE | llm.with_structured_output(BloodInfoCard)
response = doc_chain.invoke({
                            "input": """My name is Muzammil.
                            I am a student of UBIT, where as my GPA is 3.12 and my address is gulshan e iqbal, 
                            My blood group is AB+, cnic is 778899. my experince is in AI, ML and Data Science.
                            """
                        })
dict_response = dict(response)
pprint(dict_response)

# Convert and write JSON object to file
with open(f"./output/{dict_response['person_name']}-bloodgroup.json", "w") as outfile: 
    json.dump(dict(response), outfile)
    outfile.close()

doc = DocxTemplate("./doc-templates/bloodgroup-template.docx") # template
doc.render(dict_response) # Render the data into the document
doc.save(f"./output/{dict_response['person_name']}-bloodgroup.docx") # Save document
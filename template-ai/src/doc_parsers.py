# from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field
from typing import List, Optional

# Pydantic
class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: Optional[int] = Field(
        default=None, description="How funny the joke is, from 1 to 10"
    )

class CV(BaseModel):
    """CV parser"""

    person_name: str = Field(description="Name of the person")
    person_cnic: str = Field(description="CNIC card information of the person")
    person_gpa: Optional[float] = Field(default=None, description="CGPA he got in university")
    person_experiences: List[str] = Field(description="Experiences regarding to the past comapnies he has worked in")
    person_address: str = Field(description="address of his home")

class BloodInfoCard(BaseModel):
    """Blood Group parser"""


    person_name  : str = Field(description="Name of the person")
    person_cnic : str = Field(description="CNIC card information of the person")
    person_bloodgroup : str = Field(description="Blooad Group of that person")
    person_address : str = Field(description="address of his home")

class UniCard(BaseModel):
    """Uni Card"""

    person_name: str = Field(description="Name of the person")
    person_cnic: str = Field(description="CNIC card information of the person")
    person_address: str = Field(description="address of his home")
    person_department: str = Field(description="Department or feild of study he is enrolled in")
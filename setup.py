from setuptools import setup,find_packages
from typing import List

hyphen_e_dot='-e .'



def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","")for i in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements    


setup(
    name="ML Project",
    version="1.0.0",
    description="A sample Python package",
    author="Divya Ampabattuni",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


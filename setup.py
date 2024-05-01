from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] #/n will come as default as in requirements.txt. so replace it

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
setup (                    #creating package
name='mlproject',
version='0.0.1',
author='Akmal',
author_email='akmalvk6@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') #add all the requirement libraries we want

)
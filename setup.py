from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path,"r") as f:
        requirements = f.readlines()
        requirements = [i.replace("\n","") for i in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

    pass


setup(
name = "mini-1",
version="0.0.1",
author="ts0713",
author_email="tsp.0713@gmail.com",
packages=find_packages(),
#install_requires = ['pandas','numpy','scikit-learn','seaborn','scipy','matplotlib','plotly']
install_requires = get_requirements("requirements.txt")


)
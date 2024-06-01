from setuptools import find_packages,setup
from typing import List

      
def get_requirements(file_path:str)->List[str]:
      """
      This function will return teh list of requirements file
      """
      requirements = []
      with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements = [req.replace('\n',"") for req in requirements]
      return requirements



setup(
      name="mlprojel",
      version="0.0.1",
      author='Saiful',
      author_email="saifulislam003244@gmail.com",
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt')


)
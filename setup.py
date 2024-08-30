from setuptools import setup, find_packages

   setup(
       name="serial_proxy",
       version="0.1.0",
       packages=find_packages(),
       install_requires=[
           "pyserial>=3.5",
       ],
       author="Harper Reed",
       author_email="harper@modest.com",
       description="A proxy for serial communication with logging capabilities",
       long_description=open("README.md").read(),
       long_description_content_type="text/markdown",
       url="https://github.com/harperreed/serial_proxy",
       classifiers=[
           "Programming Language :: Python :: 3",
           "License :: OSI Approved :: MIT License",
           "Operating System :: OS Independent",
       ],
   )

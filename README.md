# Military Vehichle Identifier
This application is for the purposes of inputting jpg images into the program, where the software will output whether the image is a tank, plane, or helicopter

## Installation
```bash
pip install numpy
python -m pip install tensorflow[and-cuda]
pip install tensorflow
pip install PyQt5
pip install matplotlib
pip install pandas
pip install -U scikit-learn
```

## Usage
After installing necessary libraries, users can run the main file via a visual studios code editor and follow the prompts within the terminal. Creating a model on another local
machine is not recommended as the file path is hard coded to a specific directory in the CreateModel.py file. Rather, one will input `n` when 
prompted and the user interface of the program will pop up. There once you click browse, you are able to navigate through any file path of your
choosing and input any jpg images. This can be done repetitively. 

## Files
CreateModel.py - Creates a model based on a given dataset of images within a specific directory 
Interpreter.py - Takes in an input of a jpg file and is run by the model
main.py - Allows the user to choose to create a model, and then a user interface
ui.py - Calls the interpreter to be used in the ui, thus the user is able to connected to the interpreter in this way

## Contact
schusterclsol@gmail.com

from CreateModel import *
from Interpreter import *
from ui import *

#from ui import *

def main():
    prompt = input("Create a new dataset? This will take some time. y/n ")
    if (prompt.lower() == 'y'):
        x = CreateModel()
        datasetName = input("Name the dataset: ")
        x.create_model(2, 3, datasetName)
    else:
        app = QApplication(sys.argv)
        gui = Template()
        gui.show()
        sys.exit(app.exec_())


main()    
    


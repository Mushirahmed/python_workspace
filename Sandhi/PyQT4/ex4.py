import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Alert')
        self.show()
    
    def closeEvent(self,event):
        
        reply = QtGui.QMessageBox.question(self,'          Alert', "Do You Want To Quit?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
def main():    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
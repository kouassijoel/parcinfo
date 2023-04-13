import sys
from PySide2 import QtCore, QtGui, QtWidgets

class BlocNotes(QtWidgets.QMainWindow):
	"""Creation d'une application bloc note"""
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setWindowTitle("Bloc-Notes")
		self.__zoneTexte = QtWidgets.QTextEdit()
		self.setCentralWidget(self.__zoneTexte)
		# Les Actiions de notre classe
		self.__actionNew = QtWidgets.QAction(QtGui.QIcon("document-new.png"), "Nouveau",
											self)
		self.__actionNew.setShortcuts(QtGui.QKeySequence.New)
		self.__actionNew.setStatusTip("Nouveau document")
		
		self.__actionOpen = QtWidgets.QAction(QtGui.QIcon("document-open.png"), "Ouvrir", self)
		self.__actionOpen.setShortcuts(QtGui.QKeySequence.Open)
		self.__actionOpen.setStatusTip("Ouvrir un document existant")
		
		self.__actionSave = QtWidgets.QAction(QtGui.QIcon("document-save.png"), "Enregistrer", self)
		self.__actionSave.setShortcuts(QtGui.QKeySequence.Save)
		self.__actionSave.setStatusTip("Enregistrez le document")
		
		self.__actionSaveAs = QtWidgets.QAction(QtGui.QIcon("document-save-as.png"),
															"Enregistrer sous", self)
		self.__actionSaveAs.setShortcuts(QtGui.QKeySequence.SaveAs)
		self.__actionSaveAs.setStatusTip("Enregistrer le document-sous")
		
		self.__actionQuit = QtWidgets.QAction(QtGui.QIcon("exit.png"), "Quitter",
											   self)
		self.__actionQuit.setShortcuts(QtGui.QKeySequence.Quit)
		self.__actionQuit.setStatusTip("Quitter l'application")
		
		self.__actionUndo = QtWidgets.QAction(QtGui.QIcon("undo.png"), "Annuler",
											  self)
		self.__actionUndo.setShortcuts(QtGui.QKeySequence.Undo)
		self.__actionUndo.setStatusTip("Annuler la dernier operation")
		
		self.__actionRedo = QtWidgets.QAction(QtGui.QIcon("redo.png"), "Refaire",
											  self)
		self.__actionRedo.setShortcuts(QtGui.QKeySequence.Redo)
		self.__actionRedo.setStatusTip("Refaire la derniere opreartion")
		
		
		self.__actionCut = QtWidgets.QAction(QtGui.QIcon("edit-cut.png"), "Couper",
											  self)
		self.__actionCut.setShortcuts(QtGui.QKeySequence.Cut)
		self.__actionCut.setStatusTip("Couper le texte vers la presse-papier")
		
		
		self.__actionCopy = QtWidgets.QAction(QtGui.QIcon("edit-copy.png"), "Copier",
											  self)
		self.__actionCopy.setShortcuts(QtGui.QKeySequence.Copy)
		self.__actionCopy.setStatusTip("Copier le texte vers la presse-papier")
		
		self.__actionPaste = QtWidgets.QAction(QtGui.QIcon("edit-paste.png"), "Coller",
											  self)
		self.__actionPaste.setShortcuts(QtGui.QKeySequence.Paste)
		self.__actionPaste.setStatusTip("Coller le texte depuis la presse-papier")
		
		# Associations des actions au methode
		self.__actionNew.triggered.connect(self.newDocument)
		self.__actionOpen.triggered.connect(self.openDocument)
		self.__actionSave.triggered.connect(self.saveDocument)
		self.__actionSaveAs.triggered.connect(self.saveAsDocument)
		self.__actionQuit.triggered.connect(self.quit)
		self.__actionUndo.triggered.connect(self.undo)
		self.__actionRedo.triggered.connect(self.redo)
		self.__actionCut.triggered.connect(self.cut)
		self.__actionCopy.triggered.connect(self.copy)
		self.__actionPaste.triggered.connect(self.paste)
		
		self.__menuFile = self.menuBar().addMenu("Fichier")
		self.__menuFile.addAction(self.__actionNew)
		self.__menuFile.addAction(self.__actionOpen)
		self.__menuFile.addAction(self.__actionSave)
		self.__menuFile.addAction(self.__actionSaveAs)
		self.__menuFile.addSeparator()
		self.__menuFile.addAction(self.__actionQuit)
		self.__menuEdit = self.menuBar().addMenu("Edition")
		self.__menuEdit.addAction(self.__actionUndo)
		self.__menuEdit.addAction(self.__actionRedo)
		self.__menuEdit.addAction(self.__actionCut)
		self.__menuEdit.addAction(self.__actionCopy)
		self.__menuEdit.addAction(self.__actionPaste)
		
		# Ajoute des action au menu de notre application
		self.__bareFile = self.addToolBar("Fichier")
		self.__bareFile.addAction(self.__actionNew)
		self.__bareFile.addAction(self.__actionOpen)
		self.__bareFile.addAction(self.__actionSave)
		self.__bareEdit = self.addToolBar("Edition")
		self.__bareEdit.addAction(self.__actionUndo)
		self.__bareEdit.addAction(self.__actionRedo)
		self.__bareEdit.addAction(self.__actionCut)
		self.__bareEdit.addAction(self.__actionCopy)
		self.__bareEdit.addAction(self.__actionPaste)
		self.show()
	def newDocument(self):
		pass
	def openDocument(self):
		pass
	def saveDocument(self):
		pass
	def saveAsDocument(self):
		pass
	def quit(self):
		pass
	def undo(self):
		pass
	def redo(self):
		pass
	def cut(self):
		pass
	def copy(self):
		pass
	def paste(self):
		pass
	
	
app = QtWidgets.QApplication(sys.argv)
fenetre = BlocNotes()
app.exec_()
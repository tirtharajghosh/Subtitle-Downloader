# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class About(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("About")
        Dialog.resize(320, 240)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lbl_title = QtWidgets.QLabel(Dialog)
        self.lbl_title.setGeometry(QtCore.QRect(70, 20, 161, 20))
        self.lbl_title.setObjectName("lbl_title")
        self.txt_aboutHtml = QtWidgets.QTextBrowser(Dialog)
        self.txt_aboutHtml.setGeometry(QtCore.QRect(30, 50, 256, 141))
        self.txt_aboutHtml.setObjectName("txt_aboutHtml")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("About", "About"))
        self.lbl_title.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Subtitle Downloader</span></p></body></html>"))
        self.txt_aboutHtml.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Version: 1.1.0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright © 2020 <a target='_blank' href=\"mailto:tirtharajghosh.ju@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Tirtharaj Ghosh</span></a> </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MIT Licence</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NO WARRANTY</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a target='_blank' href=\"https://github.com/tirtharajghosh/Subtitle-Downloader\"><span style=\" text-decoration: underline; color:#0000ff;\">Github Repository</span></a></p></body></html>"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subtitle-downloader.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import urllib
import zipfile
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

from AboutWindow import About

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Subtitle Downloader")
        MainWindow.resize(500, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 112))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.verticalLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.btn_selectFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_selectFile.setMaximumSize(QtCore.QSize(349, 16777215))
        self.btn_selectFile.setObjectName("btn_selectFile")
        self.btn_selectFile.clicked.connect(self.handleSelectFileDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_selectFile)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.cmb_selectLang = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmb_selectLang.setObjectName("cmb_selectLang")
        self.cmb_selectLang.addItem("")
        self.cmb_selectLang.addItem("")
        self.cmb_selectLang.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.cmb_selectLang)
        self.btn_search = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_search.setStyleSheet(" background-color: rgb(114, 159, 207)")
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.handleSearch)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.btn_search)
        self.txt_searchRes = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.txt_searchRes.setMaximumSize(QtCore.QSize(400, 16777215))
        self.txt_searchRes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_searchRes.setAutoFillBackground(False)
        self.txt_searchRes.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_searchRes.setWordWrap(False)
        self.txt_searchRes.setObjectName("txt_searchRes")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.txt_searchRes)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 160, 481, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 477, 127))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tbl_subtitles = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tbl_subtitles.setGeometry(QtCore.QRect(0, 0, 481, 131))
        self.tbl_subtitles.setMinimumSize(QtCore.QSize(481, 0))
        self.tbl_subtitles.setMouseTracking(False)
        self.tbl_subtitles.setStyleSheet("")
        self.tbl_subtitles.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tbl_subtitles.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_subtitles.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_subtitles.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_subtitles.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_subtitles.setObjectName("tbl_subtitles")
        self.tbl_subtitles.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tbl_subtitles.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tbl_subtitles.setHorizontalHeaderItem(1, item)
        self.tbl_subtitles.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_subtitles.horizontalHeader().setSortIndicatorShown(True)
        self.tbl_subtitles.horizontalHeader().setStretchLastSection(True)
        self.tbl_subtitles.clicked.connect(self.enableDownload)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(400, 300, 89, 25))
        self.btn_close.setObjectName("btn_close")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(200, 300, 89, 25))
        self.btn_refresh.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        self.btn_about.setGeometry(QtCore.QRect(10, 300, 89, 25))
        self.btn_about.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.btn_about.setObjectName("btn_about")
        self.btn_about.clicked.connect(self.handleAbout)
        self.txt_movieName = QtWidgets.QLabel(self.centralwidget)
        self.txt_movieName.setGeometry(QtCore.QRect(10, 130, 481, 20))
        self.txt_movieName.setObjectName("txt_movieName")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 300, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setDisabled(True)
        self.pushButton.clicked.connect(self.handleDownload)
        self.wbv_poster = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.wbv_poster.setGeometry(QtCore.QRect(410, 10, 82, 121))
        self.wbv_poster.setAutoFillBackground(False)
        self.wbv_poster.setUrl(QtCore.QUrl("https://dev.webircle.com/sd/index.html"))
        self.wbv_poster.setObjectName("wbv_poster")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Subtitle Downloader", "Subtitle Downloader"))
        self.btn_selectFile.setText(_translate("Subtitle Downloader", "Browse File"))
        self.cmb_selectLang.setItemText(0, _translate("Subtitle Downloader", "All Languages"))
        self.cmb_selectLang.setItemText(1, _translate("Subtitle Downloader", "English"))
        self.cmb_selectLang.setItemText(2, _translate("Subtitle Downloader", "French"))
        self.btn_search.setText(_translate("Subtitle Downloader", "Search"))
        self.txt_searchRes.setText(_translate("Subtitle Downloader", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.tbl_subtitles.setSortingEnabled(True)
        item = self.tbl_subtitles.horizontalHeaderItem(0)
        item.setText(_translate("Subtitle Downloader", "Language"))
        item = self.tbl_subtitles.horizontalHeaderItem(1)
        item.setText(_translate("Subtitle Downloader", "Subtitle"))
        __sortingEnabled = self.tbl_subtitles.isSortingEnabled()
        self.tbl_subtitles.setSortingEnabled(False)
        self.tbl_subtitles.setSortingEnabled(__sortingEnabled)
        self.btn_close.setText(_translate("Subtitle Downloader", "Close"))
        self.btn_refresh.setText(_translate("Subtitle Downloader", "Refresh"))
        self.btn_about.setText(_translate("Subtitle Downloader", "About"))
        self.txt_movieName.setText(_translate("Subtitle Downloader", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.pushButton.setText(_translate("Subtitle Downloader", "Download"))

    def handleSelectFileDialog(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'Open File', '.', 'Video files (*.mp4 *.mkv)')
        self.lineEdit.setText(os.path.basename(filename[0]))
    
    def handleSearch(self):
        self.getSubtitlesList(self.lineEdit.text(), self.cmb_selectLang.itemText(self.cmb_selectLang.currentIndex()))

    def getSubtitlesList(self, title: str, lang: str) -> bool:
        query = parsename(title,div='%20')
        self.movieTitle = title
        page = requests.get("https://subscene.com/subtitles/searchbytitle?query="+query)
        print(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        subd_found = list(filter(lambda x: x.get('href').startswith('/subtitles/'), soup.find_all('a')))

        if len(subd_found)==0:
            print("No match found :(")
            return False
        else:
            if len(subd_found)==1:
                print(1, " match found. :|")
                best_match = subd_found[0]
                other_match = None
            else:
                print(len(subd_found), " matches found. :)")
                best_match = subd_found[0]
                other_match = subd_found[1:]
            print("Best match: ", best_match.contents[0])
            self.txt_movieName.setText(best_match.contents[0])

            subtitles = requests.get("https://subscene.com"+best_match.get('href'))
            subt_content = BeautifulSoup(subtitles.content, 'html.parser')

            imgLink = list(filter(lambda x: x.get('src').startswith("https://i.jeded.com"), subt_content.find_all('img')))[0]
            self.wbv_poster.setUrl(QtCore.QUrl(imgLink.get('src')))

            if lang != "All Languages":
                subt_found = list(filter(lambda x: x.get('href').startswith(best_match.get('href')) and x.contents[1].get('class')[2] == 'positive-icon' and x.contents[1].contents[0].strip() == lang, subt_content.find_all('a')))
            else:
                subt_found = list(filter(lambda x: x.get('href').startswith(best_match.get('href')) and x.contents[1].get('class')[2] == 'positive-icon', subt_content.find_all('a')))
            print(len(subt_found), " subtitle(s) found :)")
            self.txt_searchRes.setText("<html><head/><body><p align=\"center\">Total "+str(len(subt_found))+" result(s) found.</p></body></html>")
            self.tbl_subtitles.setRowCount(len(subt_found))
            self.tbl_subtitles.setColumnCount(2)
            self.subtitlesList = subt_found
            for i,subt in enumerate(subt_found):
                item = QtWidgets.QTableWidgetItem()
                self.tbl_subtitles.setVerticalHeaderItem(i, item)
                itemv = self.tbl_subtitles.verticalHeaderItem(i)
                itemv.setText(str(i+1))
                self.tbl_subtitles.setItem(i, 0, QtWidgets.QTableWidgetItem('{:10.10}'.format(subt.contents[1].contents[0].strip())))
                self.tbl_subtitles.setItem(i, 1, QtWidgets.QTableWidgetItem(subt.contents[3].contents[0].strip()))
            return True  

    def enableDownload(self):
        self.pushButton.setDisabled(False)

    def handleDownload(self):
        index = self.tbl_subtitles.selectedIndexes()
        print(index[0].row())
        chsubt = index[0].row()
        subt_href = self.subtitlesList[chsubt].get('href')
        download_page = requests.get("https://subscene.com"+subt_href)
        download_content = BeautifulSoup(download_page.content, 'html.parser')
        download_link = download_content.find_all("a", id="downloadButton")
        return downloadSrt("https://subscene.com"+download_link[0].get('href'), parsename(self.movieTitle))

    def handleAbout(self):
        d = QtWidgets.QDialog()
        a = About()
        a.setupUi(d)
        d.exec_()

def downloadSrt(url: str, filebase: str) -> bool:
    now = str(datetime.now())
    r = requests.get(url, allow_redirects=True)
    open('{now}.zip', 'wb').write(r.content)
    print("Download completed.")
    zipdata = zipfile.ZipFile('{now}.zip')    
    subtitles_zip = sorted(list(filter(lambda x: x.filename.endswith('.srt'), zipdata.infolist())),key=lambda x: x.file_size,reverse=True)
    subtitles_zip[0].filename = filebase+".srt"
    zipdata.extract(subtitles_zip[0])
    print("SRT File extraction completed.")
    if os.path.exists("{now}.zip"):
        os.remove("{now}.zip")
    return os.path.exists("{filebase}.zip")

def parsename(name: str, div= '.') -> str:
    return os.path.splitext(os.path.basename(name))[0].replace('.',div)

def get_files(dir='.', ext=[]):
    return [f for f in os.listdir(dir) if os.path.isfile(f) and f.endswith(tuple(ext)) ]

def main():
    """
    This is the MAIN ENTRY POINT of our application.  The code at the end
    of the mainwindow.py script will not be executed, since this script is now
    our main program.   We have simply copied the code from mainwindow.py here
    since it was automatically generated by '''pyuic5'''.

    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
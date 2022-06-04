# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 409)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.create_todo_text_edit = QLineEdit(self.centralwidget)
        self.create_todo_text_edit.setObjectName(u"create_todo_text_edit")
        self.create_todo_text_edit.setGeometry(QRect(20, 10, 261, 31))
        font = QFont()
        font.setPointSize(12)
        self.create_todo_text_edit.setFont(font)
        self.create_button = QPushButton(self.centralwidget)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(300, 10, 131, 31))
        self.create_button.setFont(font)
        self.todo_list = QListWidget(self.centralwidget)
        QListWidgetItem(self.todo_list)
        self.todo_list.setObjectName(u"todo_list")
        self.todo_list.setGeometry(QRect(20, 60, 411, 231))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(19, 310, 411, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.delete_button = QPushButton(self.horizontalLayoutWidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setFont(font)

        self.horizontalLayout.addWidget(self.delete_button)

        self.done_button = QPushButton(self.horizontalLayoutWidget)
        self.done_button.setObjectName(u"done_button")
        self.done_button.setFont(font)

        self.horizontalLayout.addWidget(self.done_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.create_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))

        __sortingEnabled = self.todo_list.isSortingEnabled()
        self.todo_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.todo_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"todo ....", None));
        self.todo_list.setSortingEnabled(__sortingEnabled)

        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.done_button.setText(QCoreApplication.translate("MainWindow", u"Done", None))
    # retranslateUi


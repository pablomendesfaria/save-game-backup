# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainpRdAJR.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QCheckBox, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy,
                               QSpinBox, QStackedWidget, QVBoxLayout, QWidget)
import files_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setStyleSheet(u"background-color: rgb(55, 58, 89);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_toggle_menu = QPushButton(self.frame_toggle)
        self.pushButton_toggle_menu.setObjectName(u"pushButton_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_toggle_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_toggle_menu.setSizePolicy(sizePolicy)
        self.pushButton_toggle_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_toggle_menu.setStyleSheet(u"QPushButton {\n"
                                                  "	color: rgb(255, 255, 255);\n"
                                                  "	border: 0px solid;\n"
                                                  "	icon: url(:/32x32/icons/32x32/menu.png);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "	icon: url(:/32x32/icons/32x32/menu-green-1.png);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed {\n"
                                                  "	icon: url(:/32x32/icons/32x32/menu-green-2.png);\n"
                                                  "}")
        self.pushButton_toggle_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_toggle_menu)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 40))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)

        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.pushButton_menu_home = QPushButton(self.frame_top_menus)
        self.pushButton_menu_home.setObjectName(u"pushButton_menu_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_menu_home.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_home.setSizePolicy(sizePolicy1)
        self.pushButton_menu_home.setMinimumSize(QSize(0, 40))
        self.pushButton_menu_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_menu_home.setStyleSheet(u"QPushButton {\n"
                                                "	background-image: url(:/24x24/icons/24x24/home.png);\n"
                                                "    background-position: left center;\n"
                                                "    background-repeat: no-repeat;\n"
                                                "	color: rgb(255, 255, 255);\n"
                                                "    border: none;\n"
                                                "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                "    text-align: left;\n"
                                                "    padding-left: 47px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton[Active=true] {\n"
                                                "	background-image: url(:/24x24/icons/24x24/home.png);\n"
                                                "    background-position: left center;\n"
                                                "    background-repeat: no-repeat;\n"
                                                "    border: none;\n"
                                                "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                "    border-right: 5px solid rgb(233, 123, 195);\n"
                                                "    text-align: left;\n"
                                                "    padding-left: 45px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "	background-image: url(:/24x24/icons/24x24/home-green-1.png);\n"
                                                "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "	background-image: url(:/24x24/icons/24x24/home-green-2.png);\n"
                                                "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                "}")

        self.verticalLayout_4.addWidget(self.pushButton_menu_home)

        self.pushButton_menu_folder = QPushButton(self.frame_top_menus)
        self.pushButton_menu_folder.setObjectName(u"pushButton_menu_folder")
        sizePolicy1.setHeightForWidth(self.pushButton_menu_folder.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_folder.setSizePolicy(sizePolicy1)
        self.pushButton_menu_folder.setMinimumSize(QSize(0, 40))
        self.pushButton_menu_folder.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_menu_folder.setStyleSheet(u"QPushButton {\n"
                                                  "	background-image: url(:/24x24/icons/24x24/folder.png);\n"
                                                  "    background-position: left center;\n"
                                                  "    background-repeat: no-repeat;\n"
                                                  "	color: rgb(255, 255, 255);\n"
                                                  "    border: none;\n"
                                                  "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                  "    text-align: left;\n"
                                                  "    padding-left: 47px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton[Active=true] {\n"
                                                  "	background-image: url(:/24x24/icons/24x24/folder.png);\n"
                                                  "    background-position: left center;\n"
                                                  "    background-repeat: no-repeat;\n"
                                                  "    border: none;\n"
                                                  "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                  "    border-right: 5px solid rgb(233, 123, 195);\n"
                                                  "    text-align: left;\n"
                                                  "    padding-left: 45px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "	background-image: url(:/24x24/icons/24x24/folder-green-1.png);\n"
                                                  "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed {\n"
                                                  "	background-image: url(:/24x24/icons/24x24/folder-green-2.png);\n"
                                                  "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                  "}")

        self.verticalLayout_4.addWidget(self.pushButton_menu_folder)

        self.pushButton_menu_settings = QPushButton(self.frame_top_menus)
        self.pushButton_menu_settings.setObjectName(u"pushButton_menu_settings")
        sizePolicy1.setHeightForWidth(self.pushButton_menu_settings.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_settings.setSizePolicy(sizePolicy1)
        self.pushButton_menu_settings.setMinimumSize(QSize(0, 40))
        self.pushButton_menu_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_menu_settings.setStyleSheet(u"QPushButton {\n"
                                                    "	background-image: url(:/24x24/icons/24x24/settings.png);\n"
                                                    "    background-position: left center;\n"
                                                    "    background-repeat: no-repeat;\n"
                                                    "	color: rgb(255, 255, 255);\n"
                                                    "    border: none;\n"
                                                    "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                    "    text-align: left;\n"
                                                    "    padding-left: 47px;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton[Active=true] {\n"
                                                    "	background-image: url(:/24x24/icons/24x24/settings.png);\n"
                                                    "    background-position: left center;\n"
                                                    "    background-repeat: no-repeat;\n"
                                                    "    border: none;\n"
                                                    "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                    "    border-right: 5px solid rgb(233, 123, 195);\n"
                                                    "    text-align: left;\n"
                                                    "    padding-left: 45px;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover {\n"
                                                    "	background-image: url(:/24x24/icons/24x24/settings-green-1.png);\n"
                                                    "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "	background-image: url(:/24x24/icons/24x24/settings-green-2.png);\n"
                                                    "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                    "}")

        self.verticalLayout_4.addWidget(self.pushButton_menu_settings)

        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.frame_bottom_menus = QFrame(self.frame_left_menu)
        self.frame_bottom_menus.setObjectName(u"frame_bottom_menus")
        self.frame_bottom_menus.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_bottom_menus)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.pushButton_menu_theme = QPushButton(self.frame_bottom_menus)
        self.pushButton_menu_theme.setObjectName(u"pushButton_menu_theme")
        self.pushButton_menu_theme.setMinimumSize(QSize(0, 40))
        self.pushButton_menu_theme.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_menu_theme.setStyleSheet(u"QPushButton {\n"
                                                 "	background-image: url(:/24x24/icons/24x24/sun-1.png);\n"
                                                 "    background-position: left center;\n"
                                                 "    background-repeat: no-repeat;\n"
                                                 "	color: rgb(255, 255, 255);\n"
                                                 "    border: none;\n"
                                                 "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                 "    text-align: left;\n"
                                                 "    padding-left: 47px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "	background-image: url(:/24x24/icons/24x24/sun-2.png);\n"
                                                 "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "	background-image: url(:/24x24/icons/24x24/sun-3.png);\n"
                                                 "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                 "}")

        self.verticalLayout_5.addWidget(self.pushButton_menu_theme)

        self.verticalLayout_3.addWidget(self.frame_bottom_menus, 0, Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_pages)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_pages = QStackedWidget(self.frame_pages)
        self.stackedWidget_pages.setObjectName(u"stackedWidget_pages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.label_1 = QLabel(self.page_home)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(260, 120, 191, 111))
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setStyleSheet(u"font: 48pt \"Segoe UI\";\n"
                                   "color: rgb(255, 255, 255);")
        self.stackedWidget_pages.addWidget(self.page_home)
        self.page_folder = QWidget()
        self.page_folder.setObjectName(u"page_folder")
        self.label_2 = QLabel(self.page_folder)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 110, 191, 91))
        self.label_2.setStyleSheet(u"font: 48pt \"Segoe UI\";\n"
                                   "color: rgb(255, 255, 255);")
        self.stackedWidget_pages.addWidget(self.page_folder)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_6 = QVBoxLayout(self.page_settings)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_page_3_div_1 = QFrame(self.page_settings)
        self.frame_page_3_div_1.setObjectName(u"frame_page_3_div_1")
        self.frame_page_3_div_1.setFrameShape(QFrame.NoFrame)
        self.frame_page_3_div_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_page_3_div_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_Page_3_el_1_div_1 = QFrame(self.frame_page_3_div_1)
        self.frame_Page_3_el_1_div_1.setObjectName(u"frame_Page_3_el_1_div_1")
        self.frame_Page_3_el_1_div_1.setFrameShape(QFrame.StyledPanel)
        self.frame_Page_3_el_1_div_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_Page_3_el_1_div_1)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.checkBox_page_3 = QCheckBox(self.frame_Page_3_el_1_div_1)
        self.checkBox_page_3.setObjectName(u"checkBox_page_3")
        self.checkBox_page_3.setMaximumSize(QSize(16777215, 20))
        self.checkBox_page_3.setStyleSheet(u"QCheckBox {\n"
                                           "	color: rgb(247, 248, 242);\n"
                                           "	spacing: 20px;\n"
                                           "}\n"
                                           "\n"
                                           "QCheckBox::indicator {\n"
                                           "    border: 1px solid rgb(255, 255, 255);\n"
                                           "	border-radius: 2px;\n"
                                           "	width: 15px;\n"
                                           "	height: 15px;\n"
                                           "}\n"
                                           "\n"
                                           "QCheckBox::indicator:hover {\n"
                                           "    border: 1px solid rgb(255, 209, 18);\n"
                                           "}\n"
                                           "\n"
                                           "QCheckBox::indicator:checked {\n"
                                           "	border: 1px solid rgb(255, 159, 0);\n"
                                           "	background-image: url(:/16x16/icons/16x16/check.png);\n"
                                           "}")

        self.verticalLayout_8.addWidget(self.checkBox_page_3)

        self.frame_Page_3_el_2_div_1 = QFrame(self.frame_Page_3_el_1_div_1)
        self.frame_Page_3_el_2_div_1.setObjectName(u"frame_Page_3_el_2_div_1")
        self.frame_Page_3_el_2_div_1.setFrameShape(QFrame.StyledPanel)
        self.frame_Page_3_el_2_div_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_Page_3_el_2_div_1)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.spinBox_page_3_div_1 = QSpinBox(self.frame_Page_3_el_2_div_1)
        self.spinBox_page_3_div_1.setObjectName(u"spinBox_page_3_div_1")
        self.spinBox_page_3_div_1.setMaximumSize(QSize(50, 20))
        self.spinBox_page_3_div_1.setStyleSheet(u"QSpinBox {\n"
                                                "	color: rgb(247, 248, 242);\n"
                                                "    border: 1px solid rgb(255, 255, 255);\n"
                                                "	border-radius: 2px;\n"
                                                "}\n"
                                                "\n"
                                                "QSpinBox::up-button {\n"
                                                "    subcontrol-origin: border;\n"
                                                "    subcontrol-position: top right;\n"
                                                "    width: 17px;\n"
                                                "	border: none;\n"
                                                "}\n"
                                                "\n"
                                                "QSpinBox::up-arrow {\n"
                                                "    image: url(:/512x512/icons/512x512/arrow-drop-up.png);\n"
                                                "    width: 16px;\n"
                                                "    height: 16px;\n"
                                                "}\n"
                                                "\n"
                                                "QSpinBox::down-button {\n"
                                                "    subcontrol-origin: border;\n"
                                                "    subcontrol-position: bottom right;\n"
                                                "    width: 17px;\n"
                                                "	border: none;\n"
                                                "}\n"
                                                "\n"
                                                "QSpinBox::down-arrow {\n"
                                                "    image: url(:/512x512/icons/512x512/arrow-drop-down.png);\n"
                                                "    width: 16px;\n"
                                                "    height: 16px;\n"
                                                "}")

        self.horizontalLayout_4.addWidget(self.spinBox_page_3_div_1)

        self.label_page_3_div_1 = QLabel(self.frame_Page_3_el_2_div_1)
        self.label_page_3_div_1.setObjectName(u"label_page_3_div_1")
        self.label_page_3_div_1.setMaximumSize(QSize(16777215, 20))
        self.label_page_3_div_1.setStyleSheet(u"color: rgb(247, 248, 242);")

        self.horizontalLayout_4.addWidget(self.label_page_3_div_1)

        self.verticalLayout_8.addWidget(self.frame_Page_3_el_2_div_1, 0, Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.frame_Page_3_el_1_div_1)

        self.verticalLayout_6.addWidget(self.frame_page_3_div_1)

        self.stackedWidget_pages.addWidget(self.page_settings)

        self.horizontalLayout_3.addWidget(self.stackedWidget_pages)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_pages.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_toggle_menu.setText("")
        # if QT_CONFIG(tooltip)
        self.pushButton_menu_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_menu_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_menu_folder.setText(QCoreApplication.translate("MainWindow", u"Add Folder", None))
        self.pushButton_menu_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_menu_theme.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"page 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"page 2", None))
        self.checkBox_page_3.setText(QCoreApplication.translate("MainWindow", u"Delete file after use", None))
        self.label_page_3_div_1.setText(
            QCoreApplication.translate("MainWindow", u"Backups of database to keep (0 to unlimited)", None))
    # retranslateUi

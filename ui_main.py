# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainYFNLxx.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
                               QWidget)
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
                                                  "	icon: url(:/32x32/icons/32x32/menu/menu.png)\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "	icon: url(:/32x32/icons/32x32/menu/menu-green-1.png)\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed {\n"
                                                  "	icon: url(:/32x32/icons/32x32/menu/menu-green-2.png)\n"
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
                                                "	background-image: url(:/24x24/icons/24x24/home/home.png);\n"
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
                                                "	background-image: url(:/24x24/icons/24x24/home/home.png);\n"
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
                                                "	background-image: url(:/24x24/icons/24x24/home/home-green-1.png);\n"
                                                "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "	background-image: url(:/24x24/icons/24x24/home/home-green-2.png);\n"
                                                "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                "}")

        self.verticalLayout_4.addWidget(self.pushButton_menu_home)

        self.pushButton_menu_add_game = QPushButton(self.frame_top_menus)
        self.pushButton_menu_add_game.setObjectName(u"pushButton_menu_add_game")
        sizePolicy1.setHeightForWidth(self.pushButton_menu_add_game.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_add_game.setSizePolicy(sizePolicy1)
        self.pushButton_menu_add_game.setMinimumSize(QSize(0, 40))
        self.pushButton_menu_add_game.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_menu_add_game.setStyleSheet(u"QPushButton {\n"
                                                    "	background-image: url(:/24x24/icons/24x24/folder/folder.png);\n"
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
                                                    "	background-image: url(:/24x24/icons/24x24/folder/folder.png);\n"
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
                                                    "	background-image: url(:/24x24/icons/24x24/folder/folder-green-1.png);\n"
                                                    "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "	background-image: url(:/24x24/icons/24x24/folder/folder-green-2.png);\n"
                                                    "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                    "}")

        self.verticalLayout_4.addWidget(self.pushButton_menu_add_game)

        self.pushButton_menu_settings = QPushButton(self.frame_top_menus)
        self.pushButton_menu_settings.setObjectName(u"pushButton_menu_settings")
        sizePolicy1.setHeightForWidth(self.pushButton_menu_settings.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_settings.setSizePolicy(sizePolicy1)
        self.pushButton_menu_settings.setMinimumSize(QSize(0, 40))
        self.pushButton_menu_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_menu_settings.setStyleSheet(u"QPushButton {\n"
                                                    "	background-image: url(:/24x24/icons/24x24/settings/settings.png);\n"
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
                                                    "	background-image:url(:/24x24/icons/24x24/settings/settings.png);\n"
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
                                                    "	background-image: url(:/24x24/icons/24x24/settings/settings-green-1.png);\n"
                                                    "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "	background-image: url(:/24x24/icons/24x24/settings/settings-green-2.png);\n"
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
                                                 "	background-image: url(:/24x24/icons/24x24/sun/sun-1.png);\n"
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
                                                 "	background-image: url(:/24x24/icons/24x24/sun/sun-2.png);\n"
                                                 "    border-left: 23px solid rgb(40, 42, 54);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "	background-image: url(:/24x24/icons/24x24/sun/sun-3.png);\n"
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
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.stackedWidget_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_pages.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget_pages)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_toggle_menu.setText("")
        # if QT_CONFIG(tooltip)
        self.pushButton_menu_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton_menu_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_menu_add_game.setText(QCoreApplication.translate("MainWindow", u"Add Folder", None))
        self.pushButton_menu_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_menu_theme.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
    # retranslateUi

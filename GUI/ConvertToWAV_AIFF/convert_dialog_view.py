# Form implementation generated from reading ui file '/Users/gdaliymac/Desktop/EarQuiz Frequencies/GUI/ConvertToWAV_AIFF/convert_dialog_view.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ConvertToWAV_AIFF_Dialog(object):
    def setupUi(self, ConvertToWAV_AIFF_Dialog):
        ConvertToWAV_AIFF_Dialog.setObjectName("ConvertToWAV_AIFF_Dialog")
        ConvertToWAV_AIFF_Dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        ConvertToWAV_AIFF_Dialog.resize(495, 240)
        ConvertToWAV_AIFF_Dialog.setMinimumSize(QtCore.QSize(495, 240))
        ConvertToWAV_AIFF_Dialog.setMaximumSize(QtCore.QSize(495, 240))
        ConvertToWAV_AIFF_Dialog.setSizeGripEnabled(False)
        ConvertToWAV_AIFF_Dialog.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ConvertToWAV_AIFF_Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FormatGroup = QtWidgets.QGroupBox(parent=ConvertToWAV_AIFF_Dialog)
        self.FormatGroup.setObjectName("FormatGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.FormatGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WAVBut = QtWidgets.QRadioButton(parent=self.FormatGroup)
        self.WAVBut.setObjectName("WAVBut")
        self.verticalLayout.addWidget(self.WAVBut)
        self.AIFFBut = QtWidgets.QRadioButton(parent=self.FormatGroup)
        self.AIFFBut.setObjectName("AIFFBut")
        self.verticalLayout.addWidget(self.AIFFBut)
        self.horizontalLayout.addWidget(self.FormatGroup)
        self.SamplerateGroup = QtWidgets.QGroupBox(parent=ConvertToWAV_AIFF_Dialog)
        self.SamplerateGroup.setObjectName("SamplerateGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SamplerateGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SameAsOriginalBut = QtWidgets.QRadioButton(parent=self.SamplerateGroup)
        self.SameAsOriginalBut.setObjectName("SameAsOriginalBut")
        self.verticalLayout_2.addWidget(self.SameAsOriginalBut)
        self.SR441But = QtWidgets.QRadioButton(parent=self.SamplerateGroup)
        self.SR441But.setObjectName("SR441But")
        self.verticalLayout_2.addWidget(self.SR441But)
        self.SR48But = QtWidgets.QRadioButton(parent=self.SamplerateGroup)
        self.SR48But.setObjectName("SR48But")
        self.verticalLayout_2.addWidget(self.SR48But)
        self.DivisibleBut = QtWidgets.QRadioButton(parent=self.SamplerateGroup)
        self.DivisibleBut.setMinimumSize(QtCore.QSize(335, 0))
        self.DivisibleBut.setObjectName("DivisibleBut")
        self.verticalLayout_2.addWidget(self.DivisibleBut)
        self.horizontalLayout.addWidget(self.SamplerateGroup)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=ConvertToWAV_AIFF_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(ConvertToWAV_AIFF_Dialog)
        self.buttonBox.accepted.connect(ConvertToWAV_AIFF_Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ConvertToWAV_AIFF_Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ConvertToWAV_AIFF_Dialog)

    def retranslateUi(self, ConvertToWAV_AIFF_Dialog):
        _translate = QtCore.QCoreApplication.translate
        ConvertToWAV_AIFF_Dialog.setWindowTitle(_translate("ConvertToWAV_AIFF_Dialog", "Convert to..."))
        self.FormatGroup.setTitle(_translate("ConvertToWAV_AIFF_Dialog", "Format:"))
        self.WAVBut.setText(_translate("ConvertToWAV_AIFF_Dialog", "WAVE"))
        self.AIFFBut.setText(_translate("ConvertToWAV_AIFF_Dialog", "AIFF"))
        self.SamplerateGroup.setTitle(_translate("ConvertToWAV_AIFF_Dialog", "Sampling rate:"))
        self.SameAsOriginalBut.setText(_translate("ConvertToWAV_AIFF_Dialog", "Same as original"))
        self.SR441But.setText(_translate("ConvertToWAV_AIFF_Dialog", "44100 Hz"))
        self.SR48But.setText(_translate("ConvertToWAV_AIFF_Dialog", "48000 Hz"))
        self.DivisibleBut.setText(_translate("ConvertToWAV_AIFF_Dialog", "44100 Hz or 48000 Hz \n"
" (downsample to multiple where original is higher)"))

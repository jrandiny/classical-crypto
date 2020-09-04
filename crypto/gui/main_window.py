from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from PyQt5.QtCore import QSize, QThreadPool

from crypto.gui.components.algorithm_list import AlgorithmList
from crypto.gui.components.main_input import MainInput
from crypto.gui.components.configuration_box import ConfigurationBox
from crypto.gui.dialog_window import DialogWindow
from crypto.gui.encryption_parms import EncryptionParms, ModeType
from crypto.gui.worker import Worker
from crypto.engine.engine_factory import EngineType

from multiprocessing import cpu_count


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.enc_parms = EncryptionParms.get_instance()
        QThreadPool.globalInstance().setMaxThreadCount(cpu_count() - 1)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Classical Cryptography')
        self.setMinimumSize(950, 600)
        self.central_widget = QtWidgets.QWidget(self)

        self.layout = QHBoxLayout()
        self.algorithm_list = AlgorithmList('Algorithm', EngineType.list(), self.central_widget)

        self.main_input = MainInput(self.central_widget)

        self.configuration_box = ConfigurationBox(self.central_widget)

        self.layout.addWidget(self.algorithm_list)
        self.layout.addWidget(self.main_input)
        self.layout.addWidget(self.configuration_box)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.main_input.tab_string.input_mode.btn_execute.clicked.connect(self.execute_string)
        self.main_input.tab_file.input_mode.btn_execute.clicked.connect(self.execute_string)
        output_conf_signal = self.configuration_box.post_processing.btn_group.idClicked
        output_conf_slot = self.main_input.tab_string.output_string.on_change_format
        output_conf_signal.connect(output_conf_slot)

    def show_error_dialog(self, error_msg):
        DialogWindow('Error', error_msg).exec_()

    def execute_string(self):
        mode = self.enc_parms.mode
        key = self.configuration_box.encryption_key.get_key()
        data = self.main_input.tab_string.input_string.get_data()
        engine = self.enc_parms.get_engine()

        if mode == ModeType.ENCRYPT:
            fn = engine.encrypt
        else:
            fn = engine.decrypt

        worker = Worker(fn, data, key)
        worker.signals.error.connect(self.show_error_dialog)
        worker.signals.result.connect(self.main_input.tab_string.output_string.on_result_update)
        QThreadPool.globalInstance().start(worker)

    def execute_file(self):
        pass
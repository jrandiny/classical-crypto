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
from crypto.engine.data import *
from crypto.util.file_util import FileUtil

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

        self.algorithm_list = AlgorithmList(self.central_widget)
        self.main_input = MainInput(self.central_widget)
        self.configuration_box = ConfigurationBox(self.central_widget)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.algorithm_list)
        self.layout.addWidget(self.main_input)
        self.layout.addWidget(self.configuration_box)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.main_input.tab_string.input_mode.btn_execute.clicked.connect(self.execute_string)
        self.main_input.tab_file.input_mode.btn_execute.clicked.connect(self.execute_file)

        output_conf_signal = self.configuration_box.post_processing.btn_group.idClicked
        output_conf_slot = self.main_input.tab_string.output_string.on_change_format
        output_conf_signal.connect(output_conf_slot)

        engine_type_signal = self.algorithm_list.btn_group.idClicked
        engine_type_slot = self.configuration_box.encryption_box.on_update_key_widget
        engine_type_signal.connect(engine_type_slot)

    def show_dialog_window(self, title, msg):
        DialogWindow(title, msg).exec_()

    def show_error_dialog(self, error_msg):
        self.show_dialog_window('Error', error_msg)

    def show_success_window(self, msg):
        self.show_dialog_window('Success', msg)

    def prepare_exec_fun(self):
        mode = self.enc_parms.mode
        engine = self.enc_parms.get_engine()

        key = self.configuration_box.encryption_box.get_key()
        data = self.main_input.get_data()

        key = engine.complete_key(data, key)
        self.configuration_box.encryption_box.apply_key(key)

        if mode == ModeType.ENCRYPT:
            fn = engine.encrypt
        else:
            fn = engine.decrypt

        return fn, key, data

    def execute_string(self):
        try:
            fn, key, data = self.prepare_exec_fun()
        except Exception as e:
            self.show_error_dialog(str(e))
            return

        worker = Worker(fn, data, key)
        worker.signals.error.connect(self.show_error_dialog)
        worker.signals.result.connect(self.main_input.tab_string.output_string.on_result_update)
        QThreadPool.globalInstance().start(worker)

    def execute_file(self):
        try:
            fn, key, data = self.prepare_exec_fun()
        except Exception as e:
            self.show_error_dialog(str(e))
            return

        file_fn = FileUtil.with_move_file(fn, self.main_input.get_output_path())

        worker = Worker(file_fn, data, key)
        worker.signals.error.connect(self.show_error_dialog)
        worker.signals.result.connect(self.show_success_window)
        QThreadPool.globalInstance().start(worker)
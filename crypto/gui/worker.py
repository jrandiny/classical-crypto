from PyQt5.QtCore import QRunnable, pyqtSignal, QObject, QThread


class WorkerSignals(QObject):
    """
    Signal that is emited by worker to represent the status
    (finish, fail, working, etc), and the result

    result emits integer representing result code and result representing
    the function execution result
    """

    status = pyqtSignal(int)
    result = pyqtSignal(object)
    callback = pyqtSignal(str)


class Worker(QRunnable):
    """
    Worker class to handle multithreading on GUI
    """
    def __init__(self, function, *args, **kwargs):
        """
        Constructor of worker class, used to pass function and arguments
        
        Parameters:
            function (func): function to be executed
            *args, **kwargs : any arguments that is needed for the function

        Note: arguments must be in correct order as the original function
        """
        super(Worker, self).__init__()
        self.setAutoDelete(True)
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    def useCallback(self):
        """
        Add callback signal to the arg list, used when
        executing function that requires updating status bar
        """

        self.args += (self.signals.callback, )

    def run(self):
        """
        Execute the function with the arguments
        """

        log_time = time.strftime('%H:%M:%S')
        print(f'[{log_time}] Executing {self.function.__name__}')

        try:
            result = self.function(*self.args, **self.kwargs)
            self.signals.status.emit(STATUS_SUCCESS)
            self.signals.result.emit(result)
        except Exception as e:
            print(e)
            self.signals.status.emit(STATUS_FAIL)

        log_time = time.strftime('%H:%M:%S')
        print(f'[{log_time}] Finished {self.function.__name__}')

"""
Logger 0.1a
"""
from datetime import datetime
from app.scripts.components.jsonmanager import JsonManager, AddressType
from sys import stdout
from typing import TextIO
from colorama import init, Fore, Style
init()

"""
Usage:
printf(text_print, suffix_id{0: info, 1:warn, 2:error}, log_text_in_file)
Example:
from logger import Logger, TypeLogText
l = Logger('TestModule')

l.printf('hello world!')
l.printf('some annoying and popular warn', type_message=TypeLogText., log_text_in_file=False)
"""


class LogType:
    """
    helpful class for set log suffix in func printf
    """
    INFO = 0
    DEBUG = 1
    WARN = 2
    ERROR = 3
    FATAL = 4


# main class of this module
class Logger:
    def __init__(self, module_prefix: str, debug_mess: int = None,  out_stream: TextIO = None):
        # get conf to logger
        jsm = JsonManager(AddressType.FILE, "logger_conf.json")
        jsm.load_from_file()
        self.logger_conf = jsm.get_buffer()
        self.out_stream = out_stream
        if out_stream is None:
            self.out_stream = stdout.orig_out_stream if isinstance(stdout, PrintHandler) else stdout
        self._debug_mess = debug_mess
        if debug_mess is None:
            self.debug_mess = stdout.debug_mess if isinstance(stdout, PrintHandler) else 0
        # init class data, prefix
        self.module_prefix = module_prefix
        self.__old_date = ""
        self.__path_to_log_file = ""
        self.color_suf = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.RED]
        self.suffixes = ["INFO ", "DEBUG", "WARN ", "ERROR", "FATAL"]

    def __str__(self):
        return self.module_prefix

    @staticmethod
    def __get_str_datetime(time, datetime_format: str) -> str:
        return time.strftime(datetime_format)

    # add note to file
    def __add_note(self, line: str, new_date: str):
        # check if change the date
        if self.__old_date != new_date:
            # create new file
            self.__path_to_log_file = f"{self.logger_conf['default_path']}{self.module_prefix}_{new_date}.txt"
            with open(self.__path_to_log_file, "w", encoding=self.logger_conf["encoding"]) as file:
                file.write(f"Logger version {self.logger_conf['version']} | Log of module --> {self.module_prefix}\n")
            self.__old_date = new_date
        # write a note to the file
        with open(self.__path_to_log_file, "a", encoding=self.logger_conf["encoding"]) as file:
            file.write(line)

    # print info
    def printf(self, line: str, log_type: int = 0, log_text_in_file: bool = True):
        # generate timestamp, prefix and suffix
        now_int_time = datetime.now()
        now_date = self.__get_str_datetime(now_int_time, self.logger_conf["date_format"])
        now_time = self.__get_str_datetime(now_int_time, self.logger_conf["time_format"])
        suffix = self.suffixes[log_type]
        # generate color text
        f_line = line
        if log_type == 4:
            f_line = Fore.RED + f_line
        f_line = (f"{Style.BRIGHT}[{Fore.CYAN}{now_time}{Fore.RESET}] " +
                  f"[{Fore.GREEN}{self.module_prefix}{Fore.RESET}] " +
                  f"[{self.color_suf[log_type]}{suffix}{Fore.RESET}] " +
                  f_line)

        print(f_line, file=self.out_stream)

        # need to save note in file
        if log_text_in_file:
            # generate text without ansi color
            f_line = f"[{now_time}] [{self.module_prefix}] [{suffix}] {line}\n"
            self.__add_note(f_line, now_date)


class PrintHandler:
    def __init__(self, logger: Logger, orig_out_stream: TextIO = stdout, debug_mess: int = 0,
                 save_to_file: bool = False):
        self.log = logger
        self._orig_out_stream = orig_out_stream
        self._debug_mess = debug_mess
        self._out_text = ""
        self.save_to_file = save_to_file

    @property
    def orig_out_stream(self) -> TextIO:
        return self._orig_out_stream

    @property
    def debug_mess(self) -> int:
        return self._debug_mess

    def flush(self):
        pass

    def write(self, message: str):
        if not message:
            return
        if message[-1] == "\n":
            if self._debug_mess:
                self.log.printf(self._out_text, LogType.DEBUG, log_text_in_file=self.save_to_file)
            self._out_text = ""
            return
        self._out_text += message


class ErrorHandler:
    def __init__(self, logger: Logger):
        self.log = logger
        self._err_text = ""
        self._hand_code = 0

    def flush(self):
        pass

    def write(self, message: str):
        self._err_text += message
        if not self._err_text:
            return
        if self._err_text[-1] == "r":
            self._hand_code = 1
            return
        if self._hand_code and self._err_text[-1] == "\n":
            self.log.printf(self._err_text, LogType.FATAL)
            self._err_text = ""
            self._hand_code = 0

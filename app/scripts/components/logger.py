from datetime import datetime
from app.scripts.components.jsonmanager import JsonManager, AddressType
from sys import stdout
from typing import TextIO
from colorama import init, Fore, Style
init()


VERSION = 2


class LogType:
    """
    helpful class for set log suffix in func printf
    """
    INFO = 0
    DEBUG = 1
    WARN = 2
    ERROR = 3
    FATAL = 4


class Colors:
    """
    Color themes for logger output
    """
    time = f"{Style.BRIGHT}[{Fore.CYAN}{{now_time}}{Fore.RESET}] "
    name = f"[{Fore.GREEN}{{name}}{Fore.RESET}] "
    log_types = ["INFO ", "DEBUG", "WARN ", "ERROR", "FATAL"]
    color_log_types = [
        f"{Style.BRIGHT}[{Fore.CYAN}INFO {Fore.RESET}] ",
        f"{Style.BRIGHT}[{Fore.GREEN}DEBUG{Fore.RESET}] ",
        f"{Style.BRIGHT}[{Fore.YELLOW}WARN {Fore.RESET}] ",
        f"{Style.BRIGHT}[{Fore.RED}ERROR{Fore.RESET}] ",
        f"{Style.BRIGHT}[{Fore.RED}FATAL{Fore.RESET}] "]
    color_line = ["{line}", "{line}", "{line}", "{line}", f"{Fore.RED}{{line}}"]


# main class of this module
class Logger:
    def __init__(self, name: str, debug_mess: int = None,  out_stream: TextIO = None):
        # get conf to logger
        self.cfg = JsonManager(AddressType.FILE, "cfg.json")
        self.cfg.load_from_file()
        self.out_stream = out_stream
        if out_stream is None:
            self.out_stream = stdout.orig_out_stream if isinstance(stdout, PrintHandler) else stdout
        self._debug_mess = debug_mess
        # init class data, prefix
        self.name = name
        self.__old_date = ""
        self.__path_to_log_file = ""
        self.msg_format = self.cfg["msg_format"] + Fore.RESET

    def __str__(self):
        return self.name

    def set_debug_logging(self, enable: bool):
        self._debug_mess = enable

    @staticmethod
    def __get_str_datetime(time, datetime_format: str) -> str:
        return time.strftime(datetime_format)

    # add note to file
    def __add_note(self, line: str, new_date: str):
        # check if change the date
        if self.__old_date != new_date:
            # create new file
            self.__path_to_log_file = f"{self.cfg['default_path']}{self.name}_{new_date}.txt"
            with open(self.__path_to_log_file, "w", encoding=self.cfg["encoding"]) as file:
                file.write(f"Logger version {VERSION} | Log of module --> {self.name}\n")
            self.__old_date = new_date
        # write a note to the file
        with open(self.__path_to_log_file, "a", encoding=self.cfg["encoding"]) as file:
            file.write(line)

    # print info
    def printf(self, line: str, log_type: int = 0, end: str = "\n", log_text_in_file: bool = True):
        # generate timestamp
        now_int_time = datetime.now()
        now_date = self.__get_str_datetime(now_int_time, self.cfg["date_format"])
        now_time = self.__get_str_datetime(now_int_time, self.cfg["time_format"])
        # generate color text
        c_line = self.msg_format.format(now_time=Colors.time.format(now_time=now_time),
                                        name=Colors.name.format(name=self.name),
                                        log_type=Colors.color_log_types[log_type],
                                        line=Colors.color_line[log_type].format(line=line))
        print(c_line, file=self.out_stream, end=end)
        # need to save note in file
        if log_text_in_file:
            # generate text without ansi color
            f_line = self.msg_format.format(now_time=now_time,
                                            name=self.name,
                                            log_type=Colors.log_types[log_type],
                                            line=line
                                            ) + "\n"
            # add text to file
            self.__add_note(f_line, now_date)


class PrintHandler:
    def __init__(self, logger: Logger, orig_out_stream: TextIO = stdout,
                 save_to_file: bool = False):
        self.log = logger
        self._orig_out_stream = orig_out_stream
        self._out_text = ""
        self.save_to_file = save_to_file

    @property
    def orig_out_stream(self) -> TextIO:
        return self._orig_out_stream

    def flush(self):
        pass

    def write(self, message: str | bytes):
        if not message:
            return
        if type(message) is bytes:
            message = message.decode()
        self._out_text += message
        if message[-1] == "\n":
            self.log.printf(self._out_text, LogType.DEBUG, end="", log_text_in_file=self.save_to_file)
            self._out_text = ""
            return


class ErrorHandler:
    def __init__(self, logger: Logger):
        self.log = logger
        self._err_text = ""
        self._hand_code = 0

    def flush(self):
        pass

    def write(self, message: str):
        print(">>>" + message + "<<<")
        if not message:
            return
        self._err_text += message

        if message[0] == ":":
            self._hand_code = 1
            return
        if self._hand_code and self._err_text[-1] == "\n":
            self.log.printf(self._err_text, LogType.FATAL)
            self._err_text = ""
            self._hand_code = 0

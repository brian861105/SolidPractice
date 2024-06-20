from abc import ABC, abstractmethod
import os

class ILogger(ABC):
    def log(self, message : str):
        pass

class ConsoleLogger(ILogger):
    def log(self, message : str):
        print(message)
        
class FileLogger(ILogger):
    def log(self, message : str):
        with open("myLogger.txt", "w") as file:
            file.write(message)
            
class AppEvent:
    def __init__(self, logger_type:str):
        self._logger = LogFactory.create_logger(logger_type)
    def generate(self, message:str):
        self._logger.log(message)
        
class LogFactory:
    @staticmethod
    def create_logger(logger_type : str) -> ILogger:
        if(logger_type == "Console"):
            return ConsoleLogger()
        
        elif(logger_type == "File"):
            return FileLogger()
        else:
            raise NotImplemented()
            


_Filelogger = AppEvent("File")
_Filelogger.generate("hello world")

_ConsoleLogger = AppEvent("Console")
_ConsoleLogger.generate("hello world")

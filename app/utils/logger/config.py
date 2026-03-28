from typing import Literal, Union, Annotated, Any

from pydantic import BaseModel, Field, BeforeValidator

# Function to convert string log levels to uppercase before validation
def prepare_log_level(value: Any) -> Any:
    if isinstance(value, str):
        return value.upper()
    return value

# Literal containing all valid string log levels
ValidLogLevels = Literal[
    "TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"
]

# Custom type for log level: either a valid string or an integer (e.g., 51 to disable)
LogLevel = Annotated[
    Union[ValidLogLevels, int],
    BeforeValidator(prepare_log_level)
]

class LogFormat(BaseModel):
    """Model for validating log formats by level"""
    TRACE: str
    DEBUG: str
    INFO: str
    SUCCESS: str
    WARNING: str
    ERROR: str
    CRITICAL: str

class ConsoleConfig(BaseModel):
    """Console logger configuration"""
    level: LogLevel = Field(
        ...,
        description="Log level (string) or integer (e.g., 51 to disable logging)"
    )
    format: LogFormat

class FileConfig(BaseModel):
    """File logger configuration"""
    level: LogLevel
    filepath: str = Field(..., description="Template for the log filename")
    rotation: str = Field(..., description=" File rotation(default: daily)")
    retention:str = Field(..., description="File retention(default: monthly)")
    compression: str = Field(..., description="Compression format (default: linux archive)")
    encoding: str = Field(default="utf-8", description="Encoding for the log file")
    format: LogFormat

class LoggerConfig(BaseModel):
    """Root configuration model for the logger"""
    console: ConsoleConfig
    file: FileConfig

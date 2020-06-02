import functools
import logging


def get_logger():
    """
    Creates a logging object and saves
    the output in the form of a  .log file.
    """

    logger = logging.getLogger("logger_object")
    logger.setLevel(logging.INFO)

    # Create the logging file handler
    filehandle = logging.FileHandler("Log.log")
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    filehandle.setFormatter(formatter)

    # Add handler to logger object
    logger.addHandler(filehandle)
    return logger


def exception(function):
    """
    A decorator that wraps the passed in function 
    and logs exceptions should one occur.
    """
    @functools.wraps(function)
    def wrapper(*ag, **kw):
        logger = get_logger()
        try:
            return function(*ag, **kw)
        except:
            # Log the exception
            err = "There was an exception in  "
            err += function.__name__
            logger.exception(err)
            # Re-raise the exception
            raise
    return wrapper

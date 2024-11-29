import logging
from datetime import datetime

def getLogger(name, level = logging.DEBUG, filename = f"logs/hotel-apps") -> logging.Logger:
    filename = datetime.now().strftime(f"{filename}-%Y%m%d.log")
    logging.basicConfig(level="WARNING",
        format="%(asctime)s.%(msecs)03d - %(levelname)8s:%(name)20s - %(message)s ",
        datefmt='%Y%m%d %H:%M:%S',
        force=True,
        handlers=[
            logging.FileHandler(filename),
            logging.StreamHandler()
        ])
    logger = logging.getLogger(name)
    # Setting the threshold of logger to DEBUG
    logger.setLevel(level)
    return logger

def main():
    logger = getLogger('main')
    # Test messages
    logger.debug("Harmless debug Message")
    logger.info("Just an information")
    logger.warn("Just a warn")
    logger.warning("Just a warning")
    logger.error("Just an error")
    logger.critical("Just a critical")

if __name__ == "__main__":
    main()
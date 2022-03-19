import logging

class logGen:

    def custom_logger(self,logLevel=logging.DEBUG):
        logger = logging.getLogger()
        logger.setLevel(logLevel)
        fh = logging.FileHandler("automation.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s:', datefmt='%m/%d/%y %I:%M:%S %P')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger


# *******************other method to write logg (while using this test case is fail***************)
    # @staticmethod
    # #
    # # def loggen():
    # #     logging.basicConfig(level=INFO, filename="..\Logs\Automation.log")
    # #     logger=logging.getLogger()
    # #     #logger.setLevel(logging.INFO)
    # #     return logger
    #
    # def loggen():
    #     logging.basicConfig(filename="..\Logs\Automation.log",
    #                         format='%(asctime)s: %(levelname)s: %(message)s:', datefmt='%m/%d/%y %I:%M:%S %P')
    #
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger


# *******************other method to write logg (while using this test case is fail***************)
#     def custom_logger(self):
#         logger = logging.getLogger(__name__)
#         fileHandler = logging.FileHandler('Automation.log')
#         formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
#         fileHandler.setFormatter(formatter)
#         logger.addHandler(fileHandler)
#         logger.setLevel(loggin.INFO)
#         return logger




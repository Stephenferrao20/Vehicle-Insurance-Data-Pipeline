# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# from src.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()

import os
print(os.getenv("AWS_ACCESS_KEY_ID"))
print(os.getenv("AWS_SECRET_ACCESS_KEY"))
print(os.getenv("MONGODB_URL"))
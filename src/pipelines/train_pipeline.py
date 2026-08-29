import sys

from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__ == "__main__":

    try:

        logging.info("Starting Data Ingestion")

        data_ingestion = DataIngestion()

        train_data, test_data = data_ingestion.initiate_data_ingestion()

        logging.info("Data Ingestion completed")


        logging.info("Starting Data Transformation")

        data_transformation = DataTransformation()

        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
            train_data,
            test_data
        )

        logging.info("Data Transformation completed")


        logging.info("Starting Model Training")

        model_trainer = ModelTrainer()

        model_score = model_trainer.initiate_model_trainer(
            train_arr,
            test_arr
        )

        logging.info("Model Training completed")

        print(f"Best Model R2 Score: {model_score}")


    except Exception as e:

        logging.error("Error occurred in training pipeline")

        raise CustomException(e, sys)
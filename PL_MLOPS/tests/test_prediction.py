import sys
sys.path.append("/Users/sohombanerjee/Documents/Project/ml_pipeline/PL_MLOPS/")
import pytest
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

# Fixtures-- This function will run before execution of each test cases

@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result


def test_pred_not_none(single_prediction):
    assert single_prediction is not None


def test_pred_type_str(single_prediction):
    assert isinstance(single_prediction.get("prediction")[0],str)

def test_pred_validate_result(single_prediction):
    assert single_prediction.get("prediction")[0]=='Y'
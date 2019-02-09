import pytest
import pandas as pd
from .functions import generate

#Test Specify

#Test Generate
def test_shape_output():
  '''
  Test number of rows and columns in the output match
  '''
  df_input = pd.DataFrame(columns=["Response"], data=[1,2,3])
  df_output = generate(data=df_input, n_samples=3)

  assert df_output.shape == (9,1)

def test_empty_dataframe():
  '''
  Test function response with an emtpy dataframe, expect error.
  '''
  df_input = pd.DataFrame()
  with pytest.raises(Exception):
        df_output = generate(data=df_input, n_samples=3)

def test_zero_n_samples():
  '''
  Test function response with when n_samples = 0, expect empty DataFrame
  '''
  df_input = pd.DataFrame(columns=["Response"], data=[1,2,3])
  df_output = generate(data=df_input, n_samples=0)

  assert df_output.empty == True

def test_samples_exist():
  '''
  Test whether all bootstrap values exist in the original sample.
  '''
  df_input = pd.DataFrame(columns=["Response"], data=[1,2,3])
  df_output = generate(data=df_input, n_samples=3)

  assert df_output.response.isin(df_input.response).all()

def test_overflow():
  '''
  Test function behavior when number of samples is too high.
  '''
  df_input = pd.DataFrame(columns=["Response"], data=[1])
  with pytest.raises(Exception):
      df_output = generate(data=df_input, n_samples=1e10000000)

# #Test Calculate
#
# def test_expected_output(calculate,df):
#     '''
#     Test that the output is coming out as expected.
#     '''
#
#     df = pd.read_csv("test_data_calculate.csv")
#     df_output = calculate(df)
#     # Since the calculate is taking the output of generate as input,
#     # the shape of the input should be (n,2), and the test data shape is (200,2)
#     # Hence, the output shape should be (# of sample_id, 2)
#
#     assert type(df_output) == "pd.DataFrame", "The type of the output is wrong"
#     assert df_output.shape == (10,2), "The shape of the output is wrong"
#     assert type(df_output['mean'][0]) == "numpy.int64", "The type of the output value is wrong"
#     assert df_output['mean'][3] == 38.85, "The calculate mean is wrong"
#
#
# #Test get_ci
# def test_get_ci(get_ci,df,n):
#   df = pd.read_csv("test_data_get_ci.csv")
#   df_output = get_ci(df, n)
#   '''
#   Test if the `get_ci` function is working properly
#
#   Parameters:
#   `test_get_ci`:
#       The function being test
#   df: dataFrame
#       A Data frame using for test, which only contains 2 columns: sample_id, reponse
#
#   Returns:
#   string:
#       "All tests pass. Success!" if all test are passed
#       Raising error if some test is not passed.
#   '''
#   assert type(n)== "numpy.int64" or type(n)== "float", "The type of interval is wrong"
#   assert n <= 100 or n>=0, "The value of interval should be in (0,100)"
#   assert type(df_output) == "pandas.core.frame.DataFrame", "The type of the output is wrong"
#   assert df_output.shape == (3,1), "The shape of the output is wrong"
#   assert type(df_output['mean'][0])== "numpy.int64", "The type of the output value is wrong"
#   assert df_output['mean']== 38.559, "The value of point estimate is wrong"
#   assert get_ci(df, 95)['lower_bound] == 30, "The value of lower bound is wrong"
#   assert get_ci(df, 95)['upper_bound] == 42, "The value of upper bound is wrong"
#   print("All test passed")

from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height,pressure_loss_from_pipe

def test_water_column_height():
    test=water_column_height(0.0, 0.0)
    assert test == approx(0.0)
    test=water_column_height(0.0, 10.0)
    assert test == approx(7.5)
    test=water_column_height(25.0, 0.0)
    assert test == approx(25.0)
    test=water_column_height(48.3, 12.8)
    assert test == approx(57.9)
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0)==approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2)==approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0)==approx(489.450, abs=0.001)
    
def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692,0.00,0.018,1.75) == approx(0.000, abs=0.001)   
  # Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
# pytest.main(["-v", "--tb=line", "-rN", "test_water_flow.py"])    
pytest.main(["-v", "--tb=line", "-rN", __file__])
#ALEJANDRO MORENO
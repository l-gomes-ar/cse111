import pytest
from pytest import approx

# Import the functions being tested here
from aviation_toolkit import (calculate_dead_reckoning, calculate_fuel_endurance,
                           calculate_ground_speed, calculate_off_course_correction,
                           calculate_rate_descent, calculate_tod, calculate_distance_traveled,
                           calculate_toa, convert_celsius_fahrenheit, convert_fahrenheit_celsius,
                           convert_naut_mi, convert_mi_naut, convert_naut_km, convert_km_naut,
                           convert_gallons_liters, convert_liters_gallons, convert_pounds_kg, 
                           convert_kg_pounds, convert_ft_m, convert_m_ft, convert_mb_inhg, 
                           convert_inhg_mb, convert_h_min_s_decimal_h, calculate_true_airspeed)


# Test all 'Calculate' functions
def test_calculate_dead_reckoning():
    """Test the calculate_dead_reckoning function."""
    result = calculate_dead_reckoning(45, 10, 20, 60, 60)
    assert result["latitude"] == approx(52.42640687119285)
    assert result["longitude"] == approx(62.42640687119285)

    result = calculate_dead_reckoning(90, -30, 40, 60, 60)
    assert result["latitude"] == approx(-30)
    assert result["longitude"] == approx(100)

    result = calculate_dead_reckoning(180, 50, -60, 60, 60)
    assert result["latitude"] == approx(-10)
    assert result["longitude"] == approx(-60)


def test_calculate_true_airspeed():
    """Test the calculate_true_airspeed function."""
    assert calculate_true_airspeed(10000, 150) == pytest.approx(180, rel=0.1)
    assert calculate_true_airspeed(20000, 200) == pytest.approx(280, rel=0.1)
    assert calculate_true_airspeed(30000, 250) == pytest.approx(400, rel=1e-5)
    

def test_calculate_ground_speed():
    """Test the calculate_ground_speed function."""
    result = calculate_ground_speed(500, 50, 0, 90)
    assert result == approx(500, rel=0.01)

    result = calculate_ground_speed(500, 50, 45, 90)
    assert result == approx(535.36, rel=0.01)

    result = calculate_ground_speed(600, 100, 90, 0)
    assert result == approx(600, rel=0.01)

    result = calculate_ground_speed(700, 100, 0, 270)
    assert result == approx(700, rel=0.01)


def test_calculate_off_course_correction():
    """Test the calculate_off_course_correction function."""
    result = calculate_off_course_correction(2, 100, 150)
    assert result == approx(0.458356458, rel=0.1)

    result = calculate_off_course_correction(5, 200, 300)
    assert result == approx(0.572938698, rel=0.1)
    
    result = calculate_off_course_correction(15, 500, 500)
    assert result == approx(0.859372244, rel=0.1)


def test_calculate_fuel_endurance():
    """Test the calculate_fuel_endurance function."""
    result = calculate_fuel_endurance(200, 10)
    assert result == approx(20.0, rel=0.01)

    result = calculate_fuel_endurance(100, 7)
    assert result == approx(14.29, rel=0.01)


def test_calculate_rate_descent():
    """Test the calculate_rate_descent function."""
    result = calculate_rate_descent(180)
    assert result == approx(900)

    result = calculate_rate_descent(100)
    assert result == approx(500)


def test_calculate_tod():
    """Test the calculate_tod function."""
    result = calculate_tod(12000, 2000, 1000, 240)
    assert result == approx(40)

    result = calculate_tod(10000, 1000, 500, 100)
    assert result == approx(30)


def test_calculate_distance_traveled():
    """Test the calculate_distance_traveled function."""
    result = calculate_distance_traveled(200, 30)
    assert result == approx(100)

    result = calculate_distance_traveled(250, 30)
    assert result == approx(125)


def test_calculate_toa():
    """Test the calculate_toa function."""
    result = calculate_toa(120, 240)
    assert result == approx(30)

    result = calculate_toa(200, 200)
    assert result == approx(60)

    result = calculate_toa(400, 150)
    assert result == approx(160)


# Test all 'Convert' functions
def test_convert_celsius_fahrenheit():
    """Test the convert_celsius_fahrenheit function."""
    assert convert_celsius_fahrenheit(25) == approx(77.0)
    assert convert_celsius_fahrenheit(0) == approx(32.0)
    assert convert_celsius_fahrenheit(-40) == approx(-40.0)


def test_convert_fahrenheit_celsius():
    """Test the convert_fahrenheit_celsius function."""
    assert convert_fahrenheit_celsius(77) == approx(25.0)
    assert convert_fahrenheit_celsius(32) == approx(0.0)
    assert convert_fahrenheit_celsius(-40) == approx(-40.0)


def test_convert_naut_mi():
    """Test the convert_naut_mi function."""
    assert convert_naut_mi(100) == approx(115.078)
    assert convert_naut_mi(0) == approx(0.0)
    assert convert_naut_mi(200) == approx(230.156)


def test_convert_mi_naut():
    """Test the convert_mi_naut function."""
    assert convert_mi_naut(115.078) == approx(100.0)
    assert convert_mi_naut(0) == approx(0.0)
    assert convert_mi_naut(230.156) == approx(200.0)


def test_convert_naut_km():
    """Test the convert_naut_km function."""
    assert convert_naut_km(100) == approx(185.2)
    assert convert_naut_km(0) == approx(0.0)
    assert convert_naut_km(200) == approx(370.4)


def test_convert_km_naut():
    """Test the convert_km_naut function."""
    assert convert_km_naut(185.2) == approx(100.0)
    assert convert_km_naut(0) == approx(0.0)
    assert convert_km_naut(370.4) == approx(200.0)


def test_convert_gallons_liters():
    """Test the convert_gallons_liters function."""
    assert convert_gallons_liters(10) == approx(37.8541)
    assert convert_gallons_liters(0) == approx(0.0)
    assert convert_gallons_liters(20) == approx(75.7082)


def test_convert_liters_gallons():
    """Test the convert_liters_gallons function."""
    assert convert_liters_gallons(37.8541) == approx(10.0)
    assert convert_liters_gallons(0) == approx(0.0)
    assert convert_liters_gallons(75.7082) == approx(20.0)


def test_convert_pounds_kg():
    """Test the convert_pounds_kg function."""
    assert convert_pounds_kg(10) == approx(4.53592)
    assert convert_pounds_kg(0) == approx(0.0)
    assert convert_pounds_kg(20) == approx(9.07184)


def test_convert_kg_pounds():
    """Test the convert_kg_pounds function."""
    assert convert_kg_pounds(4.53592) == approx(10.0)
    assert convert_kg_pounds(0) == approx(0.0)
    assert convert_kg_pounds(9.07184) == approx(20.0)


def test_convert_ft_m():
    """Test the convert_ft_m function."""
    assert convert_ft_m(10) == approx(3.048)
    assert convert_ft_m(0) == approx(0.0)
    assert convert_ft_m(20) == approx(6.096)


def test_convert_m_ft():
    """Test the convert_m_ft function."""
    assert convert_m_ft(3.048) == approx(10.0)
    assert convert_m_ft(0) == approx(0.0)
    assert convert_m_ft(6.096) == approx(20.0)


def test_convert_inhg_mb():
    """Test the convert_inhg_mb function."""
    assert convert_inhg_mb(30) == approx(1015.9167, rel=0.1)
    assert convert_inhg_mb(0) == approx(0.0, rel=0.1)
    assert convert_inhg_mb(15) == approx(508.95835, rel=0.1)


def test_convert_mb_inhg():
    """Test the convert_mb_inhg function."""
    assert convert_mb_inhg(1015.9167) == approx(30.0, rel=0.1)
    assert convert_mb_inhg(0) == approx(0.0, rel=0.1)
    assert convert_mb_inhg(508.95835) == approx(15.0, rel=0.1)


def test_convert_h_min_s_decimal_h():
    """Test the convert_h_min_s_decimal_h function."""
    assert convert_h_min_s_decimal_h(2, 30, 45) == approx(2.5125)
    assert convert_h_min_s_decimal_h(0, 0, 0) == approx(0.0)
    assert convert_h_min_s_decimal_h(1, 15, 30) == approx(1.2583333333)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

# pymorton (https://github.com/trevorprater/pymorton)
# Author: trevor.prater@gmail.com
# License: MIT

import unittest
import pymorton as pm
from nose.tools import assert_raises


class TestOrdinalHashing(unittest.TestCase):

    def test_hashing_2d_valid(self):
        assert pm.interleave(100, 50) == pm.interleave2(100, 50)

    def test_hashing_3d_valid(self):
        assert pm.interleave(10, 50, 40) == pm.interleave3(10, 50, 40)

    def test_hash_reversability_2d_valid(self):
        assert (100, 30) == pm.deinterleave2(pm.interleave(100, 30))

    def test_hash_reversability_3d_valid(self):
        assert pm.deinterleave3(pm.interleave(100, 30, 50)) == (100, 30, 50)

    def test_hash_ordinality_2d(self):
        assert pm.interleave(10, 25) < pm.interleave(10, 50)

    def test_hash_ordinality_3d(self):
        assert pm.interleave(10, 25, 50) < pm.interleave(10, 25, 100)

    def test_interleave2_input_length_invalid(self):
        assert_raises(ValueError, pm.interleave2, 74)

    def test_interleave2_input_type_invalid(self):
        assert_raises(ValueError, pm.interleave2, 78, "73")

    def test_interleave3_input_length_invalid(self):
        assert_raises(ValueError, pm.interleave3, 78, 73)

    def test_interleave3_input_type_invalid(self):
        assert_raises(ValueError, pm.interleave3, 78, 77, "73")

    def test_deinterleave2_input_type_invalid(self):
        assert_raises(ValueError, pm.deinterleave2, "73")

    def test_deinterleave3_input_type_invalid(self):
        assert_raises(ValueError, pm.deinterleave3, "73")

    def test_interleave_input_length_invalid(self):
        assert_raises(ValueError, pm.interleave, 77)


class TestGeoHashing(unittest.TestCase):

    def test_standard_geohashing(self):
        lat, lng = 40.712014, -74.008164
        latlng_morton = pm.interleave_latlng(lat, lng)
        assert '03023211232311330231120312032231' == latlng_morton
        assert pm.deinterleave_latlng(latlng_morton) == (40.712014, -74.008164)

    def test_invalid_positive_longitude(self):
        lat, lng = 40.712013, 190.008164
        assert pm.deinterleave_latlng(pm.interleave_latlng(lat, lng)) == (lat, round(lng - 180.0, 6))

    def test_invalid_negative_longitude(self):
        lat, lng = -40.712013, -190.008164
        assert pm.deinterleave_latlng(pm.interleave_latlng(lat, lng)) == (lat, round(lng + 180.0, 6))

    def test_invalid_positive_latitude(self):
        lat, lng = 220.712013, -74.008164
        assert pm.deinterleave_latlng(pm.interleave_latlng(lat, lng)) == (round(lat - 180.0, 6), lng)

    def test_invalid_negative_latitude(self):
        lat, lng = -220.712013, -74.008164
        assert pm.deinterleave_latlng(pm.interleave_latlng(lat, lng)) == (round(lat + 180.0, 6), lng)

    def test_non_float_input_interleave_latlng(self):
        lat, lng = -220.712013, "-74.008164"
        assert_raises(ValueError, pm.interleave_latlng, lat, lng)

    def test_geohash_ordinality(self):
        assert pm.interleave_latlng(-40.723471, -73.985361) < pm.interleave_latlng(-40.523471, -73.785361)

    def test_geohash_divisor_constant_generation(self):
        assert pm._DIVISORS[4] == 11.25


if __name__ == '__main__':
    unittest.main()


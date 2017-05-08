import unittest
import pymorton as pm

class TestPymorton(unittest.TestCase):
    def test_pymorton(self):
        # Test standard hashing
        assert(pm.interleave(100, 50) == pm.interleave2(100, 50)) 
        assert(pm.interleave(10, 50, 40) == pm.interleave3(10, 50, 40))
        assert((100, 30) == pm.deinterleave2(pm.interleave(100, 30)))
        assert(pm.deinterleave2(pm.interleave(100,30)) == (100, 30))
        assert(pm.deinterleave3(pm.interleave(100, 30, 50)) == (100, 30, 50))

        # Test geo-hashing
        lat, lng = 40.712014, -74.008164
        latlng_morton = pm.interleave_latlng(lat, lng)
        assert('03023211232311330231120312032231' == \
                latlng_morton)
        assert(pm.deinterleave_latlng(latlng_morton) == \
                (40.712013971060514, -74.00816400535405))

    def test_ordering(self):
        assert pm.interleave_latlng(-40.723471, -73.985361) < \
                pm.interleave_latlng(-40.523471, -73.785361)
        assert pm.interleave_latlng(40.723471, 40.734567) > \
               pm.interleave_latlng(40.723271, 40.734367) 

if __name__ == '__main__':
    unittest.main()



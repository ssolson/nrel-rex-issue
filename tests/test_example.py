from pandas.testing import assert_frame_equal
from os.path import abspath, dirname
import unittest
from rex import WaveX


testdir = dirname(abspath(__file__))

class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.wave_file='/nrel/US_wave/virtual_buoy/West_Coast/West_Coast_virtual_buoy_2010.h5'

    @classmethod
    def tearDownClass(self):
        pass

    def test_run_energy_period(self):
       
        with WaveX(self.wave_file, hsds=True) as rex_waves:
            data_raw = rex_waves.get_lat_lon_df('energy_period',(43.489171,-125.152137))
            print(data_raw)

    def test_run_directional_wave_spectrum(self):
        with WaveX(self.wave_file, hsds=True) as rex_waves:
            data_raw = rex_waves.get_lat_lon_df('directional_wave_spectrum',(43.489171,-125.152137))
            print(data_raw)


if __name__ == '__main__':
    unittest.main()
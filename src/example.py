
from rex import WaveX

wave_file='/nrel/US_wave/virtual_buoy/West_Coast/West_Coast_virtual_buoy_2010.h5'
with WaveX(wave_file, hsds=True) as rex_waves:
    meta = rex_waves.meta
    time_index = rex_waves.time_index
    data_raw = rex_waves.get_lat_lon_df('directional_wave_spectrum',(43.489171,-125.152137))
    # data_raw = rex_waves.get_lat_lon_df('energy_period',(43.489171,-125.152137))

    print(data_raw)
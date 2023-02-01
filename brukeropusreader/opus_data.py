import numpy as np


class OpusData(dict):
    def get_range(self, spec_name="AB", wavenums=True):
        param_key = f"{spec_name} Data Parameter"
        fxv = self[param_key]["FXV"]
        lxv = self[param_key]["LXV"]
        # the number of points here is OK. It is "AB" that can return more values (equals to zero)
        npt = self[param_key]["NPT"]
        x_no_unit = np.linspace(fxv, lxv, npt)
        if wavenums:
            return x_no_unit
        else:
            return 10_000_000 / x_no_unit

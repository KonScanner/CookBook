import numpy as np
import sys
import re


class GreatCircle():
    """
    Please use format:
    e.g. (Default r == Earth)
    Windows:
    python haversine.py haversine 48.8566 2.3522 41.9028 12.4964
    or
    python haversine.py great-circle 48.8566 2.3522 41.9028 12.4964

    Linux:
    python3 haversine.py haversine 48.8566 2.3522 41.9028 12.4964
    or
    python3 haversine.py great-circle 48.8566 2.3522 41.9028 12.4964

    Assuming no surface irregularities (of which there are ...)
    For Mars (r = 3389.5 km or 3389500)
    python haversine.py haversine 48.8566 2.3522 41.9028 12.4964 3389500

    For Jupyter (r = 69,911 km or 69911000)
    python haversine.py haversine 48.8566 2.3522 41.9028 12.4964 69911000
    """

    @staticmethod
    def great_circle(lon1: float, lat1: float, lon2: float, lat2: float, r=6378.1e3) -> float:
        """
        The great_circle, computes the shortest distance path,
        of two points on the surface of a sphere. Assumes earth
        being spherical.

        Switch r for another planet.
        https://en.wikipedia.org/wiki/Great-circle_distance
        """
        lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
        return r*np.arccos(np.sin(lat1)*np.sin(lat2) + np.cos(lat1)*np.cos(lat2)*np.cos(lon1-lon2))

    @staticmethod
    def haversine(lon1: float, lat1: float, lon2: float, lat2: float, r=6378.1e3) -> float:
        """
        The haversine formula determines the great-circle distance
        between two points on a sphere given their longitudes and latitudes.
        Important in navigation, it is a special case of a more general formula
        in spherical trigonometry, the law of haversines, that relates the sides
        and angles of spherical triangles.
        Switch r for another planet.    
        https://en.wikipedia.org/wiki/Haversine_formula
        """
        lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * \
            np.cos(lat2) * np.sin(dlon / 2) ** 2
        return 2 * r * np.arcsin(np.sqrt(a))


if __name__ == "__main__":
    args = list(sys.argv)
    if (len(args) == 6) and (re.search(r'haver', str(sys.argv[1]), re.IGNORECASE)):
        lat_1 = float(sys.argv[2])
        long_1 = float(sys.argv[3])
        lat_2 = float(sys.argv[4])
        long_2 = float(sys.argv[5])
        print(
            f"{GreatCircle().haversine(lon1=long_1, lat1=lat_1, lon2=long_2, lat2=lat_2)/1e3:.3f} km")

    elif (len(args) == 6) and (re.search(r'great', str(sys.argv[1]), re.IGNORECASE)):
        lat_1 = float(sys.argv[2])
        long_1 = float(sys.argv[3])
        lat_2 = float(sys.argv[4])
        long_2 = float(sys.argv[5])
        print(
            f"{GreatCircle().great_circle(lon1=long_1, lat1=lat_1, lon2=long_2, lat2=lat_2)/1e3:.3f} km")

    elif (len(args) == 7) and (re.search(r'haver', str(sys.argv[1]), re.IGNORECASE)):
        lat_1 = float(sys.argv[2])
        long_1 = float(sys.argv[3])
        lat_2 = float(sys.argv[4])
        long_2 = float(sys.argv[5])
        r = float(sys.argv[6])
        print(
            f"{GreatCircle().haversine(lon1=long_1, lat1=lat_1, lon2=long_2, lat2=lat_2, r=r)/1e3:.3f} km")

    elif (len(args) == 7) and (re.search(r'great', str(sys.argv[1]), re.IGNORECASE)):
        lat_1 = float(sys.argv[2])
        long_1 = float(sys.argv[3])
        lat_2 = float(sys.argv[4])
        long_2 = float(sys.argv[5])
        r = float(sys.argv[6])
        print(
            f"{GreatCircle().great_circle(lon1=long_1, lat1=lat_1, lon2=long_2, lat2=lat_2, r=r)/1e3:.3f} km")

    else:
        eval("help(GreatCircle())")
        raise ValueError

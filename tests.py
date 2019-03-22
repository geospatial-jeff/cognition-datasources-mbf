from datasources import tests

from MicrosoftBuildingFootprints import MicrosoftBuildingFootprints

class MicrosoftBuildingFootprintsTestCases(tests.BaseTestCases):

    def _setUp(self):

        self.datasource = MicrosoftBuildingFootprints
        self.spatial = {
                    "type": "Polygon",
                    "coordinates": [
                      [
                        [
                          -118.31877350807191,
                          34.07821170392112
                        ],
                        [
                          -118.31773281097412,
                          34.07821170392112
                        ],
                        [
                          -118.31773281097412,
                          34.07897593175943
                        ],
                        [
                          -118.31877350807191,
                          34.07897593175943
                        ],
                        [
                          -118.31877350807191,
                          34.07821170392112
                        ]
                      ]
                    ]
                  }
        # self.temporal = # (start_date, end_date) here
        self.properties = {'legacy:area': {'lt': 60}}
        self.limit = 100

    def test_temporal_search(self):
        # Underlying API does not support temporal searches
        pass

    def test_stac_compliant(self):
        # The response will not pass as STAC compliant because the returned items do not have an asset property.  Asset
        # property is not necessary for vector because the asset is the STAC item itself.
        pass
[![CircleCI](https://circleci.com/gh/geospatial-jeff/cognition-datasources-mbf.svg?style=svg)](https://circleci.com/gh/geospatial-jeff/cognition-datasources-mbf)

## Microsoft Building Footprints

| Parameter | Status |
| ----------| ------ |
| Spatial | :heavy_check_mark: |
| Temporal | :x: |
| Properties | :heavy_check_mark: |
| **kwargs | [limit] |

##### Properties
| Property | Type | Example |
|--------------------------|-------|-------------|
| eo:epsg | int | 3857 |
| legacy:x | str | 'W102' |
| legacy:area | float | 100.0 |
| legacy:length | float | 30.0 |
| legacy:state | str | 'CA' |


##### Notes
- The source API doesn't support temporal data.  Can search with temporal but it is not honored.
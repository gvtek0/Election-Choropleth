# get US shape file
us_shape = gpd.read_file('../data/States 21basic/geo_export_65f74268-7da4-45cb-b582-640700c3c767.shp')
us_shape = us_shape[['state_name','geometry']]
us_shape.head()
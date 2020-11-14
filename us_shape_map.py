# plot the shape file with Folium
m = folium.Map(location=[50.77500, -100],zoom_start=3)
choropleth =folium.GeoJson(data= us_shape.to_json())
m.add_child(choropleth)
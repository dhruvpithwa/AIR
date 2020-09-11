from flask import Flask, render_template
import folium
import pandas as pd
import geopandas as gpd
import os


app = Flask(__name__)

@app.route('/')
def index():

    state_geo=gpd.read_file("file.json")


    m = folium.Map(location=[22.58988 ,78.13018],
                   tiles="stamen watercolor", 
                   attr="Choropleth Map", 
                   zoom_start=4,
                   width=500,
                   height=500,
                   zoom_control=False)

    choropleth=folium.Choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=state_geo,
        columns=["Name","ID"],
        key_on='feature.properties.Name',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='AQI',
        highlight=True,
        prefer_canvas=True
    ).add_to(m)

    folium.LayerControl().add_to(m)

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['Name','ID'])
    )

    
    m.save('templates/map.html')
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
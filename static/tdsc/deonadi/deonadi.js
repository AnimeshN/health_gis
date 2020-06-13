var geojson;
var searchControl;

const domain = ['https://makerghat.urbansciences.in/','http://localhost/'];
var rootUrl = domain[0] + 'geoserver/geonode/ows';
var defaultParameters = {
service: 'WFS',
version: '1.0.0',
request: 'GetFeature',
outputFormat: 'application/json'
};

var info = L.control();
var attribute_table = L.control({position: 'bottomright'});
var layer_name;


var LayerList = [];
var pointLayerList = [];
const LAT = 19.8427, LONG = 74.0770;

const TYPENAME = {'Deonadi Watershed Villages':'geonode:deonadi_villages',
'Deonadi Watershed Drainage':'geonode:deonadi_drainage',
'Deonadi Watershed Wells':'geonode:deonadi_wells',
'Deonadi Watershed Landuse 2005-06':'geonode:deonadi_landuse_2005_06',
'Deonadi Watershed Landuse 2011-12':'geonode:deonadi_landuse_2011_12',
'Deonadi Watershed Soil Depth':'geonode:deonadi_soil',
'Deonadi Watershed contour line':'deonadi_dem_countor_4326'
};
var tempParameter;
var soil_legend;


var num = null;


var deo = null;
// $('#selector button').click(function() {
//     clear_layer();
//     if(soil_legend){
//     mymap.removeControl(soil_legend);
//     } 
//     $(this).addClass('active').siblings().removeClass('active');
//     deo = this.innerHTML;

//     var tempParameter = defaultParameters;
//     if(deo === 'Drainage in deonadi basin'){
//         // tempParameter.typeName = TYPENAME[deo]; 
//         // displayPolygon(tempParameter);
//         putWMSLayer(TYPENAME[deo]);
//         tempParameter.typeName = 'geonode:devnadi_cachment_generated'; 
//         displayPolygon(tempParameter);      
//     }else if(deo === 'Wells in catchment area'){
//         tempParameter.typeName = 'geonode:devnadi_cachment_generated'; 
//         displayPolygon(tempParameter);
//         tempParameter.typeName = TYPENAME[deo]; 
//         displayPoints(tempParameter);
//     }else if(deo === 'Deonadi Basin Villages'){
//         tempParameter.typeName = TYPENAME[deo]; 
//         tempParameter.propertyName = 'the_geom,village_na,tot_popu,area_ha,net_area,forest,area_irri';
//         displayPolygon(tempParameter);  
//         delete tempParameter['propertyName'];
//     }else{
//         putWMSLayer(TYPENAME[deo]);

//     }

// });


$('#selector').change(function () {
    clear_layer();
    if(soil_legend){
    mymap.removeControl(soil_legend);
    }        
    var deo = document.getElementById('selector').value;
    var tempParameter = defaultParameters;
    if(deo === 'Deonadi Watershed Drainage'){
        // tempParameter.typeName = TYPENAME[deo]; 
        // displayPolygon(tempParameter);
        putWMSLayer(TYPENAME[deo]);
        tempParameter.typeName = 'geonode:devnadi_cachment_generated'; 
        displayPolygon(tempParameter);      
    }else if(deo === 'Deonadi Watershed Wells'){
        tempParameter.typeName = 'geonode:devnadi_cachment_generated'; 
        displayPolygon(tempParameter);
        tempParameter.typeName = TYPENAME[deo]; 
        displayPoints(tempParameter);
    }else if(deo === 'Deonadi Watershed Villages'){
        tempParameter.typeName = TYPENAME[deo]; 
        tempParameter.propertyName = 'the_geom,village_na,tot_popu,area_ha,net_area,forest,area_irri';
        displayPolygon(tempParameter);  
        delete tempParameter['propertyName'];
    }else{
        putWMSLayer(TYPENAME[deo]);

    }
});



function getColor(d) {
    return d > 6 ? '#FF0000' :
           d > 2  ? '#FFFF00' :
           d > -1  ? '#008000' :
                      '#FFEDA0';
}


function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function style(feature) {
    return {
        weight: 2,
        opacity: 1,
        color: "black",
        fillOpacity: 0
    };
}

function river_style(feature) {
    return {
        weight: 2,
        opacity: 1,
        color: 'blue',
        fillOpacity: 1
    };
}




function clear_layer(){
    LayerList.forEach(layer => mymap.removeLayer(layer));
}

function onEachFeaturePoint(feature, layer) {
	// does this feature have a property named popupContent?
		layer.bindPopup(feature.properties.Name);
	
}
var markerClusters = L.markerClusterGroup({"chunkedLoading": true});



function displayPoints(param){
mymap.spin(true,{lines: 9, length: 2, width: 20, scale: 60,radius: 70, color: "grey"});
var parameters = L.Util.extend(param);
point_url = rootUrl + L.Util.getParamString(parameters)
var geojsonMarkerOptions = {
	radius: 8,
	fillColor: "#ff7800",
	color: "#000",
	weight: 1,
	opacity: 1,
	fillOpacity: 0.8
};

fetch(point_url)
.then(
    function(response) {
    if (response.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' +
        response.status);
        return;
    }

    // Examine the text in the response
    response.json().then(function(stressData) {
        geojson = L.geoJson(stressData.features,{
	    pointToLayer: function (feature, latlng) {
		return L.circleMarker(latlng, geojsonMarkerOptions);
	},onEachFeature: onEachFeaturePoint
});

    markerClusters.addLayer(geojson);
    mymap.addLayer(markerClusters);
    LayerList.push(markerClusters);
    pointLayerList.push(geojson);
    mymap.spin(false);
    url = "";
    });


    }
)
.catch(function(err) {
    console.log('Fetch Error :-S', err);
});
// }

    
}


    
function addSearchControl(layer,propertyName){
    var searchControl = new L.Control.Search({
    layer: layer,
    propertyName: 'village_na',
    marker: false,
    moveToLocation: function(latlng, title, mymap) {
        //mymap.fitBounds( latlng.layer.getBounds() );
        console.log(latlng);
        var zoom = mymap.getBoundsZoom(latlng.layer.getBounds());
        mymap.setView(latlng, zoom); // access the zoom
    }
});
searchControl.on('search:locationfound', function(e) {
    e.layer.setStyle({fillColor: '#3f0', color: '#0f0'});
    if(e.layer._popup)
        e.layer.openPopup();

}).on('search:collapsed', function(e) {

    featuresLayer.eachLayer(function(layer) {	//restore feature color
        featuresLayer.resetStyle(layer);
    });	
});

return searchControl;
}

L.Map.include({
    hasSearchControl: function () {
        return (this.searchControl) ? true : false;
    }
});


function displayPolygon(param){
var parameters = L.Util.extend(param);
layer_url = rootUrl + L.Util.getParamString(parameters)

mymap.spin(true,{lines: 9, length: 2, width: 20, scale: 60,radius: 70, color: "grey"});

fetch(layer_url)
.then(
    function(response) {
    if (response.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' +
        response.status);
        return;
    }

    // Examine the text in the response
    response.json().then(function(geojsonData) {
        // console.log(geojsonData)
        mymap.setView([LAT, LONG], 12);
        if(param.typeName === 'geonode:deonadi_villages'){
            propertyName = '';
            geojson = L.geoJson(geojsonData.features, {
                style : style,
                onEachFeature: onEachFeature
            });

            info.addTo(mymap);
            if(typeof searchControl === 'undefined'){
                searchControl = addSearchControl(geojson,'village_na');
                mymap.addControl(searchControl);
            }
            
            


        }else if(param.typeName === 'geonode:major_streams_dev'){
        geojson = L.geoJson(geojsonData.features, {style : river_style}); 
        }else{
        geojson = L.geoJson(geojsonData.features, {
        style : style,
    });
          
        }

    mymap.addLayer(geojson);

    mymap.spin(false);
    LayerList.push(geojson);

    });


    }
)
.catch(function(err) {
    console.log('Fetch Error :-S', err);
});

    
}

function zoomToFeature(e) {
    mymap.fitBounds(e.target.getBounds());
}


function addWMSLegend(layer){
    lagendGraphic = "https://makerghat.urbansciences.in/geoserver/wms?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH=20&HEIGHT=20&LAYER="+layer;
    soil_legend = L.wmsLegend(lagendGraphic);
}
function putWMSLayer(layer){
      
            var wms_layer = L.tileLayer.wms('https://makerghat.urbansciences.in/geoserver/wms', {
            layers: layer,
            format: 'image/png',
            transparent: true,
            style:""
            });
            wms_layer.addTo(mymap);
            LayerList.push(wms_layer);
            addWMSLegend(layer);
            
            


    }

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });

    layer.bindTooltip("<div style = 'text-transform: capitalize'>"+feature.properties.village_na+"</div>",{permanent: true, 
   direction: "center",
   className: "my-labels"});
   

}
function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5        
    });
    info.update(layer.feature.properties);
    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}



var info = L.control({position: 'bottomleft'});

info.onAdd = function (mymap) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};


info.update = function (props) {
    this._div.innerHTML = '' +  (props ?
    "<table class = 'info-class' ><tr><td>Village Name</td><td style = 'text-transform: capitalize'><b>"+props.village_na+"<b></td></tr>"+
        "<tr><td>Total Population</td><td>"+props.tot_popu+"</td></tr>"+
        "<tr><td>Area:</td><td>"+props.area_ha+"</td></tr>"+
        "<tr><td>Net Area Sown (in Hectares)</td><td>"+props.net_area+"</td></tr>"+
        "<tr><td>Forest Area (in Hectares)</td><td>"+props.forest+"</tr>"+
        "<tr><td>Area Irrigated by Source (in Hectares)<b></td><td>"+props.area_irri+"</td></tr></table>"
        : 'Hover over a village');
};

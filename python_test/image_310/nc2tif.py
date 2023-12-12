import numpy as np
import netCDF4 as nc
import matplotlib
from matplotlib import ticker, cm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from osgeo import gdal, osr
import os

os.environ['PROJ_LIB'] = r'C:\Users\HTHT\anaconda3\envs\image\Library\share\proj'

matplotlib.use('TkAgg')

out_dir = r"E:\HTHTProject\TJHT_Project\OtherFile\ziliao\nc\nc_tif"
nc_u_path = r"E:\HTHTProject\TJHT_Project\OtherFile\ziliao\nc\era5.10m_u_component_of_wind.20000101.nc"
nc_v_path = r"E:\HTHTProject\TJHT_Project\OtherFile\ziliao\nc\era5.10m_v_component_of_wind.20000101.nc"
nc_name = os.path.basename(nc_u_path)

nc_u_ds = nc.Dataset(nc_u_path)

nc_lon = nc_u_ds.variables['longitude'][:]
nc_lat = nc_u_ds.variables['latitude'][:]
nc_time = nc_u_ds.variables['time'][:]
nc_u_data = nc_u_ds.variables['u10'][:]

lon_min, lon_max, lat_min, lat_max = [nc_lon.min(), nc_lon.max(), nc_lat.min(), nc_lat.max()]
tif_width = nc_lon.size
tif_height = nc_lat.size
tif_rx = (lon_max - lon_min) / tif_width
tif_ry = (lat_max - lat_min) / tif_height

driver = gdal.GetDriverByName('GTiff')

# index = 0
# for index_data in nc_u_data:
#     out_tif_name =out_dir + '/' + nc_name + '_' + str(index) + '.tif'
#     out_tif = driver.Create(out_tif_name, tif_width, tif_height, 1, gdal.GDT_Float32)
#     geotransform = (lon_min, tif_rx, 0.0, lat_max, 0.0, -tif_ry)
#     out_tif.SetGeoTransform(geotransform)
#     #定义投影
#     prj = osr.SpatialReference()
#     prj.ImportFromEPSG(4326)
#     out_tif.SetProjection(prj.ExportToWkt())
#     #数据导出
#     out_tif.GetRasterBand(1).WriteArray(index_data)
#     out_tif.GetRasterBand(1).SetNoDataValue(-9999)
#     out_tif.FlushCache()
#     del out_tif
#     index = index + 1

out_tif_name =out_dir + '/' + nc_name + '.tif'
out_tif = driver.Create(out_tif_name, tif_width, tif_height, nc_time.size, gdal.GDT_Float32)

geotransform = (lon_min, tif_rx, 0.0, lat_max, 0.0, -tif_ry)
out_tif.SetGeoTransform(geotransform)

#定义投影
prj = osr.SpatialReference()
prj.ImportFromEPSG(4326)
out_tif.SetProjection(prj.ExportToWkt())

#数据导出
index = 1
for index_data in nc_u_data:
    out_tif.GetRasterBand(index).WriteArray(index_data)
    out_tif.GetRasterBand(index).SetNoDataValue(-9999)
    index = index + 1

out_tif.FlushCache()
del out_tif
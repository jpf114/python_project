import numpy as np
import netCDF4 as nc
import matplotlib
from matplotlib import ticker, cm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

matplotlib.use('TkAgg')

nc_u_path = r"E:\HTHTProject\TJHT_Project\OtherFile\ziliao\nc\era5.10m_u_component_of_wind.20000101.nc"
nc_v_path = r"E:\HTHTProject\TJHT_Project\OtherFile\ziliao\nc\era5.10m_v_component_of_wind.20000101.nc"
nc_u_ds = nc.Dataset(nc_u_path)
nc_v_ds = nc.Dataset(nc_v_path)

nc_lon = nc_u_ds.variables['longitude']
nc_lat = nc_u_ds.variables['latitude']
nc_lat_r = np.flip(nc_lat)
nc_time = nc_u_ds.variables['time'][:]

nc_u_data = nc_u_ds.variables['u10'][:]
#np.squeeze(nc_u_data, 0) #去掉一个维度
nc_u_data_0 = nc_u_data[0]
nc_v_data = nc_v_ds.variables['v10'][:]

# fig, ax = plt.subplots()
# cs = ax.contourf(nc_lon, nc_lat, nc_u_data_0, locator=ticker.LogLocator(), cmap=cm.PuBu_r)
#
# cbar = fig.colorbar(cs)
# plt.show()

fig, ax = plt.subplots()

u_data = np.flipud(nc_u_data[0])
v_data = np.flipud(nc_v_data[0])
strm = ax.streamplot(nc_lon, nc_lat_r, u_data, v_data)
fig.colorbar(strm.lines)
ax.set_title("sl")
plt.show()


# fig = plt.figure(figsize=(12, 8))
# gs = gridspec.GridSpec(nrows=4, ncols=6, height_ratios=[1, 1, 1, 1])

# ax0 = fig.add_subplot(gs[0, 1])
# cs = ax0.contourf(nc_lon, nc_lat, nc_u_data_0, locator=ticker.LogLocator(), cmap=cm.PuBu_r)
# fig.colorbar(cs)
# ax0.set_title('Varying Color')

# for index in range(nc_time.size):
#     loc_x = int(index / gs.ncols)
#     loc_y = int(index % gs.ncols)
#     ax0 = fig.add_subplot(gs[loc_x, loc_y])
#     u_data = np.flipud(nc_u_data[index])
#     v_data = np.flipud(nc_v_data[index])
#     strm = ax0.streamplot(nc_lon, nc_lat_r, u_data, v_data)
#     fig.colorbar(strm.lines)
#     ax0.set_title("Time(%d)" % index)
#     index = index + 1

# plt.tight_layout()
# plt.show()
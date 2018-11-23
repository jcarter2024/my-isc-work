import netCDF4
ds = netCDF4.Dataset('/home/user01/ncas-isc/python/exercises/example_data/ggas2014121200_00-18.nc')    
for v in ds.variables:
    print(v)

sst = ds.variables["SSTK"]
print(sst)

for d in sst.dimensions:
    print(d, len(ds.variables[d]))

print(sst.shape, sst.size)

for attr in sst.ncattrs():
    print(attr, '=', getattr(sst, attr))


#now we extract some data
arr = sst[1, 0, 10:20, 30:35]
print(type(arr))

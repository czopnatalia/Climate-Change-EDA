import xarray as xr
from pathlib import Path

base_dir = Path(r"C:/IiAD/uczenie_maszynowe/klimat_projekt/all_data") 

datasets = []

for folder in sorted(base_dir.iterdir()):
    if not folder.is_dir():
        continue

    # Wyszukiwanie plików
    instant_files = list(folder.glob("data_stream-oper_stepType-instant.nc"))
    accum_files   = list(folder.glob("data_stream-oper_stepType-accum.nc"))

    # Jeśli brakuje któregoś pliku → pomijamy folder
    if not instant_files or not accum_files:
        print(f"⚠️ W folderze {folder.name} nie znaleziono wymaganych plików — pomijam.")
        continue

    instant_file = instant_files[0]
    accum_file   = accum_files[0]

    # Wczytanie
    ds_instant = xr.open_dataset(instant_file, chunks={"valid_time": 365})
    ds_accum   = xr.open_dataset(accum_file,   chunks={"valid_time": 365})

    # Ujednolicenie nazw czasu (czasem w accum może być 'time')
    if "time" in ds_instant:
        ds_instant = ds_instant.rename({"time": "valid_time"})
    if "time" in ds_accum:
        ds_accum = ds_accum.rename({"time": "valid_time"})
        
    # Usuwamy expver
    if "expver" in ds_instant.variables:
        ds_instant = ds_instant.drop_vars("expver")
    if "expver" in ds_accum.variables:
        ds_accum = ds_accum.drop_vars("expver")

    # Łączenie zmiennych z tego samego roku
    ds_year = xr.merge([ds_instant, ds_accum], compat="override")
    datasets.append(ds_year)


# Sklejenie datasetów po czasie
ds_all = xr.concat(datasets, dim="valid_time")

# Posortowanie dat (ważne)
ds_all = ds_all.sortby("valid_time")

# Zapis do jednego pliku
output_file = base_dir / "era5_nowy_sacz_all_years.nc"
ds_all.to_netcdf(output_file)

print(f"\nGOTOWE! Dane zapisane do pliku:\n   {output_file}")

import pandas as pd
import numpy as np

data = pd.read_json("final_dataset.json")

data.drop_duplicates("PropertyId",inplace=True)
data.update(data[["BathroomCount","Fireplace","Furnished","Garden","GardenArea","SwimmingPool","Terrace","ToiletCount"]].fillna(0))

data.drop(data[data.BathroomCount > data.BedroomCount].index,inplace=True)
data.drop(data[data.ConstructionYear > 2033].index,inplace=True)
data.drop(data[data.GardenArea > data.SurfaceOfPlot].index,inplace=True)
data.drop(data[data.PostalCode < 1000].index,inplace=True)
data.drop(data[data.NumberOfFacades > 4].index,inplace=True)
data.drop(data[data.Price > 15000000].index,inplace=True)
data.drop(data[data.ToiletCount > 58].index,inplace=True)
data.drop(data[data.ShowerCount > 58].index,inplace=True)
data.drop(data[data.LivingArea > 8800].index, inplace=True)
data.drop(data[data.TypeOfSale == "annuity_monthly_amount"].index,inplace=True)
data.drop(data[data.TypeOfSale == "annuity_without_lump_sum"].index,inplace=True)
data.drop(data[data.TypeOfSale == "annuity_lump_sum"].index,inplace=True)

sale_data = data[data.TypeOfSale == "residential_sale"]
rent_data = data[data.TypeOfSale == "residential_monthly_rent"]

municipality_name = pd.read_excel("Conversion Postal code_Refnis code_va01012019.xlsx")
zip_code = municipality_name[["Postal code", "Nom commune","Refnis code"]]
zip_code.rename(columns={"Postal code": "PostalCode"}, inplace=True)

data_municipality_rent = pd.merge(rent_data,zip_code,on="PostalCode",how='inner')
data_municipality_rent = data_municipality_rent.drop_duplicates("PropertyId")

data_municipality = pd.merge(sale_data,zip_code,on="PostalCode",how='inner')
data_municipality = data_municipality.drop_duplicates("PropertyId")

municipality_price_m2_rent = data_municipality_rent[["Price","Nom commune","LivingArea","Province"]]
municipality_price_m2_rent.drop(municipality_price_m2_rent[municipality_price_m2_rent["Price"] < 195].index, inplace=True)
municipality_price_m2_rent.drop(municipality_price_m2_rent[municipality_price_m2_rent["Price"] > 18000].index, inplace=True)
municipality_price_m2_rent = data_municipality_rent.groupby("Nom commune",as_index=False)[["Price","LivingArea"]].mean()
municipality_price_m2_rent["Refnis code"] = data_municipality_rent["Refnis code"]
municipality_price_m2_rent["Province"] = data_municipality_rent["Province"]
municipality_price_m2_rent["€/m2"] = municipality_price_m2_rent["Price"] / municipality_price_m2_rent["LivingArea"]

municipality_price_m2 = data_municipality[["LivingArea","Price","Nom commune","Province"]]
# municipality_price_m2.drop(municipality_price_m2_rent[municipality_price_m2_rent["Price"] < 195].index, inplace=True)
# municipality_price_m2.drop(municipality_price_m2_rent[municipality_price_m2_rent["Price"] > 50000].index, inplace=True)
municipality_price_m2 = data_municipality.groupby("Nom commune",as_index=False)[["LivingArea","Price"]].sum()
municipality_price_m2["Refnis code"] = data_municipality["Refnis code"]
municipality_price_m2["Province"] = data_municipality["Province"]
municipality_price_m2["€/m2"] = municipality_price_m2["Price"] / municipality_price_m2["LivingArea"]
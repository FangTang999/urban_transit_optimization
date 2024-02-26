import pandas as pd

# 1. Read zone.csv
zone_df = pd.read_csv('./BART_with_TAZ/zone.csv')

# 2. generate OD pairs for o_zone_id and d_zone_id
# generate all possible OD pairs using pd.MultiIndex.from_product
zone_pairs = pd.MultiIndex.from_product([zone_df['zone_id'], zone_df['zone_id']], names=['o_zone_id', 'd_zone_id']).to_frame(index=False)

# filter out the OD pairs when o_zone_id == d_zone_id
zone_pairs = zone_pairs[zone_pairs['o_zone_id'] != zone_pairs['d_zone_id']]

# 3. default OD volume is 10
zone_pairs['volume'] = 10

# show results
print(zone_pairs)

zone_pairs.to_csv('./BART_with_TAZ/demand.csv', index=False)

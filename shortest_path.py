# Date: Feb 25, 2024
# Fang Tang, tangfangseu@gmail.com

# This code is to find the shortest path for OD pairs

import path4gmns as pg
import pandas as pd

network = pg.read_network(input_dir='./PHX_without_TAZ')
demand_data = pd.read_csv('./PHX_without_TAZ/demand.csv')

results = []

for index, row in demand_data.iterrows():
    o_zone_id, d_zone_id = row['o_zone_id'], row['d_zone_id']

    # distance and node sequence of shortest path
    node_path = network.find_shortest_path(o_zone_id, d_zone_id)
    print(f'\nshortest path (node id) from zone {o_zone_id} to zone {d_zone_id}: {node_path}')

    # distance and link sequence of shortest path
    link_path = network.find_shortest_path(o_zone_id, d_zone_id, seq_type='link')
    print(f'shortest path (link id) from zone {o_zone_id} to zone {d_zone_id}: {link_path}')

    # export distance, node sequence, and link sequence
    distance_with_unit = node_path.split(' | ')[0].split(': ')[1]
    distance = distance_with_unit.split(' ')[0]
    node_sequence = node_path.split(' | ')[1].split(': ')[1]
    link_sequence = link_path.split(' | ')[1].split(': ')[1]

    # merge results to list
    results.append({
        'o_zone_id': o_zone_id,
        'd_zone_id': d_zone_id,
        'distance': distance,
        'node_sequence': node_sequence,
        'link_sequence': link_sequence
    })

# convert list to DataFrame
results_df = pd.DataFrame(results)

# define the path of output file
output_file_path = './PHX_without_TAZ/shortest_path.csv'

# save DataFrame to CVS file
results_df.to_csv(output_file_path, index=False)

print(f'Results saved to {output_file_path}')
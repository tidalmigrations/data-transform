# CSV => JSON Generator for tidal apps sync command
# In the CSV, the first row can by the titles given by the client for the column
# The second row should be the tidal attribute to map the column data to tidal attributes
# Columns to be ignored should be left blank
# Rows with blank data will be skipped as well


import csv
import json
import sys

tidal_built_in_types = [
    "name", 
    "description", 
    "technical_lead", 
    "business_owner",
    "transition_overview",
    "transition_plan_complete",
    "transition_type",
    "database_size_mb",
    "forecast_midpoint_cost",
    "source_code_location",
    "paas_readiness",
    "roadblocks",
    "migration_effort_estimate",
    "total_users",
    "revenue",
    "person_hours_saved",
    "regulated_requirements",
    "annual_hosting_costs",
    "annual_staff_costs",
    "uptime_requirements",
    "data_sensitivity",
    "frequency_of_deployments",
    "pii",
    "legal_holds",
    "cots",
    "source_code_controlled",
    "continuous_delivery",
    "business_continuity_plan",
    "can_run_on_linux",
    "end_of_support_date",
    "environment",
    "move_group",
    "technical_lead",
    "business_owner",
    "technologies",
    "project",
    "clouds",
    "urls",
    "customers",
    "servers",
    "database_instances"
    ]

output = {}
output['apps'] = []

filename= "Tidal_Import_2021-03-17.xlsx - General info"

with open(f'{filename}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    column_attribute_map = []
    for row_num, row_data in enumerate(csv_reader):
        outrow = {}
        custom_field_row = {}
        
        if row_num == 0:                 # The title row, skip
            continue
        elif row_num == 1:               # the mapping row
            column_attribute_map = row_data
            continue
        else:
            for col_num, col_data  in enumerate(row_data):
                if len(col_data) == 0 or col_num < len(column_attribute_map) or column_attribute_map[col_num] is None :    # empty or outside the last mapped column, skip
                    continue                
                col_tidal_attribute = column_attribute_map[col_num]
                if col_tidal_attribute in tidal_built_in_types:
                    if col_tidal_attribute in "total_users":     # script assumes strings but this isn't
                        outrow[col_tidal_attribute] = int(col_data)
                    else:
                        outrow[col_tidal_attribute] = col_data
                else:               
                    custom_field_row[col_tidal_attribute] = col_data
        
        if len(custom_field_row) > 0:
            outrow['custom_fields'] = custom_field_row

        output['apps'].append(outrow)

with open(f'{filename}.json', 'w') as outfile:
    json.dump(output, outfile)
    
    print(f'Processed {row_num-1} row of data and wrote to {filename}.json')





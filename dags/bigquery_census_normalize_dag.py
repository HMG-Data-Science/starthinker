###########################################################################
#
#  Copyright 2019 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################
"""--------------------------------------------------------------

Before running this Airflow module...

  Install StarThinker in cloud composer from open source:

    pip install git+https://github.com/google/starthinker

  Or push local code to the cloud composer plugins directory:

    source install/deploy.sh
    4) Composer Menu
    l) Install All

--------------------------------------------------------------

Census Data Normalized

Convert given census table to percent of population, normalizing it.

Specify the geography, year, and span that make up the <a
href='https://pantheon.corp.google.com/bigquery?redirect_from_classic=true&p=bigquery-public-data&d=census_bureau_acs&page=dataset'
target='_blank'>census table names</a>.
Not every combination of geography, year, and span exists or contains all the
required fields.
Every time the query runs it will overwrite the table.

"""

from starthinker_airflow.factory import DAG_Factory

# Add the following credentials to your Airflow configuration.
USER_CONN_ID = 'starthinker_user'  # The connection to use for user authentication.
GCP_CONN_ID = 'starthinker_service'  # The connection to use for service authentication.

INPUTS = {
    'auth_write': 'service',  # Credentials used for writing data.
    'census_geography': 'zip_codes',  # Census table to get data from.
    'census_year': '2018',  # Census table to get data from.
    'census_span': '5yr',  # Census table to get data from.
    'dataset': '',  # Existing BigQuery dataset.
    'table': '',  # Table to create from this census_data.
}

TASKS = [{
    'bigquery': {
        'auth': {
            'field': {
                'name': 'auth_write',
                'kind': 'authentication',
                'order': 0,
                'default': 'service',
                'description': 'Credentials used for writing data.'
            }
        },
        'from': {
            'query':
                '           SELECT             geo_id AS Geo_ID,              '
                '/* gender */             SAFE_DIVIDE(female_pop, total_pop) '
                'AS Female_Percent,             SAFE_DIVIDE(male_pop, '
                'total_pop) AS Male_Percent,                          /* age '
                '*/             SAFE_DIVIDE(population_1_year_and_over , '
                'total_pop) AS Population_1_Year_And_Over_Percent,'
                '             SAFE_DIVIDE(population_3_years_over , total_pop)'
                ' AS Population_3_Years_And_Over_Percent,             '
                'SAFE_DIVIDE(pop_5_years_over , total_pop) AS '
                'Population_5_Years_And_Over_Percent,             '
                'SAFE_DIVIDE(pop_15_and_over , total_pop) AS '
                'Population_15_Years_And_Over_Percent,             '
                'SAFE_DIVIDE(pop_16_over , total_pop) AS '
                'Population_16_Years_And_Over_Percent,             '
                'SAFE_DIVIDE(pop_25_years_over , total_pop) AS '
                'Population_25_Years_And_Over_Percent,             '
                'SAFE_DIVIDE(pop_25_64 , total_pop) AS '
                'Population_25_To_64_Percent,                              /* '
                'male age */             SAFE_DIVIDE(male_5_to_9 , total_pop) '
                'AS Male_5_To_9_Percent,             SAFE_DIVIDE(male_10_to_14'
                ' , total_pop) AS Male_10_To_14_Percent,             '
                'SAFE_DIVIDE(male_15_to_17 , total_pop) AS '
                'Male_15_To_17_Percent,             SAFE_DIVIDE(male_18_to_19 '
                ', total_pop) AS Male_18_To_19_Percent,             '
                'SAFE_DIVIDE(male_20 , total_pop) AS Male_20_Percent,'
                '             SAFE_DIVIDE(male_21 , total_pop) AS '
                'Male_21_Percent,             SAFE_DIVIDE(male_22_to_24 , '
                'total_pop) AS Male_22_To_24_Percent,             '
                'SAFE_DIVIDE(male_25_to_29 , total_pop) AS '
                'Male_25_To_29_Percent,             SAFE_DIVIDE(male_30_to_34 '
                ', total_pop) AS Male_30_To_34_Percent,             '
                'SAFE_DIVIDE(male_35_to_39 , total_pop) AS '
                'Male_35_To_39_Percent,             SAFE_DIVIDE(male_40_to_44 '
                ', total_pop) AS Male_40_To_44_Percent,             '
                'SAFE_DIVIDE(male_45_to_49 , total_pop) AS '
                'Male_45_To_49_Percent,             SAFE_DIVIDE(male_50_to_54 '
                ', total_pop) AS Male_50_To_54_Percent,             '
                'SAFE_DIVIDE(male_55_to_59 , total_pop) AS '
                'Male_55_To_59_Percent,             SAFE_DIVIDE(male_65_to_66 '
                ', total_pop) AS Male_65_To_66_Percent,             '
                'SAFE_DIVIDE(male_67_to_69 , total_pop) AS '
                'Male_67_To_69_Percent,             SAFE_DIVIDE(male_70_to_74 '
                ', total_pop) AS Male_70_To_74_Percent,             '
                'SAFE_DIVIDE(male_75_to_79 , total_pop) AS '
                'Male_75_To_79_Percent,             SAFE_DIVIDE(male_80_to_84 '
                ', total_pop) AS Male_80_To_84_Percent,             '
                'SAFE_DIVIDE(male_85_and_over , total_pop) AS '
                'Male_85_And_Over_Percent,                          /* female '
                'age */             SAFE_DIVIDE(female_5_to_9 , total_pop) AS '
                'Female_5_To_9_Percent,             '
                'SAFE_DIVIDE(female_10_to_14 , total_pop) AS '
                'Female_10_To_14_Percent,             '
                'SAFE_DIVIDE(female_15_to_17 , total_pop) AS '
                'Female_15_To_17_Percent,             '
                'SAFE_DIVIDE(female_18_to_19 , total_pop) AS '
                'Female_18_To_19_Percent,             SAFE_DIVIDE(female_20 , '
                'total_pop) AS Female_20_Percent,             '
                'SAFE_DIVIDE(female_21 , total_pop) AS Female_21_Percent,'
                '             SAFE_DIVIDE(female_22_to_24 , total_pop) AS '
                'Female_22_To_24_Percent,             '
                'SAFE_DIVIDE(female_25_to_29 , total_pop) AS '
                'Female_25_To_29_Percent,             '
                'SAFE_DIVIDE(female_30_to_34 , total_pop) AS '
                'Female_30_To_34_Percent,             '
                'SAFE_DIVIDE(female_35_to_39 , total_pop) AS '
                'Female_35_To_39_Percent,             '
                'SAFE_DIVIDE(female_40_to_44 , total_pop) AS '
                'Female_40_To_44_Percent,             '
                'SAFE_DIVIDE(female_45_to_49 , total_pop) AS '
                'Female_45_To_49_Percent,             '
                'SAFE_DIVIDE(female_50_to_54 , total_pop) AS '
                'Female_50_To_54_Percent,             '
                'SAFE_DIVIDE(female_55_to_59 , total_pop) AS '
                'Female_55_To_59_Percent,             '
                'SAFE_DIVIDE(female_65_to_66 , total_pop) AS '
                'Female_65_To_66_Percent,             '
                'SAFE_DIVIDE(female_67_to_69 , total_pop) AS '
                'Female_67_To_69_Percent,             '
                'SAFE_DIVIDE(female_70_to_74 , total_pop) AS '
                'Female_70_To_74_Percent,             '
                'SAFE_DIVIDE(female_75_to_79 , total_pop) AS '
                'Female_75_To_79_Percent,             '
                'SAFE_DIVIDE(female_80_to_84 , total_pop) AS '
                'Female_80_To_84_Percent,             '
                'SAFE_DIVIDE(female_85_and_over , total_pop) AS '
                'Female_85_And_Over_Percent,                          /* race '
                '*/             SAFE_DIVIDE(white_pop , total_pop) AS '
                'White_Percent,             SAFE_DIVIDE(black_pop , total_pop)'
                ' AS Black_Percent,             SAFE_DIVIDE(asian_pop , '
                'total_pop) AS Asian_Percent,             '
                'SAFE_DIVIDE(hispanic_pop , total_pop) AS Hispanic_Percent,'
                '             SAFE_DIVIDE(amerindian_pop , total_pop) AS '
                'American_Indian_Percent,             '
                'SAFE_DIVIDE(other_race_pop , total_pop) AS Other_Percent,'
                '               SAFE_DIVIDE(two_or_more_races_pop , total_pop)'
                ' AS Two_or_More_Races_Percent,               '
                'SAFE_DIVIDE(hispanic_any_race , total_pop) AS '
                'Hipanic_Any_Percent,               '
                'SAFE_DIVIDE(not_hispanic_pop , total_pop) AS '
                'Not_Hispanic_Percent,                            /* race age '
                '*/             SAFE_DIVIDE(asian_male_45_54 , total_pop) AS '
                'Asian_Male_45_54_Percent,             '
                'SAFE_DIVIDE(asian_male_55_64 , total_pop) AS '
                'Asian_Male_55_64_Percent,             '
                'SAFE_DIVIDE(black_male_45_54 , total_pop) AS '
                'Black_Male_45_54_Percent,             '
                'SAFE_DIVIDE(black_male_55_64 , total_pop) AS '
                'Black_Male_55_64_Percent,             '
                'SAFE_DIVIDE(hispanic_male_45_54 , total_pop) AS '
                'Hispanic_Male_45_54_Percent,             '
                'SAFE_DIVIDE(hispanic_male_55_64 , total_pop) AS '
                'Hispanic_Male_55_64_Percent,               '
                'SAFE_DIVIDE(white_male_45_54 , total_pop) AS '
                'White_Male_45_54_Percent,               '
                'SAFE_DIVIDE(white_male_55_64 , total_pop) AS '
                'White_Male_55_64_Percent,                            /* '
                'income */             SAFE_DIVIDE(income_less_10000 , '
                'total_pop) AS Income_Less_10000_Percent,             '
                'SAFE_DIVIDE(income_10000_14999 , total_pop) AS '
                'Income_10000_14999_Percent,             '
                'SAFE_DIVIDE(income_15000_19999 , total_pop) AS '
                'Income_15000_19999_Percent,             '
                'SAFE_DIVIDE(income_20000_24999 , total_pop) AS '
                'Income_20000_24999_Percent,             '
                'SAFE_DIVIDE(income_25000_29999 , total_pop) AS '
                'Income_25000_29999_Percent,             '
                'SAFE_DIVIDE(income_30000_34999 , total_pop) AS '
                'Income_30000_34999_Percent,               '
                'SAFE_DIVIDE(income_35000_39999 , total_pop) AS '
                'Income_35000_39999_Percent,               '
                'SAFE_DIVIDE(income_40000_44999 , total_pop) AS '
                'Income_40000_44999_Percent,               '
                'SAFE_DIVIDE(income_45000_49999 , total_pop) AS '
                'Income_45000_49999_Percent,               '
                'SAFE_DIVIDE(income_50000_59999 , total_pop) AS '
                'Income_50000_59999_Percent,             '
                'SAFE_DIVIDE(income_60000_74999 , total_pop) AS '
                'Income_60000_74999_Percent,             '
                'SAFE_DIVIDE(income_75000_99999 , total_pop) AS '
                'Income_75000_99999_Percent,             '
                'SAFE_DIVIDE(income_100000_124999 , total_pop) AS '
                'Income_100000_129999_Percent,             '
                'SAFE_DIVIDE(income_125000_149999 , total_pop) AS '
                'Income_125000_149999_Percent,             '
                'SAFE_DIVIDE(income_150000_199999 , total_pop) AS '
                'Income_150000_199999_Percent,             '
                'SAFE_DIVIDE(income_200000_or_more , total_pop) AS '
                'Income_200000_Or_More_Percent,               '
                'SAFE_DIVIDE(poverty , total_pop) AS Poverty_Percent,'
                '             gini_index as Gini_Index,'
                '                          /* housing */             '
                'SAFE_DIVIDE(occupied_housing_units , housing_units ) AS '
                'Occupied_Housing_Units_Percent,             '
                'SAFE_DIVIDE(housing_units_renter_occupied , housing_units) AS'
                ' Housing_Units_Renter_Occupied_Percent,             '
                'SAFE_DIVIDE(vacant_housing_units , housing_units) AS '
                'Vacant_Housing_Units_Percent,             '
                'SAFE_DIVIDE(vacant_housing_units_for_rent , housing_units) AS'
                ' Vacant_Housing_Units_For_Rent_Percent,             '
                'SAFE_DIVIDE(vacant_housing_units_for_sale , housing_units) AS'
                ' Vacant_Housing_Units__For_Sale_Percent,             '
                'SAFE_DIVIDE(dwellings_1_units_detached , housing_units) AS '
                'Dwellings_1_Units_Detached_Percent,               '
                'SAFE_DIVIDE(dwellings_1_units_attached , housing_units) AS '
                'Dwellings_1_Units_Attached_Percent,               '
                'SAFE_DIVIDE(dwellings_2_units , housing_units) AS '
                'Dwellings_2_Units_Percent,               '
                'SAFE_DIVIDE(dwellings_3_to_4_units , housing_units) AS '
                'Dwellings_3_To_4_Units_Percent,               '
                'SAFE_DIVIDE(dwellings_5_to_9_units , housing_units) AS '
                'Dwellings_5_To_9_Units_Percent,             '
                'SAFE_DIVIDE(dwellings_10_to_19_units , housing_units) AS '
                'Dwellings_10_To_19_Units_Percent,             '
                'SAFE_DIVIDE(dwellings_20_to_49_units , housing_units) AS '
                'Dwellings_20_To_49_Units_Percent,             '
                'SAFE_DIVIDE(dwellings_50_or_more_units , housing_units) AS '
                'Dwellings_50_or_More_Units_Percent,             '
                'SAFE_DIVIDE(mobile_homes , housing_units) AS '
                'Mobile_Homes_Percent,             '
                'SAFE_DIVIDE(housing_built_2005_or_later , housing_units) AS '
                'Housing_Built_2005_Or_Later_Percent,             '
                'SAFE_DIVIDE(housing_built_2000_to_2004 , housing_units) AS '
                'Housing_Built_2000_To_2004_Percent,               '
                'SAFE_DIVIDE(housing_built_1939_or_earlier , housing_units ) '
                'AS Housing_Built_1939_Or_Earlier_Percent,'
                '                          SAFE_DIVIDE(rent_over_50_percent , '
                'housing_units) AS Rent_Over_50_Percent,             '
                'SAFE_DIVIDE(rent_40_to_50_percent , housing_units) AS '
                'Rent_40_To_50_Percent,             '
                'SAFE_DIVIDE(rent_35_to_40_percent , housing_units) AS '
                'Rent_35_To_40_Percent,             '
                'SAFE_DIVIDE(rent_30_to_35_percent , housing_units) AS '
                'Rent_30_To_35_Percent,             '
                'SAFE_DIVIDE(rent_25_to_30_percent , housing_units) AS '
                'Rent_25_To_30_Percent,               '
                'SAFE_DIVIDE(rent_20_to_25_percent , housing_units) AS '
                'Rent_20_To_25_Percent,               '
                'SAFE_DIVIDE(rent_15_to_20_percent , housing_units) AS '
                'Rent_15_To_20_Percent,               '
                'SAFE_DIVIDE(rent_10_to_15_percent , housing_units) AS '
                'Rent_10_To_15_Percent,               '
                'SAFE_DIVIDE(rent_under_10_percent , housing_units) AS '
                'Rent_Under_10_Percent,             '
                'SAFE_DIVIDE(rent_burden_not_computed , housing_units) AS '
                'Rent_Burden_Not_Computed_Percent,                        '
                'SAFE_DIVIDE(owner_occupied_housing_units , housing_units) AS '
                'Owner_occupied_Housing_Units_Percent,             '
                'SAFE_DIVIDE(million_dollar_housing_units , housing_units) AS '
                'Million_Dollar_Housing_Units_Percent,             '
                'SAFE_DIVIDE(mortgaged_housing_units , housing_units) AS '
                'Mortgaged_Housing_Units_Percent,             '
                'percent_income_spent_on_rent AS Spent_on_Rent_Percent,'
                '             SAFE_DIVIDE(group_quarters , total_pop) AS '
                'Group_Quarters_Percent,                         '
                'SAFE_DIVIDE(different_house_year_ago_different_city , '
                'housing_units) AS '
                'Different_House_year_Ago_Different_City_Percent,             '
                'SAFE_DIVIDE(different_house_year_ago_same_city , '
                'housing_units) AS Different_House_year_Ago_Same_City_Percent,'
                '                                         /* family */'
                '             SAFE_DIVIDE(married_households , households ) AS'
                ' Married_Households_Percent,             '
                'SAFE_DIVIDE(nonfamily_households , households) AS '
                'NonFamily_Households_Percent,             '
                'SAFE_DIVIDE(family_households , households) AS '
                'Family_Households_Percent,             '
                'SAFE_DIVIDE(households_public_asst_or_food_stamps , '
                'households) AS '
                'Households_Public_Assist_or_Food_Stamps_Percent,             '
                'SAFE_DIVIDE(male_male_households , households) AS '
                'Male_Male_Households_Percent,               '
                'SAFE_DIVIDE(female_female_households , households) AS '
                'Female_female_Households_Percent,               '
                'SAFE_DIVIDE(children , households) AS Children_Percent,'
                '               SAFE_DIVIDE(children_in_single_female_hh , '
                'households) AS Childern_In_Single_Female_Household_Percent,'
                '               SAFE_DIVIDE(families_with_young_children , '
                'households) AS Families_With_Young_Children_Percent,'
                '             '
                'SAFE_DIVIDE(two_parent_families_with_young_children , '
                'households) AS '
                'Two_Parent_Families_With_Young_Children_Percent,             '
                'SAFE_DIVIDE(two_parents_in_labor_force_families_with_young_children'
                ' , households) AS '
                'Two_Parents_In_Labor_Force_Families_With_Young_Children_Percent,'
                '             '
                'SAFE_DIVIDE(two_parents_father_in_labor_force_families_with_young_children'
                ' , households) AS '
                'Two_Parents_Father_In_Labor_Force_Families_With_Young_Children_Percent,'
                '             '
                'SAFE_DIVIDE(two_parents_mother_in_labor_force_families_with_young_children'
                ' , households) AS '
                'Two_Parents_Mother_In_Labor_Force_Families_With_Young_Children_Percent,'
                '             '
                'SAFE_DIVIDE(two_parents_not_in_labor_force_families_with_young_children'
                ' , households) AS '
                'Two_Parents_Not_In_Labor_Force_Families_With_Young_Children_Percent,'
                '             '
                'SAFE_DIVIDE(one_parent_families_with_young_children , '
                'households) AS '
                'One_Parent_Families_With_Young_Children_Percent,             '
                'SAFE_DIVIDE(father_one_parent_families_with_young_children , '
                'households) AS '
                'Father_One_Parent_Families_With_Young_Children_Percent,'
                '             '
                'SAFE_DIVIDE(father_in_labor_force_one_parent_families_with_young_children'
                ' , households) AS '
                'Father_In_Labor_Force_One_Parent_Families_With_Young_Children_Percent,'
                '                          /* commute */             '
                'SAFE_DIVIDE(commute_less_10_mins , total_pop) AS '
                'Commute_Less_10_Mins_Percent,             '
                'SAFE_DIVIDE(commute_10_14_mins , total_pop) AS '
                'Commute_10_14_Mins_Percent,             '
                'SAFE_DIVIDE(commute_15_19_mins , total_pop) AS '
                'Commute_15_19_Mins_Percent,             '
                'SAFE_DIVIDE(commute_20_24_mins , total_pop) AS '
                'Commute_20_24_Mins_Percent,             '
                'SAFE_DIVIDE(commute_25_29_mins , total_pop) AS '
                'Commute_25_29_Mins_Percent,             '
                'SAFE_DIVIDE(commute_30_34_mins , total_pop) AS '
                'Commute_30_34_Mins_Percent,             '
                'SAFE_DIVIDE(commute_35_44_mins , total_pop) AS '
                'Commute_35_44_Mins_Percent,             '
                'SAFE_DIVIDE(commute_45_59_mins , total_pop) AS '
                'Commute_45_59_Mins_Percent,             '
                'SAFE_DIVIDE(commuters_16_over , total_pop) AS '
                'Commuters_16_Over_Percent,             '
                'SAFE_DIVIDE(walked_to_work , total_pop) AS '
                'Walked_To_Work_Percent,             '
                'SAFE_DIVIDE(worked_at_home , total_pop) AS '
                'Worked_At_Home_Percent,             SAFE_DIVIDE(no_car , '
                'total_pop) AS No_Car_Percent,             SAFE_DIVIDE(one_car'
                ' , total_pop) AS One_Car_Percent,             '
                'SAFE_DIVIDE(two_cars , total_pop) AS Two_cars_Percent,'
                '             SAFE_DIVIDE(three_cars , total_pop) AS '
                'Three_cars_Percent,             SAFE_DIVIDE(four_more_cars , '
                'total_pop) AS Four_more_Cars_Percent,             '
                'SAFE_DIVIDE(commuters_by_public_transportation , total_pop) '
                'AS Commuters_By_Public_Transportation_Percent,             '
                'SAFE_DIVIDE(commuters_by_bus , total_pop) AS '
                'Commuters_By_Bus_Percent,             '
                'SAFE_DIVIDE(commuters_by_car_truck_van , total_pop) AS '
                'Commuters_By_Car_truck_Van_Percent,             '
                'SAFE_DIVIDE(commuters_by_carpool , total_pop) AS '
                'Commuters_By_Carpool_Percent,             '
                'SAFE_DIVIDE(commuters_by_subway_or_elevated , total_pop) AS '
                'Commuters_By_Subway_Or_Elevated_Percent,             '
                'SAFE_DIVIDE(commuters_drove_alone , total_pop) AS '
                'Commuters_Drove_Alone_Percent,                          /* '
                'education */             SAFE_DIVIDE(associates_degree , '
                'total_pop) AS Associates_Degree_Percent,             '
                'SAFE_DIVIDE(bachelors_degree , total_pop) AS '
                'Bachelors_Degree_Percent,             '
                'SAFE_DIVIDE(high_school_diploma , total_pop) AS '
                'High_School_Diploma_Percent,             '
                'SAFE_DIVIDE(less_one_year_college , total_pop) AS '
                'Less_One_year_College_Percent,             '
                'SAFE_DIVIDE(masters_degree , total_pop) AS '
                'Masters_Degree_Percent,             '
                'SAFE_DIVIDE(one_year_more_college , total_pop) AS '
                'One_Year_More_College_Percent,             '
                'SAFE_DIVIDE(less_than_high_school_graduate , total_pop) AS '
                'Less_Than_high_School_Graduate_Percent,'
                '                            '
                'SAFE_DIVIDE(high_school_including_ged , total_pop) AS '
                'High_School_including_Ged_Percent,             '
                'SAFE_DIVIDE(bachelors_degree_2 , total_pop) AS '
                'Backelors_Degree_2_Percent,             '
                'SAFE_DIVIDE(bachelors_degree_or_higher_25_64 , total_pop) AS '
                'Backelors_Degree_Or_Higher_25_64_Percent,             '
                'SAFE_DIVIDE(graduate_professional_degree , total_pop) AS '
                'GRaduate_professional_Degree_Percent,             '
                'SAFE_DIVIDE(some_college_and_associates_degree , total_pop) '
                'AS Some_College_And_Associates_Percent,'
                '                          '
                'SAFE_DIVIDE(male_45_64_associates_degree , total_pop) AS '
                'Males_45_64_Associates_Degree_Percent,             '
                'SAFE_DIVIDE(male_45_64_bachelors_degree , total_pop) AS '
                'Males_45_64_Bachelors_Degree_Percent,             '
                'SAFE_DIVIDE(male_45_64_graduate_degree , total_pop) AS '
                'Males_45_65_Graduate_Degree_Percent,             '
                'SAFE_DIVIDE(male_45_64_less_than_9_grade , total_pop) AS '
                'Male_45_64_Less_Than_9_Grade_Percent,             '
                'SAFE_DIVIDE(male_45_64_grade_9_12 , total_pop) AS '
                'Male_45_64_Grade_9_12_Percent,             '
                'SAFE_DIVIDE(male_45_64_high_school , total_pop) AS '
                'Males_45_64_High_School_Percent,             '
                'SAFE_DIVIDE(male_45_64_some_college , total_pop) AS '
                'Male_45_64_Some_College_Percent,                          '
                'SAFE_DIVIDE(in_grades_1_to_4 , total_pop) AS '
                'In_Grades_1_To_4_Percent,             '
                'SAFE_DIVIDE(in_grades_5_to_8 , total_pop) AS '
                'In_Grades_5_To_8_Percent,             '
                'SAFE_DIVIDE(in_grades_9_to_12 , total_pop) AS '
                'In_Grades_9_To_12_Percent,             SAFE_DIVIDE(in_school '
                ', total_pop) AS OIn_School_Percent,             '
                'SAFE_DIVIDE(in_undergrad_college , total_pop) AS '
                'In_Undergrad_College_Percent,                          /* '
                'labor */             SAFE_DIVIDE(employed_pop , total_pop) AS'
                ' Employed_Percent,             SAFE_DIVIDE(unemployed_pop , '
                'total_pop) AS Unemployed_Percent,             '
                'SAFE_DIVIDE(pop_in_labor_force , total_pop) AS '
                'In_Labor_Force_Percent,             '
                'SAFE_DIVIDE(not_in_labor_force , total_pop) AS '
                'Not_In_Labor_Force_Percent,             '
                'SAFE_DIVIDE(workers_16_and_over , total_pop) AS '
                'Workers_16_And_Over_Percent,             '
                'SAFE_DIVIDE(armed_forces , total_pop) AS '
                'Armed_Forces_Percent,             '
                'SAFE_DIVIDE(civilian_labor_force , total_pop) AS '
                'Civilian_labor_Force_Percent,             '
                'SAFE_DIVIDE(employed_agriculture_forestry_fishing_hunting_mining'
                ' , total_pop) AS '
                'Employed_agriculture_Forestry_Fishing_Hunting_Mining_Percent,'
                '             '
                'SAFE_DIVIDE(employed_arts_entertainment_recreation_accommodation_food'
                ' , total_pop) AS '
                'Employed_Entertainment_Recreation_Accommodation_Food_Percent,'
                '             SAFE_DIVIDE(employed_construction , total_pop) '
                'AS Employed_Construction_Percent,             '
                'SAFE_DIVIDE(employed_education_health_social , total_pop) AS '
                'Employed_Education_Health_Social_Percent,             '
                'SAFE_DIVIDE(employed_finance_insurance_real_estate , '
                'total_pop) AS Employed_Finance_Insurance_Real_Estate_Percent,'
                '             SAFE_DIVIDE(employed_information , total_pop) AS'
                ' Employed_Information_Percent,             '
                'SAFE_DIVIDE(employed_manufacturing , total_pop) AS '
                'Employed_Manufacturing_Percent,             '
                'SAFE_DIVIDE(employed_other_services_not_public_admin , '
                'total_pop) AS '
                'Employed_Other_Services_Not_Public_Admin_Percent,'
                '             SAFE_DIVIDE(employed_public_administration , '
                'total_pop) AS Employed_Public_Administration_Percent,'
                '             SAFE_DIVIDE(employed_retail_trade , total_pop) '
                'AS Eomployed_Retail_Trade_Percent,             '
                'SAFE_DIVIDE(employed_science_management_admin_waste , '
                'total_pop) AS '
                'Employed_Science_Management_Admin_Waste_Percent,             '
                'SAFE_DIVIDE(employed_transportation_warehousing_utilities , '
                'total_pop) AS '
                'Employed_Transportation_WareHousing_Utilities_Percent,'
                '             SAFE_DIVIDE(employed_wholesale_trade , '
                'total_pop) AS Employed_wholesale_Arts_Percent,             '
                'SAFE_DIVIDE(occupation_management_arts , total_pop) AS '
                'Occupation_Managment_Arts_Percent,             '
                'SAFE_DIVIDE(occupation_natural_resources_construction_maintenance'
                ' , total_pop) AS '
                'Occupation_Natural_Resources_Construction_Maintenance_Percent,'
                '             '
                'SAFE_DIVIDE(occupation_production_transportation_material , '
                'total_pop) AS '
                'Occupation_Production_Transportation_Material_Percent,'
                '             SAFE_DIVIDE(occupation_sales_office , total_pop)'
                ' AS Occupation_sales_office_Percent,             '
                'SAFE_DIVIDE(occupation_services , total_pop) AS '
                'Occupation_Services_Percent,             '
                'SAFE_DIVIDE(management_business_sci_arts_employed , '
                'total_pop) AS Management_Business_Sci_Arts_Employed_Percent,'
                '             SAFE_DIVIDE(sales_office_employed , total_pop) '
                'AS Sales_office_Eomployed_Percent,                         /*'
                ' language */             '
                'SAFE_DIVIDE(speak_only_english_at_home , total_pop) AS '
                'Speak_Only_English_Percent,             '
                'SAFE_DIVIDE(speak_spanish_at_home , total_pop) AS '
                'Speak_Spanish_Percent,             '
                'SAFE_DIVIDE(speak_spanish_at_home_low_english , total_pop) AS'
                ' Speak_Spanish_Low_English_Percent,                        '
                'total_pop           FROM             '
                '`bigquery-public-data.census_bureau_acs.{census_geography}_{census_year}_{census_span}`'
                '         ',
            'legacy':
                False,
            'parameters': {
                'census_geography': {
                    'field': {
                        'name':
                            'census_geography',
                        'kind':
                            'choice',
                        'order':
                            1,
                        'default':
                            'zip_codes',
                        'description':
                            'Census table to get data from.',
                        'choices': [
                            'zip_codes', 'state', 'zcta5',
                            'schooldistrictunified', 'puma', 'place', 'county',
                            'congressionaldistrict', 'censustract', 'cbsa'
                        ]
                    }
                },
                'census_year': {
                    'field': {
                        'name':
                            'census_year',
                        'kind':
                            'choice',
                        'order':
                            2,
                        'default':
                            '2018',
                        'description':
                            'Census table to get data from.',
                        'choices': [
                            2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011,
                            2010, 2009, 2008, 2007
                        ]
                    }
                },
                'census_span': {
                    'field': {
                        'name': 'census_span',
                        'kind': 'choice',
                        'order': 3,
                        'default': '5yr',
                        'description': 'Census table to get data from.',
                        'choices': ['1yr', '3yr', '5yr']
                    }
                }
            }
        },
        'to': {
            'dataset': {
                'field': {
                    'name': 'dataset',
                    'kind': 'string',
                    'order': 4,
                    'default': '',
                    'description': 'Existing BigQuery dataset.'
                }
            },
            'table': {
                'field': {
                    'name': 'table',
                    'kind': 'string',
                    'order': 5,
                    'default': '',
                    'description': 'Table to create from this census_data.'
                }
            }
        }
    }
}]

DAG_FACTORY = DAG_Factory('bigquery_census_normalize', {'tasks': TASKS}, INPUTS)
DAG_FACTORY.apply_credentails(USER_CONN_ID, GCP_CONN_ID)
DAG = DAG_FACTORY.execute()

if __name__ == '__main__':
  DAG_FACTORY.print_commandline()

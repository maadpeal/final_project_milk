Raw_data
-
id_cow int
date_reg date
lactation int
days_milk int
daily_prod int

unique_ids
-
id_cow int pk

lactation_summary
-
id_cow int fk - unique_ids.id_cow
lactation int
total_milk_days int
total_milk_production int

abortions_details
-
id_cow int fk - unique_ids.id_cow
ab_count int
date_reg date

mastitis_details
-
id_cow int fk - unique_ids.id_cow
mas_count int
date_reg date

insemination_details
-
id_cow int fk - unique_ids.id_cow
ins_count int
insemination_date
ins_responsible varchar
id_bull int fk - bulls_details.id_bull

gynecological_status
-
id_cow int fk - unique_ids.id_cow
status varchar
status_date date

bulls_details
-
id_bull int pk
bull_name varchar

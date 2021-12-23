import os
import pathlib    
import csv

def main():
    for file in input_files:
        output_data = LoadData.wrangle_fpl_load_curve_data(file)
        output_file = os.path.join(dir_data,os.path.basename(file))
        with open(output_file, mode='w') as f:
            f_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for o in output_data :
                f_writer.writerow(o)
            

class LoadData():
    def __init__(self):
        pass
    # Demand Curve Sample Data Methodology
    # ---------------------------------------------------------
    # Data from FPL eia.gov tools 
    # FPL's service territory includes over 4.6 million customers
    # Sample data of 11/20/20 to 11/27/20 by hour of consumer demand
    # Using the real demand curves we can estimate consumer demand
    # by Household. In Florida, a survey (https://www.floridarealtymarketplace.com/blog/how-much-power-does-a-house-use.html#:~:text=In%20Florida%2C%20the%20survey%20showed,windows%2C%20doors%2C%20and%20roofs.)
    # showed that the average home used 1,110 kWh (~14k kwh/yr) . 
    # This can be used to estimate 
    # (4.6M * 1110kWh/mo) / 730 = Total FPL Demand in kWh
    # 6,000 MWh on average. The max of the data demand is 18k MWh 
    # with an average of 12000 MWh. By cutting the demand from the
    # sample data set in half we can safely assume that the 
    # remaining clients would be commercial and ancillary loads
    # with the reasoning that the average home would be 1000kWh
    # fields :
    # 'Timestamp (Hour Ending)'
    # 'Demand (MWh)'
    def wrangle_fpl_load_curve_data(filename):
        rel_path = filename
        load_curve_data = os.path.join(dir_script, rel_path) 
        data = LoadData.get_csv(load_curve_data,['Timestamp (Hour Ending)','Demand (MWh)','Solar Generation (MWh)'])
        data_clean = LoadData.clean_data(data)
        data_clean_iso = LoadData.convert_date_time_to_ISO(data_clean)
        data_clean_iso_norm =  LoadData.convert_normalize_pwr(data_clean_iso)
        return data_clean_iso_norm    
    def get_csv(file,col_names):
        output = []
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = []
                for col in col_names:
                    r.append(row[col])
                output.append(r)
        return output
    def clean_data(data):
        #remove rows with empty field
        output = []
        skip = False
        for r in data :
            for c in r:
                if c=='':
                    skip = True
                else:
                    skip = False
            if not skip:
                output.append(r)
        return output
    def convert_date_time_to_ISO(data):
        from dateutil.parser import parse
        output = []
        for r in data :
            dt = parse(r[0])
            r[0] = dt.isoformat()
            output.append(r)
        return output
    def convert_normalize_pwr(data):
        output = []
        print(data)
        mx1 = max([int(x[1]) for x in data])
        mx2 = max([int(x[2]) for x in data])
        for r in data :
            r[1] = int(r[1])/mx1
            r[2] = int(r[2])/mx2
            output.append(r)
        return output

if __name__ == "__main__":
    from pathlib import Path
    d = Path(__file__).resolve()
    dir_root = str(d.parent.parent.parent)
    # ./script/
    dir_script =str(d.parent)
    # ./data/
    print(str(d.parent.parent))
    dir_data = os.path.join(str(d.parent.parent),'data')
    # step1_input/data
    dir_input_data = os.path.join(dir_root,'step1_input/data')
    input_files = [p for p in pathlib.Path(dir_input_data).iterdir() if p.is_file()]
    
    main()
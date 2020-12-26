import step1_raw as step1
import step2_parse as step2
import step3_ingest as step3
import step4_design as step4
import step5_analyze as step5
import yaml
import os
from pathlib import Path
import pathlib

def main():
    args = load_config(filename='config.yaml')
    df = step1.eia_raw(args)
    df = step2.eia_parse(df)
    prosumers = step3.get_prosumers(df,args)
    dso = step4.run_sim(prosumers,args)
    T = min(args['T'],df.shape[0])
    step5.sim_performance(dso,T)


def load_config(filename):
    d = Path(__file__).resolve()
    dir_data = os.path.join(str(d.parent))
    config_file = os.path.join(dir_data,filename)
    with open(config_file) as file:
        args = yaml.full_load(file)
    return args

def test_main():
    args = load_config(filename='config.yaml')
    print("RUNNING TEST 1")
    df = step1.test(args)
    print("RUNNING TEST 2")
    step2.test(df)
    print("RUNNING TEST 3")
    prosumers = step3.test(df,args)
    print("RUNNING TEST 4")
    dso = step4.test(prosumers,args) 
    print("RUNNING TEST 5")
    T = min(args['T'],df.shape[0])
    step5.sim_performance(dso,T)
       

if __name__ == "__main__":
    #main()
    test_main()
import pandas as pd
import model as m

# Step 3 : Ingesting into a instantiation of the Prosumer model
def get_prosumers(df,args):
    # [t,generation,demand]
    prosumers = [ m.Prosumer(id=n,args=args,
                    gen_curve=df['generation'], 
                    dem_curve=df['demand']) for n in range(args['N'])] 
    print("Step 3: Model generation completed.")
    return prosumers

def test(df,args):
    prosumers = get_prosumers(df,args)
    for p in prosumers:
        print(f"{p.id} : items={len(p.gen_curve)} ledger={p.ledger}")
    return prosumers
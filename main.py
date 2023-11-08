import argparse
from src.alo import ALO

# --------------------------------------------------------------------------------------------------------------------------
#    MAIN
# --------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # while(1):

    parser = argparse.ArgumentParser(description="Enter the path of << experimental_plan.yaml >> (ex) ./config/experimental_plan.yaml")
    parser = argparse.ArgumentParser(description="Script for dealing with specific file")
    parser.add_argument("--config", type=str, default=0, help="config option")
    parser.add_argument("--system", type=str, default="system", help="system option")
    parser.add_argument("--mode", type=str, default="all", help="ALO mode, train, inf, inference, all")

    args = parser.parse_args()

    try:
        if args.config != 0: 
            alo = ALO(exp_plan_file = args.config, alo_mode = args.mode)  # exp plan path
        else: 
            alo = ALO(alo_mode = args.mode)
    except:
        raise ValueError("Inappropriate config yaml file.")
        
    alo.runs()

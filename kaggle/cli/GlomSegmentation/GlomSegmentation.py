import os
import sys
from ctk_cli import CLIArgumentParser


def main(args):  
    cwd = os.getcwd()
    print(cwd)
    os.chdir(cwd)

    cmd = "python3 ../kaggle_code/inference.py  --basedir {}  --model_dir {} --girderApiUrl {} \
                --girderToken {} --input_files {}".format(args.base_dir,  args.model_dir, args.girderApiUrl, args.girderToken, args.input_files)
    print(cmd)
    sys.stdout.flush()
    os.system(cmd)  


if __name__ == "__main__":
    main(CLIArgumentParser().parse_args())
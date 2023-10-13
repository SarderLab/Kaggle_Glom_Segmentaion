import os
import sys
from ctk_cli import CLIArgumentParser

def main(args):  

    _ = os.system("printf '\n---\n\nFOUND: [{}]\n'".format(args.input_files))

    cwd = os.getcwd()
    print(cwd)
    os.chdir(cwd)
    
    cmd = "python3 ../kaggle_code/parse_args.py --input_files {} --basedir {} --model_dir {} --girderApiUrl {} --girderToken {}".format(args.input_files, args.basedir, args.model_dir, args.girderApiUrl, args.girderToken)
    print(cmd)
    sys.stdout.flush()
    os.system(cmd)  


if __name__ == "__main__":
    main(CLIArgumentParser().parse_args())

import os
import argparse

def main(args):

    from inference import predict

    print('inference starts')
    predict(args=args,tissue_type='RK')
    print('inference ends')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--girderApiUrl', dest='girderApiUrl', default=' ' ,type=str,
        help='girderApiUrl')
    parser.add_argument('--girderToken', dest='girderToken', default=' ' ,type=str,
        help='girderToken')
    parser.add_argument('--input_files', dest='input_files', default=' ' ,type=str,
        help='input_files')    
    parser.add_argument('--basedir', dest='basedir', default=os.getcwd(),type=str,
        help='base directory of code folder')
    parser.add_argument('--model_dir', dest='model_dir', default=os.getcwd(),type=str,
        help='model_dir')
    args = parser.parse_args()
    main(args=args)

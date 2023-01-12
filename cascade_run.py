#define cascade_run
import train
from easydict import EasyDict
import yaml
import os


def cascade(yaml_args):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--hsv_h_scale', type=float, default=None)
    parser.add_argument('--hsv_s_scale', type=float, default=None)
    parser.add_argument('--hsv_v_scale', type=float, default=None)
    # parser.add_argument('--logs_path', type=int, default=None)
    # parser.add_argument('--checkpoints_path', type=int, default=None)
    # parser.add_argument('--saved_models', type=int, default=None)
    parser.add_argument('--seed', type=int, default=None)
    parser.add_argument('--run', type=int, default=None)
    # parser.add_argument('--lpips', type=int, default=None)
    parser = parser.parse_args()

    if parser.hsv_h_scale is not None:
        yaml_args.hsv_h_scale = parser.hsv_h_scale
    if parser.hsv_s_scale is not None:
        yaml_args.hsv_s_scale = parser.hsv_s_scale
    if parser.hsv_v_scale is not None:
        yaml_args.hsv_v_scale = parser.hsv_v_scale
    # if parser.secret_loss is not None:
    #     yaml_args.secret_loss_scale = parser.secret_loss
    yaml_args.seed = parser.seed
    global SEED
    SEED = parser.seed
    # yaml_args.lpips_loss_scale = parser.lpips


    yaml_args.logs_path = os.path.join("./logs/" + "yuv_secret_loss_2.5_lpips_0.01_seed_" + str(parser.seed) + "_run_" + str(parser.run))
    if not os.path.exists(yaml_args.logs_path):
        os.makedirs(yaml_args.logs_path)

    yaml_args.checkpoints_path = os.path.join("./checkpoints/" + "yuv_secret_loss_2.5_lpips_0.01_seed_" + str(parser.seed) + "_run_" + str(parser.run))
    if not os.path.exists(yaml_args.checkpoints_path):
        os.makedirs(yaml_args.checkpoints_path)

    yaml_args.saved_models = os.path.join("./saved_models/" + "yuv_secret_loss_2.5_lpips_0.01_seed_" + str(parser.seed) + "_run_" + str(parser.run))
    if not os.path.exists(yaml_args.saved_models):
        os.makedirs(yaml_args.saved_models)


def get_seed():
    return SEED


import argparse
import logging
import yaml
import pathlib
import shutil
import os

#  ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗
# ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝
# ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
# ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
# ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝

default_config = "./sources/default_cfg/config.yml"

abs_default_config = pathlib.Path(default_config).resolve()
with open(abs_default_config, 'r') as file:
            config_yaml = yaml.load(file, Loader=yaml.FullLoader)

# TODO:
# list all files in default output to use them as available arguments


# ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗
# ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
# ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗
# ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝

parser = argparse.ArgumentParser(description="a script that return a list of files from multiple YAML files.")

parser.add_argument('--top-yaml', '-t',
                    metavar=config_yaml["top-yaml"],
                    nargs=1,
                    type=str,
                    help="the YAML file of the top module that call all the orthers.")

parser.add_argument('--flag', '-f',
                    metavar=config_yaml["flag"],
                    nargs='?',
                    type=str,
                    help="all sources that doesn't correpond to the specified target will be ignored.")

parser.add_argument('--log-level', '-l',
                    metavar='<INFO|DEBUG|WARNING|ERROR>',
                    nargs='?',
                    default='INFO',
                    type=str,
                    help="set the logging level of information that will be printed.")

parser.add_argument('--config-file', '-c',
                    metavar=config_yaml["config-file"],
                    nargs=1,
                    type=str,
                    help="the the CLI arguments take priority over the config file")

parser.add_argument('--dump-config',
                    action="store_true",
                    help="the the CLI arguments take priority over the config file")

parser.add_argument('--dump-format',
                    metavar="list of file name in default output folder" #TODO
                    nargs='?',
                    type=str,
                    help="dump an example of output script")

# maybe not necessary to have this argument if the file is already specified
parser.add_argument('--format-dir', '-fd',
                    metavar=config_yaml["format-dir"],
                    nargs='?',
                    type=str,
                    help="the directory where the output format script are stored")

parser.add_argument('--output-format', '-of',
                    metavar=config_yaml["output-format"],
                    nargs='?',
                    type=str,
                    help="the template filename for the output script")

parser.add_argument('--output-file', '-o',
                    )

args = parser.parse_args


# ██╗      ██████╗  ██████╗  ██████╗ ██╗███╗   ██╗ ██████╗
# ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██║████╗  ██║██╔════╝
# ██║     ██║   ██║██║  ███╗██║  ███╗██║██╔██╗ ██║██║  ███╗
# ██║     ██║   ██║██║   ██║██║   ██║██║██║╚██╗██║██║   ██║
# ███████╗╚██████╔╝╚██████╔╝╚██████╔╝██║██║ ╚████║╚██████╔╝
# ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝

numeric_level = getattr(logging, args.log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % args.log_level)
logging.basicConfig(level=numeric_level)

if args.dump_config == True:
    shutil.copy(abs_default_config, os.getcwd())

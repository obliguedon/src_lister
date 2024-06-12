import argparse
import logging
import yaml
import pathlib
import shutil
import os
from packages import yaml_utils
from packages import template_utils

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
                    metavar="list of file name in default output folder", #TODO
                    nargs='?',
                    type=str,
                    help="dump an example of output script")

parser.add_argument('--output-format', '-of',
                    metavar=config_yaml["output-format"],
                    nargs='?',
                    type=str,
                    help="the template filename for the output script")

parser.add_argument('--output-file', '-o',
                    )

args = parser.parse_args()


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


# ████████╗██╗  ██╗███████╗     █████╗ ██████╗ ██████╗
# ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔══██╗██╔══██╗
#    ██║   ███████║█████╗      ███████║██████╔╝██████╔╝
#    ██║   ██╔══██║██╔══╝      ██╔══██║██╔═══╝ ██╔═══╝
#    ██║   ██║  ██║███████╗    ██║  ██║██║     ██║
#    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝     ╚═╝

all_items = dict()

# get all the keys that need to be extracted from the YAML files by reading and listing the
# variables in the output template
if args.output_format != None:
    abs_template = pathlib.Path(args.output_format).resolve()
    template = str()
    with open(abs_template, 'r') as file:
        template = file.read()
    
    all_vars = template_utils.extractor.get_all_params(template)
    all_keys = template_utils.extractor.get_all_values(all_vars)

    if args.top_yaml != None:
        print(f"top YAML is {args.top_yaml}")
        abs_top_yaml = pathlib.Path(args.top_yaml[0]).resolve()
        all_deps = yaml_utils.extractor.get_deps(abs_top_yaml)

        for key in all_keys:
             all_items[key] = yaml_utils.extractor.get_files(all_deps, item=key, flag=args.flag)

        print (f"ALL_ITEMS = {all_items}")
        print (f"ITEMS['sources'] = {all_items["sources"]}")
        print (f"ALL_VARS['sources'] = {all_vars["sources"]}")
        output = template_utils.generator.fill_template(template, all_items)
        print(f"## OUTPUT = {output}")
    else:
        logging.error("top YAML file not specified")


# extract those key from the YAML files and put all of those in a dictionnary

# send the dictionnary to the output_generator to fill the variables in the template

# get back the output string and write it to a file
# if the output file isn't specified, print the output
# if the template isn't specified, simply print a list of everything, or just the specified key or flag.



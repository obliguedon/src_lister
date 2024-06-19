import argparse
import logging
import yaml
import pathlib
import shutil
import os
import sys
from . import yaml_utils
from . import template_utils
from importlib.metadata import version, packages_distributions

def main ():
    __name__="files_lister"

    #  ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗
    # ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝
    # ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
    # ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
    # ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
    #  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝

    default_config = "./default_cfg/config.yml"

    abs_default_config = pathlib.Path(os.path.join(os.path.dirname(__file__), default_config)).resolve()
    with open(abs_default_config, 'r') as file:
                config_yaml = yaml.load(file, Loader=yaml.FullLoader)


    # ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗
    # ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
    # ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝
    # ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗
    # ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║
    # ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝

    parser = argparse.ArgumentParser(
                        prog=__name__,
                        description='return a list of files from multiple YAML files referencing each other.',
                        epilog='visit https://github.com/obliguedon/src_lister/ for more details and examples')

    parser.add_argument('--version',
                        action='version',
                        version=version(__name__))

    parser.add_argument('--top-yaml', '-i',
                        metavar=config_yaml["top-yaml"],
                        nargs='?',
                        required=True,
                        type=argparse.FileType('r'),
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
                        metavar="./<your>/<config_file>.yml",
                        nargs='?',
                        type=argparse.FileType('r'),
                        help="the the CLI arguments take priority over the config file")

    parser.add_argument('--dump-config',
                        action="store_true",
                        help="write a config.yml file in the CWD")

    parser.add_argument('--template', '-t',
                        metavar=config_yaml["template"],
                        nargs='?',
                        required=True,
                        type=argparse.FileType('r'),
                        help="the template filename for the output script")

    parser.add_argument('--output-file', '-o',
                        metavar=config_yaml["output-file"],
                        nargs='?',
                        default=sys.stdout,
                        type=argparse.FileType('w'),
                        help="the file it which the file list will be written (default: <stdout>)")

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
    output = str()
    # get all the keys that need to be extracted from the YAML files by reading and listing the
    # variables in the output template

        # abs_template = pathlib.Path(args.template).resolve()
        # template = str()
        # with open(abs_template, 'r') as file:
    template = args.template.read()

    all_vars = template_utils.extractor.get_all_params(template)
    all_keys = template_utils.extractor.get_all_values(all_vars)

    abs_top_yaml = pathlib.Path(args.top_yaml.name).resolve()
    all_deps = yaml_utils.extractor.get_deps(abs_top_yaml)

    for key in all_keys:
        all_items[key] = yaml_utils.extractor.get_files(all_deps, item=key, flag=args.flag)

    output = template_utils.generator.fill_template(template, all_items)

    # if (args.output_file == sys.stdout):
    #     print(output)
    # else:
        # abs_output_path = pathlib.Path(os.getcwd(), args.output_file).resolve()
        # with open(abs_output_path, 'w') as file:
    args.output_file.write(f"{output}\n")
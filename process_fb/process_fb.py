import click
import os

@click.command()
@click.option("-d", "--dataset_name", help="Dataset name to be downloaded.")
@click.option("-a", "--area", help="Area to be downloaded.")
# @click.option('-f', '--file', help='File to be parsed.')
def cli(dataset_name, area):
    """Entry point for the process_fb cli."""

    #define project string
    proj_name = dataset_name + '_' + area

    # Create project directory
    os.mkdir('./fb_' + proj_name)

    # Create project src directory
    os.mkdir('./fb_' + proj_name + '/src')

    # Create project data directory
    os.mkdir('./fb_' + proj_name + '/data')

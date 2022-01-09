import json
import time
import csslib
from rich import print
from rich.prompt import Prompt
from os import path
from os import stat

# Globals
css_done = False
commands = ['test']

def generate_component(path,component):
    if component == "test":
        try:
            with open(path,"a") as f:
                f.write('/* This is a test component which is used for testing how Wave works :) */\n')
                print("[blue][WAVECSS][/blue] Generated [blue]test[/blue] component from [bold blue]WaveCSS[/bold blue]")
        except:
            print("[blue][WAVECSS][/blue] [red]ERROR: There was a problem locating or opening stylesheet[/red]")
    else:
        print("[blue][WAVECSS][/blue][yellow] Unknown component. Double check your spelling.[/yellow]")

def cli(YoN: bool,css):
        component = Prompt.ask("[blue][WAVECSS][/blue]",default="test",choices=commands,show_choices=False,show_default=False)
        generate_component(css,component)

def init_css(filepath):
    if path.isfile(css_path) == True:
        with open(filepath,'w') as f:
            f.write(csslib.header())
            f.write(csslib.param_start())
            f.write(csslib.defaults(default_font_weight,default_font_size,default_font_colour))
            f.write(csslib.param_end())
            print("[blue][WAVECSS][/blue] [green]CSS has been initialised.[/green]")
        cli(css_done,css_path)
    else:
        print("[blue][WAVECSS][/blue] [red]ERROR: There was a problem locating stylesheet. Check your configuration file.[/red]")

def main():
    with open('wave.config.json') as f:
        cfg = json.load(f)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(f"[blue][WAVECSS] [/blue][green]Loaded all config options at {current_time}[/green]")
        
        # Grab the CSS file location from config
        global css_path
        css_path = cfg['css-path']

        # Grab all other config options
        global default_font_weight
        global default_font_size
        global default_font_colour
        global css_done
        default_font_weight = cfg['default-font-weight']
        default_font_size   = cfg['default-font-size']
        default_font_colour = cfg['default-font-colour']

        # Declare that config is finished
        config_complete = True
        if stat(css_path).st_size == 0:
            init_css(css_path)
        else:
            cli(config_complete,css_path)


if __name__ == "__main__":
    main()
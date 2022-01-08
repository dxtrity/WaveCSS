import json
import time
import csslib
from rich import print
from os import path

# Globals
css_done = False

def generate_component(c,x):
    if x == "test":
        try:
            with open(c,"a") as f:
                f.write('''.test{background-color: var(--bg-d-g);}\n''')
                print("[blue][WAVECSS][/blue] Generated [blue]test[/blue] component from [bold blue]WaveCSS[/bold blue]")
        except:
            print("[blue][WAVECSS][/blue] [red]ERROR: There was a problem locating or opening stylesheet[/red]")
    else:
        print("[blue][WAVECSS][/blue][yellow]Unknown component. Double check your spelling.[/yellow]")

def cli(YoN: bool,css):
    while YoN == True:
        x = input("")
        if x == "add test":
            generate_component(css,"test")
            cli(css_done,css_path)
        else:
            cli(css_done,css_path)

def init_css(x):
    if path.isfile(x) == True:
        with open(x,'w') as f:
            f.write(csslib.header())
            f.write(csslib.param_start())
            f.write(csslib.defaults(default_font_weight,default_font_size,default_font_colour))
            f.write(csslib.param_end())
            css_done = True
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
        global css_path
        css_path = cfg['css-path']
        global default_font_weight
        global default_font_size
        global default_font_colour
        global css_done
        default_font_weight = cfg['default-font-weight']
        default_font_size   = cfg['default-font-size']
        default_font_colour = cfg['default-font-colour']
        config_complete = True
        if css_done == True:
            cli(config_complete,css_path)
        else:
            init_css(css_path)


if __name__ == "__main__":
    main()
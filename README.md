>[!NOTE]
>Because I couldn't find any docs on sine mod creation, I forked rasyidrafi's compact sidebar mod and detached it from the fork network. This is a completely different thing, and everything is unique, however rasyidrafi's mod has been used as the base.
# My windows theme.
Some things I've made over time for my windows laptop. These are all designed to be the same general theme, which are designed to replicate a modified blue version of [Shibuma by MrDLingters](https://github.com/amnweb/yasb-themes/tree/main/themes/92a8f104-ab80-45c0-95f1-82ebb2e12df6).

While this was originally meant to be blue, it has been modified to instead follow a config. You place your colors (and fonts) into config.json at the root, as such:

```json
{
    "background": "#edf6ff",
    "background2": "#c2dcf5",
    "accent": "#2777c7",
    "text": "#18324f",
    "accentText": "#040404",
    "hover": "#9bc5ec",
    "mutedBG": "#d7e9fa",
    "border": "#a8c9e8",
    "redFlash": "#e05270",
    "subtext": "#52708f",
    "icons-font": "\"Segoe Fluent Icons\"",
    "icons-font-fallback": ["\"JetBrainsMono NFP\"", "\"JetBrainsMono Nerd Font Propo\""],
    "system-font": ["\"JetBrainsMono NFP\"", "\"JetBrainsMono Nerd Font Propo\""],
    "specialFont": ["\"Segoe UI Variable\"", "\"Segoe UI\""],
    "border-radius": 0,
    "border-radius2": 0,
    "border-radius3": 0,
    "border-radiusWallpapers": 0,
    "fontSize": "\"12px\"",
    "iconSize": "\"16px\"",
    "fontSizeLarge": "\"16px\"",
    "fontWeight": 600
}
```

>[!NOTE]
>The default config has a light blue colourscheme. Only the YASB bar makes use of border-radius, border-radius2, border-radius3 all the way through to fontWeight. By default this theme requires Segoe Fluent Icons (present by default on windows), JetBrainsMono NFP/JetBrainsMono Nerd Font Proppo, and Segoe UI Variable and regular Segoe UI. All Segoe fonts are available on windows, and Nerd Fonts can be downloaded from the website.

and run `generate_formats.py` every time you change the config, to convert it to all the formats it needs to be.

# Components
## Zen browser
>[!NOTE]
>The zen theme is very unstable as it does not follow any good practices and was ragged together. It is bound to break at any time, and has only been tested with sidebar only and light mode enabled.

>[!WARNING]
>Make sure you disable auto-update for this theme in sine! Auto update will remove the config file every time you restart your browser.

A customization for the zen browser. Install it using sine, pointing at the `zen/` folder in this repo.

The mod will look for the config in the mod's folder, however the python script takes care of that for you. You need to instruct the script of the mod's folder location, by editing the first line of `generate_formats.py`: `SINE_MOD_LOCATION = Path(r"C:\Users\anthony.maxwell\AppData\Roaming\zen\Profiles\x7rsjsz9.Default (release)\chrome\sine-mods\custom")`. You want to replace `C:\Users\anthony.maxwell\AppData\Roaming\zen\Profiles\x7rsjsz9.Default (release)\chrome\sine-mods\custom` with the path to your mod folder.

<details>
<summary>How to find this path?</summary>
(This will only work after installation of the zen mod)

Open zen and go to "about:preferences", and click on "Sine mods"

<img width="405" height="43.5" alt="image" src="https://github.com/user-attachments/assets/ef4801a5-7268-4af9-8ea1-9343394a8f8b" />

Open sine settings

<img width="531" height="41" alt="image" src="https://github.com/user-attachments/assets/e5eb47a7-31cd-4e42-bcb2-5d97801bc244" />

Enable the command palette

<img width="525" height="137.5" alt="image" src="https://github.com/user-attachments/assets/da8b349d-2d60-4220-87ce-023926c3c022" />

Press `ctrl`+`shift`+`Y` and click on "Open mod folder"

<img width="503.5" height="246" alt="image" src="https://github.com/user-attachments/assets/dbe87ec0-0abb-42f2-9a1c-56feee6d9c81" />

Click on "My Theme" and copy the path that it opens in file explorer. This is the path for the python file. You can now go back and turn off the command palette.

</details>

## YASB
A modified version of [Shibuma by MrDLingters](https://github.com/amnweb/yasb-themes/tree/main/themes/92a8f104-ab80-45c0-95f1-82ebb2e12df6), designed to go on the top of the screen and modified for the blue color scheme, later adjusted to follow the colors in the config.

To install, copy all the files in `yasb/` and paste them into your YASB config, replacing the files.

You will then need to open up the file called `styles.css` in that folder, and in the first line you will see `@import url('C:/Users/anthony.maxwell/themes/config.css');`. You want to replace that with the path to your config.css, which should he located at the root of wherever you cloned this repository, or downloaded it.

For example, if the folder containing config.json is at `C:/Users/anthony.maxwell/themes/`, you would make it: `@import url('C:/Users/anthony.maxwell/themes/config.css')`.

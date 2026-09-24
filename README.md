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

and run `generate_formats.py` every time you change the config, to convert it to all the formats it needs to be.

>[!NOTE]
> When installing the zen or YASB theme, the first line will be an @import to the config, `@import url('.../config.css')` were you need to replace {PATH TO ROOT} with the path to the root of this repository, cloned, not including config.css, as that is already present.

# Components
## Zen browser
A customization for the zen browser. Install it using sine, pointing at the `zen/` folder in this repo. The configuration in sine will have an option for the path to the cloned repository, for your config.

## YASB
A modified version of [Shibuma by MrDLingters](https://github.com/amnweb/yasb-themes/tree/main/themes/92a8f104-ab80-45c0-95f1-82ebb2e12df6), designed to go on the top of the screen and modified for the blue color scheme, later adjusted to follow the colors in the config.

To install, copy all the files in `yasb/` and replace your YASB config with them.

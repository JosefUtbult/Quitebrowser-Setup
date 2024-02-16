import plugins.catppuccin as catppuccin

config.load_autoconfig()

# Request the darkmode sites when possible
config.set("colors.webpage.darkmode.enabled", True)

# Add Brave adblocker
config.set("content.blocking.method", "both");

# Set search engines
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?ia=web&q={}',
    '!g': 'https://google.com/search?hl=en&q={}'
}

# Use the catppuccin theme
catppuccin.setup(c, 'mocca', True)


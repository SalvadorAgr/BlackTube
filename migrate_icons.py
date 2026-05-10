import os
import re

mapping = {
    'bars': 'menu',
    'arrow-left': 'arrow-left',
    'arrow-right': 'arrow-right',
    'search': 'search',
    'clone': 'square-stack',
    'filter': 'filter',
    'rss': 'rss',
    'user-check': 'user-check',
    'fire': 'flame',
    'users': 'users',
    'bookmark': 'bookmark',
    'history': 'history',
    'sliders-h': 'sliders-horizontal',
    'info-circle': 'info',
    'circle-user': 'user-circle',
    'thumbs-up': 'thumbs-up',
    'thumbs-down': 'thumbs-down',
    'play': 'play',
    'pause': 'pause',
    'forward': 'fast-forward',
    'backward': 'rewind',
    'step-forward': 'skip-forward',
    'step-backward': 'skip-back',
    'trash': 'trash-2',
    'edit': 'edit-3',
    'plus': 'plus',
    'times': 'x',
    'times-circle': 'x-circle',
    'exclamation-circle': 'alert-circle',
    'check': 'check',
    'chevron-right': 'chevron-right',
    'angle-down': 'chevron-down',
    'angle-up': 'chevron-up',
    'ellipsis-v': 'more-vertical',
    'ellipsis-h': 'more-horizontal',
    'external-link-alt': 'external-link',
    'globe': 'globe',
    'lock': 'lock',
    'key': 'key',
    'keyboard': 'keyboard',
    'language': 'languages',
    'palette': 'palette',
    'shield': 'shield',
    'wifi': 'wifi',
    'video': 'video',
    'clapperboard': 'clapperboard',
    'film': 'film',
    'images': 'image',
    'database': 'database',
    'server': 'server',
    'network-wired': 'network',
    'heart': 'heart',
    'clock': 'clock',
    'clock-rotate-left': 'history',
    'share-alt': 'share-2',
    'download': 'download',
    'file-download': 'file-down',
    'file-video': 'file-video',
    'file-image': 'file-image',
    'comment': 'message-square',
    'comment-dots': 'message-square-more',
    'newspaper': 'newspaper',
    'podcast': 'podcast',
    'tower-broadcast': 'tower-control',
    'satellite-dish': 'satellite',
    'trophy': 'trophy',
    'gamepad': 'gamepad-2',
    'flask': 'flask-conical',
    'volume-high': 'volume-2',
    'volume-low': 'volume-1',
    'volume-mute': 'volume-x',
    'expand': 'maximize',
    'compress': 'minimize',
    'thumbtack': 'pin',
    'magnifying-glass': 'search',
    'list': 'list'
}

def migrate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove FontAwesomeIcon imports
    content = re.sub(r"import\s+{\s*FontAwesomeIcon\s*}\s*from\s*['\"]@fortawesome/vue-fontawesome['\"]\n?", "", content)
    
    # 2. Remove FontAwesomeIcon from components object if it exists (for non-setup components)
    content = re.sub(r"components:\s*{[^}]*FontAwesomeIcon[^}]*}", lambda m: m.group(0).replace("FontAwesomeIcon,", "").replace(",FontAwesomeIcon", "").replace("FontAwesomeIcon", ""), content)

    # 3. Replace <FontAwesomeIcon with <LucideIcon and map names
    def replace_icon(match):
        full_tag = match.group(0)
        # Try to find :icon="['fas', 'name']" or :icon="['far', 'name']" or :icon="'name'"
        icon_match = re.search(r":icon=\"\[\s*['\"]fa[sr]b?['\"]\s*,\s*['\"]([^'\"]+)['\"]\s*\]\"", full_tag)
        if not icon_match:
             icon_match = re.search(r":icon=\"['\"]([^'\"]+)['\"]\"", full_tag)
        
        if icon_match:
            fa_name = icon_match.group(1)
            lucide_name = mapping.get(fa_name, fa_name)
            # Replace FontAwesomeIcon with LucideIcon and update attributes
            new_tag = full_tag.replace("FontAwesomeIcon", "LucideIcon")
            new_tag = re.sub(r":icon=\"[^\"]+\"", f'name="{lucide_name}" :size="18"', new_tag)
            return new_tag
        
        return full_tag.replace("FontAwesomeIcon", "LucideIcon")

    content = re.sub(r"<FontAwesomeIcon[^>]+/>", replace_icon, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = 'src/renderer'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.vue'):
            migrate_file(os.path.join(root, file))

print("Migration complete!")

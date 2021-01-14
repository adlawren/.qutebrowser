c.auto_save.session = True

def remap_in_all_modes(remappings):
    for mode in c.bindings.default:
        new_dict = {}
        for key in c.bindings.default[mode]:
            if key[0] == '<':
                # ignore meta-characters
                new_dict[key] = c.bindings.default[mode][key]
            else:
                new_key = ""
                for key_character in key:
                    new_key_character = key_character
                    if key_character in remappings:
                        new_key_character = remappings[key_character]
                    new_key += new_key_character
                new_dict[new_key] = c.bindings.default[mode][key]
        c.bindings.default[mode] = new_dict

remappings = {'i': 's', 'h': 'n', 'j': 'e', 'k': 'u', 'l': 'i', 'n': 'k', 's': 'j', 'u': 'h', 'I': 'S', 'H': 'N', 'J': 'E', 'K': 'U', 'L': 'I', 'N': 'K', 'S': 'J', 'U': 'H'}

remap_in_all_modes(remappings)

c.fonts.web.size.default = 20

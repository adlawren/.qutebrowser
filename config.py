colemak_remappings = {'s': 'r', 'd': 's', 'f': 't', 'g': 'd', 'e': 'f', 'r': 'p', 't': 'g', 'n': 'k', 'j': 'n', 'k': 'e', 'l': 'i', ';': 'o', 'y': 'j', 'u': 'l', 'i': 'u', 'o': 'y', 'p': ';', 'S': 'R', 'D': 'S', 'F': 'T', 'G': 'D', 'E': 'F', 'R': 'P', 'T': 'G', 'N': 'K', 'J': 'N', 'K': 'E', 'L': 'I', ':': 'O', 'Y': 'J', 'U': 'L', 'I': 'U', 'O': 'Y', 'P': ':'}

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
                if key_character in colemak_remappings:
                    new_key_character = colemak_remappings[key_character]
                new_key += new_key_character
            new_dict[new_key] = c.bindings.default[mode][key]
    c.bindings.default[mode] = new_dict

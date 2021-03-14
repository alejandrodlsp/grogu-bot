aliases = {
    'ping' : [ 'latency', 'ms' ],
    'clear' : [ 'clean', 'purge' ],
    'kick' : [ 'a' ],
    'changeprefix' : [ 'prefix', 'change_prefix' ]
}

def get_aliases(command):
    return aliases[command] if command in aliases else []
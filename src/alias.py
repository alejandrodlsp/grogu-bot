aliases = {
    'ping' : [ 'latency', 'ms' ],
    'clear' : [ 'clean', 'purge' ],
    'kick' : [],
    'ban' : [],
    'unban' : [],
    'changeprefix' : [ 'prefix', 'change_prefix' ],
    'connect' : [ 'c' ],
    'queue' : [ 'q' ],
    'disconnect' : [ 'dc' ],
    'play' : [ 'p' ],
    'pause' : [],
    'resume' : []
}

def get_aliases(command):
    return aliases[command] if command in aliases else []
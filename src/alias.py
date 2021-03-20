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
    'play' : [ 'p', 'pl'],
    'pause' : [],
    'resume' : [ 'r' ],
    'skip' : [ 'next', 'fs', 's' ],
    'previous' : [ 'rewind', 'rw' ],
    'shuffle' : [ 'sf', 'sh' ]
}

def get_aliases(command):
    return aliases[command] if command in aliases else []
CREATE TABLE IF NOT EXISTS welcome_message (
    guild_id integer PRIMARY_KEY,

    background text NOT NULL,
    template integer NOT NULL DEFAULT 1 CHECK (template IN (1, 2, 3, 4)),
    text_color text NOT NULL DEFAULT 'white',

    FOREIGN KEY (guild_id) REFERENCES guilds(guild_id)
);

CREATE TABLE IF NOT EXISTS guilds (
    guild_id integer PRIMARY KEY,
    prefix text DEFAULT ">",
    default_role integer,
    member_log_channel integer DEFAULT 0,
    admin_log_channel integer DEFAULT 0,
    message_log_channel integer DEFAULT 0,
    meme_channel integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS experience (
    user_id integer PRIMARY KEY,
    xp integer DEFAULT 0,
    xp_lock text DEFAULT CURRENT_TIMESTAMP
);
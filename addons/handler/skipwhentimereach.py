from audiobot import Global_Audio_Bot
from audiobot.event import AudioBotPlayEvent
from audiobot.event.audiobot import AudioBotStartEvent
from player.mpv import MPVProperty

max_sec = 120
has_skip = True

def skip_when_time_reach(property, val, *args):
    global has_skip
    time_pos = 0 if val is None else int(val)
    if time_pos >= max_sec and has_skip:
        has_skip = False
        Global_Audio_Bot.playNext()

def check_play_next(event:AudioBotPlayEvent):
    global has_skip
    has_skip = True

@Global_Audio_Bot.handlers.register(AudioBotStartEvent,"addons.handler.registerskiptimereach")
def register_skiplong(event:AudioBotStartEvent):
    Global_Audio_Bot.mpv_player.registerPropertyHandler("addon.handler.skip_when_time_reach",
                                                        MPVProperty.TIME_POS,
                                                        skip_when_time_reach)
    Global_Audio_Bot.handlers._register(AudioBotPlayEvent, "addon.skip_when_time_reach_reset",
                                        check_play_next)

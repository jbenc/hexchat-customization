import hexchat

__module_name__ = 'Highlight Private Messages'
__module_author__ = 'Jiri Benc'
__module_version__ = '0.0.1'
__module_description__ = 'Color a tab with a new private message as it was highlighted'

def highlight_msg(word, word_eol, userdata):
    context = hexchat.get_context()
    context.command('GUI COLOR 3')
    return hexchat.EAT_NONE


hexchat.hook_print('Private Message', highlight_msg)
hexchat.hook_print('Private Message to Dialog', highlight_msg)
hexchat.hook_print('Private Action', highlight_msg)

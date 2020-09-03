import hexchat

__module_name__ = 'Focus to Highlighted'
__module_author__ = 'Jiri Benc'
__module_version__ = '0.0.1'
__module_description__ = 'A /focus command to switch to a tab with highlighted or private message'

context_list = []

def push_context(word, word_eol, userdata):
    context = hexchat.get_context()
    if not context in context_list:
        context_list.append(context)
    return hexchat.EAT_NONE


def pop_context(word, word_eol, userdata):
    context = hexchat.get_context()
    try:
        context_list.remove(context)
    except ValueError:
        pass
    return hexchat.EAT_NONE


def switch_focus(word, word_eol, userdata):
    hexchat.command('GUI SHOW')
    try:
        last = context_list.pop()
    except IndexError:
        return hexchat.EAT_NONE
    last.command('GUI FOCUS')
    return hexchat.EAT_ALL


hexchat.hook_print('Channel Msg Hilight', push_context)
hexchat.hook_print('Channel Action Hilight', push_context)
hexchat.hook_print('Private Message', push_context)
hexchat.hook_print('Private Message to Dialog', push_context)
hexchat.hook_print('Private Action', push_context)
hexchat.hook_print('Focus Tab', pop_context)
hexchat.hook_command('focus', switch_focus)

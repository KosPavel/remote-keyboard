Keybinds = {
        "Key.esc" : 0x01,
        "1" : 0x02,
        "2" : 0x03,
        "3" : 0x04,
        "4" : 0x05,
        "5" : 0x06,
        "6" : 0x07,
        "7" : 0x08,
        "8" : 0x09,
        "9" : 0x0A,
        "0" : 0x0B,
        "-" : 0x0C,    # - on main keyboard
        "=" : 0x0D,
        "Key.backspace" : 0x0E,    # backspace
        "Key.tab" : 0x0F,
        "q" : 0x10,
        "w" : 0x11,
        "e" : 0x12,
        "r" : 0x13,
        "t" : 0x14,
        "y" : 0x15,
        "u" : 0x16,
        "i" : 0x17,
        "o" : 0x18,
        "p" : 0x19,
        "[" : 0x1A,
        "]" : 0x1B,
        "Key.enter" : 0x1C,    # Enter on main keyboard
        "Key.ctrl_l" : 0x1D,
        "a" : 0x1E,
        "s" : 0x1F,
        "d" : 0x20,
        "f" : 0x21,
        "g" : 0x22,
        "h" : 0x23,
        "j" : 0x24,
        "k" : 0x25,
        "l" : 0x26,
        ";" : 0x27,
        "'" : 0x28,
        "`" : 0x29,    # accent grave
        "Key.shift" : 0x2A,
        "\\" : 0x2B,
        "z" : 0x2C,
        "x" : 0x2D,
        "c" : 0x2E,
        "v" : 0x2F,
        "b" : 0x30,
        "n" : 0x31,
        "m" : 0x32,
        "," : 0x33,
        "." : 0x34,    # . on main keyboard
        "/" : 0x35,    # / on main keyboard
        "Key.shift_r" : 0x36,
        "*" : 0x37,    # * on numeric keypad
        "Key.alt_l" : 0x38,    # left Alt
        "Key.space" : 0x39,
        "Key.caps_lock" : 0x3A,
        "Key.f1" : 0x3B,
        "Key.f2" : 0x3C,
        "Key.f3" : 0x3D,
        "Key.f4" : 0x3E,
        "Key.f5" : 0x3F,
        "Key.f6" : 0x40,
        "Key.f7" : 0x41,
        "Key.f8" : 0x42,
        "Key.f9" : 0x43,
        "Key.f10" : 0x44,
        "Key.num_lock" : 0x45,
        "Key.scroll_lock" : 0x46,   # Scroll Lock
        "Key.home" : 0x47,
        "Key.up" : 0x48,
        "Key.page_up" : 0x49,
        "Key.left" : 0x4B,
        "<12>" : 0x4C,
        "Key.right" : 0x4D,
        "+" : 0x4E,    # + on numeric keypad
        "Key.end" : 0x4F,
        "Key.down" : 0x50,
        "Key.page_don" : 0x51,
        "Key.insert" : 0x52,
        "Key.f11" : 0x57,
        "Key.f12" : 0x58,
        "Key.f13" : 0x64,    # : "      (NEC PC98)
        "Key.f14" : 0x65,    # : "      (NEC PC98)
        "Key.f15" : 0x66,    # : "      (NEC PC98)
            }

"""
 Alternate names for keys, to facilitate transition from DOS.

BACKSPACE       BACK : "   # backspace
NUMPADSTAR      MULTIPLY        # * on numeric keypad
LALT : "   LMENU : "  # left Alt
CAPSLOCK        CAPITAL : "# CapsLock
NUMPADMINUS     SUBTRACT        # - on numeric keypad
NUMPADPLUS      ADD : "    # + on numeric keypad
NUMPADPERIOD    DECIMAL : "# . on numeric keypad
NUMPADSLASH     DIVIDE : " # / on numeric keypad
RALT : "   RMENU : "  # right Alt
UPARROW : "UP : "# UpArrow on arrow keypad
PGUP : "   PRIOR : "  # PgUp on arrow keypad
LEFTARROW       LEFT : "   # LeftArrow on arrow keypad
RIGHTARROW      RIGHT : "  # RightArrow on arrow keypad
DOWNARROW       DOWN : "   # DownArrow on arrow keypad
PGDN : "   NEXT : "   # PgDn on arrow keypad
"""

# Esc : 0x01
# MAIN1 : 0x02
# MAIN2 : 0x03
# MAIN3 : 0x04
# MAIN4 : 0x05
# MAIN5 : 0x06
# MAIN6 : 0x07
# MAIN7 : 0x08
# MAIN8 : 0x09
# MAIN9 : 0x0A
# MAIN0 : 0x0B
# MINUS : 0x0C    # - on main keyboard
# EQUALS : 0x0D
# BACK : 0x0E    # backspace
# TAB : 0x0F
# Q : 0x10
# W : 0x11
# E : 0x12
# R : 0x13
# T : 0x14
# Y : 0x15
# U : 0x16
# I : 0x17
# O : 0x18
# P : 0x19
# LBRACKET : 0x1A
# RBRACKET : 0x1B
# RETURN : 0x1C    # Enter on main keyboard
# LCONTROL : 0x1D
# A : 0x1E
# S : 0x1F
# D : 0x20
# F : 0x21
# G : 0x22
# H : 0x23
# J : 0x24
# K : 0x25
# L : 0x26
# SEMICOLON : 0x27
# APOSTROPHE : 0x28
# GRAVE : 0x29    # accent grave
# LSHIFT : 0x2A
# BACKSLASH : 0x2B
# Z : 0x2C
# X : 0x2D
# C : 0x2E
# V : 0x2F
# B : 0x30
# N : 0x31
# M : 0x32
# COMMA : 0x33
# PERIOD : 0x34    # . on main keyboard
# SLASH : 0x35    # / on main keyboard
# RSHIFT : 0x36
# MULTIPLY : 0x37    # * on numeric keypad
# LMENU : 0x38    # left Alt
# SPACE : 0x39
# CAPITAL : 0x3A
# F1 : 0x3B
# F2 : 0x3C
# F3 : 0x3D
# F4 : 0x3E
# F5 : 0x3F
# F6 : 0x40
# F7 : 0x41
# F8 : 0x42
# F9 : 0x43
# F10 : 0x44
# NUMLOCK : 0x45
# SCROLL : " 0x46    # Scroll Lock
# NUMPAD7 : 0x47
# NUMPAD8 : 0x48
# NUMPAD9 : 0x49
# SUBTRACT : 0x4A    # - on numeric keypad
# NUMPAD4 : 0x4B
# NUMPAD5 : 0x4C
# NUMPAD6 : 0x4D
# ADD : 0x4E    # + on numeric keypad
# NUMPAD1 : 0x4F
# NUMPAD2 : 0x50
# NUMPAD3 : 0x51
# NUMPAD0 : 0x52
# DECIMAL : 0x53    # . on numeric keypad
# F11 : 0x57
# F12 : 0x58
# F13 : 0x64    # : "      (NEC PC98)
# F14 : 0x65    # : "      (NEC PC98)
# F15 : 0x66    # : "      (NEC PC98)
#
# KANA : 0x70    # (Japanese keyboard) :
# CONVERT : 0x79    # (Japanese keyboard) :
# NOCONVERT : 0x7B    # (Japanese keyboard) :
# YEN : 0x7D    # (Japanese keyboard) :
# NUMPADEQUALS : 0x8D    # : "on numeric keypad (NEC PC98)
# CIRCUMFLEX : 0x90    # (Japanese keyboard) :
# AT : 0x91    # : "      (NEC PC98)
# COLON : 0x92    # : "      (NEC PC98)
# UNDERLINE : 0x93    # : "      (NEC PC98)
# KANJI : 0x94    # (Japanese keyboard) :
# STOP : 0x95    # : "      (NEC PC98)
# AX : 0x96    # : "      (Japan AX)
# UNLABELED : 0x97    # : ": " (J3100)
# NUMPADENTER : 0x9C    # Enter on numeric keypad
# RCONTROL : 0x9D
# NUMPADCOMMA : 0xB3    # , on numeric keypad (NEC PC98)
# DIVIDE : 0xB5    # / on numeric keypad
# SYSRQ : 0xB7
# RMENU : 0xB8    # right Alt
# HOME : 0xC7    # Home on arrow keypad
# UP : 0xC8    # UpArrow on arrow keypad
# PRIOR : 0xC9    # PgUp on arrow keypad
# LEFT : 0xCB    # LeftArrow on arrow keypad
# RIGHT : 0xCD    # RightArrow on arrow keypad
# END : 0xCF    # End on arrow keypad
# DOWN : 0xD0    # DownArrow on arrow keypad
# NEXT : 0xD1    # PgDn on arrow keypad
# INSERT : 0xD2    # Insert on arrow keypad
# DELETE : 0xD3    # Delete on arrow keypad
# LWIN : 0xDB    # Left Windows key
# RWIN : 0xDC    # Right Windows key
# APPS : 0xDD    # AppMenu key

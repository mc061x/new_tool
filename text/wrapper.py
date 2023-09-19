from text.bindings import add_autocomplete_binding
from text.command_list import COMMAND_LIST
from text.lexer import LexerWrapper, MyLexer
from text.suggestor import MySuggsetor

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession, ANSI

from config.generalCfg import GeneralConfig

class TextWrapper:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.bindings = KeyBindings()
        add_autocomplete_binding(self.bindings)
    
        self.lexerWrapper = LexerWrapper(cfg)
        self.lexer = MyLexer(self.lexerWrapper)

        self.suggestor = MySuggsetor(COMMAND_LIST)
        
        self.session = PromptSession(
            auto_suggest=self.suggestor,
            key_bindings=self.bindings,
            lexer=self.lexer
        )

        self.prompt = cfg.interfaceCfg.system('$') + cfg.interfaceCfg.system(cfg.cfConfig.handle) + '> '

    def get_command(self):
        text = self.session.prompt(ANSI(self.prompt), lexer=self.lexer)
        return text
    
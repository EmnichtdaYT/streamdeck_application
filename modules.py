import abc

_modules = {}

class Module:
    @abc.abstractmethod
    def handle_action(action: str, parameters: list[str]) -> None:
        raise NotImplementedError()

def register_module(name: str, module: Module) -> None:
        _modules[name] = module
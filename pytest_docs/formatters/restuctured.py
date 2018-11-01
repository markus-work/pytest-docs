from ..models.formatter import Formatter


class RSTFormatter(Formatter):
    name = 'rst'
    marker_prefix = "\n\n**Markers:**"

    @staticmethod
    def module_name_format(element):
        return '{}\n{}\n'.format(element, "*" * len(element))

    @staticmethod
    def class_name_format(element):
        return '{}\n{}\n'.format(element, "*" * len(element))

    @staticmethod
    def func_name_format(element):
        return '{}\n{}\n'.format(element, "*" * len(element))

    @staticmethod
    def marker_format(marker):
        return "\n- {}\n".format(marker)
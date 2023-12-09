
class TextFormate:

    @staticmethod
    def cut_off_120_characters(text: str) -> str:
        return text if len(text) <= 120 else text[:116] + '...'

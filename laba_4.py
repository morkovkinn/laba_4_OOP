class Chord:
    """Базовый класс для аккордов (триад)."""

    def __init__(self, root: str, third: str, fifth: str) -> None:
        """
        Конструктор для аккорда.

        :param root: Основной тон аккорда.
        :param third: Тон третьей ступени аккорда.
        :param fifth: Тон пятой ступени аккорда.
        """
        self.root = root  # Основной тон аккорда
        self.third = third  # Тон третьей ступени
        self.fifth = fifth  # Тон пятой ступени

    def define_chord(self) -> str:
        """Определяет тип аккорда (мажорный, минорный, уменьшенный или увеличенный) на основании входящих в него нот"""
        ...
    def play(self) -> str:
        """Играет аккорд. Возвращает строку с названием аккорда."""
        return f"Играем аккорд: {self.root} - {self.third} - {self.fifth}"

    def __str__(self) -> str:
        return f"Аккорд: {self.root}, {self.third}, {self.fifth}"

    def __repr__(self) -> str:
        return f"Chord(root='{self.root}', third='{self.third}', fifth='{self.fifth}')"


class SeventhChord(Chord):
    """Дочерний класс для септаккордов."""

    def __init__(self, root: str, third: str, fifth: str, seventh: str) -> None:
        """
        Конструктор для септаккорда.

        :param root: Основной тон аккорда.
        :param third: Тон третьей ступени аккорда.
        :param fifth: Тон пятой ступени аккорда.
        :param seventh: Тон седьмой ступени аккорда.
        """
        super().__init__(root, third, fifth)  # Вызов конструктора базового класса
        self.seventh = seventh  # Тон седьмой ступени

    def play(self) -> str:
        """Играет септаккорд. Возвращает строку с названием аккорда.

        Переопределение метода play для добавления седьмой ступени в аккорд.
        """
        return f"Играем септаккорд: {self.root} - {self.third} - {self.fifth} - {self.seventh}"

    def __str__(self) -> str:
        """Возвращает строковое представление септаккорда."""
        return f"Септаккорд: {self.root}, {self.third}, {self.fifth}, {self.seventh}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление септаккорда."""
        return f"SeventhChord(root='{self.root}', third='{self.third}', fifth='{self.fifth}', seventh='{self.seventh}')"


"""
Пример использования:

if __name__ == "__main__":
    triad = Chord("C", "E", "G")
    print(triad)  # Вывод: Аккорд: C, E, G
    print(triad.play())  # Вывод: Играем аккорд: C - E - G

    seventh_chord = SeventhChord("C", "E", "G", "B")
    print(seventh_chord)  # Вывод: Септаккорд: C, E, G, B
    print(seventh_chord.play())  # Вывод: Играем септаккорд: C - E - G - B

"""